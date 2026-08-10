## General

**First remove every focus point already powered by crystals.** Build directed adjacency list `g` from each `flowFrom` to matching `flowTo`. Every crystal node begins with `vis[x]=1` and enters a queue. `bfs` follows outgoing runes, marking every focus point that can already receive magic.

After this traversal, nodes marked one require no new rune. Only the subgraph induced by `vis == 0` remains relevant.

**Why one new rune can power an entire forward region.** If Alice adds a rune from any powered point into an unpowered node `u`, then `u` and every node reachable from it become powered. The question is therefore the minimum number of starting nodes whose forward-reachable sets cover the remaining directed graph.

**Think in terms of strongly connected components.** Within an SCC, every node reaches every other, so one incoming new rune powers the whole component. Contracting SCCs produces a directed acyclic graph. Every source component of the unpowered condensation—one with no incoming edge from another unpowered component—requires its own new rune. No other component can reach it. Conversely, adding one rune into each source component powers every downstream component.

The answer is therefore the number of source SCCs in the initially unpowered region.

**The source finds that count without explicitly building SCC IDs.** Recursive `dfs` marks unpowered nodes with state two and appends a node after visiting all outgoing unvisited neighbors. This produces a DFS finishing-order list `seq`. Reversing it puts roots of still-uncovered source regions before their directed descendants.

Reachable crystal nodes have state one and are skipped. DFS-discovered but not yet selected nodes have state two.

**Greedily start from the reversed finishing order.** For each node `i` in reversed `seq`, the source checks whether it is still state two. If so, no earlier selected start reached it. Alice must conceptually add a rune into its source region, so `ans` increases by one.

A BFS from `i` then changes every forward-reachable state-two node to state one. Later nodes covered by this choice are skipped.

**Why reversed finishing order is essential.** If a component $A$ can reach component $B$ but not vice versa, DFS finishing times order the condensation so that an uncovered source-side representative is considered before descendants when the list is reversed. Selecting a descendant first could not power its predecessor and might waste an extra start. Selecting the source covers both.

Inside one SCC, the first encountered member's BFS reaches all members, so the SCC contributes once.

**Trace isolated nodes.** An unpowered focus point with no incoming or outgoing edges forms a one-node source SCC. DFS appends it, the later BFS reaches only itself, and answer increases once. Two such nodes require two runes, as in the first example's points four and five.

**Why the count is minimal.** Every unpowered source SCC has no incoming path from crystals or another unpowered SCC, so at least one added rune must enter it. The reversed-order BFS process adds exactly one start per such source and reaches all descendants. Its lower and upper bounds coincide.

**The manifest overstates the explicit implementation.** It says the source contracts SCCs. The mathematical justification uses SCC condensation, but `solution.py` never computes reverse edges, SCC labels, or a contracted graph. It uses one finishing-order DFS plus forward BFS marking to obtain the same source count.

**A recursion-depth defect remains.** `dfs` is recursive and can follow a directed path of length $10^5$. Normal Python recursion limits are much smaller, and the source has no iterative stack or limit adjustment. It can raise `RecursionError` on valid inputs.

## Complexity detail

Building the graph and all BFS/DFS traversals touch each node and directed edge only a constant number of times, so mathematical time is $O(n+m)$, where $m$ is the rune count.

Adjacency lists, states, finishing order, and queues use $O(n+m)$ space. Recursive call depth can be $O(n)$ and is the practical failure risk noted above.

## Alternatives and edge cases

- **Explicit Kosaraju or Tarjan SCCs:** Contract components and count unpowered sources directly; it is clearer but needs more machinery.
- **Iterative DFS:** It preserves finishing order while avoiding recursion-limit failure.
- **Add a rune to every unpowered node:** It is valid but ignores forward reachability and is not minimal.
- **All nodes crystal-reachable:** `seq` is empty and answer is zero.
- **Unpowered directed chain:** One rune at its source powers the whole chain.
- **Reverse chain selection:** Choosing the sink first would waste starts, which finishing order prevents.
- **Unpowered cycle:** One selected node powers the entire SCC.
- **Isolated node:** It contributes exactly one.
- **Duplicate crystal entries:** They can cause redundant initial queue pops but do not change reachability.
- **Edges into powered nodes:** DFS skips state-one destinations because they need no additional coverage.
- **No explicit added-rune endpoints:** The method returns only the minimum count.
- **State meanings:** Zero is unseen/unpowered, two is DFS-discovered/unpowered, and one is powered or covered.
- **Manifest wording:** SCCs justify the algorithm but are not explicitly contracted.
- **Required imports:** `deque`, `Deque`, and `List` must be available.
