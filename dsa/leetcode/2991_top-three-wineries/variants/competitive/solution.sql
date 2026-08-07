WITH winery_totals AS (
    SELECT country, winery, SUM(points) AS total_points
    FROM Wineries
    GROUP BY country, winery
),
ranked_wineries AS (
    SELECT country, winery, total_points,
        ROW_NUMBER() OVER (
            PARTITION BY country
            ORDER BY total_points DESC, winery
        ) AS winery_rank
    FROM winery_totals
)
SELECT country,
    MAX(CASE WHEN winery_rank = 1 THEN winery || ' (' || total_points || ')' END) AS top_winery,
    COALESCE(MAX(CASE WHEN winery_rank = 2 THEN winery || ' (' || total_points || ')' END), 'No second winery') AS second_winery,
    COALESCE(MAX(CASE WHEN winery_rank = 3 THEN winery || ' (' || total_points || ')' END), 'No third winery') AS third_winery
FROM ranked_wineries
GROUP BY country
ORDER BY country;
