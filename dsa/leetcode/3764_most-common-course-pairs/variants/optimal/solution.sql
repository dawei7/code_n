-- Write your PostgreSQL query statement below
WITH
    top_students AS (
        SELECT user_id
        FROM course_completions
        GROUP BY user_id
        HAVING COUNT(1) >= 5 AND AVG(course_rating) >= 4
    ),
    course_pairs AS (
        SELECT
            course_name AS first_course,
            LEAD(course_name) OVER (
                PARTITION BY user_id
                ORDER BY completion_date
            ) second_course
        FROM
            top_students
            JOIN course_completions USING (user_id)
    )
SELECT
    first_course,
    second_course,
    COUNT(1) AS transition_count
FROM course_pairs
WHERE second_course IS NOT NULL
GROUP BY first_course, second_course
ORDER BY transition_count DESC, LOWER(first_course) ASC, LOWER(second_course) ASC;
