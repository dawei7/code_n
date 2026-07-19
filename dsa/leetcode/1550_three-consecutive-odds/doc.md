# Three Consecutive Odds

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1550 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/three-consecutive-odds/) |

## Problem Description
### Goal
Given an integer array `arr`, determine whether it contains three odd numbers in consecutive positions anywhere in the given order. The three values only need to be odd; they do not need to be equal or consecutive in numerical value.

Return `true` as soon as any length-three contiguous block consists entirely of odd values. Return `false` when no such block exists.

### Function Contract
**Inputs**

- `arr`: an integer array of length $n$, where $1 \le n \le 1000$ and $1 \le \texttt{arr[i]} \le 1000$.

**Return value**

`true` if some three adjacent elements are all odd; otherwise `false`.

### Examples
**Example 1**

- Input: `arr = [2, 6, 4, 1]`
- Output: `false`
- Explanation: The only odd value is not part of a three-element odd run.

**Example 2**

- Input: `arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]`
- Output: `true`
- Explanation: The adjacent values `[5, 7, 23]` are all odd.

**Example 3**

- Input: `arr = [1, 3, 5]`
- Output: `true`
- Explanation: The entire array is a qualifying length-three block.
