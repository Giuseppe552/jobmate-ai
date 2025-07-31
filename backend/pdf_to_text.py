import pdfplumber

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:  # check it's not None
                text += page_text + "\n"
    return text

if __name__ == "__main__":
    cv_text = extract_text_from_pdf("demo_assets/sample_cv.pdf")
    print("Extracted CV Text:\n")
    print(cv_text[:1000])  # show first 1000 characters only
