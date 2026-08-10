## General

**Treat equations as multiplicative connections**

Each equation `a / b = value` connects two variables by a known ratio. A sequence of equations can imply another ratio: if `a / b = 2` and `b / c = 3`, then `a / c = 6`. A contradiction occurs when a new equation connects variables that are already related but gives a ratio different from the one implied by the earlier equations, outside the permitted floating-point tolerance.

Weighted union-find is useful because ordinary union-find can answer whether two variables belong to the same connected component, while the added weights preserve their ratio. Every distinct variable is first mapped to an integer ID. The parent array `p` initially makes every ID its own root, and every corresponding weight starts at `1.0`.

The most important detail is the direction of the stored weight. Before path compression, the invariant is

`w[x] = p[x] / x`.

After `find(x)` finishes, `p[x]` is the component root and the same invariant becomes

`w[x] = root / x`.

Here the symbols represent the positive numerical quantities associated with the equation variables. Remembering the ratio as “parent divided by node” is essential; assuming the opposite direction would reverse the union formula.

**Path compression must update the ratio as well as the parent**

If `x` is not a root, `find(x)` first recursively finds and compresses its current parent. Before that recursive call, `w[x] = oldParent / x`. After the call, `w[oldParent] = root / oldParent`. Multiplying them gives

`(oldParent / x) \cdot (root / oldParent) = root / x`.

That is exactly why the code performs `w[x] *= w[p[x]]` before replacing `p[x]` with the returned root. The old parent entry must still be available for the multiplication. Once both updates are complete, `x` points directly to the root and its weight correctly represents `root / x`.

For a root, `p[x] == x` and `w[x] == 1.0`, matching `x / x = 1`. Repeated calls remain correct because a node already compressed to the root simply multiplies through a root weight of one if compression is needed again.

**Join two previously separate components**

Consider a new equation `a / b = v`. After calling `find` on both endpoints, let their roots be `pa` and `pb`. The weights now mean

`w[a] = pa / a` and `w[b] = pb / b`.

If `pa != pb`, the earlier equations do not yet impose any ratio between these components, so the new equation cannot contradict them. The solution attaches root `pb` beneath root `pa` by assigning `p[pb] = pa`. It must also choose `w[pb]`, whose required meaning is now `pa / pb`.

From the known weights,

`a = pa / w[a]` and `b = pb / w[b]`.

Substituting these expressions into `a / b = v` gives

`(pa / w[a]) / (pb / w[b]) = v`,

so

`pa / pb = v \cdot w[a] / w[b]`.

The assignment `w[pb] = v * w[a] / w[b]` therefore establishes exactly the required parent-to-node ratio for the newly attached root. All existing ratios inside both components remain unchanged, and the new edge makes their combined component satisfy the new equation.

The implementation always attaches `pb` under `pa`. It does not use a rank or size heuristic. That choice keeps the weight formula simple but matters when describing the strongest theoretical time bound.

**Check an equation inside one existing component**

If `pa == pb`, earlier equations already determine the ratio between `a` and `b`. Because

`a = root / w[a]` and `b = root / w[b]`,

their implied ratio is

`a / b = w[b] / w[a]`.

Instead of explicitly dividing, the code compares `v * w[a]` with `w[b]`. These quantities are equal exactly when `v = w[b] / w[a]`. Avoiding the final division is convenient and avoids one more division operation.

The problem considers two values equal when their absolute difference is less than `10^{-5}`. Accordingly, the solution reports a contradiction when

`abs(v * w[a] - w[b]) >= 1e-5`.

The boundary is deliberate: a difference strictly below the tolerance is accepted, while a difference equal to the tolerance is not below it and is therefore contradictory.

As soon as one contradiction is found, returning `True` is sufficient. If every equation either joins separate components or agrees with the ratio already implied inside its component, the loop ends and the method returns `False`.

**Why processing equations one at a time is complete**

At the start, each isolated variable has only the trivial self-ratio and satisfies the invariant. When an equation joins two components, the derived root weight makes that equation true while preserving every relation already stored within each component. Thus, after every successful union, all equations processed so far are simultaneously represented by the weighted forest.

When an equation's endpoints already share a root, the unique ratio implied by the forest is obtained from their root-relative weights. If the new value disagrees, it cannot be made true without breaking at least one earlier equation, so a contradiction genuinely exists. If it agrees within tolerance, adding it supplies no new independent connection and the current structure already represents it.

