# Mean of Array After Removing Some Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1619 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/mean-of-array-after-removing-some-elements/) |

## Problem Description
### Goal
Given an integer array `arr`, discard the smallest 5% of its elements and the largest 5% of its elements. Removal is by sorted position, so duplicate values still occupy separate positions and exactly the prescribed number of elements is removed from each end.

Return the arithmetic mean of the remaining 90% of the array. The array length is a multiple of 20, which makes each 5% group an integer number of elements. A floating-point result within $10^{-5}$ of the exact mean is accepted.

### Function Contract
**Inputs**

- `arr`: an integer array of length $n$, where $20 \le n \le 1000$ and $n$ is a multiple of 20.
- Every value satisfies $0 \le \texttt{arr[i]} \le 10^5$.
- Exactly $k=n/20$ elements belong to each trimmed 5% group.

**Return value**

Return the mean of the $n-2k$ values remaining after the $k$ smallest and $k$ largest elements are removed.

### Examples
**Example 1**

- Input: `arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]`
- Output: `2.00000`

**Example 2**

- Input: `arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]`
- Output: `4.00000`

**Example 3**

- Input: `arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]`
- Output: `4.77778`
