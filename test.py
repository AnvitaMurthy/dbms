from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def shashank():
	return render_template('sample.html',name="Anvita")

@app.route('/p2')
def shashank2():
	return '<h1>Page 2</h1>'
if __name__ == '__main__':
   app.run(debug = True)