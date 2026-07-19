# Design Movie Rental System

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/design-movie-rental-system/) |
| Frontend ID | 1912 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Design, Heap (Priority Queue), Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A movie rental company has `n` shops. Each entry `[shop, movie, price]` describes one copy of `movie` held by `shop` at a fixed rental price; a shop carries at most one copy of any particular movie. Initially every listed copy is unrented.

Build a stateful system that searches for the five cheapest available copies of a requested movie, rents an available copy, accepts the return of a rented copy, and reports the five cheapest copies currently rented across all movies. Search results order by `(price, shop)`. Reports order by `(price, shop, movie)` and return `[shop, movie]` pairs. The operation sequence guarantees every rent and return is valid.

### Function Contract

**Inputs**

- `MovieRentingSystem(n, entries)` initializes the inventory for $n$ shops.
- `search(movie)` returns up to five shops with an unrented copy of `movie`.
- `rent(shop, movie)` marks that copy as rented.
- `drop(shop, movie)` returns that copy to the available inventory.
- `report()` returns up to five rented `[shop, movie]` pairs.
- $1 \le n \le 3 \times 10^5$, $1 \le E = \lvert\texttt{entries}\rvert \le 10^5$, and at most $10^5$ operations follow construction.
- Shop indices lie in $[0,n)$; movie IDs and prices lie in $[1,10^4]$.

**Return value**

- Construction, `rent`, and `drop` produce `null`.
- `search` and `report` produce the ordered lists described above, returning an empty list when no matching copy exists.

### Examples

**Example 1**

- Input: `operations = ["MovieRentingSystem","search","rent","rent","report","drop","search"]`, `arguments = [[3,[[0,1,5],[0,2,6],[0,3,7],[1,1,4],[1,2,7],[2,1,5]]],[1],[0,1],[1,2],[],[1,2],[2]]`
- Output: `[null,[1,0,2],null,null,[[0,1],[1,2]],null,[0,1]]`

Movie `1` is initially cheapest at shop `1`; after the two rentals, the report orders the rented copies by price.

**Example 2**

- Input: `operations = ["MovieRentingSystem","search","report"]`, `arguments = [[1,[[0,10,3]]],[10],[]]`
- Output: `[null,[0],[]]`

The only copy is available, and no copy is rented.

**Example 3**

- Input: `operations = ["MovieRentingSystem","rent","report","drop","report"]`, `arguments = [[2,[[0,5,2],[1,5,2]]],[1,5],[],[1,5],[]]`
- Output: `[null,null,[[1,5]],null,[]]`

Returning the only rented copy empties the report.
