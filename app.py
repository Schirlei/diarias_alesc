from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Os gastos dos deputados catarinenses com diárias.</p>"
