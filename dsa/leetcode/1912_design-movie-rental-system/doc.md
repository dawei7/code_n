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

### Required Complexity

- **Time:** $O(E \log E + Q \log(E + Q))$
- **Space:** $O(E + Q)$

<details>
<summary>Approach</summary>

#### General

**Index the two orderings**

Store the immutable price for every `(shop, movie)` key. For each movie, maintain a min-heap of available candidates ordered by `(price, shop)`. Maintain one global min-heap of rented candidates ordered by `(price, shop, movie)`. A set records which keys are currently rented.

`search` extracts at most five valid entries from one movie heap, records their shop IDs, and pushes those valid entries back so searching does not change availability. `report` performs the analogous bounded extraction from the global rented heap and returns `[shop, movie]` pairs. Heap tuple order implements every required tie-break directly.

**Make lazy deletion safe across repeated cycles**

Removing an arbitrary `(shop, movie)` from a heap would be expensive, so state changes leave old heap records in place. Associate each copy with a monotonically increasing version. Every rent or drop increments that version, and every newly pushed heap record includes it.

A heap record is valid only when its version equals the copy's current version and its rented state matches the heap. This rejects stale records from all earlier cycles. In particular, dropping a copy does not make its original pre-rental record valid again, so repeated searches can never return the same shop twice.

**Preserve the state transitions**

Renting increments the version, marks the key rented, and pushes its current record into the global rented heap. Dropping increments again, clears the rented state, and pushes a current record into the per-movie available heap. The problem's validity guarantees mean neither operation needs to recover from an illegal state.

#### Complexity detail

Construction inserts $E$ records and costs at most $O(E\log E)$. Each rent or drop performs one heap insertion in $O(\log(E+Q))$ time. A search or report returns at most five valid records and performs $O(\log(E+Q))$ work per returned record, plus stale removals. Every stale record is removed only once, so those removals are amortized across the full operation sequence. The total time is $O(E\log E + Q\log(E+Q))$.

Prices, states, versions, and initial heap records use $O(E)$ space. Each update can add one lazy heap record, so the worst-case space across $Q$ operations is $O(E+Q)$.

#### Alternatives and edge cases

- **Ordered sets:** Balanced ordered sets support direct deletion and insertion without stale records, with the same logarithmic operation bounds, but Python's standard library does not provide one.
- **Scan the inventory:** Filtering and sorting every search or report is simple and correct but can take $O(E\log E)$ per query.
- **Fewer than five matches:** Return every valid match without padding.
- **Equal prices in search:** The smaller shop index comes first.
- **Equal prices in reports:** Compare shop first, then movie.
- **Repeated rent/drop cycles:** Version checks must invalidate every older record so a copy appears at most once.
- **Unknown or fully rented movie:** `search` returns an empty list.

</details>
