import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

with open('model/frequent_itemsets.pkl', 'rb') as f:
    frequent_itemsets = pickle.load(f)

with open('model/rules.pkl', 'rb') as f:
    rules = pickle.load(f)

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
        user_tracks = data.get("tracks", [])

        if not user_tracks:
            return jsonify({"error": "No tracks provided."}), 400
        
        recommendations = []

        for rule in rules_list:
            if set(rule["antecedents"]).issubset(set(user_tracks)) or set(user_tracks).issubset(set(rule["antecedents"])):
                recommendations.append({
                    "recommendation": rule["consequents"],
                    "confidence": rule["confidence"]
                })
        
        recommendations.sort(key=lambda x: x["confidence"], reverse=True)

        return jsonify(recommendations)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)