from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
	return render_template('home.html')

@app.route('/aboutme')
def about():
	return render_template('aboutme.html')

@app.route('/results')
def results():
	return render_template('results.html')

@app.route('/methodology')
def methodology():
	return render_template('methodology.html')

@app.route('/researchquestion')
def researchquestion():
	return render_template('researchquestion.html')

if __name__ == '__main__':
	app.run(debug=True)