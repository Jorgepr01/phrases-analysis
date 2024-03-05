from flask import Flask,render_template, request
from flask_mysqldb import MySQL
import app.database.queries as queries
import app.models.frases as frase
import app.models.conv as conv
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'Santa'
app.config['MYSQL_PASSWORD'] = '123'
app.config['MYSQL_DB'] = 'sentimientos'    

mysql = MySQL(app)


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

@app.route("/get-frase", methods=["POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    mensaje3 = frase.AnalisisFrases()
    mens=mensaje3.psicologo(msg)
    talk=queries.eventsTalk(mysql)
    talk.insetar(1,2,"2024-02-28")
    return mens[2]

@app.route("/get-conv", methods=["POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    mensaje3 = frase.AnalisisFrases()
    mens=mensaje3.psicologo(msg)
    talk=queries.eventsTalk(mysql)
    talk.insetar(1,2,"2024-02-28")
    return mens[2]

if __name__ == '__main__':
    app.run(debug=True)