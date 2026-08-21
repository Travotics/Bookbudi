# import firebase_admin
# from firebase_admin import credentials
# from config import settings

# def initialize_firebase():
#     if firebase_admin._apps:
#         return

#     if settings.APP_ENV == "dev":
#         key_path = "dev/serviceAccountKey.json"

#     else:
#         key_path = "prd/serviceAccountKey.json"
#     cred = credentials.Certificate(key_path)
#     firebase_admin.initialize_app(cred)

import json

import firebase_admin
from firebase_admin import credentials

from config import settings


def initialize_firebase():
    if firebase_admin._apps:
        return

    if settings.FIREBASE_SERVICE_ACCOUNT_JSON:
        service_account = json.loads(
            settings.FIREBASE_SERVICE_ACCOUNT_JSON
        )

        cred = credentials.Certificate(service_account)

    elif settings.FIREBASE_SERVICE_ACCOUNT_FILE:
        cred = credentials.Certificate(
            settings.FIREBASE_SERVICE_ACCOUNT_FILE
        )

    else:
        raise ValueError(
            "Firebase service account configuration is missing"
        )

    firebase_admin.initialize_app(cred)