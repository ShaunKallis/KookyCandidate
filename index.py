from flask import Flask,render_template
from flask_bootstrap import Bootstrap


# create an instance of the Flask class
app = Flask(__name__)
bootstrap = Bootstrap(app)
# route() decorator binds a function to a URL
@app.route('/')
def home():
 return render_template('home.html')

@app.route('/policies')
def policies():
 return render_template('policies.html')

@app.route('/contribute')
def contribute():
 return render_template('contribute.html')
