# New 21 Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 837 |
| Difficulty | Medium |
| Topics | Math, Dynamic Programming, Sliding Window, Probability and Statistics |
| Official Link | [LeetCode](https://leetcode.com/problems/new-21-game/) |

## Problem Description
### Goal
Alice begins with `0` points. While her total is less than `k`, she draws a number chosen uniformly from the integers in `[1, maxPts]` and adds it to her score. Draws are independent and every value in that range has equal probability.

Alice stops drawing as soon as her score is `k` or more. Return the probability that her final score is `n` or fewer. An answer within $10^{-5}$ of the true probability is accepted.

### Function Contract
**Inputs**

- `n`: the largest final score counted as successful.
- `k`: the score at which Alice stops drawing; $0 \leq k \leq n \leq 10^4$.
- `maxPts`: the inclusive upper bound on one draw, with $1 \leq \texttt{maxPts} \leq 10^4$.

**Return value**

Return the probability that Alice's score is at most `n` when the game stops.

### Examples
**Example 1**

- Input: `n = 10, k = 1, maxPts = 10`
- Output: `1.00000`

Alice draws once, and every possible result lies at or below `10`.

**Example 2**

- Input: `n = 6, k = 1, maxPts = 10`
- Output: `0.60000`

Exactly six of the ten equally likely one-draw results are successful.

**Example 3**

- Input: `n = 21, k = 17, maxPts = 10`
- Output: `0.73278`
