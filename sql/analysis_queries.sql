-- Average marks by subject
SELECT subject, ROUND(AVG(marks), 2) AS avg_marks
FROM marks
GROUP BY subject;

-- Department-wise performance
SELECT s.department, ROUND(AVG(m.marks), 2) AS avg_marks
FROM students s
JOIN marks m ON s.student_id = m.student_id
GROUP BY s.department;

-- Students with low attendance
SELECT s.name, m.subject, m.attendance
FROM students s
JOIN marks m ON s.student_id = m.student_id
WHERE m.attendance < 75;

-- Identify low-performing students
SELECT s.name, m.subject, m.marks
FROM students s
JOIN marks m ON s.student_id = m.student_id
WHERE m.marks < 40;

-- Pass vs Fail count
SELECT result, COUNT(*) AS count
FROM exams
GROUP BY result;
