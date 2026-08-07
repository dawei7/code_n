WITH old_rankings AS (
    SELECT
        team_id,
        name,
        ROW_NUMBER() OVER (
            ORDER BY points DESC, name
        ) AS old_rank
    FROM TeamPoints
),
new_rankings AS (
    SELECT
        TeamPoints.team_id,
        ROW_NUMBER() OVER (
            ORDER BY TeamPoints.points + PointsChange.points_change DESC,
                     TeamPoints.name
        ) AS new_rank
    FROM TeamPoints
    JOIN PointsChange
      ON PointsChange.team_id = TeamPoints.team_id
)
SELECT
    old_rankings.team_id,
    old_rankings.name,
    CAST(old_rankings.old_rank AS INTEGER)
        - CAST(new_rankings.new_rank AS INTEGER) AS rank_diff
FROM old_rankings
JOIN new_rankings
  ON new_rankings.team_id = old_rankings.team_id;
