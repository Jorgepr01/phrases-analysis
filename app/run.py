from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Home')
def home():
    return render_template('home.html')

@app.route('/Diary')
def Diary():
    return render_template('Diary.html')

@app.route('/Phrases')
def Phrases():
    return render_template('Phrases.html')

@app.route('/Conversations')
def Conversations():
    return render_template('Conversations.html')



if __name__ == '__main__':
    app.run(debug=True)