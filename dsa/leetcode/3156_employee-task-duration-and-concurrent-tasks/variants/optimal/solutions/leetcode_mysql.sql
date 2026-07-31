WITH raw_events AS (
    SELECT employee_id, start_time AS event_time, 1 AS delta
    FROM Tasks
    UNION ALL
    SELECT employee_id, end_time AS event_time, -1 AS delta
    FROM Tasks
),
events AS (
    SELECT employee_id, event_time, SUM(delta) AS delta
    FROM raw_events
    GROUP BY employee_id, event_time
),
timeline AS (
    SELECT
        employee_id,
        event_time,
        SUM(delta) OVER (
            PARTITION BY employee_id
            ORDER BY event_time
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) AS active_tasks,
        LEAD(event_time) OVER (
            PARTITION BY employee_id
            ORDER BY event_time
        ) AS next_time
    FROM events
)
SELECT
    employee_id,
    FLOOR(
        SUM(
            CASE
                WHEN active_tasks > 0
                THEN TIMESTAMPDIFF(SECOND, event_time, next_time)
                ELSE 0
            END
        ) / 3600
    ) AS total_task_hours,
    MAX(active_tasks) AS max_concurrent_tasks
FROM timeline
GROUP BY employee_id
ORDER BY employee_id;

