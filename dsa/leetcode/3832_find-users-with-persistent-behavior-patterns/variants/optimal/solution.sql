WITH valid_days AS (
    SELECT
        user_id,
        action_date,
        MIN(`action`) AS `action`
    FROM activity
    GROUP BY user_id, action_date
    HAVING COUNT(*) = 1
),
numbered_days AS (
    SELECT
        user_id,
        action_date,
        `action`,
        ROW_NUMBER() OVER (
            PARTITION BY user_id, `action`
            ORDER BY action_date
        ) AS day_number
    FROM valid_days
),
qualifying_streaks AS (
    SELECT
        user_id,
        `action`,
        COUNT(*) AS streak_length,
        MIN(action_date) AS start_date,
        MAX(action_date) AS end_date
    FROM numbered_days
    GROUP BY
        user_id,
        `action`,
        julianday(action_date) - day_number
    HAVING COUNT(*) >= 5
),
ranked_streaks AS (
    SELECT
        qualifying_streaks.*,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY streak_length DESC, start_date ASC, `action` ASC
        ) AS streak_rank
    FROM qualifying_streaks
)
SELECT
    user_id,
    `action`,
    streak_length,
    start_date,
    end_date
FROM ranked_streaks
WHERE streak_rank = 1
ORDER BY streak_length DESC, user_id ASC;
