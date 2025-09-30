import firebase

firebase_config = {
    "apiKey": "AIzaSyDIHzF7epTKyyWuHSc1Mv5tHbAad9h9EXc",
    "authDomain": "yoloproject-6690e.firebaseapp.com",
    "projectId": "yoloproject-6690e",
    "databaseURL": None,
    "storageBucket": "yoloproject-6690e.firebasestorage.app",
    "messagingSenderId": "637186877622",
    "appId": "1:637186877622:web:04ed64babcf66aa9a25e17",
    "measurementId": "G-9C6ZEBT634"
}

app = firebase.initialize_app(firebase_config)
auth = app.auth()
email = "pedro@gmail.com"
password = "qwerty12345"
#auth.create_user_with_email_and_password(email, password)
user = auth.sign_in_with_email_and_password(email, password)

id_token = user['idToken']
print(id_token)
