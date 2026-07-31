WITH qualifying_users AS (
    SELECT user_id
    FROM course_completions
    GROUP BY user_id
    HAVING COUNT(*) >= 5
       AND AVG(course_rating) >= 4
),
numbered_courses AS (
    SELECT
        completions.user_id,
        completions.course_name,
        ROW_NUMBER() OVER (
            PARTITION BY completions.user_id
            ORDER BY completions.completion_date
        ) AS sequence_number
    FROM course_completions AS completions
    JOIN qualifying_users
      ON qualifying_users.user_id = completions.user_id
),
consecutive_pairs AS (
    SELECT
        current_course.course_name AS first_course,
        next_course.course_name AS second_course
    FROM numbered_courses AS current_course
    JOIN numbered_courses AS next_course
      ON next_course.user_id = current_course.user_id
     AND next_course.sequence_number = current_course.sequence_number + 1
)
SELECT
    first_course,
    second_course,
    COUNT(*) AS transition_count
FROM consecutive_pairs
GROUP BY first_course, second_course
ORDER BY
    transition_count DESC,
    first_course ASC,
    second_course ASC;
