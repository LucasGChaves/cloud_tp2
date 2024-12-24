import pickle
import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

app = Flask(__name__)

with open('/pickle/rules.pkl', 'rb') as f:
    rules = pickle.load(f)

with open('/pickle/date.pkl', 'rb') as f:
    date = pickle.load(f)

rules_list = [
    {
        "antecedents": list(rule['antecedents']),
        "consequents": list(rule['consequents']),
        "confidence": rule['confidence']
    }
    for _, rule in rules.iterrows()
]

@app.route("/", methods=["GET"])
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/recommend", methods=["POST"])
def recommend():
    try:
        data = request.json
        user_songs = data.get("songs", [])

        if not user_songs:
            return jsonify({"error": "No tracks provided."}), 400
        
        recommendations = []

        for rule in rules_list:
            if set(rule["antecedents"]).issubset(set(user_songs)) or set(user_songs).issubset(set(rule["antecedents"])):
                recommendations = recommendations + list(rule["consequents"])

        response = {
            "songs": recommendations,
            "version": os.getenv("VERSION"),
            "model_date": date
        }

        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")