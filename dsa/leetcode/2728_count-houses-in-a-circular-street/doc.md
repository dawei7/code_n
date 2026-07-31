# Count Houses in a Circular Street

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2728 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Interactive |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/count-houses-in-a-circular-street/) |

## Problem Description

### Goal

A circular street contains an unknown positive number $n$ of houses. Every house has one door, which may initially be open or closed, and the houses form a cycle: continuing in either direction eventually returns to the starting house. Your initial position and the initial door states are arbitrary.

You control a `Street` interface that can open or close the current door, report whether that door is open, and move one house to the left or right. A supplied bound `k` guarantees $n \le k$. Use only those operations and return the exact number of houses on the street.

### Function Contract

**Inputs**

- `street`: A circular `Street` positioned at an arbitrary house. Its methods are `openDoor()`, `closeDoor()`, `isDoorOpen()`, `moveRight()`, and `moveLeft()`.
- `k`: A positive upper bound on the number of houses, with $1 \le n \le k \le 10^3$.

**Return value**

Return $n$, the number of houses in the circular street.

### Examples

**Example 1**

- Input: `street = [0,0,0,0], k = 10`
- Output: `4`
- Explanation: The four entries represent four houses whose doors are initially closed; the starting point is arbitrary and does not change the cycle length.

**Example 2**

- Input: `street = [1,0,1,1,0], k = 5`
- Output: `5`
- Explanation: The street contains five houses, regardless of the mixed initial door states.

**Example 3**

- Input: `street = [1], k = 1`
- Output: `1`
- Explanation: Moving once around a one-house street returns to the same marked door.
