"""
This module provides a Flask server with an endpoint for emotion detection.
It accepts JSON data via a POST request, analyzes the emotional content of the text,
and returns the analysis results.
"""

from flask import Flask, jsonify, request
from EmotionDetection.detector import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=['POST'])
def sent_detector():
    """
    Process the POST request containing text to analyze its emotional content.

    Returns:
        JSON response containing the emotion scores or an error message if the
        input is invalid or missing.
    """
    data = request.json
    if not data or 'textToAnalyse' not in data or not data['textToAnalyse'].strip():
        return jsonify({'error': 'Invalid text! Please try again!'}), 400

    text_to_detect = data['textToAnalyse']
    response = emotion_detector(text_to_detect)
    if 'error' in response:
        return jsonify(response), 400
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
    