# Sort the Jumbled Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2191 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sort-the-jumbled-numbers/) |

## Problem Description

### Goal

The ten-entry array `mapping` defines a shuffled decimal system:
`mapping[d]` is the digit that replaces every occurrence of decimal digit `d`.
Applying all such replacements to an integer produces its mapped value;
leading zeros in that representation do not affect its numeric value.

Return the original elements of `nums` arranged in non-decreasing order of
their mapped values. Do not replace the returned numbers by their mapped
forms. When two elements have equal mapped values, preserve their relative
order from the input.

### Function Contract

**Inputs**

- `mapping`: a permutation of the digits from $0$ through $9$.
- `nums`: an array of length $n$, where $1\le n\le3\cdot10^4$ and every
  element lies in $[0,10^9)$.

**Return value**

Return a stable ordering of the original `nums` values by non-decreasing
mapped value.

### Examples

#### Example 1

- **Input:** `mapping = [8,9,4,0,2,1,3,5,7,6]`, `nums = [991,338,38]`
- **Output:** `[338,38,991]`

#### Example 2

- **Input:** `mapping = [0,1,2,3,4,5,6,7,8,9]`, `nums = [789,456,123]`
- **Output:** `[123,456,789]`

#### Example 3

- **Input:** `mapping = [5,1,2,3,4,0,6,7,8,9]`, `nums = [0,10,5]`
- **Output:** `[5,0,10]`
