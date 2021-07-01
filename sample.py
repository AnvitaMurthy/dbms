from flask import Flask,render_template,request,url_for,flash,session,redirect
from flask_mysqldb import MySQL
from flask_jsglue import JSGlue

app=Flask(__name__)
app.secret_key='rkc31'
jsglue = JSGlue(app)


#configure db
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='thebasicbenzene31'
app.config['MYSQL_DB']='project'
app.config['SESSION_TYPE'] = 'filesystem'

mysql=MySQL(app)

@app.route('/',methods=['GET','POST'])

def index():
	flash('This is a flashed message')
	return render_template('demo2.html')

@app.route('/hello/<nm>',methods=['GET','POST'])
def hello(nm):
	para="chits"
	return render_template('demo3.html',nm=nm)


if __name__=='__main__':

	app.run(debug=True)

