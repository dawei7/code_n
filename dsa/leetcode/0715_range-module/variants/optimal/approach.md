## General
**Represent uniform coordinate regions lazily**

Use a dynamic segment tree over the integer unit intervals in the published coordinate domain. A node state is untracked, tracked, or mixed. Uniform nodes need no children, so the enormous untouched domain consumes only one node.

**Assign a complete half-open range**

Convert `[left, right)` to inclusive unit indices `[left, right - 1]`. Adding assigns tracked state and removing assigns untracked state. A fully covered tree node adopts the state and discards any children because their older distinctions are overwritten.

**Descend only at assignment boundaries**

For partial overlap, create children inheriting the parent's uniform state, recurse into the intersected sides, and then collapse them back into their parent when both become uniformly equal. Only paths near range boundaries remain expanded.

**Query complete coverage**

If a queried region reaches a uniform node, that state answers the whole overlap immediately. A mixed node delegates to the necessary children, and a query spanning both halves is tracked only when both recursive results are true.

**Why assignments and queries match interval semantics**

Every leaf unit interval records exactly the latest covering add or remove operation. Range assignment changes precisely the leaves in its half-open input and preserves all others. The query returns true exactly when every covered leaf is tracked; because all operation endpoints are integers, those unit intervals partition the requested real interval without gaps.

## Complexity detail
The coordinate bound `C` has logarithmic tree height. A range assignment or query follows at most a constant number of boundary paths and takes $O(\log C)$ time. Across `q` operations, at most $O(q \log C)$ dynamic nodes are created, giving the stated total time and space bounds.

## Alternatives and edge cases
- **Sorted disjoint intervals:** merge additions, split removals, and binary-search queries; it can be compact, though array-backed insertion and deletion may shift $O(n)$ intervals.
- **Fixed full segment tree:** range assignment and query are logarithmic but allocating proportional to `C` is infeasible for the large coordinate domain.
- **Rescan every stored interval:** it is straightforward and correct but can take $O(q^2)$ total time.
- Intervals are half-open, so touching at one endpoint creates no overlap but adjacent tracked intervals jointly cover their union.
- Removing an untracked region has no effect on other coordinates.
- Re-adding a removed subrange restores its coverage.
- A query is false if even one interior unit interval is untracked.
