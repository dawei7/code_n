# Keys and Rooms

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 841 |
| Difficulty | Medium |
| Topics | Depth-First Search, Breadth-First Search, Graph Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/keys-and-rooms/) |

## Problem Description
### Goal
There are `n` rooms labeled from `0` through `n - 1`. Every room except room `0` starts locked, and a locked room can be entered only after obtaining its key. Upon visiting a room, you may take all of the distinct numbered keys stored there; each key unlocks the room bearing that number.

The array `rooms` lists the keys found in every room. Starting from room `0` and retaining every collected key, return `true` if all rooms can eventually be visited, or `false` if at least one room remains unreachable.

### Function Contract
**Inputs**

- `rooms`: a list of $n$ key lists, where $2 \leq n \leq 1000$.
- `rooms[i]` contains distinct room labels from `0` through `n - 1`.
- Define the total number of stored keys as

$$
K = \sum_{i=0}^{n-1} \lvert \texttt{rooms}[i] \rvert,
$$

with $1 \leq K \leq 3000$.

**Return value**

Return whether every room is reachable by repeatedly entering unlocked rooms and collecting all keys inside them.

### Examples
**Example 1**

- Input: `rooms = [[1], [2], [3], []]`
- Output: `true`

Rooms can be visited in order `0`, `1`, `2`, `3`.

**Example 2**

- Input: `rooms = [[1, 3], [3, 0, 1], [2], [0]]`
- Output: `false`

The only key to room `2` is trapped inside room `2` itself.

**Example 3**

- Input: `rooms = [[1], []]`
- Output: `true`
