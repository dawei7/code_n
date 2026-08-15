# Find the Maximum Length of Valid Subsequence I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3201 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/) |

## Problem Description

### Goal

You are given an integer array `nums`. Choose a subsequence `sub`, preserving the relative order of its selected elements. A subsequence of length $x$ is valid when every adjacent pair has the same sum parity:

$$
(\texttt{sub[0]}+\texttt{sub[1]})\bmod 2
=\cdots=
(\texttt{sub[x-2]}+\texttt{sub[x-1]})\bmod 2.
$$

Elements not selected may be deleted, but selected elements cannot be reordered. Return the maximum possible length of a valid subsequence.

### Function Contract

**Inputs**

- `nums`: An array of integers with $2\le\lvert\texttt{nums}\rvert\le 2\cdot10^5$ and $1\le\texttt{nums[i]}\le10^7$.

Let $n=\lvert\texttt{nums}\rvert$.

**Return value**

- The length of the longest subsequence whose adjacent-pair sums all have one common parity.

### Examples

#### Example 1

- **Input:** `nums = [1,2,3,4]`
- **Output:** `4`
- **Explanation:** The entire array alternates parity, so every adjacent sum is odd.

#### Example 2

- **Input:** `nums = [1,2,1,1,2,1,2]`
- **Output:** `6`
- **Explanation:** `[1,2,1,2,1,2]` is a longest valid subsequence; each adjacent sum is odd.

#### Example 3

- **Input:** `nums = [1,3]`
- **Output:** `2`
- **Explanation:** Both values are odd, so their sum is even and the two-element subsequence is valid.
