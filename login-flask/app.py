from flask import Flask
from flask import render_template,redirect,request,Response,session
from flask_mysqldb import MySQL,MySQLdb


app = Flask(__name__,template_folder='template')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'NOMBREBASE'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ =='__main__':
    app.secret_key="parkeadero_aragan"

    app.run(debug=True, host='0.0.0.0',port=5000, threaded=True)








