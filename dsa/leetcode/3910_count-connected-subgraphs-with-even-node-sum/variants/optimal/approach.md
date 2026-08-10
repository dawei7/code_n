## General

With at most 13 nodes, every nonempty node subset can be represented and tested. The source encodes a subset as an $n$-bit integer:

$$
\text{bit }i=1
\iff
\text{node }i\text{ belongs to the subset}.
$$

For each mask, it first checks whether the selected node-value sum is even. Only then does it run a graph traversal restricted to the selected nodes to test whether the induced subgraph is connected.

**Building the undirected adjacency lists**

For each edge $[u,v]$, the source appends:

- $v$ to `g[u]`; and
- $u$ to `g[v]`.

This symmetric insertion lets DFS travel in either direction along every undirected edge.

The traversal later uses only edges whose endpoints are selected. It does not need to construct a new graph for every subset; the visited-mask initialization blocks excluded endpoints.

**Enumerating every nonempty subset**

The value

$$
m=(1\ll n)-1
$$

has its lowest $n$ bits set to one. For example, with $n=4$:

$$
m=1111_2.
$$

The loop `for sub in range(1, m + 1)` visits every nonzero $n$-bit mask exactly once. Starting at 1 excludes the empty subset, as required.

There are $2^n-1$ such candidates. This exponential enumeration is acceptable only because $n\le13$.

**Checking the even-sum condition**

The input values are binary, but ordinary summation is sufficient:

```text
s = sum(x for i, x in enumerate(nums) if sub >> i & 1)
```

The bit expression selects exactly the nodes contained in `sub`. If `s % 2` is one, the sum is odd and the subset cannot count, so the source skips connectivity work.

If the sum is even, the subset still has to pass the induced-connectivity condition.

**Using the complement mask as previsited nodes**

The source initializes

```text
vis = m ^ sub
```

Within the lowest $n$ bits, XOR with the all-ones mask flips every subset bit:

- selected nodes have bit 0 in `vis`, meaning unvisited and available;
- excluded nodes have bit 1, meaning already blocked.

This is a compact way to make one bitmask serve two roles. A 1 means either “not part of this induced subgraph” or “selected and already reached.” DFS only recurses to a neighbor whose bit is zero, so it can never enter an excluded node.

**Choosing a guaranteed selected start node**

For a nonzero mask `sub`,

```text
sub.bit_length() - 1
```

is the index of its highest set bit. That node certainly belongs to the subset, so it is a valid DFS starting point. Connectivity does not depend on which selected node starts the traversal.

The nested `dfs` marks its node with

$$
\texttt{vis}\mathrel{|}=1\ll u.
$$

It then scans every original neighbor $v$. Recursion occurs only when `vis` still has a zero at $v$. Because excluded vertices began with ones, every recursive call stays entirely within the selected set. The traversed edges are therefore exactly usable edges of the induced subgraph.

**Why \(vis == m\) means connected**

Before DFS, every excluded node bit is already one. During DFS, a selected node bit becomes one exactly when that node is reachable from the chosen selected start through selected nodes.

After traversal:

- if every selected node is reachable, all $n$ bits are one, so `vis == m`;
- if some selected node lies in another component, its bit remains zero, so `vis != m`.

Thus the equality test is precisely the connectedness test for the selected induced subgraph.

A singleton subset is connected by definition. DFS marks its only selected node; with all excluded bits already one, `vis` becomes `m`. It is counted exactly when that node's value is even, which for binary values means zero.

**Why the traversal tests an induced subgraph**

An induced subgraph retains every original edge whose endpoints are both selected. The source starts from the full adjacency lists and blocks every excluded vertex. Consequently:

- every traversed edge has two selected endpoints; and
- every original edge between selected endpoints is available to DFS.

It neither introduces an edge nor omits a usable selected-to-selected edge. Reachability in this restricted traversal is exactly reachability in the induced subgraph.

**Example**

For `nums = [1, 0, 1]` and path edges $0-1-2$:

- subset `010₂` selects node 1. Its sum is zero and DFS marks the singleton, so it counts;
- subset `101₂` selects nodes 0 and 2. Its sum is two, but excluded node 1 is premarked and DFS cannot cross through it, so the induced subgraph is disconnected and does not count;
- subset `111₂` has sum two, and DFS reaches all three nodes through the path, so it counts.

The answer is two.

## Complexity detail

Let $n$ be the number of nodes and $E$ the number of edges.

Building adjacency lists costs $O(n+E)$ time and space.

There are $2^n-1$ nonempty masks. Computing the selected value sum scans all $n$ nodes for every mask, costing

$$
O(n2^n)
$$

time.

For an even-sum mask, DFS may visit all selected nodes and scan their adjacency lists. In the worst case this is $O(n+E)$ work for one mask. When every node value is zero, every mask has even sum, so the worst-case total is

$$
O((n+E)2^n).
$$

For a dense graph, $E=\Theta(n^2)$, giving

$$
O(n^2 2^n)
$$

worst-case time. This is more accurate for the checked-in adjacency-list source than the manifest's $O(n2^n)$ claim. The smaller bound would require treating neighbor scanning differently or using bitmask adjacency operations that are not present here.

The graph lists store $2E$ neighbor entries and $n$ list headers, using

$$
O(n+E)
$$

space. DFS recursion reaches at most $n$ frames, while `sub` and `vis` are scalar bitmasks. Hence exact auxiliary space is $O(n+E)$, or $O(n^2)$ for a dense graph—not the manifest's $O(n)$ when adjacency storage is counted.

With $n\le13$, these worst-case factors remain bounded enough for enumeration.

## Alternatives and edge cases

- **Bitmask adjacency traversal:** Store each node's neighbors as an integer mask and expand a frontier with bit operations. This can avoid scanning excluded adjacency-list entries and better supports the manifest's $O(n2^n)$ characterization.
- **Enumerate connected subsets directly:** Frontier-based generation may skip disconnected masks but requires careful duplicate prevention and still has exponential worst-case behavior.
- **Disjoint-set rebuild per subset:** Unioning selected edges for every mask is more cumbersome and has similar or worse edge-scanning cost.
- **Empty subset:** It is excluded by starting enumeration at mask 1.
- **Singleton with value zero:** Its induced graph is connected and its sum is even, so it counts.
- **Singleton with value one:** It is connected but skipped because its sum is odd.
- **Disconnected original graph:** A subset can still count if all its selected nodes lie in and connect within one component.
- **Paths through excluded nodes:** They do not establish induced connectivity; premarking excluded bits prevents DFS from using them.
- **All zero values:** Every subset passes parity, exposing the worst-case connectivity-running time.
- **All one values:** Exactly even-cardinality subsets pass the parity filter, after which connectivity is still checked.
- **No edges:** Only zero-valued singleton subsets can count; every larger induced subgraph is disconnected.
- **Complete graph:** Every nonempty subset is connected, so counting reduces to even value-sum masks, but the source still scans adjacency lists.
- **Recursion safety:** DFS depth is at most 13 under the contract, far below Python's normal recursion limit.
- **Manifest mismatch:** Actual adjacency storage is $O(n+E)$ and dense-graph time is $O((n+E)2^n)$.
