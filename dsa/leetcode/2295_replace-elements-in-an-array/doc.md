# Replace Elements in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2295 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/replace-elements-in-an-array/) |

## Problem Description

### Goal

The 0-indexed array `nums` contains $n$ distinct positive integers. Apply the
given replacement operations in order. An operation `[old, new]` finds the
current occurrence of `old` and changes that same array position to `new`.

At the moment each operation is applied, `old` is guaranteed to exist and
`new` is guaranteed not to exist. Values removed by earlier operations may
therefore be introduced again later without violating distinctness.

Return the final array after all operations. Replacements change values but
never reorder positions.

### Function Contract

**Inputs**

- `nums`: An array of $n$ distinct positive integers.
- `operations`: An array of $m$ valid ordered pairs `[old, new]`.

The contract guarantees $1 \le n,m \le 10^5$. Every numeric value is between
1 and $10^6$, inclusive.

**Return value**

The array values in their original positions after applying every replacement
sequentially.

### Examples

#### Example 1

- **Input:** `nums = [1, 2, 4, 6]`, `operations = [[1, 3], [4, 7], [6, 1]]`
- **Output:** `[3, 2, 7, 1]`

#### Example 2

- **Input:** `nums = [1, 2]`, `operations = [[1, 3], [2, 1], [3, 2]]`
- **Output:** `[2, 1]`
