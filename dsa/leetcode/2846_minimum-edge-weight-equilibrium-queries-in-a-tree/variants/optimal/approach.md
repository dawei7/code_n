## General

**Turn one path query into length minus its most common weight.** A tree has exactly one path between two nodes. Suppose that path contains $L$ edges, and weight $w$ occurs $c_w$ times.

If every edge is changed to weight $w$, the existing $c_w$ edges can stay and the other $L-c_w$ edges require one operation each. The best final weight is therefore the most frequent one, and the minimum operations are

$$
L-\max_w c_w.
$$

The problem reduces to finding the path length and all 26 path-weight frequencies quickly.

**Root the tree and record prefix information.** The source roots the tree at node zero. Adjacency list `g` stores both directions, converting weights one through 26 into indices zero through 25.

A breadth-first traversal computes for every node:

- `p[node]`, its direct parent.
- `depth[node]`, the number of edges from the root.
- `cnt[node][w]`, the number of weight-$w$ edges on the root-to-node path.
- `f[node][j]`, the ancestor $2^j$ edges above the node.

Root `cnt[0]` is 26 zeros. When visiting child `j` through edge weight `w`, the source copies the parent's frequency vector, increments bucket `w`, sets depth one larger, and enqueues the child.

Copying is necessary. If parent and child shared the same list, incrementing the child's edge would corrupt every related root path.

**Build binary ancestors during BFS.** For current node `i`, `f[i][0] = p[i]`. A $2^j$ ancestor is reached by taking two $2^{j-1}$ jumps:

`f[i][j] = f[f[i][j - 1]][j - 1]`.

The number of columns is `n.bit_length()`, enough to represent every possible tree depth.

The root's parent is itself because arrays begin with zero. Its ancestor table therefore remains zero at every level, providing a safe sentinel for lifting.

**Find the lowest common ancestor for each query.** For original query nodes `u` and `v`, working variables `x` and `y` begin at those nodes.

First, the deeper node is assigned to `x`. Scanning jump sizes from largest to smallest, whenever its depth exceeds `y`'s by at least $2^j$, `x` moves to `f[x][j]`. After this phase, both nodes have equal depth.

Next, the source again scans from large jumps down. If the $2^j$ ancestors of `x` and `y` differ, both nodes move upward by that jump. This keeps them below their common ancestor while advancing as far as possible.

After the scan, either `x == y` and that node already is the lowest common ancestor, or they are distinct children below it. In the latter case, `x = p[x]` moves once to the LCA.

**Extract path frequencies by prefix subtraction.** Let $a$ be the LCA. The root-to-`u` vector contains root-to-$a$ plus the $a$-to-`u` path. The same holds for `v`. Therefore, for weight bucket `j`,

$$
c_j=
\texttt{cnt}[u][j]+\texttt{cnt}[v][j]-2\texttt{cnt}[a][j].
$$

The two copies of the root-to-LCA prefix are removed, leaving exactly the unique `u`-to-`v` path edges. Taking the maximum over all 26 buckets gives `mx`.

**Compute path length.** The number of edges from `u` to `v` is

$$
\texttt{depth}[u]+\texttt{depth}[v]-2\texttt{depth}[a].
$$

Subtracting `mx` returns the minimum number of edges whose weights must change.

**Why queries remain independent.** No edge is changed in the stored tree. The method only calculates how many changes an isolated query would need. Every query uses the same original parent, depth, and frequency data.
BFS builds exact root-path frequency vectors and depths by extending correct parent information through one edge. Binary lifting returns the true LCA. Prefix-vector subtraction yields exact path weight counts. Keeping the most frequent weight minimizes changes because every other edge changes once and no operation can fix two edges. Thus every appended answer is optimal.

**Same-node query.** When `u == v`, the LCA is that node, path length is zero, every path frequency is zero, and `max` returns zero. The answer is zero.

## Complexity detail

Let $N$ be the number of nodes, $Q$ the number of queries, and $L=\lceil\log_2 N\rceil$.

Building adjacency lists is $O(N)$. BFS fills $L$ ancestors for each node, taking $O(NL)$. Copying and updating 26 frequency entries per child is $O(26N)=O(N)$ because 26 is fixed.

Each query uses two descending ancestor scans of $L$ positions plus a scan of 26 weights. Time per query is $O(L+26)=O(\log N)$. Total time is

$$
O((N+Q)\log N).
$$

The ancestor table uses $O(N\log N)$ space. Adjacency, parent, depth, and 26-entry frequency vectors use $O(N)$ additional space. Total auxiliary space is $O(N\log N)$.

The answer list contains $Q$ integers as required output.

## Alternatives and edge cases

- **Offline Tarjan LCA:** Queries can be answered with union-find during DFS, but path-frequency aggregation still needs careful prefix data and the implementation is more complex.
- **Heavy-light decomposition:** Split paths into logarithmically many chains and query segment data. It supports updates better, but queries here are static and root prefixes are simpler.
- **Walk each query path:** Parent traversal could take $O(N)$ per query and is too slow for twenty thousand queries.
- **All path weights equal:** The maximum frequency equals path length, so zero operations are needed.
- **Every path weight different:** The most common frequency is one for a nonempty path, so all but one edge must change.
- **One node is ancestor of the other:** Depth leveling makes both working nodes equal at the ancestor, and the second lifting phase changes nothing.
- **Same endpoint:** Empty path length and frequency are zero.
- **Weight index conversion:** Subtracting one maps source weights one through 26 to array positions zero through 25.
- **Copied frequency vectors:** Sharing them would corrupt prefix counts; `cnt[i][:]` is essential.
- **Root parent:** Self-parenting keeps oversized ancestor jumps within valid array indices.
- **Independent queries:** No mutation occurs during answering.
