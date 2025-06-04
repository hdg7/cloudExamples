import aio_pika, asyncio, io, uuid, os
from ultralytics import YOLO
from PIL import Image, ImageDraw
from db import detections, Session

RABBITMQ_URL = "amqp://guest:guest@rabbitmq/"
IMAGE_OUTPUT_DIR = "data/images"
os.makedirs(IMAGE_OUTPUT_DIR, exist_ok=True)

model = YOLO("yolov8n.pt")

async def handle_image(message: aio_pika.IncomingMessage):
    async with message.process():
        image = Image.open(io.BytesIO(message.body)).convert("RGB")
        results = model(image)
        session = Session()
        
        for result in results:
            draw = ImageDraw.Draw(image)
            for box in result.boxes:
                label = model.names[int(box.cls[0])]
                conf = float(box.conf[0])
                x1, y1, x2, y2 = [float(coord.item()) for coord in box.xyxy[0]]
                draw.rectangle([x1, y1, x2, y2], outline="red", width=2)
                draw.text((x1, y1), f"{label} {conf:.2f}", fill="red")
                
                session.execute(detections.insert().values(
                    label=label,
                    confidence=conf,
                    x1=x1, y1=y1, x2=x2, y2=y2,
                    image_path=None  # filled below
                ))

        # Save annotated image
        filename = f"{uuid.uuid4()}.jpg"
        image_path = os.path.join(IMAGE_OUTPUT_DIR, filename)
        image.save(image_path)
        
        # Update DB with image path
        session.execute(f"UPDATE detections SET image_path = '{image_path}' WHERE image_path IS NULL")
        session.commit()
        session.close()
        print(f"Processed and saved: {image_path}")
        
async def main():
    while True:
        try:
            connection = await aio_pika.connect_robust(RABBITMQ_URL)
            print("Connected to RabbitMQ")
            break
        except Exception as e:
            print("Waiting for RabbitMQ...")
            await asyncio.sleep(2)
    channel = await connection.channel()
    await channel.set_qos(prefetch_count=1)
    queue = await channel.declare_queue("image_tasks", durable=True)
    await queue.consume(handle_image)
    print("YOLO Worker listening for images...")
    await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
                                                                                                                                                                                                                                                                                            
