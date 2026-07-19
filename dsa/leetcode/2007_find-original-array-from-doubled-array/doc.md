# Find Original Array From Doubled Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2007 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/find-original-array-from-doubled-array/) |

## Problem Description

### Goal

An integer array `original` is transformed by adding one copy of twice every
element and then shuffling all the values. The resulting array is named
`changed`.

Given only `changed`, determine whether it could have been produced by this
process. If so, return any possible `original` array; its elements may appear
in any order. If no complete pairing of every value with one doubled value is
possible, return an empty list. Duplicate values represent separate
occurrences and must be matched separately.

### Function Contract

**Inputs**

- `changed`: a list of $N$ integers, where $1\le N\le10^5$ and
  $0\le\texttt{changed[i]}\le10^5$.

**Return value**

Return one array of length $N/2$ whose values and doubles form exactly the
multiset in `changed`, or `[]` when no such array exists.

### Examples

**Example 1**

- Input: `changed = [1, 3, 4, 2, 6, 8]`
- Output: `[1, 3, 4]`
- Explanation: The remaining values are respectively `2`, `6`, and `8`, the
  doubles of the returned values.

**Example 2**

- Input: `changed = [6, 3, 0, 1]`
- Output: `[]`
- Explanation: The values cannot be divided into original-and-double pairs.

**Example 3**

- Input: `changed = [1]`
- Output: `[]`
- Explanation: A doubled array must contain an even number of elements.
