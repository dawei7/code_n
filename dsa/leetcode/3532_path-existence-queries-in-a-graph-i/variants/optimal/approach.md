## General

**The graph is dense in definition but simple in structure**

The graph conceptually has an edge between every pair `i,j` whose sorted values differ by at most `maxDiff`. Explicitly checking all `O(n^2)` pairs would be wasteful.

Because `nums` is non-decreasing, connectivity is determined entirely by gaps between consecutive indices:

`gap[i] = nums[i] - nums[i-1]` for `i >= 1`.

A gap larger than `maxDiff` is an uncrossable boundary. A gap at most `maxDiff` gives a direct edge between those two consecutive nodes.

**Why a large adjacent gap separates components**

Suppose:

`nums[i] - nums[i-1] > maxDiff`.

Take any node `a <= i-1` on the left and any node `b >= i` on the right. Sorted order gives:

`nums[b] - nums[a] >= nums[i] - nums[i-1] > maxDiff`.

Therefore, no edge connects any left-side node to any right-side node. A path cannot cross the boundary because every crossing edge would have to join one node from each side.

This proves that every oversized adjacent gap splits connected components.

**Why no oversized gap means the interval is connected**

Now consider consecutive indices `L,L+1,...,R` where every adjacent gap is at most `maxDiff`. For each `j` from `L+1` through `R`:

`nums[j] - nums[j-1] <= maxDiff`.

Thus the graph contains direct edge `(j-1,j)`. These edges form a chain connecting every node in the interval. Even if endpoints `L` and `R` differ by more than `maxDiff` and have no direct edge, they have a path through the intermediate indices.

Consequently, connected components are exactly the contiguous index intervals separated by oversized adjacent gaps.

**Assign one component label per interval**

The source allocates `g = [0] * n` and starts `cnt = 0`. Node zero belongs to component zero.

For each index `i` from one onward:

- if the adjacent gap exceeds `maxDiff`, increment `cnt` to begin a new component;
- assign `g[i] = cnt`.

When a gap is small enough, `cnt` stays unchanged and the two consecutive nodes share a label. Through the chain argument, every run of equal labels is connected.

Labels need only be equal within a component and different across boundaries; their numeric values have no other meaning.

**Answer each query in constant time**

For query `[u,v]`, a path exists exactly when the two nodes lie in the same connected component. The source returns:

`g[u] == g[v]`.

After linear preprocessing, this is one array lookup and comparison per query.

**Direct edge versus path**

It is important not to test only:

`abs(nums[u] - nums[v]) <= maxDiff`.

That tests whether `u` and `v` share a direct edge, not whether a path exists. For `nums = [5,6,8]` and `maxDiff = 2`, values five and eight differ by three, but edges `5-6` and `6-8` form a path.

The component label captures this transitive connectivity.

**Duplicates and zero threshold**

When `maxDiff = 0`, consecutive equal values have gap zero and are connected; any positive gap starts a new component. Thus equal-value runs receive common labels.

Duplicate values can also create many direct edges inside a run, but only the consecutive chain is needed to prove connectivity. The algorithm never has to enumerate those redundant edges.

**Why the labels are exact**

If two nodes share a label, no oversized adjacent gap lies between their indices. Every adjacent pair along the index interval has a direct edge, forming a path.

If labels differ, at least one oversized gap lies between them. The separation proof shows no graph edge can cross that boundary, so no path can connect the nodes.

These two directions prove label equality is equivalent to path existence, which makes every returned boolean correct.

## Complexity detail

The preprocessing loop examines each of the `n-1` adjacent gaps once, taking `O(n)` time. Each of `Q` queries performs constant-time label comparisons, taking `O(Q)`. Total time is `O(n+Q)`.

The component-label array uses `O(n)` auxiliary space. The returned boolean list uses `O(Q)` required output space. Excluding output, the manifest's `O(n)` space bound is exact.

The algorithm does not allocate edges. This is significant because the implicit graph may contain `O(n^2)` edges when many values are close, yet the sorted-gap representation remains linear.

## Alternatives and edge cases

- **Build every graph edge and run DFS:** The implicit graph can be quadratic. Adjacent gaps already characterize its components.
- **Union-find consecutive nodes:** Unioning `i-1` and `i` when the gap is small is correct and nearly linear, but component labels can be assigned even more simply in one pass.
- **Binary-search component endpoints:** Recording interval right boundaries gives `O(log n)` per query. Direct labels use `O(1)` per query at the cost of an `O(n)` array.
- **Test endpoint difference only:** It misses indirect paths through intermediate values.
- **Unsorted nums:** The gap theorem relies on non-decreasing order. A general unsorted list would need sorting with original-index mapping or another method.
- **One node:** It receives label zero, and every valid query is a trivial true self-path.
- **Self query:** `g[u] == g[u]` is always true, representing the length-zero path.
- **Gap exactly maxDiff:** The adjacent edge exists because the condition is “at most,” so no new component begins.
- **Gap one larger than maxDiff:** It is a separating boundary and increments the label.
- **All gaps small:** Every node receives label zero and all queries return true.
- **All gaps oversized:** Every node gets a distinct label; only self queries are true.
- **Repeated values:** Zero gaps keep them together, including when `maxDiff = 0`.
- **Far endpoints in one component:** They may lack a direct edge but remain connected by the consecutive chain.
- **n parameter:** The source trusts the guarantee `n == len(nums)` and sizes `g` accordingly.
- **Dense implicit edge set:** The algorithm deliberately never counts or stores edges; connectivity needs only component boundaries.
