from app.utils.http_client import make_request

class GitHubService:

    BASE_URL = "https://api.github.com"

    @staticmethod
    def get_repos(token: str):
        url = f"{GitHubService.BASE_URL}/user/repos"
        return make_request("GET", url, token)

    @staticmethod
    def create_issue(owner: str, repo: str, title: str, body: str, token: str):
        url = f"{GitHubService.BASE_URL}/repos/{owner}/{repo}/issues"

        payload = {
            "title": title,
            "body": body
        }

        return make_request("POST", url, token, json=payload)
    
    @staticmethod
    @staticmethod
    def list_issues(owner: str, repo: str, token: str):
        url = f"{GitHubService.BASE_URL}/repos/{owner}/{repo}/issues"
        return make_request("GET", url, token)
    
    @staticmethod
    def create_pull_request(owner: str, repo: str, title: str, body: str, head: str, base: str, token: str):
        url = f"{GitHubService.BASE_URL}/repos/{owner}/{repo}/pulls"

        payload = {
        "title": title,
        "body": body,
        "head": head,   # source branch
        "base": base    # target branch
        }

        return make_request("POST", url, token, json=payload)
