from flask import Flask, request, jsonify
import google.generativeai as genai
from PIL import Image
import io

app = Flask(__name__)

# Configure Google Gemini API
genai.configure(api_key="AIzaSyBUqdBI6pQ1TT3bSOJa3vs_cQhlirTXu60")
model = genai.GenerativeModel("gemini-1.5-pro")


def analyze_image(image, prompt):
    response = model.generate_content([image, prompt])
    return response.text


@app.route('/', methods=['GET'])
def home():
    return "Radiology AI Model is running!"


@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']
    image = Image.open(io.BytesIO(image_file.read()))

    prompt = """You are a highly experienced radiologist with expertise in interpreting a wide range of radiology investigations..."""  # Use your existing prompt

    result = analyze_image(image, prompt)

    return jsonify({'analysis': result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
