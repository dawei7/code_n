# Design Movie Rental System

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1912 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Design, Heap (Priority Queue), Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [design-movie-rental-system](https://leetcode.com/problems/design-movie-rental-system/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/design-movie-rental-system/).

### Goal
Design a movie rental system that can search the cheapest shops for an unrented movie, rent a movie from a shop, drop it back, and report the cheapest currently rented movies.

### Function Contract
**Inputs**

- Initial entries of `[shop, movie, price]`.
- `search(movie)`: list up to five shops with that unrented movie, ordered by price then shop.
- `rent(shop, movie)`: mark that copy rented.
- `drop(shop, movie)`: mark that copy unrented.
- `report()`: list up to five rented `[shop, movie]` pairs ordered by price, shop, then movie.

**Return value**

Return `null` for constructor and updates, lists for `search` and `report`.

### Examples
**Example 1**

- Input: `["MovieRentingSystem","search","rent","rent","report","drop","search"]`, `[[3,[[0,1,5],[0,2,6],[0,3,7],[1,1,4],[1,2,7],[2,1,5]]],[1],[0,1],[1,2],[],[1,2],[2]]`
- Output: `[null,[1,0,2],null,null,[[0,1],[1,2]],null,[0,1]]`

**Example 2**

- Input: `["MovieRentingSystem","search","report"]`, `[[1,[[0,10,3]]],[10],[]]`
- Output: `[null,[0],[]]`

**Example 3**

- Input: `["MovieRentingSystem","rent","report","drop","report"]`, `[[2,[[0,5,2],[1,5,2]]],[1,5],[],[1,5],[]]`
- Output: `[null,null,[[1,5]],null,[]]`

---

## Solution
### Approach
Maintain the fixed price for every `(shop, movie)`. For each movie, keep an ordered set or heap of unrented copies keyed by `(price, shop)`, with lazy deletion if using heaps. Also maintain a global ordered set or heap of rented copies keyed by `(price, shop, movie)`. Rent and drop move one copy between those structures.

### Complexity Analysis
- **Time Complexity**: `O(log n)` per update and `O(5 log n)` for bounded reports/searches with heaps
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
