CREATE DATABASE IF NOT EXISTS student_analysis;
USE student_analysis;

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    gender VARCHAR(10),
    age INT,
    department VARCHAR(20),
    year INT
);

CREATE TABLE marks (
    student_id INT,
    subject VARCHAR(30),
    marks FLOAT,
    attendance INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

CREATE TABLE exams (
    student_id INT,
    exam_type VARCHAR(30),
    total_marks INT,
    result VARCHAR(10),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);
