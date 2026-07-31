## General

**Reveal the tree in non-decreasing value order.** Fix an endpoint value $v$. A path whose endpoints both equal $v$ is good exactly when those endpoints are connected after excluding every node with value greater than $v$. This suggests activating values from smallest to largest and maintaining the connected components of the currently allowed nodes.

Build the tree's adjacency list and group node indices by their values. For each distinct value $v$ in sorted order, visit every node in that group and unite it with each neighbor whose value is at most $v$. Neighbors below $v$ were already processed, while neighbors equal to $v$ are being processed in the same round. After all such unions, the disjoint-set structure therefore represents connectivity using only nodes with values at most $v$.

**Count endpoints only after completing the value round.** Map every node whose value is $v$ to its current component root. If one component contains $c$ such nodes, any unordered pair among them has a unique tree path containing no value above $v$, and each singleton is valid too. That component contributes

$$
\binom{c}{2} + c = \frac{c(c+1)}{2}.
$$

Summing this quantity over the components and then over all values counts every good path once. Paths with different endpoint values are never included, and processing a larger value later cannot retroactively create another path for endpoints already counted.

## Complexity detail

Sorting the distinct values costs $O(n \log n)$. Each tree edge is inspected from both endpoints, and union-find operations take $O(\alpha(n))$ amortized time, where $\alpha$ is the inverse Ackermann function. The overall time is therefore $O(n \log n)$. The adjacency list, value groups, disjoint-set arrays, and temporary component counts use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Repeated restricted traversal:** Starting a DFS or BFS from every node and allowing only nodes no larger than its value can count the same paths, but it may inspect the entire tree from every start and costs $O(n^2)$ time.
- **Pairwise path inspection:** Checking the unique path between every equal-valued pair is correct, but finding or scanning those paths can be quadratic or cubic.
- **All values equal:** Every pair of nodes is connected by a qualifying path, so the answer is $n(n+1)/2$.
- **Larger internal blocker:** Equal-valued endpoints do not form a good path when their unique path contains a larger value.
- **Lower internal nodes:** Values below the endpoints are permitted and may connect many same-valued endpoints into one component.
- **Singleton tree:** The sole node contributes exactly one good path.
- **Path orientation:** Reversing a path does not create another distinct path.
