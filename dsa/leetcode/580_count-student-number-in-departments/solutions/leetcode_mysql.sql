SELECT
    department.dept_name,
    COUNT(student.student_id) AS student_number
FROM Department AS department
LEFT JOIN Student AS student
    ON student.dept_id = department.dept_id
GROUP BY department.dept_id, department.dept_name
ORDER BY student_number DESC, department.dept_name ASC;

