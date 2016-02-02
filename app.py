from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "What a wonderful world Shipped is?"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
