# Longest Common Subsequence Between Sorted Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1940 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-common-subsequence-between-sorted-arrays/) |

## Problem Description
### Goal
You are given a collection `arrays` of integer arrays. Every inner array is
sorted in strictly increasing order. A subsequence may delete any elements
without changing the relative order of those that remain.

Return the longest sequence that is a subsequence of every inner array. Since
all inputs are strictly increasing, every value present in all arrays appears
in the same ascending order, so the required result consists of all such
common values in increasing order.

### Function Contract
**Inputs**

- `arrays`: between 2 and 100 arrays. Each contains between 1 and 100 distinct
  integers in strictly increasing order, and every value is between 1 and 100.

Let $T$ be the total number of entries across all arrays and let $V=100$ be
the fixed value-domain size.

**Return value**

- The longest common subsequence shared by every input array, listed in
  strictly increasing order. Return an empty list when no value is common to
  all arrays.

### Examples
**Example 1**

- Input: `arrays = [[1, 3, 4], [1, 4, 7, 9]]`
- Output: `[1, 4]`

**Example 2**

- Input:
  `arrays = [[2, 3, 6, 8], [1, 2, 3, 5, 6, 7, 10], [2, 3, 4, 6, 9]]`
- Output: `[2, 3, 6]`

**Example 3**

- Input: `arrays = [[1, 2, 3, 4, 5], [6, 7, 8]]`
- Output: `[]`

### Required Complexity
- **Time:** $O(T+V)$
- **Space:** $O(V)$

<details>
<summary>Approach</summary>

#### General

**Count each value's array membership**

Create one counter for every possible value from 1 through 100. Scan every
entry of every array and increment its value's counter. Strictly increasing
input means a value occurs at most once in one array, so a counter records the
number of different arrays containing that value without needing per-array
deduplication.

**Select values present everywhere**

Let $A$ be the number of input arrays. A value belongs to every array exactly
when its counter equals $A$. Visit the bounded value domain in increasing
order and emit precisely those values.

All emitted values appear in every array, and their increasing enumeration
matches their order in every strictly increasing input, so they form a common
subsequence. Any omitted value is absent from at least one array and cannot
belong to a common subsequence. Therefore including every qualifying value
produces the longest possible one.

#### Complexity detail

The counting scan visits all $T$ entries once, and enumerating the fixed domain
costs $O(V)$, for $O(T+V)$ time. The frequency array has $V+1$ positions, so
the auxiliary space is $O(V)$. Here $V=100$ is bounded by the problem, though
the notation makes the counting method explicit.

#### Alternatives and edge cases

- **Repeated set intersection:** Convert each array to a set and intersect all
  sets. This is also linear on average but requires sorting the final values
  unless order is restored from an input array.
- **Repeated linear membership searches:** For every surviving value, scan
  each next array to find it. This is correct but can take
  $O(AL^2)$ for $A$ arrays of length $L$.
- Strictly increasing inputs contain no duplicates, so raw frequency counts
  cannot be inflated within one array.
- If one array omits a value, that value must be excluded regardless of how
  many other arrays contain it.
- Disjoint arrays produce an empty result.
- If every array is identical, that entire array is the result.
- Values common only to a subset of the arrays do not qualify.

</details>
