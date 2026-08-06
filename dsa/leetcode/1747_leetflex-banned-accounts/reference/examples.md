## Examples

**Example 1**

- **Input:** `LogInfo = [[1, 1, "2021-02-01 09:00:00", "2021-02-01 09:30:00"], [1, 2, "2021-02-01 09:20:00", "2021-02-01 10:00:00"], [2, 1, "2021-02-01 12:00:00", "2021-02-01 12:30:00"], [2, 2, "2021-02-01 13:00:00", "2021-02-01 14:00:00"]]`

`LogInfo` table:

| account_id | ip_address | login | logout |
|---:|---:|---|---|
| 1 | 1 | `2021-02-01 09:00:00` | `2021-02-01 09:30:00` |
| 1 | 2 | `2021-02-01 09:20:00` | `2021-02-01 10:00:00` |
| 2 | 1 | `2021-02-01 12:00:00` | `2021-02-01 12:30:00` |
| 2 | 2 | `2021-02-01 13:00:00` | `2021-02-01 14:00:00` |

- **Output:** `[[1]]`

| account_id |
|---:|
| 1 |

- **Explanation:**
  - Account 1: Session from IP 1 (`09:00` to `09:30`) overlaps with Session from IP 2 (`09:20` to `10:00`) between `09:20` and `09:30`. IP addresses are different (1 vs 2), so account 1 is banned.
  - Account 2: Session from IP 1 ends at `12:30`, and session from IP 2 starts at `13:00`. No overlap, so account 2 is not banned.

**Example 2**

- **Input:** `account 2 uses two different IP addresses sequentially without temporal overlap`
- **Output:** `no row for account 2`

- **Explanation:** Sequential login sessions from different IP addresses do not constitute simultaneous access and do not violate rules.

**Example 3**

- **Input:** `account 3 has overlapping sessions from the exact same IP address`
- **Output:** `no row for account 3`

- **Explanation:** Overlapping sessions from the same IP address do not constitute a violation; different IP addresses are required.
