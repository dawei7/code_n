# Find the Losers of the Circular Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2682 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/find-the-losers-of-the-circular-game/) |

## Problem Description

### Goal

There are `n` friends numbered from 1 through `n` in clockwise order around a circle. Moving clockwise after friend `n` wraps back to friend 1. Friend 1 begins with a ball.

On turn $i$, the current holder passes the ball exactly $i \cdot k$ positions clockwise. Thus the first pass moves `k` positions, the second moves `2 * k`, and the distance continues increasing by `k` each turn. The game stops as soon as a friend receives the ball for the second time.

The losers are the friends who never held the ball before the game ended. Return their numbers in ascending order.

### Function Contract

**Inputs**

- `n`: The number of friends, with $1 \leq n \leq 50$.
- `k`: The base passing distance, with $1 \leq k \leq n$.

**Return value**

Return the ascending list of 1-based friend numbers that never received the ball.

### Examples

**Example 1**

- Input: `n = 5, k = 2`
- Output: `[4,5]`
- Explanation: Friends 1, 3, and 2 receive the ball before friend 3 receives it again.

**Example 2**

- Input: `n = 4, k = 4`
- Output: `[2,3,4]`
- Explanation: The first pass wraps from friend 1 back to friend 1, immediately ending the game.
