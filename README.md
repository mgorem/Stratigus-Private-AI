# Stratigus Private AI Agent

Local-first “Private AI” web analysis agent powered by LM Studio (local LLM).  
Includes run history, privacy guardrails (PII detection + optional redaction + no-store mode), and both web UI + desktop GUI.

## Architecture
- Frontend: React (Vite)
- Backend: Flask API
- Local LLM: LM Studio (local inference)
- Storage: SQLite (runs.db) for run history

## Prerequisites
- Python 3.10+ (Windows)
- Node.js 18+ (for React)
- LM Studio installed and a model downloaded (e.g. qwen2.5-vl-7b-instruct)

## Quick Start (Local Dev)

### 1) Start LM Studio
- Load the model
- Ensure the LM Studio local server is available

### 2) Backend
```powershell
cd backend
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
