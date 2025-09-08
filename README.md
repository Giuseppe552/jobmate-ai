# ⚠️ Project Moved

This repo is the **legacy prototype** of JobMate AI, built with Gradio/Hugging Face for a quick demo.  
It is no longer maintained.  

👉 Please see the **new, production-ready version** here:  
➡️ [JobMateAI (Next.js + FastAPI on Vercel/Render)](https://github.com/Giuseppe552/JobmateAI)  

**Live Demo**  
- Frontend: [Vercel App](https://jobmate-ai-six.vercel.app/)  
- Backend: [Render API](https://jobmateai-api.onrender.com/health)  

---

This old repo remains public for reference only.  


# 💼 JobMate AI

JobMate AI is a smart assistant that helps job seekers match their CVs to job descriptions using AI-powered similarity scoring.

🚀 Built with Python, Flask, React, and Hugging Face Transformers.

---

## ✨ Features

- 📄 Upload CV and job description (PDF or plain text)
- 🤖 Get an AI-generated match score between your CV and the job description
- 🧠 Semantic similarity powered by `sentence-transformers`
- 💻 Modern React frontend + Flask backend
- 🧪 Lightweight Gradio version for instant demos

---

## 🛠️ Technologies

- **Backend:** Python, Flask, `sentence-transformers`
- **Frontend:** React, Vite, JavaScript
- **PDF Parsing:** `pdfplumber`, `pdfminer.six`
- **Gradio App:** Deployed on Hugging Face Spaces  
- *(GitHub Actions CI/CD coming soon)*

---

## 🚀 Quickstart

1. **Clone the repo**  
   ```bash
   git clone https://github.com/Giuseppe552/jobmate-ai.git
  ```
**2. Set up the Python backend**
  ```bash
   cd backend
   pip install -r requirements.txt
  ```
**3. Start the React frontend**
  ```bash
   cd frontend/jobmate-ui
   npm install
   npm run dev
  ```



**🔀 Two Versions**

This repo contains two implementations:

Version	                     Tech Stack	                  Description
/backend + /frontend	         Flask + React	               Full-stack app with clean UI
/huggingface-version	         Gradio + Transformers	      Lightweight, fast demo version on Hugging Face


👉 Try the Gradio Demo on Hugging Face - (https://huggingface.co/spaces/giuseppe552/jobmate-ai))



📄 License
This project is licensed under the MIT License.


👤 Author
@Giuseppe552


This project was built to demonstrate my practical skills in full-stack development, NLP, and AI integration.
I'm open to junior/graduate roles in software engineering, AI/ML, or data science.



