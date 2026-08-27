-- Write your PostgreSQL query statement below
WITH gaps_cte AS (
  SELECT
    student_id,
    subject,
    session_date,
    hours_studied,
    COALESCE(session_date::date - LAG(session_date::date) OVER (PARTITION BY student_id ORDER BY session_date), 0) AS gap
  FROM study_sessions
),
agg_cte AS (
  SELECT
    student_id,
    ARRAY_AGG(subject ORDER BY session_date) AS seq,
    COUNT(*) AS total_sessions,
    COUNT(DISTINCT subject) AS cycle_length,
    SUM(hours_studied) AS total_study_hours,
    MAX(gap) AS max_gap
  FROM gaps_cte
  GROUP BY student_id
  HAVING
    COUNT(*) >= 6
    AND COUNT(DISTINCT subject) >= 3
    AND COUNT(*) % COUNT(DISTINCT subject) = 0
    AND MAX(gap) <= 2
),
valid_cte AS (
  SELECT
    a.student_id,
    a.cycle_length,
    a.total_study_hours
  FROM agg_cte a
  WHERE NOT EXISTS (
    SELECT 1
    FROM generate_subscripts(a.seq, 1) i
    WHERE a.seq[i] != a.seq[((i - 1) % a.cycle_length) + 1]
  )
)
SELECT
  v.student_id,
  s.student_name,
  s.major,
  v.cycle_length,
  v.total_study_hours
FROM valid_cte v
JOIN students s ON v.student_id = s.student_id
ORDER BY v.cycle_length DESC, v.total_study_hours DESC, v.student_id ASC;

