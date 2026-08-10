## General

For every query, the source first replaces its two indices with

`[min(a, b), max(a, b)]`.

Call them $l\le r$. This mutates the input `queries` list, but makes the positional reasoning uniform.

**Queries that meet immediately**

If $l=r$, Alice and Bob already occupy the same building, so answer $r$.

If `heights[l] < heights[r]`, the person at $l$ can move directly to $r$, while the other is already there. Since no common building can lie left of $r$ for the person starting at $r$, this is the leftmost answer.

The remaining case has `heights[l] >= heights[r]`. The person at $l$ cannot move to $r$. Any common destination must be at index $j>r$ and taller than both starts. Because the left height is at least the right height, the threshold reduces to

$$
\texttt{heights}[j]>\texttt{heights}[l].
$$

We need the smallest index strictly after $r$ meeting this height threshold.

**Process queries by decreasing right endpoint**

The source sorts query indices by descending `queries[i][1]`. Pointer `j` starts at the last building.

Before answering a query with right endpoint $r$, the loop inserts every building with index `j > r` into a Fenwick tree. It never inserts $r$ itself. Because later processed queries have no larger right endpoint, inserted buildings remain eligible and the pointer only moves left.

The tree therefore represents exactly the candidate suffix strictly to the right of the current query boundary.

**Reverse height ranks**

A Fenwick prefix query naturally aggregates small coordinates, while we need heights strictly greater than a threshold. The source sorts the unique heights into `s` and reverses their rank.

For a building of height $h$ at sorted position $p=\texttt{bisect_left}(s,h)$, update coordinate is

`n - p + 1`.

Larger heights have larger $p$ and therefore smaller Fenwick coordinates. Each tree node stores the minimum building index inserted for its covered coordinates.

For threshold `heights[l]` at sorted position $p$, query coordinate is `n - p`. An equal height would update at `n-p+1`, just outside this prefix, while every strictly greater height updates at a coordinate at most `n-p`. Hence `tree.query(k)` includes exactly the taller candidates.

Using $n$ rather than the number of unique heights leaves harmless gaps in coordinates. The globally smallest height may map to $n+1$ and not be inserted, but it can never be strictly taller than any query threshold drawn from the same array, so it is never a useful candidate.

**Fenwick tree returns the leftmost candidate**

`update(x, index)` propagates the minimum index through Fenwick ancestors. `query(x)` takes the minimum across the prefix. Since all represented buildings lie right of $r$ and satisfy the queried height condition, their minimum index is precisely the leftmost meeting building.

If no qualifying coordinate has been updated, the query remains infinity and the wrapper returns `-1`.


Immediate cases return $r$, which is reachable by both and is the earliest possible index not left of the rightmost start.

For a deferred query, any meeting building must be strictly right of $r$ and taller than `heights[l]`. The offline insertion and reverse-rank prefix encode exactly this set. Taking its minimum returns the leftmost valid building, and an empty set proves no meeting is possible.

## Complexity detail

Let $N$ be building count and $Q$ query count. Sorting unique heights costs $O(N\log N)$. Sorting query indices costs $O(Q\log Q)$. Each building is inserted once and each deferred query performs one Fenwick query, costing $O((N+Q)\log N)$.

Thus the exact source runs in

$$
O(N\log N+Q\log Q+Q\log N),
$$

commonly summarized as $O((N+Q)\log(N+Q))$. This does not match the manifest's heap summary or its $O(N+Q\log Q)$ bound.

The sorted heights, Fenwick array, sorted query-index list, and answer require $O(N+Q)$ space. The input query rows are mutated during normalization.

## Alternatives and edge cases

- **Min-heap sweep:** Group deferred queries at their right endpoint and sweep left to right by required height. This matches the manifest summary but is not the checked-in source.
- **Monotonic stack plus binary search:** Another editorial method answers height-threshold queries over a right-side skyline.
- **Brute force per query:** Scanning from $r$ rightward costs $O(NQ)$ in the worst case.
- **Same starting building:** Return that index without consulting heights or the tree.
- **Direct move to $r$:** Requires strict `heights[l] < heights[r]`; equal height does not permit movement.
- **Strictly taller destination:** The rank query deliberately excludes equal heights.
- **No building to the right:** The Fenwick prefix contains no eligible index and returns `-1`.
- **Duplicate heights:** Coordinate compression groups them, and strict query boundaries exclude the entire equal-height group.
- **Query mutation:** Replacing endpoints with sorted order changes the caller's nested lists, an observable side effect unrelated to the correct returned answers.
- **Manifest mismatch:** The implementation is an offline Fenwick minimum sweep, not a min-heap sweep, and its sorting plus tree operations introduce logarithmic $N$ factors.
