from app.facialRecognition import recognition
from flask import render_template, request, redirect, url_for
from app import create_app 
import cv2

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    if 'file' not in request.files:
        return redirect(url_for('index'))

    file = request.files['file']

    if file.filename == '':
        return redirect(url_for('index'))

    # Lógica de reconocimiento facial con OpenCV
    # (Aquí deberías agregar la lógica para el reconocimiento facial)

    return render_template('index.html', result='Reconocimiento Facial Exitoso')
