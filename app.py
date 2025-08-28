import streamlit as st
import numpy as np
import pickle

# Load the trained model (make sure model.pkl exists in your project)
with open('diabetes_model.pkl', 'rb') as f:
    model = pickle.load(f)

# App title
st.title("🩺 Diabetes Checker")
st.write("Enter patient details below to predict diabetes status.")

# Collect user inputs
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1)
glucose = st.number_input("Glucose Level", min_value=0, max_value=300, value=120)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=200, value=70)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
insulin = st.number_input("Insulin", min_value=0, max_value=900, value=80)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.5)
age = st.number_input("Age", min_value=0, max_value=120, value=30)

# Prediction button
if st.button("🔍 Predict"):
    features = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, 
                          insulin, bmi, dpf, age]])
    prediction = model.predict(features)[0]

    if prediction == 1:
        st.error("⚠️ The patient is **Diabetic**.")
    else:
        st.success("✅ The patient is **Not Diabetic**.")
