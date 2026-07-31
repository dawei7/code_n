## Description

Table: `activity`

| Column | Type | Meaning |
|---|---|---|
| `user_id` | integer | User who generated the activity. |
| `action_date` | date | Calendar date on which it occurred. |
| `action` | varchar | Name of the action performed. |

The composite primary key is (`user_id`, `action_date`, `action`). Consequently, the same user may have several rows on one date when those rows name different actions. Each record represents one action by one user on one date.

Find every **behaviorally stable user**. Such a user must have a run of at least five consecutive calendar days for which both conditions hold:

- exactly one action was performed on each day in the run; and
- that sole action has the same value throughout the run.

When one user has more than one qualifying run, retain only a run having maximum length for that user. Return its user, action, length, first date, and last date. Sort the result by decreasing `streak_length`, breaking ties by increasing `user_id`.
