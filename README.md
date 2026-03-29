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

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/enterSans/git_connector.git
cd app
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # For Linux/Mac
# venv\Scripts\activate    # For Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory and add:

```env
GITHUB_CLIENT_ID=your_client_id
GITHUB_CLIENT_SECRET=your_client_secret
GITHUB_REDIRECT_URI=http://localhost:8000/api/auth/callback
```

### 5. Run the server

```bash
uvicorn app.main:app --reload
```

### 6. Access the application

Open in browser:

```
http://127.0.0.1:8000/docs
```

🔑 Access Token Usage

To use the API endpoints, you must first obtain an access token via OAuth.

1. Steps to get access token:
2. Open the following URL in your browser:
```
http://127.0.0.1:8000/api/auth/login
```
3. Log in to GitHub and authorize the application.
4. After successful authentication, you will be redirected to:
```
/api/auth/callback
```
```
The response will contain:
{
  "access_token": "your_token_here"
}
```


## 📌 API Endpoints

### 🔐 Authentication

* **GET /api/auth/login**
  Redirects user to GitHub for authentication.

* **GET /api/auth/callback**
  Handles GitHub OAuth callback and returns access token.

---

### 📂 GitHub Operations

* **GET /api/github/repos**
  Fetches repositories of the authenticated user.
  **Header:**
  `Authorization: Bearer <access_token>`

---

* **POST /api/github/issues**
  Creates an issue in a repository.
  **Header:**
  `Authorization: Bearer <access_token>`
  **Body:**

  ```json
  {
    "owner": "username",
    "repo": "repo_name",
    "title": "Issue title",
    "body": "Issue description"
  }
  ```

---

* **GET /api/github/issues/{owner}/{repo}**
  Lists all issues for a given repository.
  **Header:**
  `Authorization: Bearer <access_token>`

---


* **POST /api/github/pull-request**
  Creates a pull request between branches.
  **Header:**
  `Authorization: Bearer <access_token>`
  **Body:**

  ```json
  {
    "owner": "username",
    "repo": "repo_name",
    "title": "PR title",
    "body": "PR description",
    "head": "feature-branch",
    "base": "main"
  }
  ```

