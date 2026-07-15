# Rank Transform of an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1331 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/rank-transform-of-an-array/) |

## Problem Description
### Goal
Given an integer array `arr`, replace every element by a positive integer rank that represents its order among the array's distinct values.

Ranks start at 1. A larger original value must receive a larger rank, equal values must receive the same rank, and the assigned ranks must be as small as possible. Consequently, the smallest distinct value has rank 1 and each next distinct value has the next integer rank.

Return ranks in the original element order. An empty input produces an empty output.

### Function Contract
**Inputs**

- `arr`: an integer array of length $n$, where $0\le n\le10^5$ and $-10^9\le\texttt{arr[i]}\le10^9$.

**Return value**

An array of length $n$ in which each value is replaced by one plus the number of distinct input values smaller than it.

### Examples
**Example 1**

- Input: `arr = [40,10,20,30]`
- Output: `[4,1,2,3]`

**Example 2**

- Input: `arr = [100,100,100]`
- Output: `[1,1,1]`
- Explanation: Equal elements share the smallest possible rank.

**Example 3**

- Input: `arr = [37,12,28,9,100,56,80,5,12]`
- Output: `[5,3,4,2,8,6,7,1,3]`

### Required Complexity
- **Time:** $O(n\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Order only the distinct values**

Create a set from `arr` to discard duplicates, then sort those distinct values ascending. Enumerating the sorted sequence from 1 defines the unique smallest legal rank for every value. Store this mapping in a hash table.

Scan the original array and replace each element by its mapped rank. Because the mapping is built from sorted distinct values, equal inputs use the same entry, every strict increase advances to a larger rank, and no integer rank is skipped. Those properties are exactly the ranking rules and establish minimality.

#### Complexity detail

Building the set and transforming the result take expected $O(n)$ time. Sorting at most $n$ distinct values costs $O(n\log n)$, which dominates. The distinct set, rank map, sorted values, and output use $O(n)$ space.

#### Alternatives and edge cases

- **Binary search per element:** Sort the distinct values and locate every input rank with binary search, preserving $O(n\log n)$ time but avoiding a separate rank map.
- **Count smaller distinct values:** Scanning all distinct values for every element is direct but can take $O(n^2)$ time.
- **Empty array:** Return an empty array without calling `min` or indexing a sorted value.
- **All equal:** Every element receives rank 1.
- **Negative values:** Numeric ordering, not magnitude, determines ranks.
- **Gaps in values:** Ranks remain consecutive because absent integers do not consume ranks.

</details>
