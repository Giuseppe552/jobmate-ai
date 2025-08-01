# JobMate AI

JobMate AI is a smart assistant that helps job seekers match their CVs to job descriptions using AI-powered similarity scoring. Built with Python, Flask, React, and Transformers.

## Features

- 📄 Upload CV and job description (PDF & text)
- 🤖 Get an AI-generated match score between your CV and the job
- 🧠 Uses sentence transformers for semantic similarity
- ⚡ Modern React frontend + Flask backend

## Technologies

- Python, Flask, sentence-transformers
- React, Vite, JavaScript
- PDF parsing, semantic embeddings
- GitHub Actions (coming soon)

## Setup

1. Clone the repo  
   `git clone https://github.com/Giuseppe552/jobmate-ai.git`

2. Setup the Python backend  
   `cd backend && pip install -r requirements.txt`

3. Start the frontend  
   `cd frontend/jobmate-ui && npm install && npm run dev`

## License

This project is licensed under the [MIT License](LICENSE).

## Author

👤 [@Giuseppe552](https://github.com/Giuseppe552)

## 🔀 Two Versions

This repo contains two implementations:

- `backend/` and `frontend/` → Original Flask + React version
- `huggingface-version/` → Lightweight Gradio version deployed on Hugging Face

Check out the [Gradio demo here](https://huggingface.co/spaces/giuseppe552/jobmate-ai))

