-- Write your PostgreSQL query statement below
WITH
    week_meeting_hours AS (
        SELECT
            employee_id,
            TO_CHAR(meeting_date, 'IYYY-IW') AS year_week,
            SUM(duration_hours) AS hours
        FROM meetings
        GROUP BY employee_id, TO_CHAR(meeting_date, 'IYYY-IW')
    ),
    intensive_weeks AS (
        SELECT
            e.employee_id,
            e.employee_name,
            e.department,
            COUNT(1) AS meeting_heavy_weeks
        FROM
            week_meeting_hours w
            JOIN employees e USING (employee_id)
        WHERE w.hours > 20
        GROUP BY e.employee_id, e.employee_name, e.department
    )
SELECT employee_id, employee_name, department, meeting_heavy_weeks
FROM intensive_weeks
WHERE meeting_heavy_weeks >= 2
ORDER BY meeting_heavy_weeks DESC, employee_name ASC;
