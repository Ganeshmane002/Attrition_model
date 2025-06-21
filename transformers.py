from sklearn.preprocessing import FunctionTransformer

drop_cols = ['EmployeeCount', 'StandardHours', 'Over18', 'EmployeeNumber']

def binary_cleanup(data):
    data = data.copy()

    # Map categorical columns
    data['Gender'] = data['Gender'].map({'Male': 1, 'Female': 0})
    data['OverTime'] = data['OverTime'].map({'Yes': 1, 'No': 0})

    # Check for existing columns before dropping
    existing_cols = [col for col in drop_cols if col in data.columns]
    
    # Drop only the existing columns
    if existing_cols:
        data = data.drop(columns=existing_cols)

    return data

binary_transformer = FunctionTransformer(binary_cleanup)
