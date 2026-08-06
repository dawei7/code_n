## Function Contract

**Database Schema**

**`LogInfo`**

| Column | Type | Meaning |
|---|---|---|
| `account_id` | int | User account identifier. |
| `ip_address` | int | IP address used for the login session. |
| `login` | datetime | Timestamp when session started. |
| `logout` | datetime | Timestamp when session ended. |

- `(account_id, ip_address, login)` is unique.

**Return value**

Return a table with the single column `account_id`. Include each `account_id` at most once for which at least two sessions from different IP addresses have overlapping time intervals (`login1 <= logout2 AND login2 <= logout1`).
