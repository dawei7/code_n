# Binary Search

| | |
|---|---|
| **ID** | `search_02` |
| **Category** | searching |
| **Complexity (required)** | O(log n) |
| **Difficulty** | 3/10 |
| **Interview relevance** | 8/10 |
| **Wikipedia** | [Binary search](https://en.wikipedia.org/wiki/Binary_search) |

## Problem statement

Given a **sorted** array `a[0..n-1]` (ascending) and a
`target`, find the index of `target` in the array, or `-1`
if it isn't present.

**Input:** a sorted array and a target value.
**Output:** the index of `target`, or `-1`.

**Example:**

| a | target | Answer |
|---|---|---:|
| `[1, 3, 5, 7, 9, 11, 13, 15]` | 7 | 3 |
| `[1, 3, 5, 7, 9, 11, 13, 15]` | 12 | -1 |
| `[5]` | 5 | 0 |
| `[5]` | 3 | -1 |
| `[]` | 0 | -1 |

## When to use it

- The canonical **divide-and-conquer search** and the single
  most important search algorithm. Asked in some form at
  virtually every interview.
- The "**invariant-driven**" template (left/right pointers,
  mid computation, comparison, move one pointer) is also the
  basis for many non-search problems: lower/upper bound,
  search in rotated arrays, "find first bad version",
  "find the peak", "find the minimum in a rotated sorted
  array", "search a 2D matrix", "find the kth smallest",
  etc.

## Approach

Maintain a search range `[lo, hi]` and a loop invariant:
`target` (if present) is in `a[lo..hi]`. Each iteration:
- Compute `mid`. Two common formulas:
  - `mid = (lo + hi) // 2` (classic; overflow risk for huge
    arrays in low-level languages)
  - `mid = lo + (hi - lo) // 2` (overflow-safe)
- Compare `a[mid]` to `target`:
  - **Equal:** found, return `mid`.
  - **Less than:** the answer (if any) is to the right;
    `lo = mid + 1`.
  - **Greater than:** the answer (if any) is to the left;
    `hi = mid - 1`.
- Loop until `lo > hi`. Then return `-1`.

The invariant holds at every step, so when the loop exits
with `lo > hi`, we know `target` is not in the array.

**Loop variants:**
- **Closed interval** `[lo, hi]` — initialized `lo = 0`,
  `hi = n - 1`. Exit on `lo > hi`. Most common.
- **Half-open** `[lo, hi)` — initialized `lo = 0`, `hi = n`.
  Exit on `lo == hi`. Standard in C++ `std::lower_bound`.
- **Open** `(lo, hi)` — initialized `lo = -1`, `hi = n`.
  Exit on `hi - lo == 1`. Used by some clean recursive
  formulations.

Pick one and stick with it; mixing the conventions is the
#1 source of off-by-one bugs.

## Algorithm (pseudocode)

```
binary_search(a, target):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2     # overflow-safe
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

## Walk-through

`a = [1, 3, 5, 7, 9, 11, 13, 15]`, `target = 7`.

| Iter | lo | hi | mid | a[mid] | cmp | next |
|---:|---:|---:|---:|---:|---|---|
| 1 | 0 | 7 | 3 | 7 | == | return 3 |

(Trivially found in 1 step — but log₂(8) = 3, so 1-3
iterations is expected for an 8-element array.)

Let's try `target = 12` (not present):

| Iter | lo | hi | mid | a[mid] | cmp | next |
|---:|---:|---:|---:|---:|---|---|
| 1 | 0 | 7 | 3 | 7 | < | lo = 4 |
| 2 | 4 | 7 | 5 | 11 | < | lo = 6 |
| 3 | 6 | 7 | 6 | 13 | > | hi = 5 |
| 4 | 6 | 5 | — | — | exit | return -1 |

3 iterations to confirm absence. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | O(1) — found at mid on first try | O(1) |
| **Average** | O(log n) | O(1) |
| **Worst** | O(log n) | O(1) |

Iterative is O(1) space; recursive is O(log n) stack space.

## Variants & optimizations

- **Lower bound / upper bound** — return the leftmost (or
  rightmost) position where `target` could be inserted. The
  basis for C++ `std::lower_bound` / `std::upper_bound` and
  for the bisect module in Python. The change is one line
  in the comparison (don't return early on `==`).
- **Search in rotated sorted array** — see `search_12`.
  Decide which half is sorted, then check whether `target`
  is in that half.
- **First bad version** — find the first index where
  `isBadVersion(i)` is True. Same as lower-bound, with a
  custom predicate.
- **Search a 2D matrix** — treat the flattened matrix as a
  1D sorted array; use the standard binary search with
  `mid_row = mid // n_cols`, `mid_col = mid % n_cols`.
- **Binary search on the answer** — many problems have a
  monotone "is this big enough?" check, and binary search
  can be applied to the answer space (Koko eating bananas,
  minimum days to ship, etc.).

## Real-world applications

- **Database index lookup** — B-tree indexes generalize binary
  search to disk-block-sized nodes; same O(log n) shape.
- **Dictionary lookup** — finding a word in a sorted lexicon.
- **git bisect** — binary search over the commit history to
  find the commit that introduced a bug.
- **Version range checks** — "is this version older than X?"
  is a binary search in many build systems.
- **Cache-line binary search** — for arrays small enough to
  fit in L1, binary search beats hash table lookups because
  of cache-friendliness (no pointer chasing).

## Related algorithms in cOde(n)

- **[search_03 — BFS Grid](search_03_bfs-grid.md)** — graph
  search when the array is the grid. (d=5/10, r=8/10)
- **[search_04 — DFS Grid](search_04_dfs-grid.md)** — the
  other graph-search order. (d=4/10, r=8/10)
- **[search_12 — Search in Rotated Sorted Array](search_12_search-in-rotated-sorted-array.md)** —
  the harder variant. (d=5/10, r=8/10)
- **[hash_01 — Two Sum](hash_01_two-sum.md)** — alternative
  O(n) approach using a hash map. (d=4/10, r=9/10)

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-
programming reference sites. For the canonical encyclopedia
entry, follow the Wikipedia link at the top of the page.
Source repository: <https://github.com/dawei7/code_n>.*
