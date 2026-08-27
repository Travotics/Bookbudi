from fastapi import HTTPException, Request

from firebase_admin import auth

def get_current_user(request: Request):

    authorization = request.headers.get("Authorization")

    if not authorization:
        print("No Auth header present")
        raise HTTPException(
                    status_code=401,
                    detail="Authorization header is missing"
        )

    if not authorization.startswith("Bearer "):
        print("Invalid auth bearer")
        raise HTTPException(
            status_code=401,
            detail="Invalid authorization header"
        )

    token = authorization.split(" ")[1]
    
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token

    except Exception as e:

        print("Firebase verification error:", repr(e))
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )