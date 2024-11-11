from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-tokenizer")
def get_tokenizer():
    return "tokenizer", 200

@app.route("/get-model")
def get_model():
    return "onnx", 200

if __name__ == "__main__":
    app.run(debug=True)