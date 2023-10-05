from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route("/test")
def test():
   return "<h1 style='color:blue'>Hello from Test!</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

