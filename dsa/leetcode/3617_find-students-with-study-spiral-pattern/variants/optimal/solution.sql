WITH ordered_sessions AS (
    SELECT
        ss.*,
        ROW_NUMBER() OVER (
            PARTITION BY student_id
            ORDER BY session_date, session_id
        ) AS session_number,
        LAG(session_date) OVER (
            PARTITION BY student_id
            ORDER BY session_date, session_id
        ) AS previous_date
    FROM study_sessions AS ss
),
student_stats AS (
    SELECT
        student_id,
        COUNT(*) AS session_count,
        COUNT(DISTINCT subject) AS cycle_length,
        SUM(hours_studied) AS total_study_hours
    FROM ordered_sessions
    GROUP BY student_id
    HAVING COUNT(DISTINCT subject) >= 3
       AND COUNT(*) >= 2 * COUNT(DISTINCT subject)
       AND MAX(julianday(session_date) - julianday(previous_date)) <= 2
),
valid_patterns AS (
    SELECT current_session.student_id
    FROM ordered_sessions AS current_session
    JOIN student_stats AS stats
        ON stats.student_id = current_session.student_id
    JOIN ordered_sessions AS first_cycle
        ON first_cycle.student_id = current_session.student_id
       AND first_cycle.session_number =
           ((current_session.session_number - 1) % stats.cycle_length) + 1
    GROUP BY current_session.student_id
    HAVING SUM(current_session.subject <> first_cycle.subject) = 0
)
SELECT
    students.student_id,
    students.student_name,
    students.major,
    stats.cycle_length,
    stats.total_study_hours
FROM valid_patterns
JOIN student_stats AS stats
    ON stats.student_id = valid_patterns.student_id
JOIN students
    ON students.student_id = valid_patterns.student_id
ORDER BY stats.cycle_length DESC, stats.total_study_hours DESC;
