# Count Good Triplets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1534 |
| Difficulty | Easy |
| Topics | Array, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/count-good-triplets/) |

## Problem Description
### Goal

Given an integer array `arr` and three nonnegative limits `a`, `b`, and `c`, consider triples of indices in strictly increasing order, $i<j<k$.

The triple is good when all three conditions hold: the absolute difference between `arr[i]` and `arr[j]` is at most `a`, the difference between `arr[j]` and `arr[k]` is at most `b`, and the difference between `arr[i]` and `arr[k]` is at most `c`. Return the number of good index triples; equal value triples at different indices are counted separately.

### Function Contract
**Inputs**

- `arr`: An integer array of length $n$, where $3 \leq n \leq 100$ and every value lies from 0 through 1000.
- `a`, `b`, and `c`: Integer difference limits from 0 through 1000.

**Return value**

Return the number of triples $(i,j,k)$ with $0\leq i<j<k<n$ satisfying all three pairwise absolute-difference limits.

### Examples
**Example 1**

- Input: `arr = [3, 0, 1, 1, 9, 7], a = 7, b = 2, c = 3`
- Output: `4`
- Explanation: Four index triples satisfy all three limits, including two value-identical `(3, 0, 1)` triples that use different final indices.

**Example 2**

- Input: `arr = [1, 1, 2, 2, 3], a = 0, b = 0, c = 1`
- Output: `0`
- Explanation: No increasing index triple meets both zero-difference requirements.

**Example 3**

- Input: `arr = [1, 2, 3], a = 1, b = 1, c = 2`
- Output: `1`
- Explanation: The only possible index triple satisfies every bound.
