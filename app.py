import os
from flask import Flask, render_template, request, jsonify
from model_predictor import predict_image

app = Flask(__name__)

# Define the directory to save uploaded images
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    print('Request for index page received')
    return render_template('index.html')

@app.route('/RetinaAPI/v1/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected image'}), 400
    
    # Use the predict_image function from model_predictor.py
    predicted_class, confidence, predictions = predict_image(file)
    # print the results
    print("🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴")
    print('Predicted class:', predicted_class)
    print('Confidence:', confidence)
    print('Predictions:', predictions)
    print("🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴")

    # Return the predictions in JSON format
    return jsonify({'predicted_class': predicted_class, 'confidence': confidence, 'predictions': predictions})

if __name__ == '__main__':
    app.run(debug=True)
