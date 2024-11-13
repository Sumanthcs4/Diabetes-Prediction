import numpy as np
import pandas as pd
import joblib
from flask import Flask, request, render_template

# Initialize the Flask app with a custom template folder
app = Flask(__name__, template_folder='templates')  # Adjust path if needed

# Load the trained model (replace with the correct model path if necessary)
model = joblib.load('xgb_model.pkl')

# Define the home route
@app.route('/')
def home():
    # Get the template path
    template_path = app.jinja_env.loader.get_source(app.jinja_env, 'index.html')[0]
    print(f"Trying to render template from: {template_path}")

    return render_template('index.html')  # Display the input form

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the form
        pregnancies = int(request.form['pregnancies'])
        glucose = int(request.form['glucose'])
        blood_pressure = int(request.form['blood_pressure'])
        skin_thickness = int(request.form['skin_thickness'])
        insulin = int(request.form['insulin'])
        bmi = float(request.form['bmi'])
        diabetes_pedigree_function = float(request.form['diabetes_pedigree_function'])
        age = int(request.form['age'])

        # Create an array from the inputs
        input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])

        # Make a prediction using the trained model
        prediction = model.predict(input_data)
        probability = model.predict_proba(input_data)[0][1] * 100  # Probability of being diabetic

        # Determine the prediction label (0 = Not Diabetic, 1 = Diabetic)
        prediction_text = "Diabetic" if prediction[0] == 1 else "Not Diabetic"

        # Create a message to display alongside the prediction (e.g., medical advice)
        message = "We recommend consulting a doctor for further tests and advice." if prediction[0] == 1 else "You are not diabetic. Maintain a healthy lifestyle."

        # Return the result to the result.html template
        return render_template('result.html', prediction=prediction_text, probability=round(probability, 2), message=message)

    except Exception as e:
        # Handle any errors that may occur during prediction
        return str(e)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)