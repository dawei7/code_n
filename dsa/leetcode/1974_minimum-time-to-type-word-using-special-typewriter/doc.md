# Minimum Time to Type Word Using Special Typewriter

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1974 |
| Difficulty | Easy |
| Topics | String, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/) |

## Problem Description
### Goal
A special typewriter arranges the 26 lowercase English letters in a circle.
Its pointer starts at `a`. During one second, you may either move the pointer
one position clockwise, move it one position counterclockwise, or type the
letter currently under the pointer.

Given a nonempty lowercase string `word`, type its characters from left to
right in their supplied order. Return the minimum total number of seconds
needed for all pointer movements and typing operations.

### Function Contract
**Inputs**

- `word`: a lowercase English string of length $N$, where
  $1 \le N \le 100$.

**Return value**

- The minimum number of one-second movement and typing operations required to
  produce `word`, starting with the pointer at `a`.

### Examples
**Example 1**

- Input: `word = "abc"`
- Output: `5`

**Example 2**

- Input: `word = "bza"`
- Output: `7`

**Example 3**

- Input: `word = "zjpc"`
- Output: `34`
