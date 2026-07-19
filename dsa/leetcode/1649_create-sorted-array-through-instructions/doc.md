# Create Sorted Array through Instructions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1649 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/create-sorted-array-through-instructions/) |

## Problem Description
### Goal
Start with an empty container `nums` and process `instructions` from left to right. For each current value, insert it into `nums` so that `nums` remains sorted. The cost of this insertion is the smaller of two counts measured before insertion: how many existing elements are strictly less than the value, and how many are strictly greater than it.

Equal elements contribute to neither count. Add the insertion costs for the entire instruction sequence and return the total modulo $10^9 + 7$.

### Function Contract
**Inputs**

- `instructions`: a list of $n$ integers processed in their given order, where $1 \le n \le 10^5$ and $1 \le \texttt{instructions[i]} \le 10^5$.

Let $M = \max(\texttt{instructions})$.

**Return value**

Return the sum of all insertion costs modulo $1{,}000{,}000{,}007$.

### Examples
**Example 1**

- Input: `instructions = [1, 5, 6, 2]`
- Output: `1`

Only the final insertion costs anything: one existing value is smaller than 2 and two are greater, so its cost is 1.

**Example 2**

- Input: `instructions = [1, 2, 3, 6, 5, 4]`
- Output: `3`

**Example 3**

- Input: `instructions = [1, 3, 3, 3, 2, 4, 2, 1, 2]`
- Output: `4`

Repeated values are excluded from both strict comparison counts.
