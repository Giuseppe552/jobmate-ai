from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer, util
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

@app.route('/match', methods=['POST'])
def match():
    data = request.json
    cv_text = data.get('cv_text')
    job_description = data.get('job_description')

    if not cv_text or not job_description:
        return jsonify({'error': 'Missing data'}), 400

    embedding_1 = model.encode(cv_text, convert_to_tensor=True)
    embedding_2 = model.encode(job_description, convert_to_tensor=True)

    score = util.cos_sim(embedding_1, embedding_2).item()

    return jsonify({'match_score': score})

if __name__ == '__main__':
    app.run(debug=True)
