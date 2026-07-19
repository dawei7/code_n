# Check if Array Is Sorted and Rotated

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1752 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/) |

## Problem Description

### Goal

Given an integer array `nums`, determine whether it can be obtained from an array sorted in non-decreasing order by rotating that sorted array by some number of positions. A rotation by zero positions is permitted, so an already sorted array qualifies.

Duplicates are allowed. Rotating an array `A` by $x$ positions produces an array `B` of the same length where `B[i]` equals `A[(i+x) % n]` for every valid index. Return `true` exactly when some sorted original array and some legal rotation amount produce `nums`.

### Function Contract

**Inputs**

- `nums`: a nonempty list with $1 \le \lvert\texttt{nums}\rvert \le 100$ and $1 \le \texttt{nums[i]} \le 100$.

Let $n=\lvert\texttt{nums}\rvert$.

**Return value**

- Return `True` if `nums` is a rotation, possibly by zero, of a non-decreasing array; otherwise return `False`.

### Examples

**Example 1**

- Input: `nums = [3, 4, 5, 1, 2]`
- Output: `True`
- Explanation: Rotating `[1, 2, 3, 4, 5]` to begin at `3` produces the input.

**Example 2**

- Input: `nums = [2, 1, 3, 4]`
- Output: `False`
- Explanation: No single rotation cut makes all values non-decreasing.

**Example 3**

- Input: `nums = [1, 2, 3]`
- Output: `True`
- Explanation: The array is already non-decreasing, corresponding to a zero-position rotation.
