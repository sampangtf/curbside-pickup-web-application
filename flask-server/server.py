from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def hello():
    return {"restaurants": ["r1", "r2", "r3", "r4"]}


if __name__ == "__main__":
    app.run(debug=True)
