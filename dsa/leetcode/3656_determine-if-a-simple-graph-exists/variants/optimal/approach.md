## General

**Recognize a graphical degree-sequence problem**

The array does not describe edges; it prescribes how many neighbors each vertex must have. We must decide whether some undirected simple graph realizes exactly those degrees.

“Undirected” means every edge contributes one degree to each of its two endpoints. “Simple” means a vertex cannot connect to itself and any two distinct vertices can share at most one edge.

A degree list that can be realized is called graphical. The source tests graphicality with the Erdős–Gallai characterization, which gives necessary and sufficient numerical conditions after sorting the degrees.

**Sort vertices from highest demand to lowest**

The source performs

`degrees.sort(reverse=True)`.

Write the sorted sequence as

`d1 >= d2 >= ... >= dn`.

Vertex identities do not matter for existence. Relabeling vertices cannot change whether a graph exists, so sorting is safe.

Sorting lets us ask a decisive question for every prefix: can the `count` vertices with the largest degree demands receive enough incident edges from one another and from the remaining vertices?

The source mutates the supplied `degrees` list during sorting. The answer is unaffected, but callers should not expect the original ordering to remain.

**Check the handshake parity condition**

In any undirected graph, every edge contributes exactly two to the total degree sum. Therefore

`d1 + d2 + ... + dn = 2 * number_of_edges`

must be even.

The source computes `total = sum(degrees)` and immediately returns false when `total % 2` is one. This parity check is necessary, but it is not sufficient. For example, some even-sum sequences still demand more connections among high-degree vertices than simple edges can provide.

**State the Erdős–Gallai inequality**

For every prefix size `p` from one through `n`, a graphical non-increasing sequence must satisfy

`sum of d1 through dp <= p(p - 1) + sum from i=p+1 to n of min(di, p)`.

The left side is the total degree demand of the first `p` vertices.

On the right:

- The first `p` vertices can connect among themselves. Each can have at most `p - 1` such neighbors, so internal edges can contribute at most `p(p - 1)` to their combined degrees.
- A remaining vertex of degree `di` can connect to at most `p` prefix vertices, but it also cannot supply more than its own degree. Its maximum contribution toward the prefix demand is therefore `min(di, p)`.

If the left side exceeds this total possible supply for any `p`, no simple graph can realize the degrees.

The Erdős–Gallai theorem also gives the converse: if the total is even and every one of these inequalities holds, a simple undirected graph realizing the sequence exists. The conditions are therefore a complete decision test, not merely a collection of necessary warnings.

**Why the inequalities are sufficient**

Intuitively, sorting exposes the most demanding vertices first. If every high-demand prefix can be supported by all possible internal connections plus the capped contributions of the remaining vertices, there is no hidden shortage.

The formal theorem can be related to the Havel–Hakimi construction: connect a highest-degree vertex to vertices with the next-largest available degrees, reduce those degrees, and repeat. Degree exchanges can transform any realization into this greedy form without destroying simplicity. The Erdős–Gallai inequalities are exactly the global conditions that prevent this reduction process from encountering a negative or impossible demand.

The implementation relies on that established equivalence; it does not have to construct the edges.

**Use prefix sums for the left side and tail sums**

The source builds `prefix` with `prefix[0] = 0` and

`prefix[i] = d1 + ... + di`.

For a prefix of size `p`, the left side is `prefix[p]`. The sum of a tail interval beginning at zero-based index `split` is

`prefix[n] - prefix[split]`.

Without prefix sums, adding degrees separately for every `p` would make the test quadratic.

**Split the tail where degrees fall below `p`**

The tail contribution

`sum min(di, p)`

has two simple parts:

- Tail degrees at least `p` contribute exactly `p` each.
- Tail degrees below `p` contribute their actual degree.

Because `degrees` is descending, these two groups meet at one split point.

Python’s ordinary bisect functions expect ascending data. The source creates

`negated = [-degree for degree in degrees]`.

Negating a descending sequence makes it non-decreasing. A degree `di >= p` corresponds to `-di <= -p`.

The call

`bisect_right(negated, -p, lo=p)`

searches only the zero-based tail beginning at index `p` and returns the first index after all entries no greater than `-p`. Call that index `split`. Then:

