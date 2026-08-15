# Divide Array Into Arrays With Max Difference

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2966 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/) |

## Problem Description

### Goal

You are given an integer array `nums` whose length $N$ is a multiple of three,
along with a positive integer `k`. Divide all array occurrences into exactly
$N/3$ arrays, each containing three elements.

Within every resulting array, the difference between any two values must be at
most `k`. Equivalently, each group's maximum value minus its minimum value must
not exceed `k`.

Return any 2D array representing a valid division. If no such division exists,
return an empty array.

### Function Contract

**Inputs**

- `nums`: the values to distribute among three-element arrays
- `k`: the maximum permitted difference inside any group

Let $N=\lvert\texttt{nums}\rvert$. The contract guarantees
$1\le N\le10^5$, $N$ is divisible by three,
$1\le\texttt{nums[i]}\le10^5$, and $1\le k\le10^5$.

**Return value**

Any division into $N/3$ triples satisfying the pairwise-difference limit, or
`[]` when no valid division exists.

### Examples

#### Example 1

- **Input:** `nums = [1,3,4,8,7,9,3,5,1], k = 2`
- **Output:** `[[1,1,3],[3,4,5],[7,8,9]]`
- **Explanation:** Each triple's largest and smallest values differ by at most two.

#### Example 2

- **Input:** `nums = [2,4,2,2,5,2], k = 2`
- **Output:** `[]`
- **Explanation:** Four copies of `2` force some group to contain both `2` and `5`, whose difference is three.

#### Example 3

- **Input:** `nums = [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11], k = 14`
- **Output:** `[[2,2,2],[4,5,5],[5,5,7],[7,8,8],[9,9,10],[11,12,12]]`
- **Explanation:** The displayed sorted triples all satisfy the generous limit.
