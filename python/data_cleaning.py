import pandas as pd

# Load raw datasets
students = pd.read_csv("../data/raw/students_large_raw.csv")
marks = pd.read_csv("../data/raw/marks_large_raw.csv")
exams = pd.read_csv("../data/raw/exams_large_raw.csv")

print("Raw data loaded successfully")

# -----------------------------
# DATA CLEANING & VALIDATION
# -----------------------------

# Fill missing age with average age
students["age"].fillna(round(students["age"].mean()), inplace=True)

# Fill missing marks with subject-wise average
marks["marks"] = marks.groupby("subject")["marks"].transform(
    lambda x: x.fillna(round(x.mean()))
)

# Remove duplicates
students.drop_duplicates(inplace=True)
marks.drop_duplicates(inplace=True)
exams.drop_duplicates(inplace=True)

# Save cleaned data
students.to_csv("../data/cleaned/students_cleaned.csv", index=False)
marks.to_csv("../data/cleaned/marks_cleaned.csv", index=False)
exams.to_csv("../data/cleaned/exams_cleaned.csv", index=False)

print("Data cleaning completed successfully")
