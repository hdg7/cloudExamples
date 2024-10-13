from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from ultralytics import YOLO
import cv2
from fastapi import File, UploadFile

app=FastAPI()

@app.get("/webTest", response_class=HTMLResponse)
async def read_items():
    html_content="""
    <html>
    <head>
    <title> Hello World! </title>
    </head>
    <body> <h1> Hi! World! </h1> </body>
    </html>"""
    return HTMLResponse(content=html_content, status_code=200)

# We create a FastAPI instance and define a route /webYolo that allows the user to upload an image through a POST request.
# The image is then processed and the result is returned as a JSON response.

@app.get("/webYolo")
async def read_items():
    html_content="""
    <html>
    <head>
    <title>System for Image Uploading </title>
    </head>
    <body>
    <h1> Upload your image </h1>
    <div class="container">
        <input type="file" id="imageUpload" accept="image/*">
        <div class="buttons">
            <button id="classifyButton" onclick="sendImage('classify')">Classify Image</button>
            <button id="detectButton" onclick="sendImage('detect')">Detect Objects</button>
        </div>
    </div>
    <script>
        function sendImage(action) {
            const fileInput = document.getElementById('imageUpload');
            if (fileInput.files.length === 0) {
                alert('Please select an image first.');
                return;
            }

            const formData = new FormData();
            formData.append('image', fileInput.files[0]);

            fetch(`/${action}`, {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                // Handle the response data here
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

# We define a route /classify that accepts a POST request with an image file. The image is classified using a pre-trained model and the result is returned as a JSON response.

@app.post("/classify")
async def classify_image(image: UploadFile = File(...)):
    image_bytes = await image.read()
    result = classify_image(image_bytes)
    return result

# We define a route /detect that accepts a POST request with an image file. The image is processed using a YOLO object detection model and the result is returned as a JSON response.
@app.post("/detect")
async def detect_objects(image: UploadFile = File(...)):
    image_bytes = await image.read()
    result = detect_objects(image_bytes)
    return result

# We define a function classify_image that takes an image file as input, loads a pre-trained model, and classifies the image. The result is returned as a JSON response.
def classify_image(image_bytes):
    # Load pre-trained model
    model = load_model("classifier")
    results = model(image_bytes)
    detected =[]
    for elem in results:
        try:
            detected.append(model.names[elem.probs.top1])
        except:
            continue
    return {"detections":detected}

# We define a function detect_objects that takes an image file as input, processes the image using a YOLO object detection model, and returns the detected objects as a JSON response.
def detect_objects(image_bytes):
    # Load YOLO model
    model = load_model("detector")
    # Preprocess image
    boxes =[]
    scores =[]
    classes =[]
    results = model(image_bytes)  # predict on an image
    boxes = results[0].boxes
    image_with_boxes = addBoxesImage(image_bytes, boxes)
    return {"image": image_with_boxes}

# We define helper functions 
def load_model(model_type="classifier"):
    # Load a COCO-pretrained YOLO11n model
    model = YOLO('yolo11n.yaml')
    if model_type == "classifier":
        model = YOLO("yolo11n-cls.pt")
        #model.train(data='coco8.yaml', epochs=3)
    else:
        model = YOLO("yolo11n.pt")
        model.train(data='coco8.yaml', epochs=3)
    return model

def read_box(box):
    cords = box.xyxy[0].tolist()
    cords = [round(x) for x in cords]
    class_id = model.names[box.cls[0].item()]
    conf = round(box.conf[0].item(), 2)
    return [class_id, cords, conf]
                    
def addBoxesImage(img,boxesInfo):
    colors = np.random.randint(0, 255, size=(len(model.names), 3), dtype="uint8")
    for box in boxesInfo:
        class_id=int(box.cls)
        confidence=float(box.conf)
        #color = [int(c) for c in colors[list(model.names.values()).index(class_id)]]
        color = [int(c) for c in colors[class_id]]
        cv2.rectangle(img, (int(box.xyxy[0][0]), int(box.xyxy[0][1])), (int(box.xyxy[0][2]), int(box.xyxy[0][3])), color=color, thickness=2)
        text = f"{class_id}: {confidence:.2f}"
        (text_width, text_height) = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, fontScale=10, thickness=2)[0]
        text_offset_x = int(box.xyxy[0][0])
        text_offset_y = int(box.xyxy[0][2]) - 5
        box_coords = ((text_offset_x, text_offset_y), (text_offset_x + text_width + 2, text_offset_y - text_height))
        overlay = img.copy()
        cv2.rectangle(overlay, box_coords[0], box_coords[1], color=color, thickness=cv2.FILLED)
        image = cv2.addWeighted(overlay, 0.6, img, 0.4, 0)
        cv2.putText(image, text, (int(box.xyxy[0][0]), int(box.xyxy[0][2]) - 5), cv2.FONT_HERSHEY_SIMPLEX,fontScale=10, color=(0, 0, 0), thickness=2)
        cv2.imwrite("example_yolo.png", image)
        return image
        #cv2.imwrite(currentImage + "_yolo.png", image)

                                                                                                                            
