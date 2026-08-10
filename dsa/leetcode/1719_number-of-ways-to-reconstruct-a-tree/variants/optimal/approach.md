## General

**Interpret pairs as a comparability graph**

Create an undirected graph whose vertices are the values appearing in `pairs`. Two vertices share an edge exactly when one must be an ancestor of the other in the unknown rooted tree.

The source stores this graph in two forms:

- `g` is a $510\times510$ Boolean adjacency matrix for constant-time edge tests.
- `v[x]` is the list of neighbors of `x` for iteration and degree calculation.

For each pair `x,y`, both `g[x][y]` and `g[y][x]` become true, and each endpoint enters the other's list.

**Add self-comparability for subset checks**

The algorithm collects every label with a nonempty neighbor list into `nodes` and sets `g[i][i] = True` for it.

The input contains at least one pair, so every participating node has a neighbor and is discovered this way. The diagonal true value does not claim that a node is its own ancestor under the problem definition. It is an implementation convenience for comparing closed neighborhoods: a candidate parent should be considered compatible with its own label and with the child label connected to it.

**Why degrees reveal possible parent direction**

If `y` is the parent of `x` in a valid tree, every vertex comparable with `x` must also be comparable with `y`:

- Every descendant of `x` is also a descendant of `y`.
- Every ancestor of `x` lies on the same root-to-`x` chain as `y` and is therefore an ancestor of `y` or equals `y`.

Thus `x`'s closed neighborhood must be contained in `y`'s closed neighborhood, and `y` cannot have smaller graph degree.

The source sorts `nodes` by `len(v[x])` in ascending order, processing low-degree nodes before possible parents.

**Choose the smallest-degree possible parent**

For node `x` at sorted position `i`, the source scans later nodes until it finds the first adjacent one:

`while j < len(nodes) and not g[x][nodes[j]]: j += 1`.

Later nodes have degree at least `x`'s degree. Because of sorting, the first adjacent later node `y` is a minimum-degree candidate among the nodes that could sit above `x`.

Choosing the closest feasible degree is important. In any valid reconstruction, `x` should attach to the nearest ancestor whose comparability set contains `x`'s; skipping such a candidate for a broader ancestor would fail to represent the immediate-parent relation consistently.

**Validate closed-neighborhood containment**

For every ordinary neighbor `z` of `x`, the source checks `g[y][z]`. The earlier diagonal assignments make two boundary cases work naturally:

- When `z == y`, `g[y][y]` is true.
- The relationship between `y` and `x` is already true because `y` was selected as a neighbor.

If any `z` comparable with `x` is not comparable with `y`, `y` cannot be an ancestor of `x` in any valid rooted tree. Because it is the minimum-degree available parent candidate, the required nested-neighborhood structure fails and the source returns zero.

When all checks pass, `x` can be placed below `y` consistently with the supplied ancestor pairs.

**Recognize the root**

If no later adjacent node exists, `x` has no possible parent and is counted as a root candidate. A rooted tree must have exactly one root.

The final sorted node always has no later node, so at least one root candidate exists. If `root > 1`, two nodes could not be attached above one another under the degree-compatible edge structure, and no single rooted tree can realize all pairs. The source returns zero.

In a valid comparability graph, the actual root is adjacent to every other vertex because it is their ancestor. It naturally survives as the unique no-parent node.

**Detect multiple reconstructions**

If chosen child `x` and candidate parent `y` have equal ordinary degrees, the source sets `equal = True`.

Containment plus equal cardinality means their closed comparability neighborhoods coincide. Their ancestor order can be exchanged without changing which unordered pairs are ancestor-related, yielding more than one valid parent assignment. The task needs only distinguish one way from more than one, so a single Boolean is sufficient.

If all parent-child degree increases are strict and validation succeeds, the nested neighborhoods force the parent relationships and the reconstruction is unique.

**Why the final classification is correct**

The degree order supplies a parent candidate for every non-root node. The containment test verifies the necessary nested structure of ancestor comparability sets. A unique root connects the hierarchy into one rooted tree rather than several incompatible top-level components.

Failure of containment or multiple roots makes reconstruction impossible, giving zero. When the structure is valid, equal-degree nested nodes permit an alternative ordering, giving two as the required “more than one” category. Otherwise every attachment is forced, giving one.

For a complete three-node comparability graph, all degrees are equal. A parent candidate exists with equal degree, so `equal` becomes true and the method returns two, matching the several possible chains/root choices.

## Complexity detail

Let $V$ be the number of distinct participating labels and $E$ the number of pairs. Building neighbor lists costs $O(E)$. Sorting costs $O(V\log V)$.

Across nodes, the forward scan for a later adjacent candidate can inspect $O(V)$ positions each, for $O(V^2)$ time. Containment checks iterate neighbor lists and total $O(E)$ after one candidate per node. Since $E=O(V^2)$, overall time is $O(V^2)$, matching the manifest.

The adjacency matrix is allocated at the fixed label-capacity size $510^2$. In a parameterized view it is $O(V_{\max}^2)$, while neighbor lists use $O(E)$ and node ordering uses $O(V)$. Under the problem's label bound this matches the manifest's $O(V^2)$ space description.

## Alternatives and edge cases

- **Set-based neighborhoods:** Store a set per node and test subset relations directly. It is clearer but may have larger hashing overhead than the fixed Boolean matrix.
- **Try every rooted tree:** The number of labeled trees is enormous and ignores the strong neighborhood structure encoded by pairs.
- **Missing root adjacency:** If no single node can sit above all others, multiple no-parent candidates emerge and the source returns zero.
- **Complete comparability graph:** Equal degrees create multiple valid chain orderings, so the answer is two.
- **Unique chain with forced degrees:** Strictly nested neighborhoods can force a single reconstruction.
- **Equal-degree parent and child:** It signals interchangeable ordering after containment succeeds, not immediate invalidity.
- **Containment failure:** One neighbor of the child missing from the parent's neighborhood proves impossibility.
- **Sparse disconnected-looking input:** More than one root candidate makes a single rooted reconstruction impossible.
- **Nonconsecutive labels:** The fixed matrix indexes labels directly; values need not be compressed.
- **Diagonal entries:** They support closed-neighborhood tests and are not input ancestor pairs.
- **No isolated participating nodes:** A node exists only by appearing in a pair, so every collected vertex has at least one neighbor.
- **Answer capping:** The method records only whether multiplicity exists because the required return is two for any number greater than one.
- **Tie ordering in sort:** Any equal-degree order can reveal the same ambiguity once containment is validated.
