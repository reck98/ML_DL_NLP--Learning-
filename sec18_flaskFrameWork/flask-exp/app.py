from flask import Flask, render_template

PORT = 5150
app = Flask(__name__)

@app.route('/')
def home():
    return 'Home'

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=PORT)