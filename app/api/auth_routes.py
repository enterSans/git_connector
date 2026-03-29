from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
from app.services.auth_service import AuthService

router = APIRouter(prefix="/api/auth", tags=["Auth"])


@router.get("/login")
def login():
    url = AuthService.get_github_login_url()
    return RedirectResponse(url)


@router.get("/callback")
def callback(code: str):
    result = AuthService.exchange_code_for_token(code)

    if result["error"]:
        raise HTTPException(status_code=400, detail=result["message"])

    return {
        "message": "OAuth successful",
        "access_token": result["access_token"]
    }

