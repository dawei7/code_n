# Count Collisions on a Road

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2211 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Stack, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-collisions-on-a-road/) |

## Problem Description

### Goal

Cars occupy distinct points on an infinitely long road, ordered from left to right. The character at each position of `directions` is `L`, `R`, or `S`, indicating a car moving left, moving right, or remaining stationary. Every moving car has the same speed.

Two oppositely moving cars add two collisions when they meet, while a moving car hitting a stationary car adds one. All cars involved then become stationary and may be struck later. No other direction changes occur. Return the total collision count produced by the complete evolution.

### Function Contract

**Inputs**

- `directions`: a string of length $n$, where $1 \le n \le 10^5$ and each character is `L`, `R`, or `S`.

**Return value**

Return the total number of collisions according to the stated scoring rules.

### Examples

**Example 1**

- Input: `directions = "RLRSLL"`
- Output: `5`
- Explanation: the first opposing pair contributes two, and three later moving cars each strike a stationary collision site.

**Example 2**

- Input: `directions = "LLRR"`
- Output: `0`
- Explanation: left-moving cars at the left boundary and right-moving cars at the right boundary escape forever.

**Example 3**

- Input: `directions = "SSS"`
- Output: `0`
- Explanation: no car moves, so no collision occurs.
