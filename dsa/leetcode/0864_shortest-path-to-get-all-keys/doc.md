# Shortest Path to Get All Keys

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 864 |
| Difficulty | Hard |
| Topics | Array, Bit Manipulation, Breadth-First Search, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-path-to-get-all-keys/) |

## Problem Description
### Goal
You are given an $m \times n$ grid. An empty cell is `.`, a wall is `#`, and the unique starting point is `@`. Lowercase letters are keys, while the corresponding uppercase letters are locks. Starting at `@`, one move travels one cell up, down, left, or right without leaving the grid or entering a wall.

Stepping onto a key collects it permanently. A lock may be entered only after its matching key has been collected. For some $1 \leq c \leq 6$, the grid contains exactly one key and one matching lock for each of the first $c$ lowercase letters. Find the minimum moves needed to collect every key—not necessarily to open every lock—or return `-1` if collecting them all is impossible.

### Function Contract
**Inputs**

- `grid`: an array of $m$ equal-length strings describing the cells, where $1 \leq m,n \leq 30$.

Let $c$ be the number of distinct keys, where $1 \leq c \leq 6$. Each key is unique and has one matching lock.

**Return value**

Return the minimum number of cardinal-direction moves required to collect all $c$ keys, or `-1` if no legal route can do so.

### Examples
**Example 1**

- Input: `grid = ["@.a..","###.#","b.A.B"]`
- Output: `8`

The objective is complete as soon as both keys are held; opening every lock is not required.

**Example 2**

- Input: `grid = ["@..aA","..B#.","....b"]`
- Output: `6`

**Example 3**

- Input: `grid = ["@Aa"]`
- Output: `-1`

The only route to key `a` is blocked by lock `A`.
