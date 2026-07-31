# Stone Removal Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3360 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/stone-removal-game/) |

## Problem Description

### Goal

Alice and Bob alternate turns removing stones from one pile, with Alice moving first. Alice's opening move must remove exactly $10$ stones. Every later move must remove exactly one fewer stone than the immediately preceding move, so the forced sequence of requested amounts is $10,9,8,\ldots$.

A player cannot choose a different amount or skip a turn. If the pile contains fewer stones than the current required amount, that player cannot move and loses immediately. Given the positive initial pile size $n$, determine whether Alice is the winner when both players follow these forced rules.

### Function Contract

**Inputs**

- `n`: The initial number of stones, with $1\le n\le50$.

**Return value**

- `True` if Alice makes the last successful move and Bob is the first player unable to move; otherwise `False`.

### Examples

**Example 1**

- Input: `n = 12`
- Output: `true`
- Explanation: Alice removes $10$, leaving $2$. Bob needs to remove $9$ but cannot, so Alice wins.

**Example 2**

- Input: `n = 1`
- Output: `false`
- Explanation: Alice cannot make the required opening move of $10$ stones.
