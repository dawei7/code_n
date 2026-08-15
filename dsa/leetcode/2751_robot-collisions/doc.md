# Robot Collisions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2751 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Stack, Sorting, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/robot-collisions/) |

## Problem Description

### Goal

There are $n$ robots at distinct positions on a line. Robot `i` begins at `positions[i]`, has health `healths[i]`, and moves continuously at the same speed as every other robot: left when `directions[i]` is `"L"` and right when it is `"R"`. The input order is an identity order and need not match spatial order.

When two robots meet, the one with lower health is removed and the survivor loses one health while continuing in its original direction. Equal-health robots are both removed. Resolve every collision, then return the final positive healths of surviving robots in their original input order. Return an empty array if none survive.

### Function Contract

Let $n$ be the common length of the inputs.

**Inputs**

- `positions`: An array of $n$ distinct starting coordinates, each between $1$ and $10^9$.
- `healths`: An array of positive initial health values, each between $1$ and $10^9$.
- `directions`: A length-$n$ string containing only `"L"` and `"R"`.

The common length satisfies $1 \le n \le 10^5$.

**Return value**

Return the surviving robots' final health values in original input order.

### Examples

#### Example 1

- **Input:** `positions = [5,4,3,2,1], healths = [2,17,9,15,10], directions = "RRRRR"`
- **Output:** `[2,17,9,15,10]`
- **Explanation:** Robots moving at equal speed in the same direction never meet.

#### Example 2

- **Input:** `positions = [3,5,2,6], healths = [10,10,15,12], directions = "RLRL"`
- **Output:** `[14]`
- **Explanation:** The equal-health pair disappears, while the robot originally at position `2` wins its collision and loses one health.

#### Example 3

- **Input:** `positions = [1,2,5,6], healths = [10,10,11,11], directions = "RLRL"`
- **Output:** `[]`
- **Explanation:** Both approaching pairs have equal health, so every robot is removed.
