## General

**Only subtrees containing value one need work**

The smallest positive genetic value is one. Any subtree that does not contain one has answer one immediately.

Genetic values are distinct, so at most one node has value one. The constructor scan records that node as `idx`. The answer array begins filled with ones.

If no node has value one, every subtree misses one and the initialized array is returned.

If value one exists, exactly its ancestors, including itself, have subtrees containing it. All other nodes keep answer one. This observation reduces the problem to one path from the value-one node to the root.

**Build child lists for downward traversal**

The parent array supports moving upward but not listing a node's subtree. The source builds adjacency list `g` from each parent to its children.

It then walks `idx = parents[idx]` upward one ancestor at a time. At each path node, it expands the globally known set of genetic values to include that ancestor's whole subtree.

**Add each tree node at most once**

Helper `dfs(i)` checks `vis[i]` before doing anything. On first visit, it marks the node, records its genetic value when relevant, and recursively visits children.

When the upward walk moves from a child to its parent, the parent's DFS encounters the already processed child subtree and returns immediately there. It explores only the newly introduced sibling subtrees and the parent itself.

Therefore, although DFS is called once per ancestor, no tree node is processed more than once across all calls.

**Why large genetic values can be ignored**

`has` has length `n + 2`, and the source records `nums[i]` only when it fits that range. A subtree containing at most $N$ distinct values has smallest missing positive value at most $N+1$.

Any genetic value larger than $N+1$ cannot affect whether one through $N+1$ are present, so omitting it is safe.

**Maintain one monotone missing candidate**

Candidate `i` starts at two because every processed path subtree contains genetic value one.

After adding a subtree's newly visited nodes, the loop advances `i` while `has[i]` is true. The first false position is the smallest missing value and is assigned to `ans[idx]`.

As the upward walk grows the subtree, values are only added and never removed. The smallest missing candidate can therefore only stay or increase. It never needs to restart from two.

Across the entire algorithm, the while loop increments `i` at most $N$ times.

**Trace the path behavior**

Suppose the value-one node is a leaf. Its first DFS adds only itself, so candidate two is its answer unless value two somehow also lies in that one-node subtree, which distinctness prevents.

Moving to its parent adds the parent and all sibling subtrees. If value two appears there, the candidate advances to three, and so on. Nodes outside this ancestor chain still lack value one and correctly retain answer one.

**Why the algorithm is correct**

For a node outside the value-one ancestor path, its subtree does not contain the unique value one, so answer one is correct.

For a path node, after `dfs(idx)` returns, `has` contains exactly the relevant values from its subtree: previously seen descendant-path regions plus every newly explored branch. The monotone candidate is the smallest positive absent value, so the assigned answer is correct.

The upward walk reaches every and only ancestor whose answer may exceed one, proving the full result.

**Recursive robustness of the exact source**

A valid tree can be a chain of $10^5$ nodes. Recursive `dfs` can then exceed Python's normal recursion limit and raise `RecursionError`. The amortized algorithm is linear, but an iterative stack is required for robust execution across the full stated depth.

This does not change the invariant or asymptotic space; it changes how the traversal stack is represented.

## Complexity detail

Building children costs $O(N)$. Every node is marked visited at most once, and the missing candidate advances at most $N$ times. The ancestor walk is also at most $N$, so total time is $O(N)$.

Children, answers, visited flags, and presence flags use $O(N)$ space. Recursive stack depth is $O(H)$ and can reach $O(N)$; this is also the source's runtime-depth risk.

## Alternatives and edge cases

- **Iterative DFS:** Preserves the linear amortization while avoiding Python recursion-limit failure.
- **Compute a set for every subtree:** Repeats values across ancestors and can require $O(N^2)$ work and space.
- **Small-to-large set merging:** A general tree-mex technique, but heavier than exploiting the unique value-one path.
- **No genetic value one:** Every answer is one and the method returns immediately.
- **Value one at root:** Only the root lies on its ancestor path, so one whole-tree DFS determines the root answer.
- **Value one at a leaf:** Answers are updated along the entire root path.
- **Values above $N+1$:** Safely ignored because they cannot affect a subtree mex.
- **Distinct values:** Guarantee a unique value-one node and simplify presence to Booleans.
- **Already visited child subtree:** DFS returns immediately, preventing repeated work.
- **Candidate monotonicity:** Growing subtrees can never make a previously present value disappear.
- **Deep chain:** Exact recursion is unsafe near $10^5$ depth.
- **Input preservation:** Parent and genetic arrays are read into separate supporting structures.
