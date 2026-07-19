# Path Crossing

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1496 |
| Difficulty | Easy |
| Topics | Hash Table, String |
| Official Link | [LeetCode](https://leetcode.com/problems/path-crossing/) |

## Problem Description
### Goal

A walk starts at the origin $(0, 0)$ of a two-dimensional plane. The string `path` describes that walk one character at a time: `N` moves one unit north, `S` one unit south, `E` one unit east, and `W` one unit west.

Determine whether the walk ever reaches a location that it has already visited. The starting origin counts as visited before the first move, so returning to it is a crossing. Return `true` as soon as any position is visited for a second time; if every reached position is new, return `false`.

### Function Contract
**Inputs**

Let $N$ be the length of `path`.

- `path`: a string with $1 \le N \le 10^4$.
- Every character of `path` is one of `N`, `S`, `E`, or `W`.

**Return value**

Return `true` if the walk visits any coordinate more than once; otherwise, return `false`.

### Examples
**Example 1**

- Input: `path = "NES"`
- Output: `false`
- Explanation: The three moves reach three distinct positions and do not return to the origin.

**Example 2**

- Input: `path = "NESWW"`
- Output: `true`
- Explanation: The first westward move returns to the origin, which was visited before the walk began.

**Example 3**

- Input: `path = "NS"`
- Output: `true`
- Explanation: Moving north and then south immediately revisits the origin.
