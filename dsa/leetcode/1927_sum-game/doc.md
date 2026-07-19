# Sum Game

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/sum-game/) |
| Frontend ID | 1927 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, String, Greedy, Game Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Alice and Bob play on an even-length string `num` containing decimal digits and question marks. Alice moves first. On each turn, the current player chooses one remaining `"?"` and replaces it with any digit from `0` through `9`. Play ends after every question mark has been replaced.

Bob wins exactly when the sum of the digits in the first half equals the sum in the second half. Alice wins when those sums differ. Assuming both players choose optimally, determine whether Alice has a winning strategy.

### Function Contract

**Inputs**

- `num`: an even-length string containing only digits and `"?"`.
- $2 \le \lvert\texttt{num}\rvert \le 10^5$.

**Return value**

- Return `true` if Alice can force unequal final half sums.
- Return `false` if Bob can force equality.

### Examples

**Example 1**

- Input: `num = "5023"`
- Output: `false`

There are no moves, and both halves sum to five.

**Example 2**

- Input: `num = "25??"`
- Output: `true`

Alice can make equality impossible with her first replacement.

**Example 3**

- Input: `num = "?3295???"`
- Output: `false`

Under optimal replies, Bob can always balance the final sums.
