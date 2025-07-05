from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/log-usage', methods=['GET', 'POST'])
def log_usage():
    feedback = None
    if request.method == 'POST':
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