import ast
import json
import os
import subprocess
from urllib.parse import parse_qs, urlencode
from flask import Flask, render_template, request, redirect, session, url_for

from diagnosis_rules import diagnose

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user information from the initial form
        user_info = {
            'name': request.form.get('name'),
            'car_model': request.form.get('car_model'),
            'make': request.form.get('make'),
            'year': request.form.get('year'),
            'mileage': request.form.get('mileage'),
            'date_of_diagnosis': request.form.get('date_of_diagnosis')
        }

        # Remove None values from the user_info dictionary
        user_info = {key: value for key, value in user_info.items() if value is not None}
        print('userInfoSent', user_info)
        # Redirect to the /diagnosis route with the user_info included in the URL path
        return redirect(url_for('diagnosis', **user_info))

    return render_template('index.html')

@app.route('/diagnosis', methods=['GET', 'POST'])
def diagnosis():
    if request.method == 'POST':
        # Extract symptoms directly from the form data
        symptoms = {key: request.form.getlist(key) for key in request.form}

        # Get user information from the session
        user_info = session.get('user_info', {})
        print('user_info_in diagnosis route:', user_info)
        print('requestBoody', request.args.get('name'))
        # Combine user information and diagnosis symptoms
        data = {
            'user_info': user_info,
            'symptoms': symptoms
        }

        # Redirect to the /explanation route with the encoded data
        return redirect(url_for('explanation', data=json.dumps(data)))

    # Handle GET request parameters
    user_info = {
        'name': request.args.get('name'),
        'car_model': request.args.get('car_model'),
        'make': request.args.get('make'),
        'year': request.args.get('year'),
        'mileage': request.args.get('mileage'),
        'date_of_diagnosis': request.args.get('date_of_diagnosis')
    }

    # Store user information in the session
    session['user_info'] = user_info
    print('user_info_in diagnosis get route:', user_info)

    return render_template('diagnosis.html', user_info=user_info)

@app.route('/explanation', methods=['GET'])
def explanation():
    # Retrieve user information and symptoms from the URL query string
    user_info = {key: request.args.get(key) for key in ['name', 'car_model', 'make', 'year', 'mileage', 'date_of_diagnosis']}
    symptoms_data_str = request.args.get('data', '{}')

    # Parse JSON string to a Python dictionary
    symptoms_data_dict = json.loads(symptoms_data_str)

    # Extract user_info and symptoms from the dictionary
    user_info.update(symptoms_data_dict.get('user_info', {}))
    symptoms = symptoms_data_dict.get('symptoms', {})

    # Call the diagnose function with user_info and symptoms
    diagnosis_result = diagnose(user_info=user_info, symptoms=symptoms)

    # Extract symptoms_diagnosis from the diagnosis result
    symptoms_diagnosis = diagnosis_result.get('symptoms_diagnosis', [])

    # Pass the diagnosis result and symptoms_diagnosis to the template
    return render_template('explanation.html', user_info=user_info, diagnosis_result=diagnosis_result, symptoms_diagnosis=symptoms_diagnosis)

@app.route('/streamlit', methods=['GET'])
def streamlit_integration():
    # Run Streamlit app as a subprocess
    subprocess.Popen(['streamlit', 'run', 'streamlit_app.py'])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
