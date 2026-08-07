## Function Contract

**Database Schema**

**`Calls`**

| Column | Type | Meaning |
|---|---|---|
| `from_id` | int | User ID of caller. |
| `to_id` | int | User ID of recipient. |
| `duration` | int | Duration of call in seconds. |

- `from_id != to_id`. Duplicate rows represent separate calls.

**Return value**

Return a table with columns `person1`, `person2`, `call_count`, and `total_duration`. `person1 < person2` for every row. Include one row per distinct unordered pair of users who have called each other. Row order is unrestricted.
