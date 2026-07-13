WITH crowded AS (
    SELECT
        id,
        visit_date,
        people,
        id - ROW_NUMBER() OVER (ORDER BY id) AS run_key
    FROM Stadium
    WHERE people >= 100
),
measured AS (
    SELECT
        id,
        visit_date,
        people,
        COUNT(*) OVER (PARTITION BY run_key) AS run_length
    FROM crowded
)
SELECT id, visit_date, people
FROM measured
WHERE run_length >= 3
ORDER BY visit_date;

