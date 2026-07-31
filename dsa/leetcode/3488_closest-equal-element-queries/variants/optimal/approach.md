## General

**Group equal values in circular order**

Scan `nums` from left to right and map each value to the increasing list of indices where it occurs. For any occurrence, the nearest equal index must be either the preceding or following occurrence in this cyclically ordered list. Any other equal occurrence lies beyond one of those two neighbors in the corresponding direction and cannot be closer.

For an occurrence at index `i`, let `previous` and `next` be those two cyclic neighbors. The counterclockwise and clockwise gaps are respectively `(i - previous) % n` and `(next - i) % n`. Their minimum is the required distance. A value with only one occurrence has no valid other index, so its precomputed answer remains `-1`.

Store the result for every array index in `closest`. Each query then needs only `closest[query]`; repeated query indices reuse the same work.

**Why adjacent cyclic occurrences are sufficient**

Walking clockwise from `i`, the first equal value encountered is `next`; every later equal index requires at least as many steps. The symmetric statement holds counterclockwise for `previous`. Since every circular route begins in one of these two directions, the smaller adjacent gap is the global minimum.

## Complexity detail

Let $n$ be the length of `nums` and $q$ the number of queries. Building the value groups and visiting every stored occurrence once takes $O(n)$ expected time. Producing the output takes $O(q)$ time, for $O(n+q)$ total expected time. Reading both inputs and writing $q$ answers gives a matching $\Omega(n+q)$ lower bound.

The grouped index lists and the per-index answer array contain $O(n)$ entries in total. Apart from the returned output, auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Binary search per query:** grouped sorted positions support predecessor and successor searches in $O(\log n)$ per query, for $O(n+q\log n)$ total time; batch preprocessing removes that repeated work.
- **Scan the entire array per query:** is simple but can take $O(nq)$ time.
- **Duplicate query indices:** require no special handling because each answer was already computed by index.
- **One occurrence:** must return `-1`; the queried index itself cannot be reused.
- **Two occurrences:** both cyclic neighbors refer to the same other index, but the two directional gaps may differ and their minimum is still correct.
- **Boundary adjacency:** indices 0 and $n-1$ are one step apart.
- **Several equal occurrences:** only predecessor and successor in cyclic index order can attain the minimum distance.
