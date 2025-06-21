import streamlit as st
import pandas as pd
import joblib

from transformers import binary_cleanup

# Load the trained model
model = joblib.load('Attrition_Model.joblib')

# Set up the Streamlit app
st.title("Employee Attrition Prediction")
st.write("Enter employee information to predict if the employee will leave the company.")

# Input features
def user_input():
    BusinessTravel = st.selectbox("Business Travel", ['Travel_Rarely', 'Travel_Frequently', 'Non-Travel'])
    Department = st.selectbox("Department", ['Sales', 'Research & Development', 'Human Resources'])
    EducationField = st.selectbox("Education Field", ['Life Sciences', 'Medical', 'Marketing', 'Technical Degree', 'Other', 'Human Resources'])
    JobRole = st.selectbox("Job Role", ['Sales Executive', 'Research Scientist', 'Laboratory Technician',
                                        'Manufacturing Director', 'Healthcare Representative', 'Manager',
                                        'Sales Representative', 'Research Director', 'Human Resources'])
    MaritalStatus = st.selectbox("Marital Status", ['Single', 'Married', 'Divorced'])

    Gender = st.selectbox("Gender", ['Male', 'Female'])
    OverTime = st.selectbox("OverTime", ['Yes', 'No'])

    Age = st.slider("Age", 18, 60, 30)
    DailyRate = st.number_input("Daily Rate", value=800)
    DistanceFromHome = st.slider("Distance From Home", 1, 30, 5)
    Education = st.selectbox("Education Level", [1, 2, 3, 4, 5])
    EnvironmentSatisfaction = st.selectbox("Environment Satisfaction", [1, 2, 3, 4])
    HourlyRate = st.number_input("Hourly Rate", value=60)
    JobInvolvement = st.selectbox("Job Involvement", [1, 2, 3, 4])
    JobLevel = st.selectbox("Job Level", [1, 2, 3, 4, 5])
    JobSatisfaction = st.selectbox("Job Satisfaction", [1, 2, 3, 4])
    MonthlyIncome = st.number_input("Monthly Income", value=5000)
    MonthlyRate = st.number_input("Monthly Rate", value=15000)
    NumCompaniesWorked = st.slider("Number of Companies Worked", 0, 10, 2)
    PercentSalaryHike = st.slider("Percent Salary Hike", 10, 25, 15)
    PerformanceRating = st.selectbox("Performance Rating", [1, 2, 3, 4])
    RelationshipSatisfaction = st.selectbox("Relationship Satisfaction", [1, 2, 3, 4])
    StockOptionLevel = st.selectbox("Stock Option Level", [0, 1, 2, 3])
    TotalWorkingYears = st.slider("Total Working Years", 0, 40, 5)
    TrainingTimesLastYear = st.slider("Training Times Last Year", 0, 6, 3)
    WorkLifeBalance = st.selectbox("Work Life Balance", [1, 2, 3, 4])
    YearsAtCompany = st.slider("Years at Company", 0, 40, 5)
    YearsInCurrentRole = st.slider("Years in Current Role", 0, 18, 3)
    YearsSinceLastPromotion = st.slider("Years Since Last Promotion", 0, 15, 1)
    YearsWithCurrManager = st.slider("Years with Current Manager", 0, 17, 2)

    # Collecting inputs into a DataFrame
    data = pd.DataFrame({
        'BusinessTravel': [BusinessTravel],
        'Department': [Department],
        'EducationField': [EducationField],
        'JobRole': [JobRole],
        'MaritalStatus': [MaritalStatus],
        'Gender': [Gender],  
        'OverTime': [OverTime],
        'Age': [Age],
        'DailyRate': [DailyRate],
        'DistanceFromHome': [DistanceFromHome],
        'Education': [Education],
        'EnvironmentSatisfaction': [EnvironmentSatisfaction],
        'HourlyRate': [HourlyRate],
        'JobInvolvement': [JobInvolvement],
        'JobLevel': [JobLevel],
        'JobSatisfaction': [JobSatisfaction],
        'MonthlyIncome': [MonthlyIncome],
        'MonthlyRate': [MonthlyRate],
        'NumCompaniesWorked': [NumCompaniesWorked],
        'PercentSalaryHike': [PercentSalaryHike],
        'PerformanceRating': [PerformanceRating],
        'RelationshipSatisfaction': [RelationshipSatisfaction],
        'StockOptionLevel': [StockOptionLevel],
        'TotalWorkingYears': [TotalWorkingYears],
        'TrainingTimesLastYear': [TrainingTimesLastYear],
        'WorkLifeBalance': [WorkLifeBalance],
        'YearsAtCompany': [YearsAtCompany],
        'YearsInCurrentRole': [YearsInCurrentRole],
        'YearsSinceLastPromotion': [YearsSinceLastPromotion],
        'YearsWithCurrManager': [YearsWithCurrManager]
    })

    return data

# Get input
input_df = user_input()

# Show user inputs
st.subheader("Entered Data:")
st.write(input_df)

# Predict on button click
if st.button("Predict Attrition"):
    prediction = model.predict(input_df)
    st.subheader("Prediction Result:")
    if prediction[0] == 'Yes' or prediction[0] == 1:
        st.error("⚠️ The employee is likely to leave (Attrition = Yes)")
    else:
        st.success("✅ The employee is likely to stay (Attrition = No)")
