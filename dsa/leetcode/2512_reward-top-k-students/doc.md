# Reward Top K Students

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2512 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Sorting, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/reward-top-k-students/) |

## Problem Description

### Goal

Two lists identify words with positive and negative meanings. No word appears in both lists. Every student begins with zero points: each occurrence of a positive word in that student's report adds $3$ points, each occurrence of a negative word subtracts $1$ point, and every other word contributes nothing.

The 0-indexed arrays `report` and `student_id` have the same length. Report `report[i]` belongs to the student whose unique identifier is `student_id[i]`.

Rank the students in non-increasing order of their scores. When two students have the same score, the student with the smaller identifier ranks higher. Return the identifiers of the top `k` students in ranking order.

### Function Contract

**Inputs**

- `positive_feedback`: A nonempty list of distinct lowercase feedback words worth $3$ points per occurrence.
- `negative_feedback`: A nonempty list of distinct lowercase feedback words worth $-1$ point per occurrence.
- `report`: A nonempty list of lowercase, single-space-separated student reports.
- `student_id`: A list of unique positive student identifiers aligned with `report`.
- `k`: The number of highest-ranked student identifiers to return.

The two feedback lists are disjoint. Let $n = \lvert\texttt{report}\rvert = \lvert\texttt{student_id}\rvert$; then $1 \le n \le 10^4$ and $1 \le k \le n$. Each report has length from $1$ through $100$, each feedback word has length from $1$ through $100$, and every student identifier is at most $10^9$.

**Return value**

A list containing exactly `k` student identifiers, ordered first by decreasing score and then by increasing identifier.

### Examples

#### Example 1

- **Input:** `positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is studious","the student is smart"], student_id = [1,2], k = 2`
- **Output:** `[1,2]`
- **Explanation:** Both students earn $3$ points. Student `1` ranks first because its identifier is smaller.

#### Example 2

- **Input:** `positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is not studious","the student is smart"], student_id = [1,2], k = 2`
- **Output:** `[2,1]`
- **Explanation:** Student `1` earns $3-1=2$ points, while student `2` earns $3$ points.
