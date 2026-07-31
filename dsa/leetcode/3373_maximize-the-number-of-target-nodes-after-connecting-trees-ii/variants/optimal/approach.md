## General

Every tree is bipartite. Color its root $0$, then give every traversed neighbor the opposite color. Two nodes have even path length exactly when they have the same color, because each edge flips the color once. Therefore, for first-tree node `i`, the number of targets already in its tree is the size of `i`'s color class.

Adding a single bridge does not alter any path wholly inside the first tree: there is no second bridge through which a detour could return. For a second-tree node `x`, connect `i` directly to a second-tree endpoint `v`. Its new distance is

$$
1 + \operatorname{dist}_{T_2}(v,x).
$$

This distance is even precisely when `x` has the color opposite to `v`. Thus choosing `v` from one color class makes every node in the other class a target. Since both classes are nonempty, choose an endpoint in the smaller class and obtain the larger class as the second-tree contribution. This best contribution is independent of `i`.

Traverse each tree once, recording every node's color and both class sizes. For every first-tree node, add its own class size to the larger second-tree class size. The color characterization accounts for every possible target, and the direct bridge construction attains the stated maximum.

## Complexity detail

Let $n$ and $m$ be the node counts of the first and second trees. Building and traversing both adjacency lists takes $O(n+m)$ time. The adjacency lists, color arrays, traversal stacks, and returned answer require $O(n+m)$ space.

The benchmark defines `size` as $n+m$ and uses equal-length path trees. The reference visits every node and edge a constant number of times. A correct slower baseline that launches a fresh traversal from every first-tree node needs quadratic work to recover the same even-distance counts, so its runtime ratio grows across the tiers and must fail the scaling verdict.

## Alternatives and edge cases

- **Breadth-first coloring:** A queue produces the same two-coloring and asymptotic bounds as the iterative depth-first traversal.
- **Traversal from every query node:** Counting even distances separately is correct but repeats the same bipartition information and costs $O(n^2+m)$ time.
- **Try every bridge:** Explicitly testing endpoint pairs performs far more work even though parity reduces every choice to two color classes.
- **Recursive DFS:** The recurrence is simple, but a path may contain $10^5$ nodes and overflow Python's recursion limit.
- **Two-node trees:** Each color class contains one node, so either bridge endpoint gives the same contribution.
- **Unbalanced bipartitions:** A star's center and leaves produce sharply different first-tree answers; the second-tree bonus always uses its larger class.
- **Arbitrary edge order:** Coloring starts from label $0$ and follows adjacency, so neither sorted edges nor parent-before-child input is required.
- **Independent queries:** The same best second-tree color class can be reused because each temporary bridge is removed before the next query.
