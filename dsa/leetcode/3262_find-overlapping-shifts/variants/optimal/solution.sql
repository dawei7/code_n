-- Write your PostgreSQL query statement below
SELECT
    t1.employee_id,
    COUNT(*) AS overlapping_shifts
FROM
    EmployeeShifts t1
    JOIN EmployeeShifts t2
        ON t1.employee_id = t2.employee_id
        AND t1.start_time < t2.start_time
        AND t1.end_time > t2.start_time
GROUP BY t1.employee_id
HAVING COUNT(*) > 0
ORDER BY t1.employee_id;
