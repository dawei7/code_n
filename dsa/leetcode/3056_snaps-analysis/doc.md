# Snaps Analysis

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3056 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/snaps-analysis/) |

## Problem Description

### Goal

Users spend time either sending or opening snaps. Each user belongs to one age
bucket, and the analysis must combine the activity of every user in the same
bucket.

For each represented age bucket, calculate what percentage of its total snap
time was spent on `send` activities and what percentage was spent on `open`
activities. Round both percentages to two decimal places. The result may be
returned in any order.

### Function Contract

**Inputs**

- `Activities(activity_id, user_id, activity_type, time_spent)`: each unique
  activity is either `send` or `open` and records its duration.
- `Age(user_id, age_bucket)`: maps each unique user to an age bucket.

Let $n$ be the number of activity rows and $g$ the number of represented age
buckets.

**Return value**

- A table with columns `age_bucket`, `send_perc`, and `open_perc`, with each
  percentage rounded to two decimal places.

### Examples

**Example 1**

For age bucket `31-35`, user `123` spends `3.50` sending and `5.75` opening.
The total is `9.25`, so the returned percentages are `37.84` and `62.16`.

**Example 2**

If several users share an age bucket, their activity times are added before
either percentage is calculated; users are not averaged separately.

**Example 3**

If every activity in a represented bucket is a `send`, its percentages are
`100.00` for sending and `0.00` for opening.
