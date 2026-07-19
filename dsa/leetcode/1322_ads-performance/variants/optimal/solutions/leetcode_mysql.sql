SELECT
    ad_id,
    ROUND(COALESCE(
        100.0 * SUM(CASE WHEN action = 'Clicked' THEN 1 ELSE 0 END)
        / NULLIF(SUM(CASE WHEN action IN ('Clicked', 'Viewed') THEN 1 ELSE 0 END), 0),
        0
    ), 2) AS ctr
FROM Ads
GROUP BY ad_id
ORDER BY ctr DESC, ad_id;
