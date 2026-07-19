# Maximum Points You Can Obtain from Cards

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1423 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/) |

## Problem Description

### Goal

A row of cards has point values in `cardPoints`. On each move, take exactly one card from either the left end or the right end of the remaining row. Continue until exactly `k` cards have been taken.

Return the maximum total value of the selected cards. Choices at the two ends interact because removing a card exposes the next card on that same side, and all `k` moves are required.

### Function Contract

**Inputs**

- `card_points`: an array of $n$ positive card values, where $1 \le n \le 10^5$ and $1 \le \texttt{card_points[i]} \le 10^4$.
- `k`: the exact number of cards to take, where $1 \le k \le n$.

**Return value**

- The maximum sum obtainable by taking exactly `k` cards from the two ends.

### Examples

**Example 1**

- Input: `card_points = [1,2,3,4,5,6,1], k = 3`
- Output: `12`

**Example 2**

- Input: `card_points = [2,2,2], k = 2`
- Output: `4`

**Example 3**

- Input: `card_points = [9,7,7,9,7,7,9], k = 7`
- Output: `55`
