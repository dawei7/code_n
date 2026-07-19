# Build Array from Permutation

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/build-array-from-permutation/) |
| Frontend ID | 1920 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You are given a zero-indexed permutation `nums`. If its length is $N$, it contains every integer from $0$ through $N-1$ exactly once, so every value is also a valid index into the same array.

Construct and return an array `ans` of length $N$. For every index `i`, first read `nums[i]`, use that value as a second index, and set `ans[i] = nums[nums[i]]`. The original ordering determines both lookup steps; the task asks for the composed permutation rather than a reordered copy of the input.

### Function Contract

**Inputs**

- `nums`: a permutation of the integers from $0$ through $N-1$.
- $1 \le N \le 1000$.

**Return value**

- Return an array `ans` of length $N$ satisfying `ans[i] = nums[nums[i]]` for every $0 \le i < N$.

### Examples

**Example 1**

- Input: `nums = [0, 2, 1, 5, 3, 4]`
- Output: `[0, 1, 2, 4, 5, 3]`

For example, `ans[3] = nums[nums[3]] = nums[5] = 4`.

**Example 2**

- Input: `nums = [5, 0, 1, 2, 3, 4]`
- Output: `[4, 5, 0, 1, 2, 3]`

**Example 3**

- Input: `nums = [0]`
- Output: `[0]`
