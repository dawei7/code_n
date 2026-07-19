# Hand of Straights

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 846 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/hand-of-straights/) |

## Problem Description
### Goal
Alice has a collection of cards, each labeled with an integer. She wants to rearrange every card into groups containing exactly `groupSize` cards. Within each group, the card values must be consecutive integers; repeated values are allowed only when separate physical cards supply them to one or more groups.

Given the values in `hand` and the required group size, determine whether all cards can be partitioned into such consecutive groups. Every card must belong to exactly one group, so an unused card or a group with fewer than `groupSize` cards makes the arrangement invalid.

### Function Contract
**Inputs**

- `hand`: an integer array of length $n$, where $1 \leq n \leq 10^4$ and $0 \leq \texttt{hand[i]} \leq 10^9$.
- `group_size`: the app-local name for LeetCode's `groupSize`, with $1 \leq \texttt{group\_size} \leq n$.

**Return value**

Return `true` if all cards can be rearranged into groups of `group_size` consecutive values; otherwise return `false`.

### Examples
**Example 1**

- Input: `hand = [1,2,3,6,2,3,4,7,8], group_size = 3`
- Output: `true`

One valid partition is `[1,2,3]`, `[2,3,4]`, and `[6,7,8]`.

**Example 2**

- Input: `hand = [1,2,3,4,5], group_size = 4`
- Output: `false`

Five cards cannot all be placed into groups of four.

**Example 3**

- Input: `hand = [1,2,2,3,3,4], group_size = 3`
- Output: `true`

The cards form `[1,2,3]` and `[2,3,4]`.
