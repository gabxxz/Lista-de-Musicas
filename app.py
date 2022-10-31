from flask import Flask 

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello,Web!'

def bye():

app.run(debug=True)