import pyrebase

firebase_config = {
    "apiKey": "YOUR_API_KEY",
    "authDomain": "your-project-id.firebaseapp.com",
    "databaseURL": "",  
    "projectId": "your-project-id",
    "storageBucket": "your-project-id.appspot.com",
    "messagingSenderId": "YOUR_SENDER_ID",
    "appId": "YOUR_APP_ID",
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

email = "pedro123@gmail.com"
password = "qwerty12345"

user = auth.sign_in_with_email_and_password(email, password)
id_token = user['idToken']
print(id_token)
