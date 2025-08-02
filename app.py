from flask import Flask, render_template 
from flask import request
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from sklearn.impute import SimpleImputer
import warnings
warnings.filterwarnings('ignore')
import joblib
import adult_preprocessing as ap
import children_preprocesing as cp

app = Flask(__name__)

# Load the trained model and columns
adult_model = joblib.load('lr_model_for_adult.pkl')
child_model = joblib.load('lr_model_for_children.pkl')


@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')



@app.route('/adult_index', methods=['GET', 'POST'])
def adult_predict():
    if request.method == 'POST':
        # Get form values
        gender = request.form['gender']
        jundice_yes = int(request.form['jaundise'])
        autism = request.form['autism']
        relation = request.form['relation']
        result = int(request.form['result'])
        ethnicity = request.form['ethnicity']
        contry_of_res = request.form['contry_of_res']
        A1_Score = int(request.form['A1_Score'])
        A2_Score = int(request.form['A2_Score'])
        A3_Score = int(request.form['A3_Score'])
        A4_Score = int(request.form['A4_Score'])
        A5_Score = int(request.form['A5_Score'])
        A6_Score = int(request.form['A6_Score'])
        A7_Score = int(request.form['A7_Score'])
        A8_Score = int(request.form['A8_Score'])
        A9_Score = int(request.form['A9_Score'])
        A10_Score = int(request.form['A10_Score'])

        # Create dictionaries
        scores_dict = ap.create_score_dict(A1_Score, A2_Score, A3_Score, A4_Score, A5_Score, 
                                           A6_Score, A7_Score, A8_Score, A9_Score, A10_Score)

        ethnicity_dict = ap.create_ethnicity_dict(ethnicity)
        relation_dict = ap.create_relation_dict(relation)
        gender_dict = ap.create_gender_dict(gender)
        autism_dict = ap.create_autism_dict(autism)
        scaled_values = ap.minmax_scaling(result)
        country_dict = ap.create_country_dict(contry_of_res)

        # Combine data into a single dictionary
        data = {**scores_dict, **scaled_values, **gender_dict, **ethnicity_dict, 
                'jundice_yes': jundice_yes, **autism_dict, **country_dict, **relation_dict}

        # Convert to DataFrame for model prediction
        data = pd.DataFrame([data])

        # Make prediction
        prediction_result = adult_model.predict(data)

        if prediction_result[0] == 1:
            prediction = 'The Adult is likely to have autism.'
        else:
            prediction = 'The Adult is unlikely to have autism.'

        return render_template('adult_index.html', prediction=prediction)
    else:
        return render_template('adult_index.html')
    




@app.route('/child_index', methods=['GET', 'POST'])
def child_predict():
    if request.method == 'POST':
        # Get form values
        Age_Mons = int(request.form['Age_Mons']) * 12
        gender = request.form['gender']
        jundice_yes = int(request.form['jaundise'])
        autism = request.form['autism']
        relation = request.form['relation']
        result = int(request.form['result'])
        ethnicity = request.form['ethnicity']
        contry_of_res = request.form['contry_of_res']
        A1_Score = int(request.form['A1_Score'])
        A2_Score = int(request.form['A2_Score'])
        A3_Score = int(request.form['A3_Score'])
        A4_Score = int(request.form['A4_Score'])
        A5_Score = int(request.form['A5_Score'])
        A6_Score = int(request.form['A6_Score'])
        A7_Score = int(request.form['A7_Score'])
        A8_Score = int(request.form['A8_Score'])
        A9_Score = int(request.form['A9_Score'])
        A10_Score = int(request.form['A10_Score'])

        # Create dictionaries
        scores_dict = cp.create_score_dict(A1_Score, A2_Score, A3_Score, A4_Score, A5_Score, 
                                           A6_Score, A7_Score, A8_Score, A9_Score, A10_Score)

        ethnicity_dict = cp.create_ethnicity_dict(ethnicity)
        relation_dict = cp.create_relation_dict(relation)
        gender_dict = cp.create_gender_dict(gender)
        autism_dict = cp.create_autism_dict(autism)
        scaled_values = cp.minmax_scaling(Age_Mons, result)
        country_dict = cp.create_country_dict(contry_of_res)

        # Combine data into a single dictionary
        data = {**scores_dict, **scaled_values, **gender_dict, **ethnicity_dict, 
                'jundice_yes': jundice_yes, **autism_dict, **country_dict, **relation_dict}

        # Convert to DataFrame for model prediction
        data = pd.DataFrame([data])

        # Make prediction
        prediction_result = child_model.predict(data)

        if prediction_result[0] == 1:
            prediction = 'The child is likely to have autism.'
        else:
            prediction = 'The child is unlikely to have autism.'

        return render_template('child_index.html', prediction=prediction)
    else:
        return render_template('child_index.html')

        
if __name__ == "__main__":
    app.run(debug=True)