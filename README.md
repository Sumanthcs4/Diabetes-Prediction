# Diabetes Prediction Using Pima Indian Health Data

This project is aimed at predicting the likelihood of diabetes in patients using a machine learning approach on the Pima Indians Diabetes Database. The final model, **XGBoost**, is deployed in a simple and user-friendly Flask web application for real-time predictions based on user input.

## Project Overview

- **Objective**: Predict the probability of diabetes based on medical and demographic factors (e.g., age, BMI, glucose levels).
- **Dataset**: Pima Indians Diabetes Database, containing various medical attributes.
- **Technology Stack**: Python, Flask, XGBoost, scikit-learn, HTML/CSS.

## Key Features

- **Data Preprocessing**: Handles missing values, scales features, and prepares data for modeling.
- **Model Selection**: Various classification models were evaluated, with **XGBoost** chosen as the final model due to superior performance.
- **Deployment**: Flask application allows for predictions based on user-provided health metrics.
- **User Interface**: Interactive and visually appealing UI for ease of use.

## Getting Started

### Prerequisites

- Python 3.7 or above
- Git

### Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Sumanthcs4/Diabetes-Prediction.git
   cd Diabetes-Prediction
Diabetes Prediction Using Pima Indian Health Data

This project is aimed at predicting the likelihood of diabetes in patients using a machine learning approach on the Pima Indians Diabetes Database. The final model, XGBoost, is deployed in a simple and user-friendly Flask web application for real-time predictions based on user input.
Project Overview

    Objective: Predict the probability of diabetes based on medical and demographic factors (e.g., age, BMI, glucose levels).
    Dataset: Pima Indians Diabetes Database, containing various medical attributes.
    Technology Stack: Python, Flask, XGBoost, scikit-learn, HTML/CSS.

Key Features

    Data Preprocessing: Handles missing values, scales features, and prepares data for modeling.
    Model Selection: Various classification models were evaluated, with XGBoost chosen as the final model due to superior performance.
    Deployment: Flask application allows for predictions based on user-provided health metrics.
    User Interface: Interactive and visually appealing UI for ease of use.

Getting Started
Prerequisites

    Python 3.7 or above
    Git

Instructions

    Clone the Repository:

git clone https://github.com/Sumanthcs4/Diabetes-Prediction.git
cd Diabetes-Prediction

Set Up the Virtual Environment:

python -m venv venv
source venv/bin/activate  # On Windows: `venv\Scripts\activate`

Install Required Packages:

pip install -r requirements.txt

Run the Flask Application:

    python flask_app/app.py

    Access the Application: Open your browser and navigate to http://127.0.0.1:5000/ to use the prediction tool.

Project Structure

    flask_app/: Flask application code, including:
        app.py: Main application file.
        templates/: HTML templates for web pages.
        static/: Static files, such as CSS for styling.
    notebooks/: Jupyter notebook for exploratory data analysis (EDA) and model training.
    data/: Dataset (diabetes.csv).
    requirements.txt: List of packages needed for the project.
