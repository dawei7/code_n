## General

**Turn edge deletion into a target component sum**

If deleting edges creates $k$ components and every component has the same sum `t`, then the total node sum `s` must satisfy

$$
s = k \cdot t.
$$

Therefore $k$ must divide `s`, and its target is forced to be `t = s // k`. Maximizing deleted edges is equivalent to maximizing the number of components, because splitting a connected tree into $k$ components requires deleting exactly $k-1$ edges.

The solution tries possible component counts `k` from largest to smallest. The first feasible count immediately gives the maximum deletion answer `k-1`.

**Bound the number of components**

No component can have sum smaller than the largest single node value `mx` because the component containing that node includes at least that positive value. Hence `t >= mx`. Since `t=s/k`, this implies

$$
k \le \left\lfloor \frac{s}{mx} \right\rfloor.
$$

There also cannot be more than `n` non-empty components. The loop consequently begins at `min(n, s // mx)`.

It stops before 1 because one component always exists without deleting an edge and would yield answer zero. If no tested `k>=2` works, returning zero covers that fallback.

Only values of `k` satisfying `s % k == 0` are tested with DFS, because unequal integer component sums cannot add to `s` otherwise.

**Root the tree temporarily**

The adjacency list `g` stores each undirected edge in both directions. The nested `dfs(i, fa)` treats node `i` as the root of its current subtree and `fa` as its parent. Skipping the parent prevents walking back across the same undirected edge and recursing forever.

For one candidate target `t`, the DFS returns one of three meanings:

- A value from 1 through `t-1` is the sum of the connected residual portion of this subtree that still needs to join its parent.
- Zero means the subtree's residual has reached exactly `t` and forms one or more completed components, so nothing needs to cross the parent edge.
- Negative one means this candidate target is impossible within the subtree.

The return value is not the complete raw subtree sum. Completed target-sized components are conceptually cut away and contribute zero to their parent.

**Combine children and cut completed components**

At node `i`, `x` starts as `nums[i]`. For each child `j`, the DFS obtains `y`. If `y == -1`, the child subtree cannot be partitioned for this target, so the current subtree also fails immediately.

Otherwise `y` is added to `x`. A zero child contributes nothing because its component can be separated by deleting the edge to `i`. A positive child residual must remain connected to `i` and becomes part of the current residual sum.

After all children:

- If `x > t`, the candidate fails. Every node value is positive, so adding ancestors or other nodes can only increase this connected residual; it can never shrink back to `t`.
- If `x < t`, the residual is not complete and `x` is returned upward.
- If `x == t`, this group is a complete component. Returning zero tells the parent it may be cut off cleanly.

At the root, success requires `dfs(0,-1) == 0`. A positive root residual would mean some nodes remain in a component smaller than the target, while negative one means an overshoot occurred.

**Why this subtree rule is sufficient**

In a rooted tree, deleting an edge separates an entire child subtree from its parent side. For a fixed positive target, whenever the residual sum at a subtree reaches `t`, cutting it is safe: it already forms a valid connected component, and keeping it attached would only make an ancestor residual larger.

If a residual exceeds `t`, no alternative placement of cuts inside already processed children can reduce it unless one of those child residuals itself formed a target component. The recursion already returns such completed children as zero. Every remaining positive residual is required to stay attached because it is smaller than `t` and cannot form a valid component alone.

Inductively, each DFS return is therefore the only relevant sum that must cross the parent edge after extracting all possible valid components below. Root return zero means every node belongs to one target-sum component.

**Trace the sample structure**

For `nums = [6,2,2,2,6]`, the total is 18 and maximum node is 6. The greatest possible component count is three, giving target 6. Rooting at node 0, the leaf node 2 returns residual 2. Node 4 has value 6 and returns zero, representing its own completed component. Node 3 therefore contributes only its own 2 upward. Node 1 combines its value 2 with residuals 2 and 2 to reach 6 and returns zero. Root 0 is itself 6 and returns zero. Three components are feasible, so two edges can be deleted.

**The exact traversal differs from the summary**

The manifest describes iterative postorder traversal, but the protected source uses recursive `dfs`. Its mathematical logic is postorder because children are evaluated before their parent sum is decided, yet operationally it consumes Python call-stack depth.

For a path-shaped tree with up to 20,000 nodes, recursion can exceed Python's default recursion limit. This is a practical risk in the exact file. An explicit parent/order stack can implement the same feasibility test safely.

## Complexity detail

Let $S=\sum\texttt{nums}$, $K=\min(n,\lfloor S/mx\rfloor)$, and let $d(S)$ be the number of positive divisors of $S$. The outer loop inspects at most $K=O(n)$ candidate counts. It runs a full DFS only for divisors of $S$ in that range. Each DFS visits every node and edge once, taking $O(n)$ time.

A precise bound is $O(K+n\,d(S))$, which is $O(n\,d(S))$ because $K\le n$ and $d(S)\ge1$. Early overshoots can make individual failed checks faster but do not change the worst case.

The adjacency list uses $O(n)$ space for a tree. A recursive DFS can use $O(n)$ stack frames on a skewed tree. The graph dictionary and scalar values remain linear overall, so auxiliary space is $O(n)$.

The candidate target `t` is captured from the outer loop by the nested function and changes before each new DFS call. Each call completes before the loop advances, so it always uses the intended target.

## Alternatives and edge cases

- **Iterative postorder feasibility:** Build parent and traversal-order arrays, then accumulate residual sums in reverse order. This matches the manifest wording, preserves the same complexity, and avoids recursion-depth failure.
- **Try target sums instead of component counts:** Enumerate divisors `t` of the total and derive `k=S/t`. Testing smaller targets first also seeks more components, but candidate ordering must remain careful.
- **Subset-style partitioning:** General graph partition methods are unnecessary and often exponential. Tree edges impose a hierarchy that postorder residual sums exploit.
- **One node:** No `k>=2` candidate exists, so zero edges are deleted.
- **Total not divisible by `k`:** Equal integer component sums are impossible, and the DFS is correctly skipped.
- **Target below the maximum node:** The component containing that node would already exceed the target, so the initial upper bound excludes such counts.
- **Residual exactly target:** It must return zero, not `t`, because the component can be cut and should not be added again by its parent.
- **Residual above target:** Positive node values mean it can never be repaired by adding more nodes, so failure is final.
- **All node values equal:** Deleting every edge is feasible, producing $n$ singleton components and answer $n-1$.
- **Only one component feasible:** The candidate loop finds none above one and returns zero.
- **Recursive implementation:** A deep tree may raise `RecursionError` even though the algorithmic idea is correct; an explicit stack is safer for the stated maximum $n$.
