## General

Computing the inversion count independently for every window repeats almost all work: consecutive windows share `k - 1` elements. Instead, maintain the inversion count while the window advances and use a Fenwick tree as a frequency table ordered by value.

The values can be as large as $10^9$, but only their relative order matters. Coordinate compression maps the distinct values of `nums` to ranks from $1$ through $U$ without changing any `<` or `>` relationship. A Fenwick-tree prefix sum can then count the elements whose values are less than or at most a given value in $O(\log U)$ time.

Build the first window from left to right. Before inserting a value `x` at position `i`, every value already stored occurs earlier in the window. The new inversions ending at `x` are therefore the stored values strictly greater than `x`: `i - count_at_most(x)`. Adding these contributions gives the first window's exact inversion count.

When the window moves one position right, let `x` be the outgoing leftmost value. Because `x` precedes every other value in the old window, precisely `count_less_than(x)` current inversions begin at `x`. Subtract that count, then remove one occurrence of `x` from the tree. Next let `y` be the incoming value. It follows all `k - 1` retained elements, so exactly `(k - 1) - count_at_most(y)` new inversions end at `y`. Add that contribution and insert `y`.

These are the only pairs that disappear or appear during a slide; every pair between two retained elements keeps both its order and its inversion status. Consequently each maintained total is the exact inversion count of its window, and taking the minimum of those totals returns the requested answer.

## Complexity detail

Let $N$ be the array length and $U$ the number of distinct values, with $U\leq N$. Compression costs $O(N\log N)$ time. Each element participates in a constant number of Fenwick-tree queries and updates, each costing $O(\log U)$, so the total running time is $O(N\log N)$. The compressed values and tree contain $O(U)$ entries, giving $O(N)$ auxiliary space in the worst case.

## Alternatives and edge cases

- **Recount each window:** A merge-sort inversion counter can evaluate one window in $O(K\log K)$ time, but repeating it for all $N-K+1$ windows costs $O((N-K+1)K\log K)$.
- **Maintain an ordinary sorted list:** Binary search finds the relevant rank quickly, but inserting and deleting in an array-backed list shifts $O(K)$ elements and can make the complete scan $O(NK)$.
- **Segment tree:** A frequency segment tree supports the same rank queries and updates in $O(\log U)$ time; it is correct but typically has a larger implementation and constant-factor footprint than a Fenwick tree.
- **Duplicate values:** Equal elements must not be counted. Removal queries values strictly below the outgoing value, while insertion counts retained values strictly above the incoming value.
- **Single-element windows:** For `k = 1`, no index pair exists, so every window has inversion count zero.
- **One full-array window:** For `k = n`, the ordinary inversion count of the entire array is the only candidate.
- **Descending window:** A strictly descending window of length $K$ has the maximum possible inversion count $K(K-1)/2$.
- **Large result:** With $K=10^5$, the count can exceed $2^{31}-1$; fixed-width implementations need a 64-bit return value.
