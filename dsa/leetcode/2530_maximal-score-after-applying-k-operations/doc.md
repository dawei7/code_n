# Maximal Score After Applying K Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2530 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximal-score-after-applying-k-operations/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `nums`, an integer `k`, and an initial score of zero. In one operation, choose any index `i`, add the current `nums[i]` to the score, and then replace that array value with $\lceil\texttt{nums[i]}/3\rceil$.

Perform exactly `k` operations. The same index may be chosen repeatedly, using its updated value each time. Return the largest total score attainable by choosing the operation sequence optimally.

### Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers.
- `k`: The exact number of operations to perform.

Let $n = \lvert\texttt{nums}\rvert$. The constraints are $1 \le n,k \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^9$.

**Return value**

Return the maximum score obtainable after exactly `k` selections and replacements.

### Examples

#### Example 1

- **Input:** `nums = [10, 10, 10, 10, 10], k = 5`
- **Output:** `50`
- **Explanation:** Select each value once; all five selected rewards are `10`.

#### Example 2

- **Input:** `nums = [1, 10, 3, 3, 3], k = 3`
- **Output:** `17`
- **Explanation:** Selecting `10`, then its replacement `4`, then one `3` gives the optimal score `10 + 4 + 3`.
