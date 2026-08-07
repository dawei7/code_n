WITH weekly_hours AS (
    SELECT
        employee_id,
        date(
            meeting_date,
            '-' || ((CAST(strftime('%w', meeting_date) AS INTEGER) + 6) % 7) || ' days'
        ) AS week_start,
        SUM(duration_hours) AS total_hours
    FROM meetings
    GROUP BY
        employee_id,
        date(
            meeting_date,
            '-' || ((CAST(strftime('%w', meeting_date) AS INTEGER) + 6) % 7) || ' days'
        )
    HAVING SUM(duration_hours) > 20
)
SELECT
    e.employee_id,
    e.employee_name,
    e.department,
    COUNT(*) AS meeting_heavy_weeks
FROM weekly_hours AS w
JOIN employees AS e
    ON e.employee_id = w.employee_id
GROUP BY e.employee_id, e.employee_name, e.department
HAVING COUNT(*) >= 2
ORDER BY meeting_heavy_weeks DESC, e.employee_name ASC;
