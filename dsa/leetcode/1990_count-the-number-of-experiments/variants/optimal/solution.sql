WITH Platforms AS (
    SELECT 'Android' AS platform
    UNION ALL
    SELECT 'IOS'
    UNION ALL
    SELECT 'Web'
),
ExperimentNames AS (
    SELECT 'Reading' AS experiment_name
    UNION ALL
    SELECT 'Sports'
    UNION ALL
    SELECT 'Programming'
)
SELECT
    p.platform,
    n.experiment_name,
    COUNT(e.experiment_id) AS num_experiments
FROM Platforms AS p
CROSS JOIN ExperimentNames AS n
LEFT JOIN Experiments AS e
    ON e.platform = p.platform
   AND e.experiment_name = n.experiment_name
GROUP BY p.platform, n.experiment_name;
