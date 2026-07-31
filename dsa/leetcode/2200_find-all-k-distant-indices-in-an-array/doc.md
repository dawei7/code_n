# Find All K-Distant Indices in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2200 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/) |

## Problem Description

### Goal

Given a 0-indexed integer array `nums`, a value `key`, and a distance limit `k`, call an index $i$ k-distant when at least one index $j$ satisfies both `nums[j] == key` and

$$
\lvert i-j\rvert \le k.
$$

Return every k-distant index in increasing order. The `key` value is guaranteed to occur in the array.
An index needs only one qualifying key occurrence, even when several key
positions have overlapping distance neighborhoods.

### Function Contract

**Inputs**

- `nums`: an integer array of length $n$, where $1 \le n \le 1000$ and every value lies in $[1,1000]$.
- `key`: a value that occurs in `nums`.
- `k`: the inclusive maximum index distance, where $1 \le k \le n$.

**Return value**

Return all indices that are within distance `k` of at least one occurrence of `key`, sorted in increasing order.

### Examples

**Example 1**

- Input: `nums = [3,4,9,1,3,9,5]`, `key = 9`, `k = 1`
- Output: `[1,2,3,4,5,6]`

The key positions `2` and `5` cover the intervals `[1,3]` and `[4,6]`.

**Example 2**

- Input: `nums = [2,2,2,2,2]`, `key = 2`, `k = 2`
- Output: `[0,1,2,3,4]`

Every index is itself a key position and therefore qualifies.
