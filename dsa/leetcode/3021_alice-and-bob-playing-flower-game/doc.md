# Alice and Bob Playing Flower Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3021 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/alice-and-bob-playing-flower-game/) |

## Problem Description

### Goal

Alice and Bob play on two lanes containing $x$ and $y$ flowers. Alice moves
first. On every turn, the current player chooses either lane that still
contains a flower and removes exactly one flower from it.

The player who removes the final flower, leaving both lanes empty, immediately
wins. Given positive bounds `n` and `m`, count the ordered choices $(x,y)$ for
which Alice wins, where $1\le x\le n$ and $1\le y\le m$.

### Function Contract

**Inputs**

- `n`: the inclusive upper bound for the first lane's positive flower count
- `m`: the inclusive upper bound for the second lane's positive flower count

The contract guarantees $1\le n,m\le10^5$.

**Return value**

Return the number of ordered pairs $(x,y)$ in the stated ranges for which
Alice wins under optimal legal play.

### Examples

#### Example 1

- **Input:** `n = 3, m = 2`
- **Output:** `3`

The winning pairs are $(1,2)$, $(2,1)$, and $(3,2)$.

#### Example 2

- **Input:** `n = 1, m = 1`
- **Output:** `0`

The only game contains two flowers, so Bob removes the last one.

#### Example 3

- **Input:** `n = 2, m = 2`
- **Output:** `2`

Exactly the opposite-parity pairs $(1,2)$ and $(2,1)$ have an odd total.
