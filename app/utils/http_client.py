import requests

def make_request(method, url, token, json=None):
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }

    try:
        response = requests.request(method, url, headers=headers, json=json)

        if response.status_code >= 400:
            return {
                "error": True,
                "status_code": response.status_code,
                "message": response.json()
            }

        return {
            "error": False,
            "data": response.json()
        }

    except requests.exceptions.RequestException as e:
        return {
            "error": True,
            "message": str(e)
        }