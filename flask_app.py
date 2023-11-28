from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Wat is dit leuk om te doen zeg!</p>