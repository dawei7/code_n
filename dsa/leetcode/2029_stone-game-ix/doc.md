# Stone Game IX

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2029 |
| Difficulty | Medium |
| Topics | Array, Math, Greedy, Counting, Game Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/stone-game-ix/) |

## Problem Description

### Goal

Alice and Bob alternately remove one stone from a collection, with Alice
moving first. Every stone has a positive integer value. After each removal,
the current player loses immediately if the sum of all values removed so far
is divisible by $3$.

If the stones run out without either player triggering such a sum, Bob wins
automatically, even when Alice would otherwise move next. Assuming both
players choose optimally, determine whether Alice can force a win.

### Function Contract

Let $N$ be the number of stones.

**Inputs**

- `stones`: a list of $N$ values, where $1 \le N \le 10^5$ and
  $1 \le \texttt{stones[i]} \le 10^4$.

**Return value**

- `True` if Alice has a winning strategy under optimal play; otherwise,
  `False`.

### Examples

**Example 1**

- Input: `stones = [2, 1]`
- Output: `True`
- Explanation: Bob must take the remaining stone and makes the cumulative sum
  equal to `3`, so Bob loses.

**Example 2**

- Input: `stones = [2]`
- Output: `False`
- Explanation: Alice makes a safe move, but exhaustion awards the game to Bob.

**Example 3**

- Input: `stones = [5, 1, 2, 4, 3]`
- Output: `False`
