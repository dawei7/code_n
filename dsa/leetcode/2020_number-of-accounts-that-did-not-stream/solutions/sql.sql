WITH StreamedIn2021 AS (
    SELECT DISTINCT account_id
    FROM Streams
    WHERE stream_date BETWEEN '2021-01-01' AND '2021-12-31'
)
SELECT COUNT(*) AS accounts_count
FROM Subscriptions AS subscription
LEFT JOIN StreamedIn2021 AS streamed
  ON streamed.account_id = subscription.account_id
WHERE subscription.start_date <= '2021-12-31'
  AND subscription.end_date >= '2021-01-01'
  AND streamed.account_id IS NULL;
