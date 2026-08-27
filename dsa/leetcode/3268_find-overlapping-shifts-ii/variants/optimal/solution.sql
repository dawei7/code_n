-- Write your PostgreSQL query statement below
WITH
    T AS (
        SELECT DISTINCT employee_id, start_time AS st
        FROM EmployeeShifts
        UNION
        SELECT DISTINCT employee_id, end_time AS st
        FROM EmployeeShifts
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
            INNER JOIN EmployeeShifts ON P.employee_id = EmployeeShifts.employee_id
        WHERE P.st >= EmployeeShifts.start_time AND P.ed <= EmployeeShifts.end_time
        GROUP BY P.employee_id, P.st, P.ed
    ),
    U AS (
        SELECT
            t1.employee_id,
            SUM(
                EXTRACT(EPOCH FROM (LEAST(t1.end_time, t2.end_time) - t2.start_time)) / 60
            )::int AS total_overlap_duration
        FROM
            EmployeeShifts t1
            JOIN EmployeeShifts t2
                ON t1.employee_id = t2.employee_id
                AND t1.start_time < t2.start_time
                AND t1.end_time > t2.start_time
        GROUP BY t1.employee_id
    )
SELECT
    S.employee_id,
    MAX(S.concurrent_count) AS max_overlapping_shifts,
    COALESCE(AVG(U.total_overlap_duration), 0)::int AS total_overlap_duration
FROM
    S
    LEFT JOIN U ON S.employee_id = U.employee_id
GROUP BY S.employee_id
ORDER BY S.employee_id;

