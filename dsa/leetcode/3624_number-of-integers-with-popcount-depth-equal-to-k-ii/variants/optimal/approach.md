## General

The array changes over time, and range queries ask for a count by popcount-depth. Recomputing every value in `[left,right]` would be too slow.

The source maintains one Fenwick tree for each possible depth from 0 through 5. Tree `d` contains a 1 at index `i` exactly when the current value at that index has depth `d`. A range query then becomes one frequency query in the corresponding tree.

**Computing one value's depth**

The helper starts `steps=0` and repeatedly replaces `value` with `value.bit_count()` until it reaches 1. Each replacement increments `steps`.

For `value=1`, the loop does not run and depth is zero. For 7:

`7 -> 3 -> 2 -> 1`,

so the helper returns 3.

Values are at most `10^15`. One popcount reduces them to at most about 50, and a few more steps reach 1. Depth calculation is effectively constant under these constraints.

**Six independent frequency arrays**

`trees = [[0]*(size+1) for _ in range(6)]` creates Fenwick storage for depths 0 through 5.

During initialization, array index `index` is enumerated from 1 because Fenwick trees use one-based indexing. After computing `current_depth`, the source places a raw 1 at:

`trees[current_depth][index]`.

It also appends the depth to `depths` using normal zero-based array indexing. `depths[i]` records the current classification of position `i` and is essential for later updates.

**Building all Fenwick trees in linear time**

Instead of calling the logarithmic `add` function for every initial element, the source converts each raw frequency array into Fenwick form.

For each one-based `index`, its immediate Fenwick parent is:

`index + (index & -index)`.

Adding the current node's accumulated value to that parent builds the parent's covered interval. Running this once from left to right constructs one tree in `O(n)` time. Repeating for six trees is still `O(n)` because six is constant.

**What a Fenwick entry represents**

At position `i`, `i & -i` is the size of the suffix block represented by that node. The entry stores the count for indices:

`i-(i&-i)+1 ... i`

in one-based coordinates.

This overlapping block structure supports both point updates and prefix sums in logarithmic time.

**Prefix sums**

`prefix_sum(tree,end)` returns the count in the half-open zero-based range `[0,end)`.

Although `end` is passed as a count of elements, it is also the correct one-based Fenwick endpoint. The helper adds `tree[end]` and removes the least significant set bit repeatedly:

`end -= end & -end`.

Those disjoint Fenwick blocks partition the requested prefix.

**Inclusive range query**

For query `[1,left,right,wanted_depth]`, the desired zero-based interval is inclusive. The source computes:

`prefix_sum(tree,right+1) - prefix_sum(tree,left)`.

The first term counts indices 0 through `right`. The second removes indices before `left`. Their difference is exactly `left...right`.

Only the tree for `wanted_depth` is consulted.

**Point updates**

For `[2,index,value]`, the helper computes `new_depth` and reads `old_depth=depths[index]`.

If the classifications differ:

- add `-1` at `index` in the old-depth tree;
- add `+1` at `index` in the new-depth tree;
- replace `depths[index]`.

`add` converts the zero-based index to one-based with `index += 1`, then updates every Fenwick ancestor using:

`index += index & -index`.

If old and new depths match, no tree update is necessary even when the numeric value changed. Queries depend only on depth.

**Why `nums` itself is not updated**

The exact source never assigns `nums[index]=value`. This is safe for its future logic because it never again reads an old numeric value at an index. Later queries use only Fenwick counts, and later updates need only the current old depth, stored in `depths`.

The data structure therefore preserves exactly the information required by the operations, not the full updated numbers.

**Core invariant**

After initialization and after every processed query, for every depth `d` and index `i`:

> the conceptual point frequency represented by `trees[d]` is 1 if `depths[i]==d` and 0 otherwise.

Initialization places exactly one marker for each index. A range query does not change state. An update moving between depths removes the old unique marker and inserts the new one. An update within the same depth leaves the marker correct.

Thus every Fenwick range result equals the number of current indices having the requested depth.

**Following the first example**

Values 2 and 4 both have depth 1, so tree 1 initially has markers at indices 0 and 1. Query `[0,1]` returns 2.

Updating index 1 to value 1 changes its depth from 1 to 0. The source subtracts one from tree 1 and adds one to tree 0. The next depth-0 range query returns one.

## Complexity detail

Let `n` be the array length and `q` the number of queries. Under the bounded value domain, computing a depth takes constant time with a very small iterated-popcount factor.

Initializing depths costs `O(n)`. Building six Fenwick trees costs `O(6n)=O(n)`.

A type-1 query performs two prefix sums, each `O(\log n)`. A depth-changing update performs two point updates, also `O(\log n)`. Total time is:

$$
O(n+q\log n).
$$

Six arrays of length `n+1` and the `depths` array use `O(n)` space. The answer list uses up to `O(q)` output space; excluding output, auxiliary space is `O(n)`.

## Alternatives and edge cases

- **Segment tree of depth-count vectors:** Store six counts per node. It supports the same operations but has larger constants and more code.
- **Ordered index sets per depth:** Updates move an index between sets, while range counts require a structure supporting rank queries.
- **Scan each query range:** It can degrade to `O(nq)`.
- **Update to the same depth:** No Fenwick change is needed, even if the numeric value differs.
- **Value 1:** Its depth is zero because the sequence already starts at 1.
- **Powers of two above 1:** Their depth is one.
- **Single-index range:** The prefix difference returns either zero or one.
- **Whole-array range:** Use `right+1=n` and `left=0`.
- **Repeated updates at one index:** `depths` always supplies the current classification, so markers do not drift.
- **Depth bound:** Positive values through `10^15` fit within the six allocated depth categories.
- **No mutation of `nums`:** The logical updated values are not preserved, but all future required depth behavior is preserved in `depths`.
- **One-based Fenwick indexing:** Raw arrays have an unused slot zero; conversion in `add` is essential.
- **Inclusive query endpoints:** `right+1` turns the right boundary into the needed half-open prefix.
- **Input query order:** Operations are processed sequentially, so each answer reflects all preceding updates.
