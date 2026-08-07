WITH event_history AS (
    SELECT
        subscription_events.*,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY event_date DESC, event_id DESC
        ) AS recency,
        MIN(event_date) OVER (PARTITION BY user_id) AS first_event_date,
        MAX(event_date) OVER (PARTITION BY user_id) AS last_event_date,
        MAX(monthly_amount) OVER (PARTITION BY user_id) AS max_historical_amount,
        MAX(
            CASE WHEN event_type = 'downgrade' THEN 1 ELSE 0 END
        ) OVER (PARTITION BY user_id) AS has_downgrade
    FROM subscription_events
)
SELECT
    user_id,
    plan_name AS current_plan,
    monthly_amount AS current_monthly_amount,
    max_historical_amount,
    CAST(julianday(last_event_date) - julianday(first_event_date) AS INTEGER)
        AS days_as_subscriber
FROM event_history
WHERE recency = 1
  AND event_type <> 'cancel'
  AND has_downgrade = 1
  AND monthly_amount * 2 < max_historical_amount
  AND julianday(last_event_date) - julianday(first_event_date) >= 60
ORDER BY days_as_subscriber DESC, user_id ASC;
