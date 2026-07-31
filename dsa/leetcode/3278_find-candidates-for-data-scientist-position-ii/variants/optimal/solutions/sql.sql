WITH project_requirements AS (
    SELECT
        project_id,
        COUNT(*) AS required_skills
    FROM Projects
    GROUP BY project_id
),
candidate_scores AS (
    SELECT
        p.project_id,
        c.candidate_id,
        100 + SUM(
            CASE
                WHEN c.proficiency > p.importance THEN 10
                WHEN c.proficiency < p.importance THEN -5
                ELSE 0
            END
        ) AS score
    FROM Projects AS p
    INNER JOIN Candidates AS c
        ON c.skill = p.skill
    INNER JOIN project_requirements AS pr
        ON pr.project_id = p.project_id
    GROUP BY p.project_id, c.candidate_id, pr.required_skills
    HAVING COUNT(*) = pr.required_skills
),
ranked_candidates AS (
    SELECT
        project_id,
        candidate_id,
        score,
        ROW_NUMBER() OVER (
            PARTITION BY project_id
            ORDER BY score DESC, candidate_id ASC
        ) AS candidate_rank
    FROM candidate_scores
)
SELECT
    project_id,
    candidate_id,
    score
FROM ranked_candidates
WHERE candidate_rank = 1
ORDER BY project_id ASC;
