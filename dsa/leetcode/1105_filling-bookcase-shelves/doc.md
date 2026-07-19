# Filling Bookcase Shelves

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1105 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open](https://leetcode.com/problems/filling-bookcase-shelves/) |

## Problem Description

### Goal

Each entry `books[i] = [thickness_i, height_i]` describes the thickness and height of the $i$th book. Place all books onto successive bookcase shelves whose available width is `shelfWidth`.

Every shelf receives a consecutive group of books in their original order, and the sum of their thicknesses may not exceed `shelfWidth`. Adding a shelf increases the bookcase height by the maximum height among the books placed on it. Partition the complete ordered sequence into shelves so that the sum of these shelf heights is as small as possible.

### Function Contract

**Inputs**

- `books`: an ordered list of $n$ pairs `[thickness, height]`, where $1 \leq n \leq 1000$, $1 \leq \texttt{thickness} \leq \texttt{shelf_width}$, and $1 \leq \texttt{height} \leq 1000$.
- `shelf_width`: the maximum total thickness of one shelf, where $1 \leq \texttt{shelf_width} \leq 1000$.

**Return value**

The minimum total height of a bookcase containing all books in the given order.

### Examples

**Example 1**

- Input: `books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4`
- Output: `6`

An optimal arrangement has shelf heights 1, 3, and 2. The second book does not need to share the first shelf.

**Example 2**

- Input: `books = [[1,3],[2,4],[3,2]], shelf_width = 6`
- Output: `4`

All three books fit on one shelf, whose height is 4.
