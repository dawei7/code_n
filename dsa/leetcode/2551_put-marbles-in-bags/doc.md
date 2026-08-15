# Put Marbles in Bags

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2551 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [put-marbles-in-bags](https://leetcode.com/problems/put-marbles-in-bags/) |

## Problem Description

### Goal

The 0-indexed array `weights` lists marbles in a fixed order, and exactly `k` bags must receive all of them. No bag may be empty. The marbles placed in each bag must form a contiguous interval of the original array, so the distribution is a partition into exactly `k` non-empty subarrays.

If a bag contains indices `i` through `j`, inclusive, its cost is `weights[i] + weights[j]`. A distribution's score is the sum of all bag costs. Return the difference between the maximum and minimum scores over every valid distribution.

### Function Contract

**Inputs**

- `weights`: The positive marble weights in their fixed order.
- `k`: The exact number of non-empty contiguous bags.

The constraints are $1 \le k \le \lvert\texttt{weights}\rvert \le 10^5$ and $1 \le \texttt{weights[i]} \le 10^9$.

**Return value**

Return the maximum attainable score minus the minimum attainable score.

### Examples

#### Example 1

- **Input:** `weights = [1,3,5,1], k = 2`
- **Output:** `4`
- **Explanation:** The minimum score is 6 and the maximum score is 10.

#### Example 2

- **Input:** `weights = [1,3], k = 2`
- **Output:** `0`
- **Explanation:** Only one two-bag distribution exists, so both extreme scores are equal.
