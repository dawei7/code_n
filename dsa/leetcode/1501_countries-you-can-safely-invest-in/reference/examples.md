## Examples

**Example 1**

- **Input:** `Person = [[1, "Rachel", "212-7484074"], [2, "Finley", "070-6980802"], [3, "Daniel", "051-8800922"], [4, "Bob", "051-1234567"], [5, "Stella", "051-9999999"], [6, "Jonathan", "972-1234567"]], Country = [["Peru", "051"], ["Israel", "972"], ["Morocco", "212"]], Calls = [[1, 2, 33], [2, 1, 4], [3, 4, 59], [3, 5, 102], [4, 3, 330], [4, 5, 5], [5, 4, 13], [5, 3, 3], [6, 1, 1], [1, 6, 7]]`

`Person` table:

| id | name | phone_number |
|---:|---|---|
| 1 | Rachel | `212-7484074` |
| 2 | Finley | `070-6980802` |
| 3 | Daniel | `051-8800922` |
| 4 | Bob | `051-1234567` |
| 5 | Stella | `051-9999999` |
| 6 | Jonathan | `972-1234567` |

`Country` table:

| name | country_code |
|---|---|
| Peru | `051` |
| Israel | `972` |
| Morocco | `212` |

`Calls` table:

| caller_id | callee_id | duration |
|---:|---:|---:|
| 1 | 2 | 33 |
| 2 | 1 | 4 |
| 3 | 4 | 59 |
| 3 | 5 | 102 |
| 4 | 3 | 330 |
| 4 | 5 | 5 |
| 5 | 4 | 13 |
| 5 | 3 | 3 |
| 6 | 1 | 1 |
| 1 | 6 | 7 |

- **Output:** `[["Peru"]]`

| country |
|---|
| Peru |

- **Explanation:**
  - Total duration across 10 call rows is $33 + 4 + 59 + 102 + 330 + 5 + 13 + 3 + 1 + 7 = 557$.
  - Global average duration across call rows is $557 / 10 = 55.7$.
  - Peru (`051`) participants are involved in calls (3,4), (3,5), (4,3), (4,5), (5,4), (5,3). Since both caller and callee belong to Peru for these 6 calls, Peru has 12 endpoint entries totaling $2 \times (59 + 102 + 330 + 5 + 13 + 3) = 1748$, giving an average of $1748 / 12 \approx 145.67$.
  - Morocco (`212`) has 4 endpoints (from calls 1, 2, 9, 10) averaging $(33 + 4 + 1 + 7) / 4 = 11.25$.
  - Israel (`972`) has 2 endpoints (from calls 9, 10) averaging $(1 + 7) / 2 = 4.0$.
  - Only Peru's average ($145.67$) strictly exceeds the global average ($55.7$).

**Example 2**

- **Input:** `Person = [[1, "A", "001-0000001"], [2, "B", "002-0000002"], [3, "C", "002-0000003"]], Country = [["Alpha", "001"], ["Beta", "002"]], Calls = [[1, 2, 10], [2, 3, 30]]`
- **Output:** `[["Beta"]]`

- **Explanation:** Global call average is $(10 + 30) / 2 = 20$. Alpha's endpoint average is $10$. Beta's endpoint values are 10, 30, 30 (average $70 / 3 \approx 23.33$). Beta exceeds 20.

**Example 3**

- **Input:** `Person = [[1, "A", "001-0000001"], [2, "B", "002-0000002"]], Country = [["Alpha", "001"], ["Beta", "002"], ["Unused", "003"]], Calls = [[1, 2, 7]]`
- **Output:** `[]`

- **Explanation:** Both Alpha and Beta have average duration 7, which equals the global average 7. Since the comparison is strictly greater than, no country qualifies. Unused country has no call endpoints and is excluded.
