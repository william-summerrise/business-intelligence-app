from flask import Flask, render_template, request
import csv
import os
import json

app = Flask(__name__)

@app.route('/')
def home_page():
    """
        Renders the home page using the index.html template.

        This page has no special logic.
    """

    return render_template('index.html')

@app.route('/log-usage', methods=['GET', 'POST'])
def log_usage():
    """
        Renders the log usage form, with special handling for POST requests that
        take the submitted form data and writes it to log/service-data.csv
    """

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
    """
        Handles the services api by reading log/service-data.csv and converting
        it to a standard JSON format.
    """

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

@app.route('/summary')
def summary():
    """
        Renders the summary page by reading log/service-data.csv.

        The actual summary generation is handled in summary.html, not here.
    """

    data = []
    with open('log/service-data.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append({
                'name': row[0],
                'service': row[1],
                'sector': row[2],
                'date': row[3]
            })

    return render_template('summary.html', data=data)

@app.route('/log-engagement', methods=['GET', 'POST'])
def log_engagement():
    feedback = None
    if request.method == 'POST':
        if not request.form['method'] or \
           not request.form['time'] or \
           not request.form['notes']:
            feedback = 'There was an error logging form data, make sure you filled in all fields correctly!'
        else:
            os.makedirs('log', exist_ok=True)
            with open('log/engagement.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                    request.form['method'],
                    request.form['time'],
                    request.form['notes']
                ])
            feedback = 'Engagement Logged!'

    return render_template('log-engagement.html', feedback=feedback)

@app.route('/dashboard')
def dashboard():
    usage_data = []
    with open('log/service-data.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            usage_data.append({
                'name': row[0],
                'service': row[1],
                'sector': row[2],
                'date': row[3]
            })
    
    engagement_data = []
    with open('log/engagement.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            engagement_data.append({
                'method': row[0],
                'time': row[1],
                'notes': row[2]
            })

    return render_template('dashboard.html', usage_data=usage_data, engagement_data=engagement_data)

@app.route('/survey', methods=['GET', 'POST'])
def survey():
    feedback = None
    if request.method == 'POST':
        if not request.form['satisfaction'] or \
           not request.form['ease']:
            feedback = 'There was an error logging form data, make sure you filled in all fields correctly!'
        else:
            os.makedirs('log', exist_ok=True)
            with open('log/survey.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                    request.form['satisfaction'],
                    request.form['ease'],
                    request.form['suggestions']
                ])
            feedback = 'Thank you for taking the survey! Your feedback is appreciated.'

    return render_template('survey.html', feedback=feedback)