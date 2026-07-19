## General
**Interpret the matrix as an undirected graph**

Each city is a vertex, and every entry equal to one is an edge. A province is exactly a connected component of this graph; indirect paths matter even when two cities have a zero in their matrix entry.

**Start one traversal per unseen component**

Scan cities in index order. When a city has not been visited, increment the province count and start a depth-first traversal from it. Mark a city as soon as it is pushed so no connection can schedule it repeatedly.

**Discover neighbors from the current row**

Popping city `i` exposes row `isConnected[i]`. Every connected, unvisited index in that row belongs to the same province and is added to the stack. When the stack empties, every city reachable from the start has been marked.

**Why the number of starts is the number of provinces**

A traversal follows every direct edge from every reached city, so it marks the entire connected component of its start and cannot cross into another component. Later scan positions inside that component are already marked and create no new count. Conversely, the first scanned city of every component is unvisited and creates exactly one count, giving a one-to-one correspondence between traversal starts and provinces.

## Complexity detail
For each of the `n` cities, its matrix row of length `n` is scanned once, so time is $O(n^2)$. The visited array and explicit traversal stack each use $O(n)$ space.

## Alternatives and edge cases
- **Breadth-first search:** replacing the stack with a queue gives the same $O(n^2)$ time and $O(n)$ space.
- **Disjoint-set union:** unioning connected pairs also works in $O(n^2 \alpha(n))$ time and $O(n)$ space, with more machinery than direct traversal.
- **Transitive closure:** Floyd-Warshall can derive all reachability information but costs $O(n^3)$ time and $O(n^2)$ extra space.
- **Isolated city:** its diagonal entry still forms a one-city province.
- **Indirect connection:** cities in the same province need not have a direct matrix edge.
- **Symmetric entries:** each undirected edge appears twice, but the visited check prevents duplicate traversal.
- **Single city:** starts one traversal and yields one province.
