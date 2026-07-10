import streamlit as st

import joblib
import pandas as pd

model = joblib.load("model/best_model.pkl")
scaler = joblib.load("model/scaler.pkl")

st.set_page_config(
    page_title="Student Placement Prediction",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Placement Prediction")

st.header("Enter Student Details")

age = st.number_input("Age", 18, 30)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

degree = st.selectbox(
    "Degree",
    ["B.Tech", "BCA", "MCA", "B.Sc"]
)

branch = st.selectbox(
    "Branch",
    ["CSE", "ECE", "EEE", "ME", "CE"]
)

cgpa = st.number_input(
    "CGPA",
    min_value=0.0,
    max_value=10.0,
    value=7.0
)

internships = st.number_input(
    "Internships",
    min_value=0,
    max_value=10,
    value=0
)

projects = st.number_input(
    "Projects",
    min_value=0,
    max_value=20,
    value=0
)

coding = st.slider(
    "Coding Skills",
    1,
    10,
    5
)

communication = st.slider(
    "Communication Skills",
    1,
    10,
    5
)

aptitude = st.slider(
    "Aptitude Test Score",
    0,
    100,
    50
)

soft = st.slider(
    "Soft Skills Rating",
    1,
    10,
    5
)

certifications = st.number_input(
    "Certifications",
    min_value=0,
    max_value=20,
    value=0
)

backlogs = st.number_input(
    "Backlogs",
    min_value=0,
    max_value=10,
    value=0
)
gender_map = {"Male": 1, "Female": 0}
degree_map = {"B.Tech": 0, "BCA": 1, "MCA": 2, "B.Sc": 3}
branch_map = {"CSE": 0, "ECE": 1, "EEE": 2, "ME": 3, "CE": 4}
if st.button("Predict Placement"):

    # convert input into correct format (EXACT column order)
    input_data = [[
        age,
        gender_map[gender],
        degree_map[degree],
        branch_map[branch],
        cgpa,
        internships,
        projects,
        coding,
        communication,
        aptitude,
        soft,
        certifications,
        backlogs
    ]]

    # scale input
    input_scaled = scaler.transform(input_data)

    # predict
    prediction = model.predict(input_scaled)

    # show result
    if prediction[0] == 1:
        st.success("🎉 Student WILL be PLACED")
    else:
        st.error("❌ Student will NOT be placed")






