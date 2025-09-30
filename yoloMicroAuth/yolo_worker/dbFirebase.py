import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin
cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()

# Example function to save a detection record
def save_detection(label, confidence, x1, y1, x2, y2, image_path):
    doc_ref = db.collection("detections").document()
    doc_ref.set({
        "label": label,
        "confidence": confidence,
        "x1": x1,
        "y1": y1,
        "x2": x2,
        "y2": y2,
        "image_path": image_path
    })
    return doc_ref.id

def update_image_path(doc_id, new_image_path):
    doc_ref = db.collection("detections").document(doc_id)
    try:
        doc_ref.update({"image_path": new_image_path})
        print(f"Updated image_path for document {doc_id} to '{new_image_path}'")
    except Exception as e:
        print(f"Error updating document {doc_id}: {e}")
                                
#docs = db.collection("detections").stream()
#for doc in docs:
#    print(f"{doc.id} => {doc.to_dict()}")
