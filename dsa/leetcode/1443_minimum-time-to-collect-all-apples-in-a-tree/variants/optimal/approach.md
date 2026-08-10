## General

**The answer is determined by useful edges.** The input is a tree rooted conceptually at node `0`. Because it is a tree, every non-root node has exactly one path back to the root. If a node or any node below it has an apple, the edge connecting that subtree to its parent must be crossed to reach the apple. Since the trip must finish back at node `0`, that same edge must also be crossed in the opposite direction. Every useful edge therefore contributes exactly two seconds.

Conversely, an edge leading to a subtree with no apples never needs to be entered. Removing all such useless branches leaves the smallest connected part of the tree containing the root and every apple-bearing node. Traversing each edge of that remaining subtree once outward and once back is sufficient, so charging two seconds per useful edge is both necessary and achievable.

The recursive function `dfs(u, cost)` computes this pruning decision from the leaves upward. Its return value is the complete travel cost contributed by the useful part of the subtree reached at `u`. The parameter `cost` is the price of connecting `u` back to the caller:

- The initial root call uses `cost = 0` because there is no parent edge above node `0`.
- Every recursive call to a neighboring node uses `cost = 2` because, if that neighbor's subtree is useful, the connecting edge must be traversed once in each direction.

Passing this two-second charge into the child is a compact variation of the editorial's approach, which often has the parent add two after receiving a useful child result. Both conventions count the same edges. The stored solution lets the child decide whether its incoming edge should contribute.

**Build both directions of the tree.** Each pair `[u, v]` describes an undirected edge, so the adjacency list adds `v` to `g[u]` and `u` to `g[v]`. A tree does not come with parent pointers. After the root is chosen, DFS discovers the parent-child direction through traversal.

Because every adjacency entry also points back to the node just visited, the algorithm needs to prevent walking in circles. It uses `vis`, a Boolean array of length `n`. On entering `dfs(u, cost)`, it immediately returns zero if `u` is already marked. Otherwise it marks `u` before exploring neighbors. When a child later sees the edge back to `u`, that recursive call finds `vis[u]` true and contributes zero. This gives the same effect as explicitly passing a parent node.

Returning zero for an already visited neighbor does not lose apples. That neighbor is the ancestor whose own DFS frame is already responsible for its apple and its other descendants. The backward adjacency entry should not start a second traversal of it or charge the edge again.

**Collect the costs reported by descendants.** The variable `nxt_cost` begins at zero. For every neighbor `v`, the function adds `dfs(v, 2)`. A neighbor whose branch contains no apple returns zero. A useful child returns its own descendant costs plus two for the edge connecting it to `u`. Summing all neighbor returns therefore gives the exact cost of visiting every useful descendant branch of `u` and coming back to `u` after each one.

After all neighbors have been processed, the function decides whether `u`'s entire rooted subtree matters. If `hasApple[u]` is false and `nxt_cost == 0`, neither `u` nor any unvisited descendant contains an apple. The branch is useless, so `dfs` returns zero. In particular, it does not add `cost`, which means the parent never pays to enter this branch.

Otherwise, this subtree is useful. Either `u` itself has an apple, or at least one descendant branch returned a positive cost. The function returns `cost + nxt_cost`. For a non-root node, the added `cost = 2` charges the necessary trip across its parent edge. For the root, `cost = 0` ensures there is no imaginary edge above node `0`.

**Understand the important base cases without a separate leaf test.** A leaf with no apple has no useful descendant costs and fails the apple test, so it returns zero. A leaf with an apple has `nxt_cost = 0` but passes `hasApple[u]`, so it returns two to a parent or zero if the leaf is also the root. An internal node without its own apple but with a useful child has positive `nxt_cost`, so it returns that child cost plus its own incoming-edge charge. These cases arise naturally from the same final condition.

If only node `0` has an apple, the descendants all return zero. The root is useful because `hasApple[0]` is true, but it returns `cost + nxt_cost = 0 + 0`. This is correct: the apple is already at the starting point, so no edge traversal is needed.

**A branch-by-branch example.** Suppose node `0` connects to nodes `1` and `2`. Node `1` has two leaf descendants, one with an apple and one without, while the entire branch under `2` contains no apple. The apple leaf returns two for its incoming edge. The empty leaf returns zero. Node `1` receives a positive `nxt_cost`, so it returns that descendant cost plus two for edge `0-1`. Node `2` receives only zeros and returns zero, so edge `0-2` is never charged. The root adds the useful return from node `1` and nothing from node `2`.

This traversal may conceptually explore an empty branch while calculating which branches matter, but the returned time describes the optimal apple-collection walk, not the computational DFS's own movements. Inspecting a branch in memory costs algorithm time; it does not mean the person in the problem physically walks there.

