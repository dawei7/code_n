# X of a Kind in a Deck of Cards

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 914 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Math, Counting, Number Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/) |

## Problem Description
### Goal

You are given an integer array `deck`, where `deck[i]` is the number written on the $i$th card. Partition every card into one or more groups. All groups must share one size $x$, and that size must satisfy $x>1$.

Each group must contain exactly $x$ cards, and every card within one group must have the same integer written on it. Return `true` if all cards can be partitioned under these rules; otherwise, return `false`.

### Function Contract
**Inputs**

- `deck`: an array of $n$ card values, where $1 \le n \le 10^4$ and every value is between $0$ and $10^4-1$, inclusive.

**Return value**

`true` if some common group size $x>1$ divides the frequency of every distinct card value; otherwise, `false`.

### Examples
**Example 1**

- Input: `deck = [1,2,3,4,4,3,2,1]`
- Output: `true`
- Explanation: Four groups of size $2$ can be formed, one for each value.

**Example 2**

- Input: `deck = [1,1,1,2,2,2,3,3]`
- Output: `false`
- Explanation: The frequencies $3$, $3$, and $2$ have no common divisor greater than $1$.

**Example 3**

- Input: `deck = [7,7,7]`
- Output: `true`
- Explanation: The entire deck is one group of size $3$.
