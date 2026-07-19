# Probability of a Two Boxes Having The Same Number of Distinct Balls

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1467 |
| Difficulty | Hard |
| Topics | Array, Math, Dynamic Programming, Backtracking, Combinatorics, Probability and Statistics |
| Official Link | [LeetCode](https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/) |

## Problem Description
### Goal

There are $2n$ balls belonging to $K$ distinct colors. The array `balls` has one entry per color, and `balls[i]` is the number of balls of color `i`. All balls are shuffled uniformly at random. The first $n$ shuffled balls are placed in box 1, while the remaining $n$ balls are placed in box 2.

The two boxes are distinguishable: exchanging their contents produces a different distribution. Balls of the same color are indistinguishable for determining which colors occur, but the random shuffle gives different physical balls equal chances to occupy the first half. Return the probability that box 1 and box 2 contain the same number of distinct colors. An absolute error of at most $10^{-5}$ is accepted.

### Function Contract
**Inputs**

- `balls`: an array of length $K$, where $1 \le K \le 8$ and $1 \le \texttt{balls[i]} \le 6$.
- The total number of balls is even. Let $2n=\sum_{i=0}^{K-1}\texttt{balls[i]}$, so each box receives exactly $n$ balls.
- Let $B=\max_i \texttt{balls[i]}$.

**Return value**

Return the probability that the two equal-sized boxes contain equal numbers of distinct colors.

### Examples
**Example 1**

- Input: `balls = [1,1]`
- Output: `1.00000`
- Explanation: Either color may go to box 1, and both possible distributions leave one distinct color in each box.

**Example 2**

- Input: `balls = [2,1,1]`
- Output: `0.66667`
- Explanation: Eight of the twelve equally likely physical-ball shuffles produce equal distinct-color counts after the first two positions are separated from the last two.

**Example 3**

- Input: `balls = [1,2,1,2]`
- Output: `0.60000`
- Explanation: The favorable shuffle weight is `108` out of `180` total equal-sized assignments.
