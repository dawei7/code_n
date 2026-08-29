## General

**Unreachability is determined entirely by connected components**

In an undirected graph, two nodes can reach one another exactly when they belong to the same connected component. Therefore the individual paths do not need to be counted. The task reduces to finding each component's size and counting pairs whose endpoints come from different components.

If previously discovered components contain `s` nodes altogether and a newly discovered component contains `t` nodes, then every one of those `t` new nodes is unreachable from every one of the `s` previous nodes. This creates

`s \cdot t`

new unordered pairs. No pair inside the new component is counted because its endpoints are reachable, and pairs with components not discovered yet will be counted later when those components become new.

The solution combines this counting formula with depth-first search.

**Build an undirected adjacency list**

The list `g` has one inner list for every node. For an edge `[a, b]`, the code appends `b` to `g[a]` and `a` to `g[b]`. Both directions are required because reachability may traverse an undirected edge either way.

An isolated node simply has an empty neighbor list. It is still a connected component of size one and will be handled by the outer loop.

The Boolean list `vis` records whether a node has already been discovered by an earlier DFS call. It serves two purposes: it prevents endless movement back and forth across undirected edges, and it ensures each node contributes to exactly one component size.

**Make DFS return the number of newly visited nodes**

The helper `dfs(i)` first checks `vis[i]`. If the node was already visited, it returns zero because this call discovers no new member. Otherwise, it marks the node and returns

`1 + sum(dfs(j) for j in g[i])`.

The one counts node `i` itself. Each recursive neighbor call counts all still-unvisited nodes reachable through that neighbor. A neighbor already reached by another branch returns zero, so cycles and multiple routes do not double-count nodes.

When `dfs(i)` begins at an unvisited node, recursion follows every edge path within that component. It cannot leave the component because no edge crosses between components. It eventually visits every component node because each is connected to the start by some path. The returned sum is therefore exactly that component's size.

The outer loop still calls `dfs(i)` for every node `i`. If `i` belongs to a component found earlier, the immediate visited check returns `t = 0`. The later arithmetic then adds nothing and changes nothing. This avoids needing a separate `if not vis[i]` branch in the outer loop.

**Count each cross-component pair once**

Before processing a newly encountered component, `s` equals the total number of nodes in all earlier components. After DFS returns its size `t`, `ans += s * t` counts every pair with one endpoint in the new component and one in an earlier component.

Then `s += t` expands the previous-node total so that future components will pair against this one as well.

For component sizes `4`, `1`, and `2`, the updates are:

- first component: `0 \cdot 4 = 0` new pairs, then `s = 4`;
- second component: `4 \cdot 1 = 4` new pairs, then `s = 5`;
- third component: `5 \cdot 2 = 10` new pairs, then `s = 7`.

The total is 14. This is the same set of pairs one could count as `4 \cdot (1 + 2) + 1 \cdot 2`, only accumulated in the reverse component direction.

Suppose two nodes belong to different components `A` and `B`. Whichever component is discovered later causes their pair to be counted, because the earlier endpoint is included in `s` and the later endpoint is included in `t`. The pair is not counted before both endpoints have appeared, and it is never counted again after both components become part of `s`. Thus every unreachable unordered pair contributes exactly once.

**Why reachable pairs never enter the answer**

Nodes in the same component are all included together in one DFS result `t`. The update multiplies `t` only by `s`, which contains nodes from earlier, disjoint components. It never forms `t \cdot t` or chooses two nodes inside the current component.

Because connected components partition all nodes, every pair is either within one component and excluded or crosses two components and is counted once. The final `ans` is therefore exactly the number of unreachable pairs.

**The implementation uses recursive DFS**

The recursive expression is concise, but the graph may contain a component whose DFS tree has depth `n`, such as a long path. Python's default recursion limit can be much smaller than the allowed `n = 100000`. The mathematical algorithm remains correct, but an iterative stack or BFS is safer for the most deeply shaped valid inputs.

## Complexity detail

Let `n` be the node count and `e` the edge count. Constructing the adjacency list takes `O(n + e)` time including creation of the `n` lists. DFS newly visits each node once. Each undirected edge appears in two adjacency lists, so neighbor traversal considers it twice. Calls made toward already visited neighbors return immediately and are included in this same `O(e)` accounting. The outer scan adds `O(n)` work. Total time is `O(n + e)`.

The adjacency list stores `2e` neighbor entries, and `vis` stores `n` flags, for `O(n + e)` auxiliary space. The recursive call stack can contain `O(n)` frames in the worst case, which is already within the combined `O(n + e)` bound.

The answer can be as large as `n(n-1)/2` when every node is isolated. Python integers safely hold that value. In fixed-width languages, the multiplication should use a 64-bit integer before overflow can occur.

## Alternatives and edge cases

- **Iterative DFS:** Replace recursive calls with an explicit stack and count nodes as they are popped or pushed. It has the same `O(n + e)` bounds and avoids Python recursion-depth failure.
- **Breadth-first search:** A queue finds the same component sizes level by level. It is equally correct and iterative, with a worst-case queue of `O(n)` nodes.
- **Union-find:** Union every edge, obtain each representative's component size, then apply the same cross-component formula. With path compression and union by size or rank, it is near-linear and uses `O(n)` space without an adjacency list.
- **Count all pairs then subtract reachable pairs:** Begin with `n(n-1)/2` and subtract `t(t-1)/2` for each component. This is mathematically equivalent; the running-prefix formula avoids one final combinatorial subtraction.
- **Multiply each component by `n - t` and sum:** This counts every cross-component pair twice, once from each endpoint's component, so it would require division by two. The prefix method counts once directly.
- **Complete connected graph:** The first DFS returns `n` while `s = 0`, and all later DFS calls return zero. The answer correctly remains zero.
- **No edges:** Every DFS discovers one isolated node. The accumulated products become `0 + 1 + 2 + \cdots + (n-1) = n(n-1)/2`.
- **One node:** Its component has size one and there is no different-node pair, so the answer is zero.
- **Several components of equal size:** Component identity and discovery order do not affect the total. Each cross-component endpoint combination is still counted once.
- **Cycles:** The visited check prevents recursion from looping and makes already reached neighbors contribute zero.
- **Multiple paths to one node:** The first path marks it; every later path receives zero from that node, preventing duplicate size contributions.
- **Input edge uniqueness:** Repeated edges are excluded by the contract. Even if present, visited checks would preserve correctness, but the adjacency list and traversal would do redundant work.
- **Self-loops:** The contract excludes them. A self-loop would immediately call an already visited node and contribute zero, so it would not change component size.
- **Recursion depth:** A star graph has shallow recursion, while a path graph may reach linear depth. The same asymptotic graph size can therefore behave differently under Python's recursion limit.
- **Input mutation:** The method builds separate adjacency and visited lists and never changes `edges`.
