-- Write your PostgreSQL query statement below
SELECT COUNT(DISTINCT s.account_id) AS accounts_count
FROM Subscriptions s
WHERE s.start_date <= '2021-12-31'
  AND s.end_date >= '2021-01-01'
  AND s.account_id NOT IN (
      SELECT account_id
      FROM Streams
      WHERE stream_date >= '2021-01-01'
        AND stream_date <= '2021-12-31'
  );
