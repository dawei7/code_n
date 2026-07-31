# Count Subarrays With Score Less Than K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2302 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Sliding Window, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/count-subarrays-with-score-less-than-k/) |

## Problem Description
### Goal
For any array, define its score as the product of its element sum and its
length. For example, `[1, 2, 3, 4, 5]` has sum $15$, length $5$, and score
$15\cdot 5=75$.

Given the positive integer array `nums` and the integer `k`, count the
nonempty subarrays whose scores are strictly less than `k`. A subarray must be
a contiguous sequence of `nums`; choosing elements with gaps does not qualify.

### Function Contract
**Inputs**

- `nums`: An array of $n$ positive integers.
- `k`: The exclusive upper bound on a qualifying subarray's score.

The contract guarantees $1 \le n \le 10^5$, $1 \le \texttt{nums[i]} \le
10^5$, and $1 \le \texttt{k} \le 10^{15}$.

**Return value**

The number of nonempty contiguous ranges `[left:right]` for which

$$
\left(\sum_{i=\texttt{left}}^{\texttt{right}}\texttt{nums[i]}\right)
(\texttt{right}-\texttt{left}+1) < \texttt{k}.
$$

### Examples
**Example 1**

- Input: `nums = [2, 1, 4, 3, 5]`, `k = 10`
- Output: `6`
- Explanation: The five singleton ranges and `[2, 1]` have scores below $10$.
  A score equal to $10$, such as that of `[1, 4]`, does not qualify.

**Example 2**

- Input: `nums = [1, 1, 1]`, `k = 5`
- Output: `5`
- Explanation: All one- and two-element subarrays qualify, while the complete
  array has score $3\cdot3=9$.
