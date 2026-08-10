## General

**Exploit the tiny value domain**

Node values range only from one through fifty. The tree may contain up to $10^5$ nodes, so repeatedly walking from each node to the root would be too slow. Instead, the exact solution remembers the deepest active ancestor for each possible value.

Before traversing the tree, it builds `f`. For every value `i` from one through fifty, `f[i]` lists every value `j` in the same range satisfying `gcd(i, j) == 1`.

This table turns a coprimality search at node `i` into a scan over at most fifty candidate values. Fifty is fixed by the constraint, so that scan is constant time in asymptotic terms.

**Represent the rooted path with per-value stacks**

`stks[v]` is a stack of ancestors on the current root-to-node path whose node value is `v`. Each entry is a pair `(node index, depth)`.

Depth increases as DFS moves away from root zero. Within one value's stack, entries are pushed in path order, so the top entry is the closest active ancestor having that value.

There can still be several coprime value choices. The solution examines the top of every stack named in `f[nums[i]]` and selects the entry with the greatest depth. That entry is the closest coprime ancestor overall.

**Find the current node's answer before pushing itself**

At the beginning of `dfs(i, fa, depth)`, variables `t` and `k` are both minus one. `t` will hold the best ancestor node, and `k` its depth.

For each value `v` coprime with `nums[i]`, the code looks at `stks[v]`. If it is non-empty and its top depth exceeds `k`, parallel assignment `t, k = stk[-1]` saves that node and depth.

After the scan, `ans[i] = t`. If no qualifying stack was non-empty, `t` remains minus one.

The current node is not pushed before this search, which correctly enforces that a node is not its own ancestor. Only nodes strictly above it are active in the stacks.

**Build the rooted traversal from an undirected tree**

`g` stores both directions for every edge. DFS receives `fa`, the parent from which it arrived. While iterating through `g[i]`, it skips `j == fa` and recursively visits every other neighbor as a child.

Because the graph is a tree, excluding the parent is enough to prevent revisiting nodes. There are no cycles that require a general visited set.

Root zero is called with parent minus one and depth zero, so it has no active ancestors and receives answer minus one.

**Understand the unusual push placement**

For each child `j`, the exact source performs:

`stks[nums[i]].append((i, depth))`,

then recursively explores that child, then pops the entry.

Thus the current node is pushed separately around each child call rather than once around the whole child loop. During the recursive call, the child and all its descendants can see the current node as an ancestor. After returning, the pop restores the stack state for the next branch.

Re-pushing for a sibling produces the same logical path state and remains correct. A more conventional implementation would push once before iterating all children and pop once afterward, reducing constant overhead but not changing results or asymptotic complexity.

**Why backtracking is essential**

Nodes from one subtree are not ancestors of nodes in a sibling subtree. If the DFS failed to pop entries after returning, a later sibling could incorrectly select a deep node from the earlier branch.

The push-recursion-pop pattern makes `stks` describe exactly the current root-to-parent path at the start of every call. It is a compact path-state structure rather than a global collection of all previously visited nodes.

**Trace the first example**

At root zero with value two, all stacks are initially empty, so its answer is minus one. Before DFS enters child one, root zero is pushed on stack two.

Node one has value three. Value two is coprime with three, so the top entry `(0,0)` is selected and answer one is zero.

Before entering node two, node one is pushed on stack three. Node two also has value three, so stack three is not eligible because three is not coprime with itself. Stack two still contains root zero, making zero the closest valid ancestor.

For node three with value two, node one's value three is coprime and has greater depth than root candidates, so answer three is one.

**Why the algorithm is correct**

At entry to `dfs(i,...)`, each `stks[v]` contains exactly ancestors of node `i` having value `v`, ordered by depth. Its top is therefore the closest ancestor with that value.

The precomputed list `f[nums[i]]` contains exactly values coprime with the current value. Comparing the top depths across those stacks selects the deepest, hence closest, valid ancestor. If none exists, minus one is correct.

Backtracking preserves the stack invariant for every recursive branch. Since DFS visits every tree node, every answer entry is computed correctly.

## Complexity detail

Let $n$ be the number of nodes. Building the adjacency list takes $O(n)$ time because a tree has $n-1$ edges. Coprime-table construction performs $50^2$ gcd checks, which is constant with respect to $n$.

Each node scans at most 50 coprime candidate values and processes each incident tree edge a constant number of times. Because 50 is fixed, total time is $O(n)$, matching the manifest.

The adjacency list, answer list, and recursive call stack use $O(n)$ space in the worst case. Across all value stacks, at most the nodes on the current root path are active, using $O(n)$ worst-case space. Total auxiliary and result-related storage is $O(n)$.

Python recursion depth can reach $n$ for a chain-shaped tree, which may exceed the default recursion limit even though the asymptotic algorithm is linear.

## Alternatives and edge cases

- **Walk ancestors for every node:** It is simple but takes $O(n^2)$ on a chain.
- **Push once around all children:** This conventional DFS structure avoids repeated push/pop for siblings while preserving the same stack invariant.
- **Store only one latest node per value:** Save and restore the previous entry during DFS. It can replace explicit stacks because traversal is nested, but stacks make depth history clearer.
- **Euler tour with offline queries:** It is much more machinery than needed for the fixed value domain.
- **Root node:** It has no ancestor and always receives minus one.
- **Same value as ancestor:** It is eligible only when that value is one, since `gcd(v,v)=v`.
- **Value one:** One is coprime with every allowed value, including itself.
- **Several eligible ancestors:** The largest depth, not smallest node index, determines closeness.
- **No eligible ancestor:** All relevant stacks are empty and `t` remains minus one.
- **Sibling branches:** Pop operations prevent one sibling from appearing as another's ancestor.
- **Tree parent:** Skipping `fa` is sufficient because the input is acyclic.
- **Fixed range fifty:** It converts the per-node candidate scan into constant asymptotic work.
- **Depth pair:** Storing depth permits comparison across different value stacks.
- **Recursive chain:** Correctness holds, but practical stack overflow is possible at maximum $n$.
- **Input preservation:** The method builds separate graph and answer structures without changing `nums` or `edges`.
