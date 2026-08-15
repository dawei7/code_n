# Minimum Discards to Balance Inventory

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3679 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sliding Window, Simulation, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-discards-to-balance-inventory/) |

## Problem Description

### Goal

The array `arrivals` records the item type arriving on each successive day. On its arrival day, an item may either be kept or discarded; a discarded item never contributes to later inventory windows.

For every day, consider the interval containing that day and up to the preceding $w-1$ days. Among the arrivals kept within any such window, no item type may occur more than $m$ times. If retaining the current arrival would violate that limit for its type, it must instead be discarded.

Return the minimum total number of discarded arrivals while satisfying the per-type limit in every window.

### Function Contract

**Inputs**

- `arrivals`: a list of $n$ positive item-type identifiers, where $1\le n\le10^5$ and each identifier is at most $10^5$.
- `w`: the window length, satisfying $1\le w\le n$.
- `m`: the maximum retained count of one type in a window, satisfying $1\le m\le w$.

Days are described as 1-indexed in the problem statement; the function receives the arrivals as an ordinary zero-indexed list.

**Return value**

Return the minimum number of arrivals that must be discarded so every window contains at most $m$ kept items of each type.

### Examples

#### Example 1

- **Input:** `arrivals = [1, 2, 1, 3, 1], w = 4, m = 2`
- **Output:** `0`

The first type never appears more than twice among retained arrivals in a four-day window.

#### Example 2

- **Input:** `arrivals = [1, 2, 3, 3, 3, 4], w = 3, m = 2`
- **Output:** `1`

The third consecutive arrival of type 3 must be discarded because the current three-day window already retains two of that type.

#### Example 3

- **Input:** `arrivals = [1, 1, 1, 1], w = 3, m = 2`
- **Output:** `1`

Discarding the third arrival lets the first expire before the fourth arrives, so no second discard is needed.
