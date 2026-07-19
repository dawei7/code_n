SELECT
    question_id AS survey_log
FROM SurveyLog
GROUP BY question_id
ORDER BY
    1.0 * SUM(CASE WHEN action = 'answer' THEN 1 ELSE 0 END)
        / NULLIF(SUM(CASE WHEN action = 'show' THEN 1 ELSE 0 END), 0) DESC,
    question_id ASC
LIMIT 1;

