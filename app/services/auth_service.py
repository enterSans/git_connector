import requests
from app.core.config import settings

class AuthService:

    @staticmethod
    def get_github_login_url():
        return (
            "https://github.com/login/oauth/authorize"
            f"?client_id={settings.GITHUB_CLIENT_ID}"
            f"&redirect_uri={settings.GITHUB_REDIRECT_URI}"
            "&scope=repo"
        )

    @staticmethod
    def exchange_code_for_token(code: str):
        url = "https://github.com/login/oauth/access_token"

        response = requests.post(
            url,
            headers={"Accept": "application/json"},
            data={
                "client_id": settings.GITHUB_CLIENT_ID,
                "client_secret": settings.GITHUB_CLIENT_SECRET,
                "code": code
            }
        )

        data = response.json()

        if "access_token" not in data:
            return {
                "error": True,
                "message": data
            }

        return {
            "error": False,
            "access_token": data["access_token"]
        }