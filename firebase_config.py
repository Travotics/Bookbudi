import firebase_admin
from firebase_admin import credentials
from config import settings

def initialize_firebase():
    if firebase_admin._apps:
        return

    if settings.APP_ENV == "dev":
        key_path = "dev/serviceAccountKey.json"

    else:
        key_path = "prd/serviceAccountKey.json"
    cred = credentials.Certificate(key_path)
    firebase_admin.initialize_app(cred)