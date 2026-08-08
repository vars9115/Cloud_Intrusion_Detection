from flask import Flask, render_template, request, jsonify
from detection import detect_intrusion

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/detect", methods=["POST"])
def detect():
    data = request.get_json()

    result = detect_intrusion(data)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)