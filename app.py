from flask import Flask, render_template, request, jsonify
import os
from model.ai_model import predict_image

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure uploads folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Upload + AI detection route
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Call AI model
        result, confidence = predict_image(filepath)

        # Return JSON (IMPORTANT for your UI)
        return jsonify({
            "result": result,
            "confidence": confidence
        })

    return jsonify({
        "error": "No file uploaded"
    })

# Run app
if __name__ == '__main__':
    if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)