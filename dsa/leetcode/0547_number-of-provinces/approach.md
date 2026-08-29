## General

The matrix describes an undirected graph:

- each city is a vertex;
- `isConnected[i][j] == 1` means an edge directly connects cities `i` and `j`.

A province is exactly a connected component of this graph. The solution counts how many depth-first searches are needed to visit every city.

Array `vis` records whether each city has already been assigned to a discovered province. It begins false for all `n` cities.

The outer loop considers every city index `i`. If `vis[i]` is already true, that city was reached from an earlier component start and belongs to a province already counted.

If `vis[i]` is false, no previously explored city connects to it directly or indirectly. It begins a new province. The method calls `dfs(i)` and increments `ans` once.

**What one DFS accomplishes.** The helper first sets `vis[i] = True`. Marking before exploring neighbors prevents a cycle from recursing back into the same city.

It then scans row `isConnected[i]`. At column `j`, value `x` says whether the current city `i` directly connects to city `j`.

If `x` is one and `vis[j]` is false, DFS recursively visits `j`. That recursive call repeats the process for all of `j`'s neighbors, so the traversal follows paths of any length, not only direct connections from the starting city.

The diagonal entry `isConnected[i][i]` is one, but city `i` has already been marked before the row scan. The `not vis[j]` condition prevents self-recursion.

Because the matrix is symmetric, every edge appears in both directions. Visited marking ensures those duplicate representations do not cause duplicate traversal.

For:

`[[1,1,0],[1,1,0],[0,0,1]]`,

the outer loop starts DFS at city zero. It reaches city one, marking both as one component. City one is skipped by the outer loop. City two remains unvisited, so a second DFS starts there and the answer becomes two.

For an identity matrix, each city connects only to itself. Every outer-loop city is still unvisited when reached, so each begins its own province and the answer is `n`.

**Why one DFS does not leave part of its province unvisited.** If another city belongs to the same province, a path of direct connections leads from the starting city to it. DFS follows every unvisited edge at each path step, so induction along that path shows the city is eventually marked.

**Why one DFS cannot cross into another province.** Recursion moves only along matrix entries equal to one. Any reached city therefore has a direct path back through the recursive call chain to the start. By definition it belongs to the same connected component.

**Why counting starts is correct.** The first unvisited city of every province launches exactly one DFS, and that DFS marks the entire province. All later cities in it are skipped. Different provinces cannot mark one another. Thus `ans` increases once per province and only once.

The algorithm never modifies `isConnected`. The separate visited array keeps graph data and traversal state distinct.

Recursion order has no effect on the count. Scanning neighbors from zero upward simply chooses a deterministic traversal order.

It is useful to distinguish a city being *considered* from it being *discovered*. The outer loop considers every index, but only an unvisited index discovers a new component. Inside DFS, the same city may appear as a neighbor in many matrix rows; the visited flag turns all appearances after the first into constant-time skips. This is why a densely connected province still increases the answer only once.

The method also does not assume connections must pass through lower-numbered cities. A province can be discovered from whichever member appears first in the outer loop, and recursive edges may move to smaller or larger indices freely. Component membership is structural, not based on city numbering.

## Complexity detail

Let $n$ be the number of cities. Every city is marked once, but processing a city scans its complete matrix row of length $n$. Across all cities, time is $O(n^2)$, matching the manifest.

The visited array uses $O(n)$ space. The recursion stack can contain up to $O(n)$ cities along a path, so total auxiliary space is $O(n)$.

The dense matrix input itself occupies $O(n^2)$ but is not auxiliary storage created by the method.

Even though each city becomes visited once, the time is not merely $O(n)$ because its complete row must be inspected to find which of the $n$ possible neighbors are connected. An adjacency-list representation would make traversal $O(n+e)$, but the supplied matrix requires examining $n^2$ entries.

## Alternatives and edge cases

- **Breadth-first search:** A queue can mark one component at a time with the same $O(n^2)$ time and $O(n)$ space.
- **Union-find:** Union every connected pair and count roots. It is useful for edge streams but still scans this full matrix.
- **Count direct neighbor groups only:** Direct adjacency is not enough; indirect paths must merge cities into one province.
- **Single city:** One unvisited start launches DFS and returns one province.
- **Identity matrix:** Every city is isolated, so the result is `n`.
- **Fully connected matrix:** The first DFS marks all cities and the result is one.
- **Self-connections:** Diagonal ones are harmless because the current city is marked first.
- **Symmetric duplicate edges:** Visited checks prevent repeated recursive work.
- **Long chain of cities:** Indirect connectivity makes the entire chain one province.
- **Recursion depth:** With up to 200 cities, the call depth is bounded and modest; an explicit stack is an easy substitute.
- **Input immutability:** Connectivity entries remain unchanged.
