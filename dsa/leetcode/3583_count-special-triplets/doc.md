# Count Special Triplets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3583 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-special-triplets/) |

## Problem Description

### Goal

Given an integer array `nums`, count the index triplets $(i,j,k)$ whose indices satisfy $0\le i<j<k<n$ and whose outer values are both exactly twice the middle value:

$$
\texttt{nums[i]}=2\cdot\texttt{nums[j]}
\quad\text{and}\quad
\texttt{nums[k]}=2\cdot\texttt{nums[j]}.
$$

Different index choices count as different triplets, even when they contain equal values. Return the count modulo $10^9+7$.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $3\le n\le10^5$ and $0\le\texttt{nums[i]}\le10^5$.

**Return value**

Return the number of special index triplets modulo $10^9+7$.

### Examples

#### Example 1

- **Input:** `nums = [6, 3, 6]`
- **Output:** `1`
- **Explanation:** The indices $(0,1,2)$ form the only valid triplet because both outer values are $2\cdot3$.

#### Example 2

- **Input:** `nums = [0, 1, 0, 0]`
- **Output:** `1`
- **Explanation:** The indices $(0,2,3)$ qualify; doubling the middle value zero still gives zero.

#### Example 3

- **Input:** `nums = [8, 4, 2, 8, 4]`
- **Output:** `2`
- **Explanation:** The valid index triplets are $(0,1,3)$ and $(1,2,4)$.

---
