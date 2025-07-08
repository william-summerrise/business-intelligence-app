from flask import Flask, render_template, request
import csv
import os
import json

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/log-usage', methods=['GET', 'POST'])
def log_usage():
    feedback = None
    if request.method == 'POST':
        # make sure all form inputs exist
        if not request.form['name'] or \
           not request.form['service'] or \
           not request.form['sector'] or \
           not request.form['date']:
            feedback = 'There was an error logging form data, make sure you filled in all fields correctly!'
        else:
            os.makedirs('log', exist_ok=True)
            with open('log/service-data.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                    request.form['name'],
                    request.form['service'],
                    request.form['sector'],
                    request.form['date']
                ])
            feedback = 'Service Data Logged!'

    return render_template('log-usage.html', feedback=feedback)

@app.route('/api/services')
def services_api():
    output = []
    with open('log/service-data.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            output.append({
                'name': row[0],
                'service': row[1],
                'sector': row[2],
                'date': row[3]
            })
    resp = app.make_response(json.dumps(output, separators=(',', ':')))
    resp.mimetype = 'text/json'
    return resp