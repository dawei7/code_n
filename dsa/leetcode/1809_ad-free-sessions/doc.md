# Ad-Free Sessions

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/ad-free-sessions/) |
| Frontend ID | 1809 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |

## Problem Description

### Goal

The `Playback` table records viewing sessions. Each `session_id` is unique, and every row identifies the customer plus the session's `start_time` and `end_time`. A session includes both endpoints of this interval. Sessions belonging to the same customer never overlap.

The `Ads` table records individual advertisements, including the customer who saw each ad and its `timestamp`. Report every playback session during which its customer saw no ad. An ad affects a session only when both the customer identifiers match and the timestamp lies within that session's inclusive interval. Return the qualifying `session_id` values in any order.

### Function Contract

**Inputs**

- `Playback(session_id, customer_id, start_time, end_time)`: one row per session. `session_id` is unique, `start_time <= end_time`, and sessions of one customer do not intersect.
- `Ads(ad_id, customer_id, timestamp)`: one row per shown ad. `ad_id` is unique.
- Let $P$ be the number of playback rows and $A$ the number of ad rows.

**Return value**

- Return one column named `session_id`.
- Include a session exactly when no row in `Ads` has the same `customer_id` and a `timestamp` from `start_time` through `end_time`, inclusive.
- Result order is unrestricted.

### Examples

**Example 1**

- Input: sessions `(1,1,1,5)`, `(2,1,15,23)`, `(3,2,10,12)`, `(4,2,17,28)`, `(5,2,2,8)`; ads `(1,1,5)`, `(2,2,15)`, `(3,2,20)`
- Output: `[[2],[3],[5]]`

The ad at time `5` belongs to session `1`, and the ad at time `20` belongs to session `4`. The remaining sessions are ad-free.

**Example 2**

- Input: `Playback = [[7,3,10,20]]`, `Ads = [[1,3,10]]`
- Output: `[]`

An ad at the inclusive start boundary makes the session ineligible.

**Example 3**

- Input: `Playback = [[8,4,10,20]]`, `Ads = [[1,9,15]]`
- Output: `[[8]]`

An ad at the right time but for a different customer does not affect the session.

### Required Complexity

- **Time:** $O((P + A)\log(A + 1))$
- **Space:** $O(P + A)$

<details>
<summary>Approach</summary>

#### General

**Match ads on both identity and time**

Left join each `Playback` row to `Ads` using two conditions: equal `customer_id` values and `a.timestamp BETWEEN p.start_time AND p.end_time`. `BETWEEN` is inclusive in SQL, matching the contract at both session boundaries. Placing these predicates in `ON` is essential because unmatched playback rows must survive the join.

**Recognize a missing match through the ad key**

When no ad satisfies the join condition, the left join supplies `NULL` for every ad-side column. Filter for `a.ad_id IS NULL`. Because `ad_id` is a non-null primary key, this test can only mean that no real ad row matched; it cannot confuse a stored null value with absence.

**Why the anti-join returns exactly the ad-free sessions**

If a session appears, its joined ad key is null, so no same-customer ad occurred within its interval and the session is ad-free. Conversely, any session with such an ad produces only matched rows with non-null ad keys and is removed. A session without one produces its single null-extended row and remains. Thus the result includes every and only qualifying `session_id`.

#### Complexity detail

A database can build or use a customer-and-time access path for the $A$ ad rows and probe it for the $P$ session intervals. Building a balanced access structure and performing the range probes takes $O((P+A)\log(A+1))$ time. Same-customer sessions do not overlap, so an ad can match at most one session and successful join output does not add a larger asymptotic term. The join structure plus as many as $P$ returned identifiers uses $O(P+A)$ space. Physical plans may improve these expected bounds with an existing suitable index or hash/range strategy.

#### Alternatives and edge cases

- **Correlated `NOT EXISTS`:** It expresses the anti-semijoin clearly, but a row-by-row plan without a reusable customer-time access path can rescan `Ads` for every session and degrade to $O(PA)$ work.
- **Group joined rows and use `HAVING COUNT(ad_id) = 0`:** It is correct but introduces aggregation state that the non-null-key anti-join does not need.
- **`NOT IN` over advertised sessions:** It can work after deriving session IDs, but null semantics make `NOT EXISTS` or a left anti-join safer and more direct.
- **Ad at `start_time`:** The start boundary is included, so the session is not ad-free.
- **Ad at `end_time`:** The end boundary is also included.
- **Different customer:** Timestamp overlap alone is insufficient; customer identity must match.
- **Ad before or after the interval:** It has no effect on that session.
- **Several ads in one session:** Any single match is enough to exclude it, and duplicate joined rows never reach the filtered result.
- **No ads:** Every playback session is returned.
- **Output order:** No `ORDER BY` is required because the contract accepts any order.

</details>
