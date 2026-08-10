## General

**Translate "all paths lead there" into graph conditions**

For the answer to be true, the part of the directed graph reachable from `source` must satisfy two structural rules:

1. Every reachable node with no outgoing edge must be `destination`.
2. No directed cycle may be reachable from `source`.

The first rule prevents a path from getting stuck at the wrong terminal. The second prevents a path from looping forever and creates only finitely many possible paths in the reachable subgraph.

These rules also ensure that a path to `destination` actually exists. In a finite acyclic directed graph, repeatedly following outgoing edges must eventually reach a terminal node. If every reachable terminal is `destination`, at least one such walk from `source` ends there.

Depth-first search is a natural fit because its active recursion stack identifies directed cycles, while its return value can say whether every continuation from one node is valid.

**Build the adjacency list**

The graph representation is:

```python
g = [[] for _ in range(n)]
for a, b in edges:
    g[a].append(b)
```

`g[i]` contains every node reachable by one outgoing edge from node `i`. A node is terminal exactly when `g[i]` is empty.

Parallel edges are retained. That is harmless: following the same destination twice does not change whether it is valid, and memoized states make repeated completed work constant time.

Self-loops are also retained. They must be detected as cycles, and the DFS coloring does so.

**The destination itself must be terminal**

Before starting DFS, the exact solution checks:

```python
if g[destination]:
    return False
```

If `destination` has an outgoing edge, a path can arrive there and then continue. It is not a terminal endpoint as required. A self-loop at the destination is also invalid because it permits infinitely many traversals.

This check is valid even if destination is unreachable. In that case the overall answer would be false anyway because no source path reaches the destination.

Making the requirement explicit also simplifies the interpretation of the recursive base case: the only acceptable terminal node is an actually terminal destination.

**Use three logical colors**

The state array is initialized as:

```python
st = [0] * n
```

Each value has one of three meanings:

- Zero means unvisited. DFS has not yet analyzed this node.
- One means visiting. The node is on the active recursion path and its descendants are still being processed.
- Two means verified. Every path beginning at this node has already been proven to terminate correctly at `destination`.

These are commonly called white, gray, and black states. Distinguishing visiting from verified is essential in a directed graph. Encountering a visiting node proves a cycle, while encountering a verified node permits safe reuse of previous work.

**Reuse a state or reject a back edge**

The first DFS condition is:

```python
if st[i]:
    return st[i] == 2
```

If `st[i]` is one, the current recursion path has returned to a node whose processing has not finished. The edges along the recursion stack plus this return edge form a directed cycle. That cycle is reachable from `source`, so some walks can repeat it indefinitely and the answer must be false.

If `st[i]` is two, the node and all of its reachable continuations were already verified. Returning true immediately avoids exploring the same subgraph again.

The condition `if st[i]` covers both nonzero states, and the equality distinguishes their outcomes.

An edge to a verified node is not a cycle in the active DFS path. It may be a cross edge or a forward connection into shared valid work, and memoization correctly accepts it.

**Validate terminal nodes**

For an unvisited node, the next condition is:

```python
if not g[i]:
    return i == destination
```

A node with no outgoing edges ends every path that reaches it. It is acceptable exactly when it is `destination`. Reaching any other terminal immediately proves that at least one source path ends at the wrong place.

The terminal node is returned from before being marked state two. A later parallel or converging path may evaluate the same terminal again, but that evaluation is constant time and returns the same answer. Marking it verified would also be possible, but is not necessary for correctness or asymptotic complexity.

This condition also handles a graph consisting of one node. If `source == destination` and the node has no outgoing edges, DFS returns true. If source is a different terminal, it returns false.

**Explore all outgoing choices**

A nonterminal unvisited node is placed on the active path:

```python
st[i] = 1
```

Then every outgoing neighbor must be valid:

```python
for j in g[i]:
    if not dfs(j):
        return False
```

The universal word "all" in the problem is why one bad neighbor is enough to fail. If `dfs(j)` is false, there is a path through `j` that reaches a wrong terminal or a reachable cycle. That path is also a bad path from `i`, so the function short-circuits.

Conversely, `i` is safe only after every neighbor returns true. At that point, every possible first edge from `i` leads into a subgraph whose paths all end correctly.

