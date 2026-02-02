from flask import Flask, render_template

PORT = 5050


app = Flask(__name__)

@app.route('/')
def home():
    return {
        'message' : 'Hello from reck98 they this '
    }


@app.route('/index')
def route():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(port=PORT, debug=True)