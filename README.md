# Student Performance Data Analysis Project

## 📌 Project Overview
This project is an end-to-end data analysis solution designed to analyze student academic performance using Python, SQL, and Microsoft Excel. The project focuses on cleaning raw academic data, identifying performance trends, analyzing the impact of attendance, and generating automated reports to support data-driven decision-making.

The project structure and workflow are aligned with real-world data analytics and consulting practices, making it suitable for entry-level Analyst and Data Analyst roles.

---

## 🎯 Objectives
- Analyze structured student academic performance data
- Clean and validate large datasets with missing and inconsistent values
- Identify subject-wise and department-wise performance trends
- Analyze the impact of attendance on academic performance
- Automate Excel report and dashboard generation
- Derive actionable insights from data

---

## 🧰 Tools & Technologies
- Python (Pandas, Matplotlib, OpenPyXL)
- SQL (MySQL)
- Microsoft Excel
- Git & GitHub
- VS Code

---

## 📂 Project Structure
Student_Performance_Analysis/
│
├── data/
│   ├── raw/
│   │   ├── students_large_raw.csv
│   │   ├── marks_large_raw.csv
│   │   └── exams_large_raw.csv
│   │
│   └── cleaned/
│       ├── students_cleaned.csv
│       ├── marks_cleaned.csv
│       └── exams_cleaned.csv
│
├── python/
│   ├── data_cleaning.py
│   ├── analysis_visualization.py
│   └── excel_report_generator.py
│
├── sql/
│   ├── create_tables.sql
│   └── analysis_queries.sql
│
├── excel/
│   └── Student_Performance_Report.xlsx
│
├── graphs/
│   ├── attendance_vs_marks.png
│   ├── average_marks_by_student.png
│   └── pass_vs_fail_distribution.png
│
└── README.md

---

## 📊 Dataset Description

### Students Dataset
Contains demographic and academic information:
- student_id
- name
- gender
- age
- department
- year

### Marks Dataset
Contains subject-wise academic performance:
- student_id
- subject
- marks
- attendance

### Exams Dataset
Contains exam-level outcomes:
- student_id
- exam_type
- total_marks
- result (Pass / Fail)

The datasets intentionally include missing values and varied distributions to simulate real-world data challenges.

---

## 🧹 Data Cleaning & Validation
File: python/data_cleaning.py

- Filled missing age values using average age
- Filled missing marks using subject-wise averages
- Removed duplicate records
- Validated data consistency
- Stored cleaned datasets for analysis

---

## 📈 Data Analysis & Visualization
File: python/analysis_visualization.py

Analysis performed:
- Subject-wise average marks analysis
- Attendance vs marks relationship
- Pass vs Fail distribution

Visualizations generated:
- Bar chart for subject-wise performance
- Scatter plot for attendance impact
- Pie chart for pass vs fail distribution

---

## 🗄️ SQL Analysis
Files:
- sql/create_tables.sql
- sql/analysis_queries.sql

SQL operations include:
- Creating relational tables with primary and foreign keys
- Using JOINs to combine student and performance data
- Aggregations using GROUP BY
- Filtering low-performing and low-attendance students

---

## 📊 Excel Reporting & Automation
File: python/excel_report_generator.py

The Excel reporting process is fully automated using Python:
- Reads cleaned CSV files
- Generates multiple Excel sheets
- Creates charts programmatically (bar, scatter, pie)
- Eliminates manual Excel work

Generated output:
- excel/Student_Performance_Report.xlsx

---

## 📌 Key Insights
- Students with attendance below 75% tend to score significantly lower
- Programming-related subjects show higher average performance
- Department-wise performance variations are clearly observed
- Attendance is a strong factor influencing academic success

---

## 🚀 Outcomes
- Built an end-to-end data analysis pipeline
- Demonstrated real-world data cleaning and validation
- Applied SQL joins and aggregations on large datasets
- Automated Excel reporting using Python
- Created an industry-ready analytics project

---

## ▶️ How to Run the Project

python python/data_cleaning.py  
python python/analysis_visualization.py  
python python/excel_report_generator.py  

---

## 🧠 Interview-Ready Summary
I built an end-to-end student performance data analysis project using Python, SQL, and Excel. I cleaned and validated large datasets, analyzed academic trends using SQL joins and Python, automated Excel dashboard creation, and derived insights such as the impact of attendance on student performance.

---

## 👤 Author
Praveen Kammala  
Final-year Computer Science Engineering student  
Aspiring Data Analyst / Analyst
