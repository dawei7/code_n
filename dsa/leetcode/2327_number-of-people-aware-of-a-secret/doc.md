# Number of People Aware of a Secret

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2327 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Dynamic Programming, Queue, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-people-aware-of-a-secret/) |

## Problem Description

### Goal

On day 1, exactly one person discovers a secret. A person who learns it begins
sharing it with one new person per day once `delay` days have elapsed since
their discovery day. Every recipient follows the same rule independently, so
the population of people who can share may grow over time.

Each person forgets the secret `forget` days after discovering it. They cannot
share on their forgetting day or on any later day, and they no longer count as
knowing the secret after forgetting it. Determine how many people still know
the secret at the end of day `n`, returning the count modulo $10^9+7$.

### Function Contract

**Inputs**

- `n`: The final day to examine, with $2 \le n \le 1000$.
- `delay`: The number of days between discovering the secret and first being
  able to share it.
- `forget`: The number of days between discovering and forgetting the secret,
  with $1 \le \texttt{delay} < \texttt{forget} \le n$.

**Return value**

The number of people who know the secret at the end of day `n`, modulo
$10^9+7$.

### Examples

#### Example 1

- **Input:** `n = 6`, `delay = 2`, `forget = 4`
- **Output:** `5`
- **Explanation:** The original person shares on days 3 and 4, then forgets on
  day 5. By the end of day 6, five people still know the secret.

#### Example 2

- **Input:** `n = 4`, `delay = 1`, `forget = 3`
- **Output:** `6`
- **Explanation:** New recipients can share beginning the next day. The original
  person forgets on day 4, while the remaining sharers create three new
  recipients that day.

#### Example 3

- **Input:** `n = 2`, `delay = 1`, `forget = 2`
- **Output:** `2`
- **Explanation:** On day 2, the original person has not forgotten and shares
  with one new person.
