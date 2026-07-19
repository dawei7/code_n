SELECT COUNT(*) AS accounts_count
FROM Subscriptions AS subscription
WHERE subscription.start_date <= '2021-12-31'
  AND subscription.end_date >= '2021-01-01'
  AND NOT EXISTS (
      SELECT 1
      FROM Streams AS stream
      WHERE stream.account_id = subscription.account_id
        AND stream.stream_date BETWEEN '2021-01-01' AND '2021-12-31'
  );
