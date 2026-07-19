# Maximum Difference Between Increasing Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2016 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-difference-between-increasing-elements/) |

## Problem Description

### Goal

Given a zero-indexed integer array `nums`, choose indices $i$ and $j$ such
that $i<j$ and `nums[i] < nums[j]`. Among all such increasing pairs, maximize
the difference `nums[j] - nums[i]`.

The index order is mandatory: a smaller value that occurs after a larger value
cannot be used as the first endpoint of a pair with that earlier element. If
no pair satisfies both the index and strict-value conditions, return $-1$.

### Function Contract

**Inputs**

- `nums`: a list of $N$ integers, where $2\le N\le1000$ and
  $1\le\texttt{nums[i]}\le10^9$.

**Return value**

Return the maximum positive later-minus-earlier difference, or `-1` when no
increasing pair exists.

### Examples

**Example 1**

- Input: `nums = [7, 1, 5, 4]`
- Output: `4`
- Explanation: Indices $1$ and $2$ produce $5-1=4$.

**Example 2**

- Input: `nums = [9, 4, 3, 2]`
- Output: `-1`
- Explanation: No later value is strictly larger than an earlier one.

**Example 3**

- Input: `nums = [1, 5, 2, 10]`
- Output: `9`
- Explanation: The first and last values produce $10-1=9$.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Keep the best earlier endpoint.** Scan from left to right while maintaining
`minimum`, the smallest value strictly before the current position. If the
current `value` is larger, `value - minimum` is the greatest valid difference
ending at this position, because no other earlier value can yield a larger
subtraction result.

**Update only after evaluating the current position.** Compare the candidate
against the best answer, then incorporate `value` into `minimum` for future
positions. Initializing the answer to `-1` preserves the required result when
every current value is less than or equal to its prefix minimum.

For any valid optimal pair $(i,j)$, the stored minimum when the scan reaches
$j$ is no larger than `nums[i]`. The candidate considered at $j$ is therefore
at least the optimal pair's difference and is itself valid. Conversely, every
recorded candidate uses an earlier minimum and a strictly larger current
value. The maximum recorded candidate is consequently exactly the optimum.

#### Complexity detail

Here $N$ is the length of `nums`. Each value is processed once, giving $O(N)$
time. The prefix minimum and best difference use $O(1)$ space.

#### Alternatives and edge cases

- **Check every index pair:** Direct enumeration is correct but takes
  $O(N^2)$ time.
- **Prefix-minimum array:** Precomputing the smallest earlier value for every
  index also yields $O(N)$ time but consumes unnecessary $O(N)$ space.
- Equal values do not form an increasing pair because the inequality is
  strict.
- A decreasing or constant array returns `-1`, not zero.
- Values near $10^9$ require ordinary integer subtraction but do not change
  the algorithm.

</details>
