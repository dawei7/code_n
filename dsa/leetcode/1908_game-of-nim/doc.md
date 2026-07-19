# Game of Nim

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/game-of-nim/) |
| Frontend ID | 1908 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Bit Manipulation, Brainteaser, Game Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Alice and Bob play with several non-empty piles of stones, and Alice takes the first turn. On each turn, the current player chooses exactly one non-empty pile and removes any positive number of stones from it. A move may empty the selected pile, but it cannot affect another pile.

The players both choose their moves optimally. When no stones remain, the player whose turn it is cannot move and loses; the other player wins. Given the initial number of stones in every pile, determine whether Alice has a strategy that guarantees her victory.

### Function Contract

**Inputs**

- `piles`: a list of $N$ positive integers, where `piles[i]` is the number of stones in pile $i$.
- $1 \le N \le 7$.
- $1 \le \texttt{piles[i]} \le 7$.

**Return value**

- Return `True` if Alice wins under optimal play; otherwise return `False`.

### Examples

**Example 1**

- Input: `piles = [1]`
- Output: `True`

Alice removes the only stone, leaving Bob without a legal move.

**Example 2**

- Input: `piles = [1,1]`
- Output: `False`

After Alice empties either pile, Bob empties the other one and wins.

**Example 3**

- Input: `piles = [1,2,3]`
- Output: `False`

The initial bitwise XOR is zero, so every move gives Bob a position from which the XOR can be restored to zero.
