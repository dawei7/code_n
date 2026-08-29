## General

**Model each conversion as a directed weighted edge**

A conversion `[source, target, factor]` says:

one `source` unit equals `factor` `target` units.

Represent this as a directed edge:

`source -> target` with weight `factor`.

The direction matters. The contract guarantees that every unit is reachable from unit zero through a unique combination of conversions without reversing any edge. With `n` units and exactly `n-1` conversions, this reachable directed structure behaves as an arborescence rooted at zero: every non-root unit has one unique directed path from zero.

The protected source stores only the given direction:

`g[source].append((target, factor))`.

It does not add a reverse edge because reverse conversions are neither needed nor authorized by the stated path guarantee.

**A path product is the conversion answer**

Suppose the unique path from unit zero to unit `v` is:

`0 -> a -> b -> ... -> v`

with edge factors `w_1, w_2, ..., w_t`.

One unit of type zero becomes `w_1` units of type `a`. Each of those becomes `w_2` units of type `b`, so the amount is multiplied again. Continuing along the path gives:

`w_1 * w_2 * ... * w_t`

units of type `v`.

Therefore, if the conversion value at a parent `s` is `mul` and edge `s -> t` has factor `w`, then:

`answer[t] = mul * w`.

This local propagation is all the DFS needs.

**Why unit zero has value one**

One unit of type zero is already exactly one unit of type zero. The empty path has an empty product, whose multiplicative identity is one.

The source begins:

`dfs(0, 1)`.

Inside the call, it assigns `ans[0] = 1`. Every descendant call receives the parent path product extended by one edge.

**Reduce after every multiplication**

Answers may be enormous because a path can contain many factors up to `10^9`. The requested output is modulo:

`MOD = 10^9 + 7`.

The source passes:

`mul * w % mod`.

This is valid because modular multiplication preserves products:

`(A * B) mod MOD = ((A mod MOD) * (B mod MOD)) mod MOD`.

Once a path product has been reduced, no information needed for later modular answers is lost. Reducing on every edge also prevents values from growing with path length.

**The DFS invariant**

For a call `dfs(s, mul)`, the invariant is:

`mul` equals the product, modulo `MOD`, of all conversion factors on the unique directed path from unit zero to `s`.

It holds at the root because the empty path product is one. The function stores this value into `ans[s]`. For child edge `s -> t` with factor `w`, the unique root-to-`t` path is the root-to-`s` path followed by this edge. Passing `mul * w % mod` therefore establishes the invariant for `t`.

By induction down the conversion tree, every visited unit receives exactly its required value.

**Why no visited set appears**

In a general directed graph, DFS needs a visited set to avoid cycles and repeated work. The source has none. It relies completely on the guarantee that unit zero reaches every other unit through a unique directed combination, together with the `n-1` edge count.

Under that structure, no node is reached along two different directed paths and no reachable directed cycle can exist. Each node is called exactly once. If the input did not satisfy this guarantee, the source could overwrite answers, revisit nodes, or recurse forever.

**A branching example**

For conversions:

`0 -> 1` with factor two,

`0 -> 2` with factor three,

`1 -> 4` with factor five,

the DFS starts unit zero at one. It sends two to unit one and three to unit two. From unit one it sends:

`2 * 5 = 10`

to unit four. Branches are independent because every answer depends only on its unique path, not on sibling conversions.

**Material execution defect in the protected Python source**

The mathematical traversal is correct, but the exact implementation uses recursive Python calls without increasing the recursion limit or switching to an explicit stack. A valid input may be a chain of up to `100,000` units:

`0 -> 1 -> 2 -> ... -> 99999`.

That creates recursion depth `100,000`, far beyond Python's usual recursion limit of roughly one thousand. The protected source can raise `RecursionError` on such an input even though it satisfies every documented constraint.

Thus the algorithmic idea and computed recurrence are correct, but the supplied implementation is not robust across the full legal depth range. An iterative DFS or BFS should be used to remove this execution hazard. This document records the defect rather than silently treating recursive stack depth as unlimited.

**Why the returned array is complete**

The answer array begins with zeros merely as storage. The reachability guarantee says every unit lies on a directed path from zero, so DFS should assign all `n` positions when execution completes. The zeros are not intended to mean unreachable units.

Since every node is visited once, every stored path product is exact modulo `MOD`, and the array index is the unit identifier, returning `ans` has the requested ordering.

## Complexity detail

Let `n` be the number of units. Building `g` creates one adjacency-list entry for each of `n-1` conversions, taking `O(n)` time and `O(n)` space.

Under the promised unique-path structure, DFS enters every node once and examines every edge once. Its arithmetic work is `O(n)`, so total algorithmic time is `O(n)`.

The adjacency lists and answer array use `O(n)` heap space. The recursive call stack uses `O(h)` additional space, where `h` is the conversion-tree height. In the worst legal case `h = n`, so total auxiliary space remains `O(n)` asymptotically, but the practical Python recursion failure described above occurs well before that theoretical memory bound.

Modulo reduction keeps stored numeric magnitudes bounded by `MOD`. Python safely multiplies the intermediate values; a fixed-width language should use a sufficiently wide type for `mul * w` before applying modulo.

## Alternatives and edge cases

- **Iterative DFS with a stack:** Store `(unit, path_product)` pairs and process the same recurrence without recursion depth limits. This is the direct robust repair while preserving `O(n)` time and space.
- **Breadth-first traversal:** A queue works equally well because each node has one unique root path; traversal order does not affect its path product.
- **Topological dynamic programming:** It can propagate values in a more general DAG, but the rooted unique-path guarantee makes a tree traversal simpler.
- **Add reverse conversion edges:** Reversing would require modular division or rational values and violates the source direction contract. Only forward edges belong in `g`.
- **Recompute a path per unit:** Following ancestors independently could repeat shared prefixes and become quadratic. One traversal shares the propagation work.
- **Root unit:** Its answer is one, even when it has many outgoing conversions.
- **Conversion factor one:** The child inherits the parent's modular amount unchanged.
- **Factor divisible by MOD:** That child and every descendant path product become zero modulo `MOD`.
- **Deep chain:** Algorithmically linear, but the exact recursive source can fail with `RecursionError`; an explicit stack is required for full constraint safety.
- **Wide star rooted at zero:** Recursion depth is only two, and each child receives its direct factor.
- **Input order:** Adjacency order changes DFS visit order but not any unique path product.
- **No visited set:** Safe only because the graph guarantee prevents multiple directed paths and reachable cycles.
- **Unreachable unit in invalid input:** Its answer would remain the initialization zero, but the contract excludes this situation.
- **Large raw product:** Reducing at every edge is mathematically exact for the requested residues.
