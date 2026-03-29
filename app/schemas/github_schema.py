from pydantic import BaseModel


class CreateIssueRequest(BaseModel):
    owner: str
    repo: str
    title: str
    body: str


class CreatePRRequest(BaseModel):
    owner: str
    repo: str
    title: str
    body: str
    head: str   
    base: str   