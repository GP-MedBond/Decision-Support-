import pandas as pd

# Load the dataset
file_path = "/content/GP-2025.xlsx"  # Ensure the file is in the same folder as your script
df = pd.read_excel(file_path, sheet_name="Main data")

# Define a function to classify insurance risk
def classify_insurance_risk(row):
    bmi = row["BMI"]
    chronic_disease = row["Chronic_Disease"]
    smoker = row["smoker"]
    hemoglobin = row["Hemoglobin_g_dL"]
    wellness_score = row["Wellness score"]

    # Rule 1: High Risk
    if bmi > 30 and chronic_disease == "Yes":
        return "High Risk", "Increase Insurance Cost by 30%"

    # Rule 2: Moderate Risk
    if smoker == "Yes" and hemoglobin < 12:
        return "Moderate Risk", "Increase Insurance Cost by 15%"

    # Rule 3: Low Risk
    if wellness_score > 80:
        return "Low Risk", "Decrease Insurance Cost by 10%"

    # Default: Moderate Risk
    return "Moderate Risk", "No Change"

# Apply the function to each row in the DataFrame
df["Insurance Risk"], df["Insurance Suggestion"] = zip(*df.apply(classify_insurance_risk, axis=1))

# Save the updated DataFrame in the same directory as the script
output_path = "Insurance_Risk_Analysis.xlsx"
df.to_excel(output_path, index=False)

print(f"Processing complete. Results saved to {output_path}")
