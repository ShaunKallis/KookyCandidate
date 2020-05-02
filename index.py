from flask import Flask,render_template, make_response,request
from flask_bootstrap import Bootstrap
from policies import statements

# create an instance of the Flask class
app = Flask(__name__)
bootstrap = Bootstrap(app)
# route() decorator binds a function to a URL
@app.route("/set")
def setcookie():
    resp = make_response("setting cookie")
    resp.set_cookie('count','0')
    return resp

@app.route('/')
def home():
    count = request.cookies.get('count')
    return render_template('home.html', statements = statements, count = count)

@app.route('/policies')
def policies():
 return render_template('policies.html')

@app.route('/contribute')
def contribute():
 return render_template('contribute.html')
