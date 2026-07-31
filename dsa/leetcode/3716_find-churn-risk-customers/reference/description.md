## Description

Table: `subscription_events`

| Column | Type | Meaning |
|---|---|---|
| `event_id` | integer | Unique event identifier. |
| `user_id` | integer | User whose subscription changed. |
| `event_date` | date | Date of the subscription event. |
| `event_type` | varchar | One of `start`, `upgrade`, `downgrade`, or `cancel`. |
| `plan_name` | varchar | `basic`, `standard`, `premium`, or `NULL` for a cancellation. |
| `monthly_amount` | decimal | Monthly cost after this event; a cancellation stores `0`. |

Find users who show all four churn-risk signals:

- Their latest event is not `cancel`, so the subscription is currently active.
- Their history contains at least one `downgrade`.
- The current monthly amount is strictly less than 50% of their greatest historical monthly amount.
- At least 60 days separate their first and last events.

For every qualifying user, return `user_id`, `current_plan`, `current_monthly_amount`, `max_historical_amount`, and `days_as_subscriber`. Order longer subscriptions first, then order equal durations by increasing `user_id`.
