import firebase_admin
from firebase_admin import auth, credentials

cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)

def verify_token(id_token: str):
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token
    except Exception as e:
        print("Invalid token:", e)
        return None
                        
