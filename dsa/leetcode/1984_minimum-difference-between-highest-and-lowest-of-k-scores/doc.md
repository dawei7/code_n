# Minimum Difference Between Highest and Lowest of K Scores

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1984 |
| Difficulty | Easy |
| Topics | Array, Sliding Window, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/) |

## Problem Description
### Goal
The 0-indexed integer array `nums` records one score for each student. Select
the scores of exactly `k` different students. For a particular selection, its
spread is the highest selected score minus the lowest selected score; scores
between those extremes do not otherwise affect the measurement.

Choose the `k` scores so that this spread is as small as possible, and return
the minimum achievable difference. Selection is by array position, so equal
scores belonging to different students may all be chosen.

### Function Contract
**Inputs**

- `nums`: a list of $N$ student scores, where $1 \le N \le 1000$ and
  $0 \le \texttt{nums[i]} \le 10^5$.
- `k`: the exact number of students to choose, where $1 \le k \le N$.

**Return value**

- The smallest possible value of
  $\max(\text{chosen scores}) - \min(\text{chosen scores})$ among all
  selections of exactly `k` positions.

### Examples
**Example 1**

- Input: `nums = [90], k = 1`
- Output: `0`

The only selected score is both the minimum and maximum.

**Example 2**

- Input: `nums = [9, 4, 1, 7], k = 2`
- Output: `2`

Choosing scores `7` and `9` gives the smallest spread.

**Example 3**

- Input: `nums = [1, 5, 6, 14, 15], k = 3`
- Output: `5`

Choosing `1`, `5`, and `6` gives spread `5`.
