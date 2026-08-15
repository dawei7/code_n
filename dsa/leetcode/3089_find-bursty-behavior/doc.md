# Find Bursty Behavior

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3089 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/find-bursty-behavior/) |

## Problem Description

### Goal

The `Posts` table records when users publish posts. Identify users whose February 2024 activity contains a burst: within some period of seven consecutive calendar days, the user's post count is at least twice that user's average weekly post count across the month.

Only posts dated from February 1 through February 28, 2024 are part of the calculation. For the average, treat those 28 days as exactly four weeks. For each qualifying user, report the largest seven-day post count found anywhere in that interval together with the monthly total divided by four.

Return the result in ascending order of `user_id`.

### Function Contract

**Inputs**

- `Posts`: a table with one row per post.
  - `post_id`: the post's unique identifier.
  - `user_id`: the identifier of the user who wrote the post.
  - `post_date`: the calendar date on which the post was written.

Let $n$ be the number of rows whose `post_date` is from `2024-02-01` through `2024-02-28`, inclusive.

**Return value**

Return a table with these columns:

- `user_id`: a user whose maximum seven-day count is at least twice their February average.
- `max_7day_posts`: the user's greatest number of February posts in any inclusive seven-day window ending on a date when that user posted.
- `avg_weekly_posts`: the user's number of February posts divided by $4$.

Order rows by `user_id` ascending.

### Examples

#### Example 1

- **Input:** `Posts = [(1, 1, "2024-02-27"), (2, 5, "2024-02-06"), (3, 3, "2024-02-25"), (4, 3, "2024-02-14"), (5, 3, "2024-02-06"), (6, 2, "2024-02-25")]`
- **Output:** `[(1, 1, 0.25), (2, 1, 0.25), (5, 1, 0.25)]`
- **Explanation:** Users 1, 2, and 5 each have one February post, so their weekly average is $0.25$ and their maximum seven-day count is $1$. User 3's three posts are too widely separated: the maximum seven-day count is $1$, below twice the weekly average of $0.75$.

#### Example 2

- **Input:** one user has four February posts, with two posts on February 10 and the other two more than six days away from that date.
- **Output:** that user is returned with `max_7day_posts = 2` and `avg_weekly_posts = 1.0`.
- **Explanation:** The largest window meets the threshold exactly because $2 = 2 \cdot 1$.

#### Example 3

- **Input:** a user posts on January 31, February 1, February 28, and February 29.
- **Output:** only the February 1 and February 28 posts contribute, producing `max_7day_posts = 1` and `avg_weekly_posts = 0.5`.
- **Explanation:** This problem deliberately limits the measured interval to February 1 through February 28, even though 2024 is a leap year.
