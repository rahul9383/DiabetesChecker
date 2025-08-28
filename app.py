import streamlit as st
import numpy as np
import pickle

# Load the trained model (make sure diabetes_model.pkl exists in your project)
with open('diabetes_model1.pkl', 'rb') as f:
    model = pickle.load(f)

# App title
st.set_page_config(page_title="Diabetes Checker", page_icon="🩺", layout="centered")
st.title("🩺 Diabetes Checker")
st.markdown("### Enter patient details below to check diabetes risk.")

st.markdown("---")

# Sidebar for inputs
st.sidebar.header("🔢 Input Patient Data")

pregnancies = st.sidebar.text_input("Pregnancies")
glucose = st.sidebar.text_input("Glucose Level")
blood_pressure = st.sidebar.text_input("Blood Pressure")
skin_thickness = st.sidebar.text_input("Skin Thickness")
insulin = st.sidebar.text_input("Insulin")
bmi = st.sidebar.text_input("BMI")
dpf = st.sidebar.text_input("Diabetes Pedigree Function")
age = st.sidebar.text_input("Age")

# Prediction button
if st.button("🔍 Predict Diabetes"):
    try:
        # Convert all inputs to float
        features = np.array([[float(pregnancies), float(glucose), float(blood_pressure),
                              float(skin_thickness), float(insulin), float(bmi),
                              float(dpf), float(age)]])
        
        prediction = model.predict(features)[0]

        st.markdown("---")
        if prediction == 1:
            st.error("⚠️ The patient is **Diabetic**.")
        else:
            st.success("✅ The patient is **Not Diabetic**.")

    except ValueError:
        st.warning("⚠️ Please fill in all fields with valid numbers before predicting.")

# Footer
st.markdown("---")
