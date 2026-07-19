## General
**Record adjacency and node degrees**

Build a symmetric Boolean adjacency matrix so any potential edge can be tested in constant time. While reading each undirected edge, increment the degree of both endpoints.

**Enumerate every node triple once**

Choose indices satisfying `first < second < third`. This ordering covers each three-node set exactly once. Skip a pair immediately when `first` and `second` are not adjacent; otherwise the third node completes a connected trio precisely when it is adjacent to both.

**Convert node degrees into trio degree**

For a triangle with nodes $a$, $b$, and $c$, the sum

$$
\deg(a)+\deg(b)+\deg(c)
$$

counts every edge leaving the trio once. It also counts each of the triangle's three internal edges twice, once at each endpoint. Subtracting six removes these internal contributions, so the trio degree is

$$
\deg(a)+\deg(b)+\deg(c)-6.
$$

**Track the minimum and detect absence**

Minimize this value across every discovered triangle. The ordered enumeration cannot omit a trio, and the degree formula counts exactly its boundary edges, so the smallest recorded value is the requested minimum. If no candidate was recorded, the graph has no connected trio and the answer is `-1`.

## Complexity detail
Building degrees and adjacency takes $O(n^2+m)$ initialization and input time. The three ordered loops examine $O(n^3)$ triples with constant-time adjacency and degree work, so total time is $O(n^3)$. The adjacency matrix occupies $O(n^2)$ space, while degrees use $O(n)$.

## Alternatives and edge cases
- **Adjacency-set intersections:** For each edge, intersect the endpoints' neighbor sets to find common third nodes. This can be faster on sparse graphs but has representation-dependent bounds.
- **Count boundary edges separately per trio:** Scanning all outside nodes after finding every triangle is correct but increases worst-case time to $O(n^4)$.
- **Enumerate arbitrary edge triples:** Testing whether three selected edges form a triangle can cost $O(m^3)$ and repeats unnecessary combinations.
- **No triangle:** Return `-1`, even if the graph contains many paths or cycles of length greater than three.
- **Isolated triangle:** Its degree is zero, the smallest possible answer.
- **Complete graph:** Every triple is connected, and each has degree $3(n-3)$.
- **Shared triangle edges:** Different trios may overlap; each ordered node triple must still be evaluated independently.
- **Duplicate edges:** The contract excludes them, so degrees can be incremented directly without deduplication.
- **Disconnected graph:** Components without triangles do not affect a trio found elsewhere.
