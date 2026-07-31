## Examples

**Example 1**

- Input: `subscription_events` table (16 rows)

| `event_id` | `user_id` | `event_date` | `event_type` | `plan_name` | `monthly_amount` |
|---:|---:|---|---|---|---:|
| 1 | 501 | `2024-01-01` | `start` | `premium` | 29.99 |
| 2 | 501 | `2024-02-15` | `downgrade` | `standard` | 19.99 |
| 3 | 501 | `2024-03-20` | `downgrade` | `basic` | 9.99 |
| 4 | 502 | `2024-01-05` | `start` | `standard` | 19.99 |
| 5 | 502 | `2024-02-10` | `upgrade` | `premium` | 29.99 |
| 6 | 502 | `2024-03-15` | `downgrade` | `basic` | 9.99 |
| 7 | 503 | `2024-01-10` | `start` | `basic` | 9.99 |
| 8 | 503 | `2024-02-20` | `upgrade` | `standard` | 19.99 |
| 9 | 503 | `2024-03-25` | `upgrade` | `premium` | 29.99 |
| 10 | 504 | `2024-01-15` | `start` | `premium` | 29.99 |
| 11 | 504 | `2024-03-01` | `downgrade` | `standard` | 19.99 |
| 12 | 504 | `2024-03-30` | `cancel` | `NULL` | 0.00 |
| 13 | 505 | `2024-02-01` | `start` | `basic` | 9.99 |
| 14 | 505 | `2024-02-28` | `upgrade` | `standard` | 19.99 |
| 15 | 506 | `2024-01-20` | `start` | `premium` | 29.99 |
| 16 | 506 | `2024-03-10` | `downgrade` | `basic` | 9.99 |

- Output: users 501 and 502 with current plan metrics

| `user_id` | `current_plan` | `current_monthly_amount` | `max_historical_amount` | `days_as_subscriber` |
|---:|---|---:|---:|---:|
| 501 | `basic` | 9.99 | 29.99 | 79 |
| 502 | `basic` | 9.99 | 29.99 | 70 |

- Explanation: The six users are evaluated as follows:

  - **User 501:** The latest event is an active downgrade to `basic`; the history contains two downgrades. Current revenue `9.99 / 29.99 = 33.3%` of the maximum, and January 1 through March 20 spans 79 days. All four tests pass.
  - **User 502:** The latest event is an active downgrade to `basic`, and one downgrade is present. Current revenue is again `9.99 / 29.99 = 33.3%`, while January 5 through March 15 spans 70 days. This user also qualifies.
  - **User 503:** The latest event is an active upgrade to `premium`, but the history contains no downgrade, so the user is not at risk.
  - **User 504:** The latest event is `cancel`, so the user is not currently active and is excluded.
  - **User 505:** The latest event is an active upgrade to `standard`, but no downgrade appears in the history, so the user is excluded.
  - **User 506:** The latest event is an active downgrade to `basic`, and `9.99` is below half of `29.99`; however, January 20 through March 10 is only 50 days, so the duration requirement fails.

The two qualifying rows are sorted by `days_as_subscriber` descending; the `user_id` tie-break would be ascending.