**Why the sum of separately explored children is optimal.** In a tree, distinct child subtrees share only their parent. Any walk that starts at `u`, collects apples from a useful child subtree, and ultimately returns to root `0` must come back across that child's connecting edge. It cannot exit through another child because trees contain no cross edge. Thus each useful child's round trip is unavoidable, and child costs can be added without overlap.

By induction from leaves upward, each recursive return equals twice the number of useful edges in that rooted branch, including its incoming edge when appropriate. Empty branches return zero. Useful branches include their unavoidable incoming charge plus optimal descendant charges. At the root, the zero incoming charge leaves exactly twice the number of edges in the minimal root-to-apples subtree. That is the minimum required time.

## Complexity detail

Let `n` be the number of nodes. A tree has exactly `n - 1` edges. Building `g` inserts two adjacency entries per edge, so it takes `O(n)` time and `O(n)` space.

Each node is fully processed once because `vis` is set on first entry. Every undirected edge appears in two adjacency lists. DFS examines both entries, but the entry leading back to an already visited node returns immediately. The total traversal work is therefore proportional to the nodes plus adjacency entries, or `O(n)`.

The adjacency list contains `2(n - 1)` neighbor references, and `vis` contains `n` Booleans, giving `O(n)` explicit storage. The recursion stack can also reach `O(n)` depth when the tree is a chain. Total auxiliary space is consequently `O(n)`, matching the manifest.

The returned integer is only a count; the algorithm does not construct the actual route. Its maximum value is twice the number of tree edges, so the logical answer is at most `2(n - 1)`. Summing child costs remains constant work per adjacency entry.

Python has a practical recursion-depth limit that may be lower than the maximum chain length allowed by the constraints. The asymptotic bound remains `O(n)`, but a production Python implementation for a very deep tree may need an iterative postorder traversal or an explicitly increased safe recursion limit. That runtime concern does not change the DFS recurrence.

## Alternatives and edge cases

- **Pass the parent instead of a visited array:** A recursive call can receive `parent` and skip only that neighbor. Because the graph is guaranteed to be a tree, this prevents revisits and saves the `vis` array, although the adjacency list and recursion stack still require `O(n)` space.
- **Parent adds two for useful children:** A child can return only its descendant cost, and the parent can add `child_cost + 2` when the child has an apple or positive descendant cost. This is equivalent to the stored solution's `cost` parameter; the charge must appear in exactly one place.
- **Iterative postorder traversal:** Build parent and traversal-order arrays with an explicit stack, then process nodes in reverse order to mark useful branches. This avoids Python recursion-depth failures while preserving `O(n)` time and space.
- **Construct an explicit route:** One could record the outward and return visits for every useful edge. That may be useful if the route itself were requested, but this problem asks only for time, so an integer sum is sufficient.
- **Repeated trips from the root:** Returning to node `0` after every individual apple can traverse shared prefix edges many extra times. DFS combines all apples in the same subtree before returning across their shared parent edge.
- **No apples anywhere:** Every non-root subtree returns zero, `nxt_cost` at the root remains zero, and the answer is zero.
- **Apple only at the root:** The root's apple makes its subtree logically useful, but its incoming cost is zero and no descendant cost exists, so the answer is still zero.
- **Apple at a non-root leaf:** Every edge on the unique root-to-leaf path is useful and contributes two. Side branches without apples contribute nothing.
- **Apples on an ancestor and descendant:** The ancestor's apple requires no additional edge beyond those already needed to reach it. The path to the descendant is counted once outward and once back, not once per apple.
- **Several apples in one child subtree:** Shared edges above their branching point are charged only once in each direction. This is the central advantage over independent root-to-apple trips.
- **Several useful root children:** Their costs add because each branch must be entered and exited through its own root edge. The order of visiting those branches does not change total time.
- **Single-node tree:** There are no edges. Whether node `0` has an apple or not, the function returns zero because collection requires no movement.
- **Long chain:** The mathematical answer and linear work remain correct, but recursive Python may exceed its call-stack limit. An iterative postorder version is the robust alternative for that shape.
- **Visited parent has an apple:** The immediate zero return on revisiting an ancestor is correct. That ancestor's original DFS frame handles its apple; counting it again through the backward edge would duplicate work.
- **Undirected input:** Adding only `u -> v` would wrongly assume that every edge is oriented away from root `0`. Storing both directions is necessary because the input's endpoint order does not encode parenthood.
- **Return-to-root requirement:** The factor of two depends on having to come back to node `0`. If the walk could finish at the last apple, one root-to-end path might be traversed only once and the recurrence would need to change.
