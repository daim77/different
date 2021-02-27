from flask import Flask


SECRET_MESSAGE = 'Babis je idiot a dela veci jen JAKO'
app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_secret_message():
    return SECRET_MESSAGE