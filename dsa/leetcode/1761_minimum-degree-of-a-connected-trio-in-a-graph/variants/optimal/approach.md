## General

**A connected trio is a triangle**

Three vertices form a connected trio exactly when all three undirected edges among them exist. In graph terminology, the trio is a triangle.

The exact solution needs two kinds of information:

- Whether a particular edge exists, answered by a Boolean adjacency matrix `g`.
- The total graph degree of each vertex, stored in `deg`.

It builds both structures in one pass over `edges`, then enumerates every ordered triple of distinct vertex indices in increasing order and tests whether it is a triangle.

**Convert labels and build an undirected matrix**

Input vertices are numbered from one through `n`, while Python list indices run from zero through `n - 1`. Each edge endpoint is reduced by one before indexing.

For edge `(u, v)`, the assignments:

`g[u][v] = g[v][u] = True`

record both directions. This symmetry is required because the graph is undirected. The source also increments `deg[u]` and `deg[v]`, since the edge contributes one to each endpoint's ordinary degree.

The input has no repeated edges and no self-loops, so each increment represents one distinct incident edge.

**Enumerate every three-vertex set once**

The loops choose:

- `i` from zero upward,
- `j` from `i + 1` upward,
- `k` from `j + 1` upward.

Thus every examined triple satisfies `i < j < k`. Any set of three distinct vertices has exactly one such increasing order, so no trio is omitted and none is counted in multiple permutations.

The source checks `g[i][j]` before entering the `k` loop. If that first required edge is absent, no triple containing this particular `i, j` pair can be a triangle, so it skips all candidate `k` values for that pair.

Inside, `g[i][k] and g[j][k]` check the other two required edges. All three Boolean entries being true is necessary and sufficient for a connected trio.

**Derive the trio's external degree**

For triangle vertices `i`, `j`, and `k`, the sum:

`deg[i] + deg[j] + deg[k]`

counts every edge incident to a trio vertex. Every external edge has exactly one endpoint inside, so it contributes once, exactly as desired.

The triangle itself has three internal edges: `i-j`, `i-k`, and `j-k`. Each internal edge contributes to the degree of both endpoints, so the degree sum counts each twice. The internal contribution is therefore:

$$
3\cdot 2=6.
$$

Subtracting six leaves exactly the number of edges with one endpoint in the trio and the other outside:

`deg[i] + deg[j] + deg[k] - 6`.

This formula avoids scanning all neighbors separately for every triangle.

**Track the smallest trio degree**

`ans` starts at positive infinity, a sentinel larger than every real trio degree. Whenever a triangle is found, the source applies its module-level two-argument `min` function to retain the smaller of the existing answer and the new degree.

The custom `min(a, b)` shadows Python's built-in name inside this module, but for these two numeric arguments it behaves exactly as needed: it returns `a` when `a < b` and otherwise `b`.

If no triangle is found, `ans` remains infinity and the method returns minus one. Otherwise it returns the minimum recorded external degree.

**Trace the first example**

Vertices one, two, and three have all three connecting edges, so their zero-based indices pass the matrix tests. Their degrees include two internal triangle edges each plus the external edges one-to-four, two-to-five, and three-to-six.

The degree sum therefore contains six internal incidences and three external ones. Subtracting six yields degree three, matching the example.

**Why the algorithm is correct**

The adjacency matrix exactly represents all input edges. The increasing loops enumerate every three-vertex set once, and the three matrix tests accept exactly triangles.

For each accepted triangle, the degree-sum formula removes precisely its six internal degree incidences and retains each outside edge once. Thus every candidate value is that trio's true degree.

Taking the minimum over all accepted triples returns the minimum connected-trio degree. If the accepted set is empty, returning minus one matches the required no-trio result.

## Complexity detail

Let $n$ be the number of vertices and $m$ the number of edges. Matrix allocation takes $O(n^2)$ time and space, and edge processing takes $O(m)$ time.

The nested loops examine $O(n^3)$ triples in the dense worst case, with constant-time adjacency lookups and arithmetic. Total time is $O(n^3+m+n^2)=O(n^3)$, matching the manifest.

The Boolean adjacency matrix dominates storage at $O(n^2)$. The degree list uses $O(n)$ and scalar loop state uses $O(1)$, so total auxiliary space is $O(n^2)$.

The guard on `g[i][j]` can skip many inner loops in sparse graphs, improving practical runtime, but does not change the dense worst-case bound.

## Alternatives and edge cases

- **Adjacency sets:** Intersect neighbor sets along edges to find triangles, often improving sparse-graph behavior while using $O(n+m)$ storage.
- **Check all six permutations:** It is redundant because increasing indices already enumerate each vertex set exactly once.
- **Scan external neighbors per trio:** It would add work; the degree-sum-minus-six formula is constant time.
- **No triangle:** Infinity remains unchanged and the method returns minus one.
- **Isolated-from-outside triangle:** Each trio vertex has degree two, so the expression gives zero.
- **Several trios:** Every increasing triple is considered, and only the smallest degree remains.
- **Shared edges between trios:** Each trio is evaluated independently from global degrees.
- **Complete graph:** Every triple is a trio; its external degree is $3(n-3)$.
- **Vertex-label conversion:** Subtracting one is essential before matrix indexing.
- **Undirected edge:** Both matrix directions and both degree increments must be recorded.
- **No repeated edges:** Degrees are not inflated by duplicate input rows.
- **Internal subtraction:** Six is fixed because a triangle has three edges counted twice, not because it has six distinct edges.
- **Custom min:** It accepts exactly the two arguments used by the source; calling it like the general built-in with an iterable would differ.
- **n below three:** The loops find no triple and return minus one naturally.
