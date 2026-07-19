# Car Fleet II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1776 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Stack, Heap (Priority Queue), Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/car-fleet-ii/) |

## Problem Description

### Goal

There are $n$ cars moving in the same direction on a one-lane road. `cars[i] = [position_i, speed_i]` gives car $i$'s initial position in meters and speed in meters per second. Positions are strictly increasing, so the array lists cars from back to front.

Treat every car as a point. When cars occupy the same position, they form one fleet at that position and continue at the initial speed of the slowest car in the fleet. For every original car, return the time at which it first collides with the next car or fleet ahead. Use `-1` if that collision never occurs. A returned time within $10^{-5}$ of the exact value is accepted.

### Function Contract

**Inputs**

- `cars`: an array of $n$ pairs `[position, speed]`.
- Positions are strictly increasing.
- The constraints guarantee $1 \le n \le 10^5$ and $1 \le \text{position}, \text{speed} \le 10^6$.

**Return value**

Return an array of $n$ floating-point collision times. Entry $i$ is car $i$'s first collision time, or `-1.0` when it never catches a car or fleet ahead.

### Examples

**Example 1**

- Input: `cars = [[1,2],[2,1],[4,3],[7,2]]`
- Output: `[1.0,-1.0,3.0,-1.0]`
- Explanation: Cars `0` and `2` catch their respective next cars after one and three seconds.

**Example 2**

- Input: `cars = [[3,4],[5,4],[6,3],[9,1]]`
- Output: `[2.0,1.0,1.5,-1.0]`
- Explanation: The collision schedule accounts for fleets that form before a car farther back arrives.

**Example 3**

- Input: `cars = [[1,1],[2,2],[3,3]]`
- Output: `[-1.0,-1.0,-1.0]`
- Explanation: Every car ahead is faster, so no car catches another.
