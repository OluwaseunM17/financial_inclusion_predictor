import pandas as pd
import streamlit as st
import pickle
from PIL import Image
img = Image.open("fin_inclusion.jpeg")
model = pickle.load(open("fin_inc.pkl","rb"))
st.header("Financial Inclusion App")
st.image(img)
st.sidebar.header("Individual's metrics")
st.subheader("Introduction")
st.text("Financial inclusion is the availability and equality of opportunities "
        "to access financial services.\nThis webapp aims to be able to predict"
        " whether an individual possesses a bank account or not.")

def report():
    location_type = st.sidebar.radio("Select location type of individual",
                                     ("Rural","Urban"))
    if (location_type == "Rural"):
        location_type = 0
    else:
        location_type = 1
    cellphone_access = st.sidebar.selectbox("Does the Individual possess access "
                                            "to a cellphone", ("Yes", "No"))
    if cellphone_access == "No":
        cellphone_access = 0
    else:
        cellphone_access = 1
    age_of_respondent = st.sidebar.number_input("Enter age of the individual")
    gender = st.sidebar.radio("Select Gender of Individual ",("Female","Male"))
    if (gender == "Female"):
        gender_of_respondent = 0
    else:
        gender_of_respondent = 1
    e_level = st.sidebar.selectbox("Select individual's education level",
                                           ("No formal education",
                                            "Other/Dont know/RTA",
                                            "Primary education",
                                            "Secondary education",
                                            "Tertiary education",
                                            "Vocational/Specialised training"))
    if (e_level == "No formal education"):
        education_level = 0
    elif (e_level == "Other/Dont know/RTA"):
        education_level = 1
    elif (e_level == "Primary education"):
        education_level = 2
    elif (e_level == "Secondary education"):
        education_level = 3
    elif (e_level == "Tertiary education"):
        education_level = 4
    else:
        education_level = 5

    jt = st.sidebar.selectbox("Select Job Type",
                          ("Dont Know/Refuse to answer",
                           "Farming and Fishing",
                           "Formally employed Government",
                           "Formally employed Private",
                           "Government Dependent",
                           "Informally employed",
                           "No Income", "Other Income",
                           "Remittance Dependent", "Self employed"))
    if (jt == "Dont Know/Refuse to answer"):
        job_type = 0
    elif (jt == "Farming and Fishing"):
        job_type = 1
    elif (jt == "Formally employed Government"):
        job_type = 2
    elif (jt == "Formally employed Private"):
        job_type = 3
    elif (jt == "Government Dependent"):
        job_type = 4
    elif (jt == "Informally employed"):
        job_type = 5
    elif (jt == "No Income"):
        job_type = 6
    elif (jt == "Other Income"):
        job_type = 7
    elif (jt == "Self employed"):
        job_type = 8
    else:
        job_type = 9
    user_report = {
        'location_type': location_type,
        "cellphone_access": cellphone_access,
        "age_of_respondent": age_of_respondent,
        "gender_of_respondent": gender_of_respondent,
        "education_level": education_level,
        "job_type": job_type
    }
    data = pd.DataFrame(user_report, index=[0])
    return data

insta = report()

st.subheader("Individual's Summary")
st.write(insta)
if st.button("Predict"):
    answer = model.predict(insta)
    if (answer == 0):
        st.write("This individual does not possess a bank account.")
    else:
        st.write("This individual possesses a bank account.")
