WITH MedalWins AS (
    SELECT contest_id, gold_medal AS user_id
    FROM Contests
    UNION ALL
    SELECT contest_id, silver_medal AS user_id
    FROM Contests
    UNION ALL
    SELECT contest_id, bronze_medal AS user_id
    FROM Contests
),
NumberedWins AS (
    SELECT
        user_id,
        contest_id - ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY contest_id
        ) AS streak_group
    FROM MedalWins
),
StreakCandidates AS (
    SELECT user_id
    FROM NumberedWins
    GROUP BY user_id, streak_group
    HAVING COUNT(*) >= 3
),
GoldCandidates AS (
    SELECT gold_medal AS user_id
    FROM Contests
    GROUP BY gold_medal
    HAVING COUNT(*) >= 3
),
CandidateIds AS (
    SELECT user_id FROM StreakCandidates
    UNION
    SELECT user_id FROM GoldCandidates
)
SELECT u.name, u.mail
FROM Users AS u
JOIN CandidateIds AS c
  ON c.user_id = u.user_id;
