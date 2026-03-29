# GitHub Connector API

## 🚀 Features

* OAuth 2.0 authentication with GitHub
* Fetch repositories
* Create issues
* List issues
* Create pull requests

## 🛠 Tech Stack

* Python
* FastAPI
* GitHub REST API

## ▶️ Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 🔐 Authentication

Authenticates users via GitHub and provides secure access using temporary access tokens.

## 📌 Endpoints

* GET /api/github/repos
* POST /api/github/issues
* GET /api/github/issues/{owner}/{repo}
* POST /api/github/pull-request
