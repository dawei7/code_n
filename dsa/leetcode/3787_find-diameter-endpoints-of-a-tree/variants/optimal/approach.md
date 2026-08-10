## General

**Find one diameter before finding all endpoints**

A standard tree property says that a farthest node from any starting node is an endpoint of some diameter.

The source runs `bfs(0)` and calls the returned farthest node `a`. It then runs `bfs(a)`; the farthest node `b` forms a diameter endpoint pair with `a`. The distance

`d = dist1[b]`

is the tree's diameter length.

This identifies one diameter $(a,b)$, but the problem asks for endpoints of every possible diameter. A third BFS supplies the information needed to mark all of them.

**Understand what one BFS returns**

`bfs(start)` initializes every distance to `-1`, assigns zero to `start`, and explores with a queue.

In an unweighted tree, BFS reaches nodes in nondecreasing edge distance. Each unvisited neighbor receives `dist[u]+1`. Since a tree has one simple path between two nodes, that value is the exact path length.

`far` tracks any node with the greatest distance encountered so far. Ties need no special handling: any farthest node is sufficient for the diameter procedure.

**Measure from both fixed diameter endpoints**

The second BFS stores all distances from `a` in `dist1` and returns `b`. The third BFS starts at `b` and stores all distances in `dist2`.

For every node `i`, the source marks it special when

`dist1[i] == d or dist2[i] == d`.

In words, a node is special if it is diameter distance away from at least one endpoint of the fixed diameter.

**Why every marked node is special**

If `dist1[i] == d`, the path from `a` to `i` has the maximum possible tree distance $d$. It is therefore a diameter, and `i` is one of its endpoints.

The same argument applies when `dist2[i] == d`: path $(b,i)$ is a diameter. Thus the test never marks an invalid node.

**Why every special node is found**

For endpoints `a,b` of a fixed tree diameter, a fundamental tree identity is

$$
\operatorname{ecc}(x)
=
\max\bigl(\operatorname{dist}(x,a),\operatorname{dist}(x,b)\bigr),
$$

where $\operatorname{ecc}(x)$ is the greatest distance from `x` to any node.

Intuitively, project `x` and any other node `y` onto the unique path from `a` to `b`. The diameter path already extends as far as possible in both directions. Whichever endpoint lies opposite `x`'s attachment direction is at least as far from `x` as `y` can be. Branches cannot extend farther without creating a path longer than the diameter.

A node `x` is an endpoint of some diameter exactly when its eccentricity equals the diameter length $d$: then a farthest node from `x` is distance $d$ away.

Using the identity, this happens exactly when

$$
\max(\texttt{dist1}[x],\texttt{dist2}[x])=d.
$$

No distance can exceed $d$, so the maximum equals $d$ precisely when at least one of the two stored distances equals $d$. This is the source's marking condition.

**Trace the multi-diameter example**

In the seven-node example, one BFS may choose node zero as `a` and node four as `b`, with diameter length four.

Node five is also distance four from node zero, so `dist1[5]==d` and it is marked. Node six is distance four from node four, so `dist2[6]==d` and it is marked.

Together with endpoints zero and four, the result marks all four nodes `0,4,5,6` even though only one fixed diameter was selected initially.

**Build the binary result**

`ans` starts with `"0"` at every node. The loop changes positions satisfying the distance test to `"1"`. Joining the character list produces an $N$-character string whose positions preserve node numbering.

The approach finds endpoint membership only. It does not need to enumerate the possibly quadratic number of diameter paths.

## Complexity detail

Building the adjacency list takes $O(N)$ time and space because a tree has $N-1$ edges.

Each BFS visits every node and both directions of every edge once, taking $O(N)$ time and $O(N)$ queue/distance space. Three BFS runs remain $O(N)$ total time. Constructing and joining the answer also costs $O(N)$.

The adjacency list, two retained distance arrays, temporary BFS data, queue, and answer use $O(N)$ space.

## Alternatives and edge cases

- **Compute all-pairs distances:** This costs $O(N^2)$ time and space, unnecessary for endpoint membership.
- **Mark only `a` and `b`:** A tree may have many diameter paths with additional endpoints.
- **Use distance from one endpoint only:** It finds endpoints opposite that side but can miss alternatives on the same side as that endpoint; both arrays are required.
- **Mark nodes whose two distances sum to `d`:** That identifies nodes lying on the chosen diameter path, not endpoints of any diameter.
- **Use DFS instead of BFS:** On an unweighted tree, either traversal can compute distances, but the exact source uses BFS.
- **Tie for farthest node:** Any tied farthest choice is a valid starting diameter endpoint.
- **Two-node tree:** Both nodes are distance one from the other and both are marked.
- **Path-shaped tree:** Only its two leaves are diameter endpoints.
- **Star-shaped tree:** Every leaf is an endpoint of a leaf-to-leaf diameter; the center is not.
- **Multiple deepest branches:** Distances to the fixed endpoints reveal all peripheral branch leaves.
- **Internal node:** Its eccentricity is smaller than `d`, so neither stored distance reaches `d`.
- **Valid-tree guarantee:** Unique paths and the two-sweep diameter property depend on connected acyclic input.
- **Iterative BFS:** Queue traversal avoids recursion-limit concerns.
- **Output indexing:** Each character directly corresponds to the same numbered node.
