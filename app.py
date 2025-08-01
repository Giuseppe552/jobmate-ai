import gradio as gr
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def match_score(cv_text, job_description):
    if not cv_text or not job_description:
        return "Error: Missing input"

    embedding_1 = model.encode(cv_text, convert_to_tensor=True)
    embedding_2 = model.encode(job_description, convert_to_tensor=True)

    score = util.cos_sim(embedding_1, embedding_2).item()
    return f"Match Score: {score:.2f}"

demo = gr.Interface(
    fn=match_score,
    inputs=["text", "text"],
    outputs="text",
    title="JobMate AI",
    description="Enter a CV and Job Description to see how well they match."
)

demo.launch()
