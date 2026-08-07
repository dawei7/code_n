## Function Contract

**Database Schema**

**`UserVisits`**

| Column | Type | Meaning |
|---|---|---|
| `user_id` | int | Unique user identifier; composite primary key with `visit_date`. |
| `visit_date` | date | Date of the visit during 2020. |

- `(user_id, visit_date)` is unique.

**Return value**

Return a table with columns `user_id` and `biggest_window`. For each user, `biggest_window` is the maximum number of days between consecutive visits, using `2021-01-01` as the default next visit date for the last visit. Row order is unrestricted.
