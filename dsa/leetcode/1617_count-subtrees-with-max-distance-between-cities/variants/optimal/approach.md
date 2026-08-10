## General

**Enumerate every city subset**

With at most 15 cities, every subset can be represented by an $N$-bit mask and enumerated. Bit `u` is one when zero-based city `u` belongs to the candidate subtree.

Single-city subsets are skipped with:

`mask & (mask - 1) == 0`.

Such a mask has exactly one set bit. Its diameter is zero, while the output contains only distances one through $N-1$.

The remaining tasks for each mask are:

- determine whether the selected cities form a connected induced subtree;
- if connected, calculate their diameter.

**Build the original tree**

Input city labels are one-based. The source subtracts one from both endpoints and builds an undirected adjacency list `g`.

The original graph is a tree, so there is exactly one simple path between any two cities and no cycles. A selected subset is connected exactly when a traversal restricted to selected bits reaches all of them.

**How the restricted DFS marks visits**

`msk` is a mutable copy of the candidate mask. In `dfs(u,d)`, the statement:

`msk ^= 1 << u`

clears `u`’s bit because the function is called only when that bit is currently set. A cleared bit means the selected city has been visited.

For every neighbor `v`, recursion occurs only if `v`’s bit remains set. This both restricts traversal to the subset and prevents returning to an already visited parent.

Because the original graph is a tree, every selected reachable node is visited once. After DFS, `msk == 0` exactly when all selected cities were reachable from the starting city.

**Track a farthest city**

`mx` stores the greatest depth seen during the current DFS, and `nxt` stores a city attaining it. When `d` exceeds `mx`, both are updated.

The first start city is:

`cur = msk.bit_length() - 1`,

the index of the mask’s most significant set bit. Any selected city would work for connectivity and the first farthest search.

If the first DFS leaves nonzero bits, the subset is disconnected and is not a valid subtree. Its diameter is not counted.

**Why two DFS traversals give the diameter**

For a connected subset of a tree, the induced edges also form a tree. A standard tree property says a farthest vertex from any starting vertex is an endpoint of some diameter.

The first restricted DFS finds such a farthest city in `nxt`. The source then resets `msk = mask` and `mx = 0` and runs `dfs(nxt)`. The maximum distance reached from that endpoint is the subtree diameter.

It increments:

`ans[mx - 1] += 1`.

Index zero represents diameter one, so subtracting one maps distance $d$ to output position $d-1$.

**Why stale `nxt` is harmless**

`nxt` is initialized outside the mask loop and is not explicitly reset for every subset. For a connected subset with at least two cities, the first DFS reaches depth at least one, which is greater than reset `mx = 0` and therefore assigns `nxt` to a city in the current subset.

For a disconnected subset where the start component contains only one city, `nxt` might remain stale, but `msk != 0` makes the source skip the second DFS. It is never used incorrectly.

**A small example**

For the tree one-two-three with subset containing all three, start at some selected city. The first DFS reaches a farthest endpoint. The second DFS from that endpoint reaches the other endpoint at distance two, so `ans[1]` increases.

For subset `{1,3}` without city two, restricted DFS from one cannot reach three because the unique path uses an unselected city. A bit remains in `msk`, so this disconnected subset is rejected.

**Why all and only valid subtrees are counted**

Every subset with at least two cities is enumerated once. The first DFS accepts it exactly when all selected vertices are connected through selected vertices, which is the subtree definition.

For each accepted subset, the two-sweep tree property yields its exact maximum pairwise distance, and one corresponding output counter is incremented. Disconnected and singleton subsets contribute nowhere. Therefore, every output entry has the required count.

## Complexity detail

There are $2^N$ masks. A restricted DFS visits at most $N$ selected vertices and scans adjacency from those vertices. Since the original graph has $N-1$ edges, this is $O(N)$ per traversal. Connected masks perform two traversals; disconnected masks perform one.

Total time complexity is $O(2^N N)$.

The adjacency list uses $O(N)$ space for a tree, the recursive call stack can reach $O(N)$, and the answer has $N-1$ entries. Mask and scalar state are constant-size under the bounded-bit model. Auxiliary space is $O(N)$.

## Alternatives and edge cases

- **All-pairs distances plus subset connectivity:** Precompute distances and test every pair inside each connected mask. This can add an $O(N^2)$ factor per subset.
- **Floyd-Warshall:** It provides all distances in $O(N^3)$ but does not by itself establish that the selected induced subset is connected without outside vertices.
- **Enumerate edge subsets:** A tree has $N-1$ edges, but translating connected edge sets to unique vertex subtrees requires care. Vertex masks follow the definition directly.
- **Singleton subset:** It has diameter zero and is skipped because no output bucket represents zero.
- **Two adjacent cities:** Connected, diameter one, and counted in `ans[0]`.
- **Two nonadjacent cities without path vertices:** Disconnected as a selected subset and rejected.
- **Whole tree:** Always connected and counted under the original tree diameter.
- **Restricted path:** Traversal cannot pass through an unselected city, even if the original tree connects the endpoints through it.
- **XOR visit marking:** It is safe only because recursion enters vertices whose bits are known set. Applying XOR twice would restore a bit, which the neighbor guard prevents.
- **Farthest ties:** Any farthest city can serve as a diameter endpoint; strict `mx < d` keeps the first encountered tie.
- **One-based input:** Subtracting one is necessary before bit operations and adjacency indexing.
- **Recursive depth:** $N\le15$, so recursion is safely shallow.
- **Output offset:** Diameter $d$ increments index $d-1$, matching the one-indexed problem description.
