from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html.jinja')

@app.route('/sql-injection')
def sql_injection():
    print(request.endpoint)
    return render_template('sql-injection.html.jinja')

@app.route('/cross-site-scripting')
def xss():
    return render_template('xss.html.jinja')

@app.route('/cross-site-request-forgery')
def xsrf():
    return render_template('xsrf.html.jinja')

@app.route('/xsrf-data')
def xsrf_data():
    return {
        'data': 'This is an example of using JSON in an API.'
    }
