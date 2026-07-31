WITH shift_events AS (
    SELECT
        employee_id,
        DATE(start_time) AS shift_date,
        start_time AS event_time,
        1 AS event_order,
        1 AS delta
    FROM EmployeeShifts

    UNION ALL

    SELECT
        employee_id,
        DATE(start_time) AS shift_date,
        end_time AS event_time,
        0 AS event_order,
        -1 AS delta
    FROM EmployeeShifts
),
active_timeline AS (
    SELECT
        employee_id,
        event_time,
        SUM(delta) OVER (
            PARTITION BY employee_id, shift_date
            ORDER BY event_time ASC, event_order ASC
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) AS active_shifts,
        LEAD(event_time) OVER (
            PARTITION BY employee_id, shift_date
            ORDER BY event_time ASC, event_order ASC
        ) AS next_time
    FROM shift_events
)
SELECT
    employee_id,
    MAX(active_shifts) AS max_overlapping_shifts,
    SUM(
        TIMESTAMPDIFF(MINUTE, event_time, next_time)
        * active_shifts * (active_shifts - 1) / 2
    ) AS total_overlap_duration
FROM active_timeline
GROUP BY employee_id
ORDER BY employee_id ASC;
