from flask import Flask,render_template,request,url_for,flash
from flask_mysqldb import MySQL

app=Flask(__name__)

#configure db
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='thebasicbenzene31'
app.config['MYSQL_DB']='dbms'
app.secret_key = 'super secret key2'

mysql=MySQL(app)

@app.route('/',methods=['GET','POST'])
def index():
	cur=mysql.connection.cursor()
	cur.execute("")
	return render_template('sample.html')

if __name__=='__main__':
	app.run(debug=True)