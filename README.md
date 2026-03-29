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


## 📌 Endpoints

* GET /api/github/repos
* POST /api/github/issues
* GET /api/github/issues/{owner}/{repo}
* POST /api/github/pull-request
