# Find All Lonely Numbers in the Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2150 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [find-all-lonely-numbers-in-the-array](https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/) |

## Problem Description

### Goal

Given an integer array `nums`, call a value $x$ lonely when it occurs exactly
once and neither adjacent integer value, $x-1$ nor $x+1$, occurs anywhere in
the array.

Return every lonely value in `nums`. The result may list those values in any
order. Both parts of the definition matter: duplicates disqualify a value even
when its neighboring integers are absent, and the presence of either neighbor
disqualifies an otherwise unique value.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $1 \leq n \leq 10^5$ and
  $0 \leq \texttt{nums[i]} \leq 10^6$.

**Return value**

Return a list containing each lonely value exactly once, in any order.

### Examples

**Example 1**

- Input: `nums = [10, 6, 5, 8]`
- Output: `[10, 8]`
- Explanation: `10` and `8` occur once and have no adjacent integer in the
  array. The values `5` and `6` disqualify each other.

**Example 2**

- Input: `nums = [1, 3, 5, 3]`
- Output: `[1, 5]`
- Explanation: `1` and `5` have absent neighbors, while `3` is excluded
  because it occurs twice.
