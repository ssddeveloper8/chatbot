Steps

STEP 1 — Extract the ZIP
STEP 2 — Open Project in VS Code
STEP 3 — Install Python (Python 3.12)
STEP 4 — Create Virtual Environment
Open VS Code terminal:
	python -m venv venv
	- Activate Virtual Environment
	venv\Scripts\activate
STEP 5 — Install All Dependencies
pip install -r requirements.txt
STEP 6 — Install Ollama (LLM Engine)
link - https://ollama.com/download
Pull Model - 
	ollama pull mistral
Verify Ollama Running - You should see model name.
STEP 7 — Setup Database
databases.yaml -
  		host: localhost
  		port: 5432
  		user: postgres
  		password: your_password
  		database: your_db_name
Must match their PostgreSQL.
STEP 8 — Run Backend Server
Inside project folder: - Inside project folder (venv - should be activated) 
	Run - uvicorn app:app
Expected output:
Uvicorn running on http://127.0.0.1:8000
Application startup complete.
STEP 9 — Test API (Postman)
POST : http://127.0.0.1:8000/ask
