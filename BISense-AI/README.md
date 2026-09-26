# BISense AI

A modular BIS knowledge assistant implementing conversational routing, specialized agents, hybrid RAG, OCR/label analysis, conservative compliance assistance, citations, freshness utilities, STT/TTS and FastAPI APIs.

## Run
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# set GROQ_API_KEY in .env
python scripts/ingest_data.py
uvicorn backend.app.main:app --reload
```
Frontend: `cd frontend && npm install && npm run dev`.

Install system packages: Tesseract OCR and FFmpeg.

The supplied BIS CSV datasets belong in `data/raw/`. The RAG pipeline also accepts PDFs under `data/documents/`.

Compliance output is deliberately conservative: OCR/image recognition does not by itself establish legal compliance.
