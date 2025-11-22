📌 Employee Attrition Prediction – ML Pipeline

- This project predicts whether an employee will leave the company (Attrition) using Machine Learning. The dataset contains 1470 employee records with 35 features related to demographics, job satisfaction, salary, work environment, etc.


🚀 Tech Stack : 

- Python, Scikit-learn, Pandas, NumPy, Machine Learning Pipeline, Logistic Regression


📂 Project Workflow

- Data Loading & Exploration

- Feature Selection

- Dropped unnecessary features: EmployeeCount, Over18, StandardHours, EmployeeNumber

- Binary Column Encoding

- Gender → Male:1, Female:0

- OverTime → Yes:1, No:0

Preprocessing Pipelines

- Numerical → Median imputation + StandardScaler

- Categorical → Most frequent imputation + One-Hot Encoding

Final ML Pipeline

- Cleanup → Preprocessing → Logistic Regression model


Model Training & Evaluation

- full_pipeline.fit(x_train, y_train)



📊 Objective

- Predict if an employee is likely to leave the organization and help HR make proactive retention decisions.



📝 How to Run

- pip install -r requirements.txt

- streamlit run app.py



📦 Output

- Trained Attrition prediction model

- Preprocessed and transformed dataset

- Performance metrics on test data
