import { useState } from 'react';
import './App.css';

function App() {
  const [cvText, setCvText] = useState('');
  const [jobText, setJobText] = useState('');
  const [score, setScore] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setScore(null);
    setError('');

    try {
      const response = await fetch('http://127.0.0.1:5000/match', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          cv_text: cvText,
          job_description: jobText
        })
      });

      const data = await response.json();
      setScore(data.match_score.toFixed(2));
    } catch (err) {
      console.error(err);
      setError('Error connecting to server');
    }

    setLoading(false);
  };

  return (
    <div className="app-container">
      <h1>JobMate AI</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          placeholder="Paste your CV text here..."
          value={cvText}
          onChange={(e) => setCvText(e.target.value)}
        ></textarea>
        <textarea
          placeholder="Paste job description here..."
          value={jobText}
          onChange={(e) => setJobText(e.target.value)}
        ></textarea>
        <button type="submit" disabled={loading}>
          {loading ? 'Matching...' : 'Match CV to Job'}
        </button>
      </form>
      {score && <div className="score">Match Score: {score}</div>}
      {error && <div className="error">{error}</div>}
    </div>
  );
}

export default App;
