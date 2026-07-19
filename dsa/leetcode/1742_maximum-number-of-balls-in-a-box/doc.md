# Maximum Number of Balls in a Box

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1742 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, Math, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-balls-in-a-box/) |

## Problem Description

### Goal

A factory has one ball for every integer label from `lowLimit` through `highLimit`, inclusive. There are infinitely many numbered boxes. Each ball is placed into the box whose number equals the sum of the decimal digits in that ball's label; for example, ball `321` goes into box $3+2+1=6$.

After assigning every ball by this rule, return the greatest number of balls held by any one box. If several boxes tie for the largest occupancy, return that shared occupancy rather than a box number.

### Function Contract

**Inputs**

- `lowLimit`: the smallest ball label.
- `highLimit`: the largest ball label, with $1 \le \texttt{lowLimit} \le \texttt{highLimit} \le 10^5$.

Let $R=\texttt{highLimit}-\texttt{lowLimit}+1$ and let $D$ be the number of decimal digits in `highLimit`.

**Return value**

- Return the maximum frequency of any decimal digit sum among all $R$ labels.

### Examples

**Example 1**

- Input: `lowLimit = 1, highLimit = 10`
- Output: `2`
- Explanation: Labels `1` and `10` both have digit sum $1$, while every other box receives at most one ball.

**Example 2**

- Input: `lowLimit = 5, highLimit = 15`
- Output: `2`
- Explanation: Boxes $5$ and $6$ each receive two balls, which is the maximum occupancy.

**Example 3**

- Input: `lowLimit = 19, highLimit = 28`
- Output: `2`
- Explanation: Labels `19` and `28` both have digit sum $10$.
