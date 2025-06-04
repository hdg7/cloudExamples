from fastapi import FastAPI, UploadFile, File, HTTPException, Depends, Header
from auth import verify_token
import aio_pika
import asyncio

app = FastAPI()
RABBITMQ_URL = "amqp://guest:guest@rabbitmq/"

async def get_current_user(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid auth header")
    token = authorization.split(" ")[1]
    decoded = verify_token(token)
    if not decoded:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return decoded 


async def connect_rabbitmq():
    while True:
        try:
            connection = await aio_pika.connect_robust(RABBITMQ_URL)
            channel = await connection.channel()
            await channel.declare_queue("image_tasks", durable=True)
            app.state.connection = connection
            app.state.channel = channel
            print("Connected to RabbitMQ")
            break
        except Exception as e:
            print("Waiting for RabbitMQ...")
            await asyncio.sleep(2)

@app.on_event("startup")
async def startup():
    await connect_rabbitmq()

@app.on_event("shutdown")
async def shutdown():
    await app.state.connection.close()
       
@app.post("/upload/")
async def upload_image(file: UploadFile = File(...), user=Depends(get_current_user)):
    image_bytes = await file.read()
    message = aio_pika.Message(body=image_bytes)
    await app.state.channel.default_exchange.publish(message, routing_key="image_tasks")
    return {"status": "queued"}
                                
