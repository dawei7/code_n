-- Write your PostgreSQL query statement below
WITH
    T AS (
        SELECT DISTINCT employee_id, start_time AS st
        FROM Tasks
        UNION
        SELECT DISTINCT employee_id, end_time AS st
        FROM Tasks
    ),
    P AS (
        SELECT
            employee_id,
            st,
            LEAD(st) OVER (
                PARTITION BY employee_id
                ORDER BY st
            ) AS ed
        FROM T
    ),
    S AS (
        SELECT
            P.employee_id,
            P.st,
            P.ed,
            COUNT(1) AS concurrent_count
        FROM
            P
            INNER JOIN Tasks ON P.employee_id = Tasks.employee_id
        WHERE P.st >= Tasks.start_time AND P.ed <= Tasks.end_time
        GROUP BY P.employee_id, P.st, P.ed
    )
SELECT
    employee_id,
    FLOOR(SUM(EXTRACT(EPOCH FROM (ed - st)) / 3600.0)) AS total_task_hours,
    MAX(concurrent_count) AS max_concurrent_tasks
FROM S
GROUP BY employee_id
ORDER BY employee_id;

