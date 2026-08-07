SELECT COUNT(DISTINCT p.user_id) AS user_cnt
FROM Purchases AS p
CROSS JOIN Parameters AS bounds
WHERE p.time_stamp BETWEEN bounds.startDate AND bounds.endDate
  AND p.amount >= bounds.minAmount;
