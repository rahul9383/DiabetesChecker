import streamlit as st
import numpy as np
import pickle

# Load the trained model (make sure diabetes_model.pkl exists in your project)
with open('diabetes_model1.pkl', 'rb') as f:
    model = pickle.load(f)

# App title
st.title("🩺 Diabetes Checker")
st.write("Enter patient details below to predict diabetes status.")

# Collect user inputs (start blank)
pregnancies = st.text_input("Pregnancies")
glucose = st.text_input("Glucose Level")
blood_pressure = st.text_input("Blood Pressure")
skin_thickness = st.text_input("Skin Thickness")
insulin = st.text_input("Insulin")
bmi = st.text_input("BMI")
dpf = st.text_input("Diabetes Pedigree Function")
age = st.text_input("Age")

# Prediction button
if st.button("🔍 Predict"):
    try:
        # Convert all inputs to float
        features = np.array([[int(pregnancies), float(glucose), float(blood_pressure),
                              float(skin_thickness), float(insulin), float(bmi),
                              float(dpf), int(age)]])
        
        prediction = model.predict(features)[0]

        if prediction == 1:
            st.success("⚠️ The patient is **Diabetic**.")
        else:
            st.success("✅ The patient is **Not Diabetic**.")
    except ValueError:
        st.warning("⚠️ Please fill in all fields with valid numbers before predicting.")
