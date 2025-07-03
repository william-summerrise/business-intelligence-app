from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/log-usage', methods=['GET', 'POST'])
def log_usage():
    feedback = None
    if request.method == 'POST':
        print('Got service data:')
        print(f'  Name: {request.form["name"]}')
        print(f'  Service: {request.form["service"]}')
        print(f'  Sector: {request.form["sector"]}')
        print(f'  Date: {request.form["date"]}')
        feedback = 'Service Data Logged!'

    return render_template('log-usage.html', feedback=feedback)