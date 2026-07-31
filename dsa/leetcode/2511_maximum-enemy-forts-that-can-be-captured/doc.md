# Maximum Enemy Forts That Can Be Captured

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2511 |
| Difficulty | Easy |
| Topics | Array, Two Pointers |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/) |

## Problem Description
### Goal
You are given a 0-indexed array `forts` describing positions along a line. A value of `1` marks a fort under your command, `0` marks an enemy fort, and `-1` marks a position with no fort.

Choose one of your forts at index `i` and move its army to an empty position `j`. Every position strictly between `i` and `j` must contain an enemy fort. All enemy forts crossed during the move are captured.

Return the maximum number of enemy forts that can be captured by one valid move. Return `0` if no such move is possible or if you command no fort.

### Function Contract
**Inputs**

- `forts`: A list of $n$ integers, each equal to `-1`, `0`, or `1`, using the meanings above.

The constraint is $1 \le n \le 1000$.

**Return value**

An integer equal to the greatest number of enemy forts captured by one valid move.

### Examples
**Example 1**

- Input: `forts = [1,0,0,-1,0,0,0,0,1]`
- Output: `4`
- Explanation: Moving the army from index `8` to the empty position at index `3` crosses and captures four enemy forts. The other valid move captures only two.

**Example 2**

- Input: `forts = [0,0,1,-1]`
- Output: `0`
- Explanation: The owned fort and empty destination are adjacent, so their valid move crosses no enemy forts.
