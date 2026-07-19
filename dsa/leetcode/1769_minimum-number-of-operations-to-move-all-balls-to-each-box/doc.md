# Minimum Number of Operations to Move All Balls to Each Box

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1769 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/) |

## Problem Description

### Goal

A binary string `boxes` describes $n$ boxes arranged in a line. Character `0` means that a box is empty, while `1` means that it initially contains one ball.

One operation moves one ball from its current box to an adjacent box. Several balls may occupy the same box after moves.

For every possible target index, determine the minimum operations needed to bring all balls to that box. Calculate each target independently from the original configuration and return all $n$ costs.

### Function Contract

**Inputs**

- `boxes`: a binary string of length $n$, where $1 \le n \le 2000$.
- `boxes[i] = "1"` means box `i` initially contains one ball; `"0"` means it is empty.

**Return value**

- Return an integer array `answer` of length $n$.
- `answer[i]` is the minimum number of adjacent one-step ball moves required to gather every initially present ball in box `i`.

### Examples

**Example 1**

- Input: `boxes = "110"`
- Output: `[1,1,3]`
- Explanation: Gathering at indices `0` or `1` costs one move; gathering at index `2` costs two moves for the first ball and one for the second.

**Example 2**

- Input: `boxes = "001011"`
- Output: `[11,8,5,4,3,4]`
- Explanation: Each entry sums the distances from the balls initially at indices `2`, `4`, and `5`.

**Example 3**

- Input: `boxes = "0"`
- Output: `[0]`
- Explanation: With no balls present, every required movement cost is zero.
