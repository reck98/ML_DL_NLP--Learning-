from flask import Flask, render_template, request, redirect, url_for


PORT = 5050

app = Flask(__name__)

@app.route('/')
def home():
    return {
        'message' : 'Hello From reck98'
    }

@app.route('/index', methods = ['GET'])
def index():
    return render_template('index.html')
    
@app.route('/form', methods = ['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        return f"Hello {name}"
    
      
    return render_template('form.html')


@app.route('/success/<score>')
def success(score):
    return f"Your score is {score}"

@app.route('/sucif/<score>/<name>')
def sucif(score, name):
    return render_template('sucif.html', results = int(score), name = name)


@app.route('/submit', methods = ['GET', 'POST'])
def submit():
    if request.method == 'GET':
        return render_template('submit.html')
    
    
    DSA = float(request.form.get('DSA'))
    ML = float(request.form.get('ML'))
    CP = float(request.form.get('CP'))
    name = str(request.form.get('name'))
    tot = DSA + CP + ML
    avg = int(tot/3)

    return redirect(url_for('sucif', score = avg, name = name))


if __name__ == "__main__":
    app.run(debug=True, port=PORT)