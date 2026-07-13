# Nim Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 292 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Brainteaser, Game Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/nim-game/) |

## Problem Description
### Goal
A single pile starts with positive `n` stones. You move first, and the two players alternate removing exactly one, two, or three stones from the remaining pile. The player who takes the final stone wins the game.

Assuming both players choose moves optimally, return `True` when the first player has a strategy that guarantees victory regardless of the opponent's responses. Return `False` when every legal first move allows an optimal opponent to force the win. The task asks for the existence of a winning strategy, not for a particular sequence of removals or the number of turns.

### Function Contract
**Inputs**

- `n`: the positive number of stones in the initial pile

**Return value**

`True` when the first player can force a win; otherwise `False`.

### Examples
**Example 1**

- Input: `n = 4`
- Output: `false`

**Example 2**

- Input: `n = 1`
- Output: `true`

**Example 3**

- Input: `n = 2`
- Output: `true`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Work backward from the end**

Piles of one, two, or three stones are immediately winning. A pile of four is different: every move leaves an immediately winning pile for the opponent. This is the first losing position.

**The four-stone rhythm**

After either player removes `x` stones, the other can remove $4 - x$. Together the two turns consume exactly four stones. Consequently, a player who hands the opponent a multiple of four can restore that situation after every response.

If `n` is not divisible by four, the first player removes $n \bmod 4$ stones and establishes this rhythm. If `n` is divisible by four, every opening move breaks the multiple, and the opponent establishes the rhythm instead. This proves that the losing piles are exactly `4, 8, 12, ...`.

#### Complexity detail

Testing $n \bmod 4$ uses constant time and space regardless of the pile size.

#### Alternatives and edge cases

- Dynamic programming can label every pile from `1` through `n`, but costs $O(n)$ time and space to rediscover the same pattern.
- A recursive game tree repeats equivalent pile sizes and is much more expensive without memoization.
- The contract begins with a positive pile, so there is no zero-stone case to define.

</details>
