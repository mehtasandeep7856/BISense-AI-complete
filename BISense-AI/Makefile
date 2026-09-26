install:
	pip install -r requirements.txt
ingest:
	python scripts/ingest_data.py
api:
	uvicorn backend.app.main:app --reload
test:
	pytest -q
frontend:
	cd frontend && npm install && npm run dev
