from flask import Flask, render_template, request
import numpy as np
import pickle
import json
import spacy
import joblib
import re
from unidecode import unidecode

# Carga el modelo en español
nlp = spacy.load("es_core_news_sm")

# NO FUNCIONA
def tokenizar(texto):
    return [token.text for token in nlp(texto) if not token.is_stop]

# NO FUNCIONA
def preprocessor(tokens):
    tokens = [re.sub('[\W]+', ' ', token.lower()) for token in tokens]
    tokens = [unidecode(token) for token in tokens]
    tokens = ['[NUM]' if re.match(r'\d+(\.\d+)?', token) else token for token in tokens]
    tokens = [token for token in tokens if token not in nlp.Defaults.stop_words]

    for i in range(len(tokens)):
        tokens[i] = tokens[i].replace('Ã¡', 'a')
        tokens[i] = tokens[i].replace('Ã©', 'e')
        tokens[i] = tokens[i].replace('Ã³', 'o')
        tokens[i] = tokens[i].replace('Ã±', 'ñ')
        tokens[i] = tokens[i].replace('Ã', 'i')

    return tokens

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        input_texts = request.form.getlist('text')

        # Realiza las predicciones para cada texto
        predictions = model.predict(input_texts)

        # Devuelve las predicciones en un formato adecuado
        response = {'predictions': predictions.tolist()}

        return json.dumps(response)
    else:
        return 'Unsupported method'

if __name__ == "__main__":
    app.run(debug=True)