- Indices `p` through `split - 1` have degrees at least `p`.
- Indices `split` through `n - 1` have degrees below `p`.

Using `bisect_right` places degrees equal to `p` in the first group. That is correct because `min(p, p) = p`. Placing them in the second group would produce the same numeric contribution, but the chosen boundary is consistent.

**Reconstruct the right side in the source**

For prefix size `p`, the source computes:

`p * (p - 1)`

for the maximum internal contribution.

There are `split - p` high tail degrees, each capped at `p`, contributing

`(split - p) * p`.

The remaining low tail degrees contribute their actual sum

`prefix[n] - prefix[split]`.

Adding the three pieces gives `available`. If

`prefix[p] > available`,

the prefix demands more degree than any simple graph could supply, so the method returns false.

If every prefix passes and the total sum is even, the Erdős–Gallai theorem guarantees existence and the source returns true.

**Trace the feasible example**

For `[3, 1, 2, 2]`, sorting gives `[3, 2, 2, 1]` with even total eight.

For `p = 1`, the leading degree three can receive at most zero internal contribution plus one connection from each of the three tail vertices, totaling three, so it passes.

For `p = 2`, the leading sum is five. The two prefix vertices can contribute two degree units internally, and the tail degrees two and one contribute `min(2, 2) + min(1, 2) = 3`, totaling five. Later prefixes also pass, so a realization exists.

For `[1, 3, 3, 1]`, sorting gives `[3, 3, 1, 1]`. At `p = 2`, the leading demand is six. Internal connections supply at most two degree units, and the two tail vertices can supply only one each, for four total. The failed inequality proves impossibility.

## Complexity detail

Sorting `n` degrees costs `O(n log n)` time. Computing the total, prefix sums, and negated sequence costs `O(n)`.

The loop evaluates `n` prefix sizes. Each `bisect_right` call costs `O(log n)`, and all other arithmetic in one iteration is constant time. This phase is `O(n log n)`, so total time remains `O(n log n)`.

The `prefix` and `negated` arrays each store `O(n)` integers, giving `O(n)` explicit auxiliary space. Python’s in-place sort may use additional temporary memory internally, but the overall bound remains `O(n)`.

An optimized Erdős–Gallai implementation can reuse a moving split pointer and perform the post-sort checks in `O(n)`, but sorting still dominates at `O(n log n)`. The exact source uses binary search independently for clarity.

## Alternatives and edge cases

- **Havel–Hakimi with a max-heap:** Repeatedly connect the largest remaining degree to other largest degrees. It can constructively test graphicality but is generally more involved and may cost more heap operations.
- **Naive Erdős–Gallai sums:** Recompute both sides by scanning the tail for every prefix. This costs `O(n^2)` and is unnecessary with prefix sums and a split search.
- **Only check even total:** Parity is necessary but does not prevent high-degree prefixes from exceeding available simple connections.
- **Only check each degree below `n`:** The constraints already ensure individual bounds, but valid individual values can still form an impossible sequence.
- **Use ordinary bisect on descending degrees:** Python bisect assumes ascending order. Negation converts the search domain correctly.
- **Search the whole array instead of the tail:** The capped-tail sum begins after the first `p` vertices. Including prefix entries would double-count their capacity.
- **Degree equal to `p`:** It contributes `p` to `min(degree, p)`. `bisect_right` includes it in the capped group.
- **All zero degrees:** The sum is even and every inequality passes; the graph with no edges is a valid simple graph.
- **Single vertex:** Constraint bounds force degree zero. The source returns true for that one isolated vertex.
- **Odd degree sum:** Return false immediately because no undirected edge can contribute an odd total.
- **Maximum degree `n - 1`:** Such a vertex must connect to every other vertex. The prefix inequalities verify that the remaining degree demands can support those required connections.
- **Repeated degrees:** Sorting and bisect handle duplicates directly; vertices with equal desired degree remain distinct.
- **No self-loops:** The internal cap is `p(p - 1)` rather than `p^2` because each prefix vertex has only `p - 1` other prefix vertices available.
- **No parallel edges:** Each tail vertex contributes at most one edge to each of the `p` prefix vertices, which is why its contribution is capped at `p`.
- **Input mutation:** The source sorts `degrees` in place. Copy the list first if the caller must preserve its original order.
