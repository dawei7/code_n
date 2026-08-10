## General

**The challenge is answering greater-count queries quickly.** For each new value $x$, we need the number of existing elements strictly greater than $x$ in each destination array. Scanning both arrays every time would take quadratic time.

The exact source uses coordinate compression and one Binary Indexed Tree, also called a Fenwick tree, per destination.

**Compress large values into ordered ranks.** `st = sorted(set(nums))` contains every distinct input value in increasing order. `bisect_left(st, x) + 1` maps $x$ to a one-based rank `i`.

Compression preserves comparisons: a value has a greater rank exactly when it is numerically greater. One-based ranks match Fenwick tree indexing, where index zero is unused.

**Understand Fenwick operations.** `update(i,1)` adds one occurrence at rank $i$. It moves upward with `x += x & -x`, updating aggregate ranges that contain that rank.

`query(i)` returns the total count at ranks 1 through $i$. It moves toward zero with `x -= x & -x` and accumulates the stored range sums.

Since rank $i$ represents value $x$, `query(i)` counts elements less than or equal to $x$. Therefore:

`len(arr1) - tree1.query(i)`

counts elements strictly greater than $x$ in `arr1`. The symmetric expression gives `b` for `arr2`. Including equal values in the prefix is essential because the problem asks for strictly greater values.

**Initialize both representations consistently.** `nums[0]` enters `arr1` and its rank is updated in `tree1`. `nums[1]` does the same for `arr2` and `tree2`. The list and tree for each destination must always describe the same multiset.

**Apply the complete tie-breaking rule.** For each later $x$:

- if `a > b`, append to `arr1`;
- if `a < b`, append to `arr2`;
- if counts tie and `len(arr1) <= len(arr2)`, append to `arr1`;
- otherwise append to `arr2`.

The `<=` handles both prescribed cases at once: a shorter first array wins, and equal lengths still choose `arr1`.

After appending, the corresponding Fenwick tree is updated at rank $i$. Forgetting this update would make future greater counts inconsistent with the actual array.

**A trace of one query.** If `arr1=[5,3,1]` and new $x=2$, the prefix query through rank 2 counts the one value 1 that is at most 2. Length three minus one gives two greater values, 5 and 3, without scanning them.
Before each new value, each tree stores exact frequencies of its destination array at compressed ranks. Fenwick prefix totals therefore produce exact greater counts. The conditional implements the statement's priority rules and updates both the list and matching tree, preserving the invariant. Final concatenation is consequently the defined result.

**The extra tree index.** The source constructs each tree with `m + 1` even though real ranks are 1 through $m$. Some updates propagate into the extra index $m+1$. Queries never request beyond $m$, so that extra aggregate is harmless, merely one unused slot beyond what is necessary.

## Complexity detail

Building the set and sorting $M\le N$ distinct values costs $O(N+M\log M)$. Every later element performs binary search, two Fenwick queries, and one update, each $O(\log M)$. Total time is $O(N\log N)$.

Compressed values, two tree arrays, destination arrays, the `nums[2:]` slice, and final result use $O(N)$ space. The returned concatenation is output space; auxiliary structures remain linear even excluding it.

The input is not modified.

## Alternatives and edge cases

- **Scan both arrays per insertion:** It directly computes greater counts but costs $O(N^2)$ worst-case time.
- **Two sorted multisets:** They support rank queries, but Python has no standard logarithmic ordered multiset; Fenwick trees are explicit and predictable.
- **Segment tree:** It provides the same asymptotic operations with more code and memory constants.
- **Equal values:** Prefix query includes them, so they are not mistakenly counted as strictly greater.
- **Greater-count tie:** Array length decides; equal lengths choose `arr1` through `<=`.
- **All values equal:** Every greater count is zero, so assignments balance lengths with the first-array final tie.
- **One destination has more greater elements:** Count comparison takes priority over length.
- **Coordinate compression:** It handles values up to $10^9$ without allocating a billion-sized frequency array.
- **Tree/list synchronization:** Each append must be followed by exactly one matching update.
- **Input slice:** `nums[2:]` creates a real linear temporary but does not change the $O(N)$ bound.
- **Why subtract from array length:** A Fenwick prefix gives the complement of the desired strict-greater set. Every stored element is either at most $x$ or greater than $x$, so length minus prefix count is exact.
- **Duplicate frequency:** Updating by one for every occurrence means trees store multiplicities, not merely presence. This is required because `greaterCount` counts elements.
- **Final list order:** Fenwick ranks determine destinations only; values are appended to `arr1` and `arr2` in arrival order, which the final concatenation preserves.
- **Binary search always succeeds:** Every processed value came from `nums` and therefore appears in compressed set `st`, so `bisect_left` returns its exact rank.