By induction over the input order, failure of a consistency check is both necessary and sufficient for the processed system to become contradictory. If no check fails, the final collection remains mutually consistent according to the stated tolerance.

**Variable mapping is separate from ratio logic**

The code first scans all equation endpoints and gives every new string a consecutive integer ID. Although the mapping object has a default factory, the explicit membership check ensures IDs are assigned intentionally and never confused with the valid ID zero. Once mapping is finished, the union-find arrays can be compact lists indexed by integers rather than dictionaries indexed by variable names.

## Complexity detail

Let `V` be the number of distinct variables and `M` the number of equations. Building the mapping takes `O(M)` expected dictionary operations and creates arrays of length `V`. Processing each equation performs two `find` operations and at most one constant-time union or consistency comparison.

This exact implementation uses path compression but no union-by-rank or union-by-size. The familiar `O((V + M)\alpha(V))` bound requires the combination of path compression with a balancing union heuristic, so it should not be claimed unconditionally for this code. With arbitrary linking and path compression alone, a conservative amortized bound is `O((V + M)\log V)`, while an individual `find` before compression can traverse `O(V)` parents. The small source constraints make either cost modest in practice. Adding rank or size while preserving the weight formulas would recover the standard inverse-Ackermann amortized bound.

The parent array, weight array, variable-to-ID mapping, and recursive `find` call stack use `O(V)` auxiliary space. A badly shaped tree can make one recursive call reach depth `O(V)` before path compression flattens it. The mapping stores variable names as dictionary keys, so if the total characters in distinct names are included in memory accounting, that text contributes its own input-dependent storage; the union-find structures themselves remain linear in `V`.

All ratio arithmetic uses floating-point numbers. The algorithm follows the contract's absolute tolerance rather than promising exact symbolic arithmetic. The values are positive, so the divisions used while linking components never divide by zero.

## Alternatives and edge cases

- **Weighted graph traversal for every equation:** Store both directed ratios for each accepted equation, then run DFS or BFS to discover the implied ratio when checking a new connection. This is conceptually direct but may revisit much of a component for many equations, leading to roughly `O(M(V + M))` work in a dense repeated-query scenario.
- **Logarithmic transformation:** Convert multiplicative equations into additive differences with logarithms and use a potential-based structure. This can clarify the algebra but still uses floating-point approximations and adds logarithm operations; positive values make it possible, but the direct ratios are simpler.
- **Union by rank or size:** Maintain a balancing array and attach the smaller or shallower component beneath the other. This improves the formal amortized bound, but the root-weight formula must be inverted appropriately when the attachment direction is reversed.
- **Ordinary unweighted union-find:** It can tell whether `a` and `b` are connected but cannot recover the ratio implied between them, so it cannot decide whether a cycle-forming equation is consistent.
- **Assuming `w[x] = x / root`:** That interpretation reverses every derived ratio. In this implementation, `w[x]` is parent divided by node before compression and root divided by node afterward.
- **Updating the parent before the compression weight:** The multiplication needs the old parent's root-relative weight. Carelessly overwriting references or using a stale direction can destroy the invariant even if connectivity remains correct.
- **Equation joining two separate components:** It is never immediately contradictory because no earlier equation relates those components. The new value defines their relative scale through `w[pb]`.
- **Repeated equation:** If its value agrees with the already implied ratio within tolerance, it changes nothing. If it disagrees by at least `10^{-5}` under the implementation's comparison, the method returns `True`.
- **Reciprocal equation:** After accepting `a / b = v`, an equation `b / a = 1 / v` should agree through the same root-relative weights. A materially different reciprocal is detected as a contradiction.
- **Self-equation:** For `a / a = v`, both endpoints have the same root and equal weights, so consistency requires `v` to be within tolerance of `1`. No special branch is necessary.
- **Disconnected groups at the end:** Different components may remain unrelated. That is not a contradiction; it only means the equations never specify a ratio between those groups.
- **Tolerance boundary:** The code accepts only differences strictly smaller than `1e-5`. A difference exactly equal to `1e-5` satisfies the `>=` test and is reported as contradictory.
- **Relative versus absolute error:** The implementation uses the absolute comparison required by the local contract. Replacing it with relative error would change behavior for very large or very small ratios.
- **Long parent chain:** Always attaching `pb` under `pa` can temporarily create a deep tree. Path compression flattens every traversed route, but Python recursion depth is still a practical reason that rank or an iterative `find` could be preferable for much larger unconstrained inputs.
