# Minimum Operations to Make Binary Array Elements Equal to One I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3191 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Queue, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/) |

## Problem Description

### Goal

You are given a binary array `nums`. An operation chooses any three
consecutive elements and flips all three: each selected `0` becomes `1`, and
each selected `1` becomes `0`. You may apply the operation any number of
times, including zero.

Return the minimum number of operations required to make every array element
equal to `1`. If no sequence of allowed length-three flips can achieve that
state, return `-1`.

### Function Contract

**Inputs**

- `nums`: A binary list of length $n$, where $3 \le n \le 10^5$ and every
  element is either `0` or `1`.

**Return value**

Return the minimum number of length-three flips that makes the entire array
equal to `1`, or `-1` if this is impossible.

### Examples

#### Example 1

- **Input:** `nums = [0, 1, 1, 1, 0, 0]`
- **Output:** `3`
- **Explanation:** Flip the windows beginning at indices `0`, `1`, and `3`.

#### Example 2

- **Input:** `nums = [0, 1, 1, 1]`
- **Output:** `-1`
- **Explanation:** No sequence of length-three flips can make every bit equal to
  `1`.
