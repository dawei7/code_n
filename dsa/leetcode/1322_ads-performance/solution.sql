SELECT
    ad_id,
    ROUND(COALESCE(SUM(CASE WHEN action = 'Clicked' THEN 1 ELSE 0 END) / SUM(action IN ('Clicked', 'Viewed')) * 100, 0), 2) AS ctr
FROM Ads
GROUP BY 1
ORDER BY 2 DESC, 1;
