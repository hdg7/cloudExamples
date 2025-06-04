from fastapi import FastAPI, UploadFile, File
import aio_pika
import asyncio

app = FastAPI()
RABBITMQ_URL = "amqp://guest:guest@rabbitmq/"

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
async def upload_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    message = aio_pika.Message(body=image_bytes)
    await app.state.channel.default_exchange.publish(message, routing_key="image_tasks")
    return {"status": "queued"}
                                
