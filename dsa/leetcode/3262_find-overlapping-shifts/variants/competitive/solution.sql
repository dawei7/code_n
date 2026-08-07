WITH shift_events AS (
    SELECT
        employee_id,
        start_time AS event_time,
        1 AS event_order,
        1 AS delta,
        1 AS is_start
    FROM EmployeeShifts

    UNION ALL

    SELECT
        employee_id,
        end_time AS event_time,
        0 AS event_order,
        -1 AS delta,
        0 AS is_start
    FROM EmployeeShifts
),
active_counts AS (
    SELECT
        employee_id,
        is_start,
        COALESCE(
            SUM(delta) OVER (
                PARTITION BY employee_id
                ORDER BY event_time ASC, event_order ASC
                ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
            ),
            0
        ) AS active_before
    FROM shift_events
)
SELECT
    employee_id,
    SUM(active_before) AS overlapping_shifts
FROM active_counts
WHERE is_start = 1
GROUP BY employee_id
HAVING SUM(active_before) > 0
ORDER BY employee_id ASC;
