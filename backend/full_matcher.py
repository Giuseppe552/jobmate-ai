import pdfplumber
from sentence_transformers import SentenceTransformer, util

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Extract text from your sample CV
cv_text = extract_text_from_pdf("demo_assets/sample_cv.pdf")

# Define a job description for testing
job_description = "We are looking for a social media manager with skills in SEO, content creation, ad management, and data analysis."

# Embed both texts
emb1 = model.encode(job_description, convert_to_tensor=True)
emb2 = model.encode(cv_text, convert_to_tensor=True)

# Compare embeddings
score = util.cos_sim(emb1, emb2)
print(f"Match Score: {score.item():.2f}")
