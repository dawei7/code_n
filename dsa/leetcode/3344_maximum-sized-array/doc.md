# Maximum Sized Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3344 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Binary Search, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-sized-array/) |

## Problem Description

### Goal

For a chosen positive integer $n$, define a three-dimensional $n \times n \times n$ array $A$. Its indices satisfy $0 \le i,j,k<n$, and each entry is

$$
A[i][j][k]=i\,(j\mathbin{\mathrm{OR}}k),
$$

where $\mathrm{OR}$ is bitwise OR on the non-negative indices.

You are given a non-negative budget `s`. Find the largest positive dimension $n$ for which the sum of every entry in $A$ is at most `s`. The array is conceptual; its elements do not need to be constructed or stored.

### Function Contract

**Inputs**

- `s`: The maximum permitted array sum, where $0 \le s \le 10^{15}$.

**Return value**

- The greatest positive integer $n$ whose corresponding three-dimensional array has total sum at most `s`.

### Examples

**Example 1**

- Input: `s = 10`
- Output: `2`
- Explanation: Dimension `2` has total sum `3`, while dimension `3` has total sum `45`.

**Example 2**

- Input: `s = 0`
- Output: `1`
- Explanation: The sole entry for dimension `1` is zero.
