from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

job_description = "Looking for a data analyst with Python, SQL, and Excel experience."
cv_content = "I have used Python for data cleaning and visualization, and know Excel."

emb1 = model.encode(job_description, convert_to_tensor=True)
emb2 = model.encode(cv_content, convert_to_tensor=True)

score = util.cos_sim(emb1, emb2)
print(f"Match Score: {score.item():.2f}")
