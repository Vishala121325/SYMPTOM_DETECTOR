from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and label encoder
model = pickle.load(open('symptom_model.pkl', 'rb'))
label_encoder = pickle.load(open('label_encoder.pkl', 'rb'))

symptoms = ['fever', 'cough', 'fatigue', 'headache', 'runny_nose', 'sore_throat', 'nausea', 'diarrhea']

@app.route('/')
def home():
    return render_template('index.html', symptoms=symptoms)

@app.route('/predict', methods=['POST'])
def predict():
    input_feature = [int(request.form.get(symptom, 0)) for symptom in symptoms]
    prediction = model.predict([input_feature])[0]
    predicted_disease = label_encoder.inverse_transform([prediction])[0]
    
    return render_template('index.html', symptoms=symptoms, result=f"Predicted illness: {predicted_disease}")

if __name__ == '__main__':
    app.run(debug=True)
