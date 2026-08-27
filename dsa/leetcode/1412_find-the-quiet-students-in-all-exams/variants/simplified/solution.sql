-- Write your PostgreSQL query statement below
WITH
    T AS (
        SELECT
            student_id,
            RANK() OVER (
                PARTITION BY exam_id
                ORDER BY score
            ) AS rk1,
            RANK() OVER (
                PARTITION BY exam_id
                ORDER BY score DESC
            ) AS rk2
        FROM Exam
    )
SELECT student_id, student_name
FROM
    T
    JOIN Student USING (student_id)
GROUP BY 1
HAVING SUM(CASE WHEN rk1 = 1 THEN 1 ELSE 0 END) = 0 AND SUM(CASE WHEN rk2 = 1 THEN 1 ELSE 0 END) = 0
ORDER BY 1;
