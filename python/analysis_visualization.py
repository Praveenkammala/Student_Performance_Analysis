import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
marks = pd.read_csv("../data/cleaned/marks_cleaned.csv")
exams = pd.read_csv("../data/cleaned/exams_cleaned.csv")

# -----------------------------
# ANALYSIS
# -----------------------------

# Average marks by subject
avg_subject = marks.groupby("subject")["marks"].mean()

# Bar Chart: Average Marks
avg_subject.plot(kind="bar")
plt.title("Average Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()

# Scatter Plot: Attendance vs Marks
plt.scatter(marks["attendance"], marks["marks"])
plt.title("Attendance vs Marks")
plt.xlabel("Attendance (%)")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()

# Pass vs Fail count
result_count = exams["result"].value_counts()

# Pie Chart: Pass vs Fail
result_count.plot(kind="pie", autopct="%1.1f%%")
plt.title("Pass vs Fail Distribution")
plt.ylabel("")
plt.tight_layout()
plt.show()
