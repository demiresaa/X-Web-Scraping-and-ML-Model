from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)
CORS(app)

# Model ve Vectorizer'ı yükle
model = pickle.load(open("akp.pickle", "rb"))
vectorizer = pickle.load(open("vectorizer.pickle", "rb"))

@app.route('/')
def home():
    return "Flask uygulaması çalışıyor!"
@app.route('/predict', methods=['POST'])
def predict():
    # İstekten JSON veri al
    data = request.json['text']
    
    # Metni vektörize et
    metin_dokuman = vectorizer.transform([data])
    
    # Tahmin yap
    y_pred = model.predict(metin_dokuman.toarray())
    
    # NumPy int64 türünü Python int türüne dönüştür
    prediction = int(y_pred[0])
    
    # Tahmin sonucunu JSON formatında döndür
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
