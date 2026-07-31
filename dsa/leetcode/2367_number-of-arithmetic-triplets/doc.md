# Number of Arithmetic Triplets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2367 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Two Pointers, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-arithmetic-triplets/) |

## Problem Description

### Goal

You receive a 0-indexed, strictly increasing integer array `nums` and a
positive integer `diff`. An index triplet $(i,j,k)$ is arithmetic when
$i<j<k$ and both consecutive value gaps equal `diff`.

Return the number of unique arithmetic triplets. Because the array is strictly
increasing, each required value can occur at only one index, and positive
`diff` automatically preserves the index order when all three values exist.

### Function Contract

**Inputs**

- `nums`: A strictly increasing list of $n$ integers.
- `diff`: The required positive difference between adjacent triplet values.

The constraints are $3\le n\le200$, $0\le\texttt{nums[i]}\le200$, and
$1\le\texttt{diff}\le50$.

**Return value**

Return the number of index triplets satisfying both required differences.

### Examples

**Example 1**

- Input: `nums = [0,1,4,6,7,10], diff = 3`
- Output: `2`

**Example 2**

- Input: `nums = [4,5,6,7,8,9], diff = 2`
- Output: `2`
