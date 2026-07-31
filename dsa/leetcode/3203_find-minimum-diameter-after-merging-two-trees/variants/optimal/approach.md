## General

**Measure each original diameter in linear time**

In a tree, start a breadth-first search from any node. A farthest reached node is an endpoint of some diameter. A second search from that endpoint reaches the opposite endpoint, and its distance is the tree diameter. Apply these two searches independently to both trees, obtaining diameters $d_1$ and $d_2$.

This also handles a one-node tree: its adjacency list contains one empty list, both searches remain at node `0`, and its diameter is zero.

**Connect centers to minimize the cross-tree path**

The radius of a tree with diameter $d$ is

$$
\left\lceil\frac{d}{2}\right\rceil.
$$

A center is a node whose maximum distance to any node equals that radius. If the new edge joins chosen nodes $u$ and $v$, the longest path that uses it has length

$$
\operatorname{ecc}_1(u)+1+\operatorname{ecc}_2(v),
$$

where each eccentricity is the farthest distance from the chosen endpoint inside its original tree. No choice can make an eccentricity smaller than the corresponding radius, and choosing centers attains both radii. Therefore the smallest possible cross-tree contribution is

$$
\left\lceil\frac{d_1}{2}\right\rceil
+1+
\left\lceil\frac{d_2}{2}\right\rceil.
$$

Adding the edge does not shorten paths lying entirely inside either original tree, so the merged diameter cannot be below $d_1$ or $d_2$. Connecting centers attains the maximum of exactly these three unavoidable quantities. The answer is therefore

$$
\max\left(d_1,d_2,
\left\lceil\frac{d_1}{2}\right\rceil+
\left\lceil\frac{d_2}{2}\right\rceil+1\right).
$$

## Complexity detail

Building both adjacency lists and running two breadth-first searches per tree touches every node and edge a constant number of times. With $N=n+m$, time complexity is $O(N)$ and the adjacency lists plus queues use $O(N)$ auxiliary space.

The implementation stores `(node, parent, distance)` in the queue, avoiding a separate visited set because each input graph is guaranteed to be a tree.

## Alternatives and edge cases

- **Search from every node:** Computing all eccentricities finds centers and diameters directly, but repeated tree traversals take $O(n^2+m^2)$ time.
- **Tree dynamic programming:** A postorder and rerooting pass can compute diameters or eccentricities in linear time, but two endpoint searches are simpler for unweighted trees.
- **Connect arbitrary diameter endpoints:** This can maximize rather than minimize the new cross-tree path; centers are the optimal endpoints.
- **Two singleton trees:** Each original diameter is zero, and the required connecting edge gives diameter one.
- **One singleton tree:** Its radius is zero, so attach it to a center of the other tree.
- **Odd diameter:** A tree has two adjacent centers, and either center has radius $(d+1)/2$.
- **Even diameter:** The unique center lies halfway along every diameter path.
- **Dominating original tree:** A very large original diameter may remain the merged diameter even after the best connection.
- **Node labels:** The two trees have independent namespaces; equal numeric labels across `edges1` and `edges2` do not identify the same node.
