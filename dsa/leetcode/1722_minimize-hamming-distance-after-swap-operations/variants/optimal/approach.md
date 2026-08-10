## General

**Allowed swaps create independent index components**

Treat indices as vertices of an undirected graph and each allowed pair as an edge. If two indices lie in the same connected component, values can be moved between them through a sequence of allowed edge swaps.

In fact, swaps along the edges of a connected graph can realize any permutation of the values inside that component. A value can be routed along a path, and repeated transpositions generate arbitrary rearrangements. Values can never cross between different components because no allowed-swap path connects them.

Therefore exact positions inside one component are flexible; only the multiset of source values in that component matters.

**Build components with disjoint-set union**

`p = list(range(n))` initially makes every index its own representative.

The nested `find(x)` follows parent pointers to a root. During recursive return, `p[x] = find(p[x])` rewrites the path directly to that root. This path compression speeds up later searches.

For each allowed pair `a,b`, the source performs

`p[find(a)] = find(b)`.

This makes the root of `a`'s component a child of `b`'s root, merging the components. If both roots are already the same, the assignment is harmless.

All unions finish before component value counts are built, so component membership never changes during the matching phase.

**Count source values within each component**

`cnt = defaultdict(Counter)` maps a component representative to a frequency counter.

For each source position `i` with value `x`, the source obtains its compressed root `j = find(i)` and increments `cnt[j][x]`.

After this pass, `cnt[root][value]` is the number of copies of that value available anywhere in that component. The count deliberately forgets exact positions, because arbitrary within-component permutation makes those positions interchangeable.

**Consume values required by target**

For each target position `i` with desired value `x`, the algorithm finds the same index component and executes

`cnt[j][x] -= 1`.

If a copy was available, the old count was positive and the new count remains nonnegative. One source occurrence can be placed at this target position, so it need not contribute to Hamming distance.

If the new count is negative, all source copies of `x` in this component have already been assigned to earlier target requests. This occurrence cannot be matched by any rearrangement, and the Boolean expression `cnt[j][x] < 0` adds one to `ans`.

Python treats `True` as one and `False` as zero, so

`ans += cnt[j][x] < 0`

is a compact conditional increment.

**Why decrementing below zero counts every shortage**

Suppose a component contains two copies of value five but target requests it four times. The successive counts after decrement are one, zero, negative one, and negative two. Exactly the last two requests increment `ans`, matching the shortage of two.

`Counter` returns zero for a previously absent value, so the first request for a completely unavailable value becomes negative one and is counted immediately.

**Why matching values independently is sufficient**

Within one component, maximizing equal positions is a multiset intersection problem. For each value $v$, at most

$$
\min(\text{source frequency of }v,\text{target frequency of }v)
$$

positions can match. Those matches for different values do not conflict because they consume disjoint source occurrences and target positions.

The counter pass realizes exactly all such matches. Every remaining target occurrence must mismatch regardless of how values are permuted. Thus the sum of frequency shortages is the minimum possible Hamming distance.

**Trace the first example**

Allowed swaps form components `{0,1}` and `{2,3}`. The first component's source multiset is `{1,2}`, exactly matching target values two and one, so it contributes zero mismatches.

The second component has source values three and four, while target requests four and five. Four is consumed successfully; five drives its count negative and contributes one. The answer is one.

**Why actual swapping is unnecessary**

Constructing a particular final source arrangement would add work without changing the objective. Frequency feasibility proves which target positions can collectively be satisfied. The problem asks only for the minimum count, so the algorithm stops at that aggregate result.

## Complexity detail

Let $n$ be the array length and $m$ the number of allowed swaps. Hash-map and counter operations take expected constant time. There are $m$ unions and $O(n)$ additional `find` calls.

The manifest states $O((n+m)\alpha(n))$, the classic bound for path compression combined with union by rank or size. The exact source uses path compression but no balancing heuristic. A conservative standard amortized bound for path compression alone is $O((n+m)\log n)$, and a single adversarial `find` can encounter a linear-height chain before compression. Thus the inverse-Ackermann manifest claim is stronger than this implementation directly supports.

The parent array uses $O(n)$ space. Across all component counters, each source occurrence contributes to one frequency and there are at most $n$ distinct component-value entries. Total auxiliary space is $O(n)$.

Recursive `find` also uses stack proportional to the current parent-chain height. Without rank balancing, an adversarial union order can make that depth large enough to matter in Python.

## Alternatives and edge cases

- **Union by rank or size:** Add a balancing array while retaining path compression. This supports the manifest's inverse-Ackermann amortized bound and reduces recursion-depth risk.
- **Graph traversal components:** Build adjacency lists and label components with DFS or BFS in $O(n+m)$ time and space.
- **Simulate swaps:** Searching actual swap sequences is unnecessary and can be enormous; component permutations capture all reachability.
- **No allowed swaps:** Every index is its own component, so the result equals the ordinary Hamming distance.
- **One connected component:** Source values may be permuted globally, and the answer is the multiset shortage against all target values.
- **Duplicate values:** Counter multiplicities ensure each occurrence is used at most once.
- **Target value absent from a component:** Its counter becomes negative and adds a mismatch.
- **Same value in another component:** It cannot help because swaps cannot cross component boundaries.
- **Repeated or redundant edges:** Re-unioning an existing component changes nothing.
- **Already equal arrays:** Every target decrement consumes an available value and the answer stays zero.
- **Input preservation:** Source and target are not rearranged; only DSU and frequency structures change.
- **Deep DSU chain:** Recursive path compression eventually flattens it, but the first traversal may be deep because union by rank is absent.
