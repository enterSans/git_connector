from fastapi import APIRouter, Header, HTTPException
from app.services.github_service import GitHubService
from app.schemas.github_schema import CreateIssueRequest
from app.schemas.github_schema import CreatePRRequest

router = APIRouter(prefix="/api/github", tags=["GitHub"])



@router.post("/pull-request")
def create_pull_request(
    request: CreatePRRequest,
    authorization: str = Header(...)
):
    
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token format")

    token = authorization.split(" ")[1]

    result = GitHubService.create_pull_request(
        request.owner,
        request.repo,
        request.title,
        request.body,
        request.head,
        request.base,
        token
    )

    if result["error"]:
        raise HTTPException(
            status_code=result.get("status_code", 500),
            detail=result.get("message")
        )

    return result["data"]



@router.get("/issues/{owner}/{repo}")
def list_issues(
    owner: str,
    repo: str,
    authorization: str = Header(...)
):

    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token format")

    token = authorization.split(" ")[1]

    result = GitHubService.list_issues(owner, repo, token)

    if result["error"]:
        raise HTTPException(
            status_code=result.get("status_code", 500),
            detail=result.get("message")
        )

    return result["data"]

@router.get("/repos")
def get_repos(authorization: str = Header(...)):
  
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token format")

    token = authorization.split(" ")[1]

    result = GitHubService.get_repos(token)


    if result["error"]:
        raise HTTPException(
            status_code=result.get("status_code", 500),
            detail=result.get("message")
        )

    return result["data"]



@router.post("/issues")
def create_issue(
    request: CreateIssueRequest,
    authorization: str = Header(...)
):
    
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token format")

    token = authorization.split(" ")[1]

    result = GitHubService.create_issue(
        request.owner,
        request.repo,
        request.title,
        request.body,
        token
    )

    
    if result["error"]:
        raise HTTPException(
            status_code=result.get("status_code", 500),
            detail=result.get("message")
        )

    return result["data"]