If a failure occurs, some active states remain marked one. The false result immediately propagates to the original call and the whole function ends, so those states are never reused in a later independent decision.

**Memoize a completely verified node**

After all neighbors succeed, the code executes:

```python
st[i] = 2
return True
```

State two certifies both required properties for paths beginning at `i`: no explored continuation contains a cycle, and every terminal reached is destination. Future edges reaching `i` can return this result without repeating its descendants.

**Why the root result is correct**

If `dfs(source)` returns false, the recursion found one of three conclusive violations: destination has outgoing edges, a reachable terminal is not destination, or an edge returns to a visiting node and forms a reachable directed cycle. Each violation directly contradicts the contract.

If it returns true, every reachable nonterminal had all outgoing edges checked, no active-state edge was found, and every reachable terminal was destination. The reachable subgraph is therefore acyclic and all of its maximal paths end at destination. The function returns true exactly in the required cases.

Disconnected graph components do not matter because `dfs` begins only at `source`. Their terminals and cycles cannot occur on a path starting from source.

## Complexity detail

Let `V = n` and let `E` be the number of directed edges.

Building `g` takes `O(V + E)` time: `V` empty lists are created and each edge is appended once. During DFS, every reachable nonterminal node is fully processed at most once before becoming state two. Its adjacency list is scanned once. Repeated visits to a verified node take constant time.

Across the traversal, at most all vertices and all edges are examined, so total time is `O(V + E)`. Early rejection may inspect less, but the worst-case bound includes the entire graph. Parallel edges each occupy and require one adjacency entry, so they are correctly included in `E`.

The adjacency list uses `O(V + E)` space. The state array uses `O(V)`. Recursive depth can reach `O(V)` in a long directed chain, so the call stack also uses `O(V)` space. Total auxiliary space is `O(V + E)`.

The editorial's suggestion that pruning always reduces the traversal to `O(V)` is not a safe general bound: a valid acyclic graph can contain many edges, and confirming all paths requires inspecting them. The manifest's `O(V + E)` time and space bounds accurately describe the exact solution.

## Alternatives and edge cases

- **Iterative three-color DFS:** Store explicit stack frames containing a node and its next neighbor index. This preserves `O(V + E)` bounds while avoiding Python recursion-depth limits on a chain of up to 10000 nodes.
- **Topological processing of the reachable subgraph:** One can first identify reachable nodes, reject reachable cycles with a topological count, and verify all reachable terminals. This is valid but needs more bookkeeping than the direct DFS.
- **A simple visited Boolean is insufficient:** Seeing an already visited node does not say whether it is an active back edge or a safely completed shared subgraph. Three states are necessary for directed-cycle reasoning.
- **Destination has an outgoing edge:** The explicit precheck returns false, including when that edge is a self-loop.
- **Source equals destination:** The result is true only when destination is terminal. If it has outgoing edges, paths can continue and the precheck returns false.
- **Source is a wrong terminal:** `g[source]` is empty but `source != destination`, so DFS immediately returns false.
- **Wrong terminal on one branch:** Even if many other branches reach destination, the first wrong terminal makes its recursive call false and invalidates the universal condition.
- **Reachable cycle with an exit to destination:** The exit does not help. A path may traverse the cycle arbitrarily many times, so the visiting-state encounter returns false.
- **Unreachable cycle:** DFS never touches it, and it correctly has no effect on paths beginning at source.
- **Self-loop:** The node is marked visiting before its neighbor call reaches the same node. State one returns false and detects the cycle.
- **Parallel edges:** If the first copy leads to a verified child, later copies return true immediately. They do not create a cycle by themselves.
- **Diamond-shaped DAG:** Multiple branches may converge on one node. The first traversal verifies it, and later branches reuse state two rather than treating convergence as a cycle.
- **No edges:** The answer is true only when `source == destination`; otherwise source is a wrong terminal.
- **Long chain:** Correctness is straightforward, but recursive depth may exceed the interpreter's configured limit. An iterative stack is safer in environments with a low recursion limit.
- **At least one path condition:** In a finite reachable acyclic graph, following edges must end at a terminal. If DFS returns true, that terminal can only be destination, so existence follows from the other verified conditions.
