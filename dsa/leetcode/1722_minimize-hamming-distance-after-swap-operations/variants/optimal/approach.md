## General
**Convert permitted swaps into components**

Treat indices as graph vertices and every allowed pair as an undirected edge. Repeated swaps along a path can move values between any two vertices in the same connected component, while no operation can move a value between different components. Use disjoint-set union with union by size and path compression to identify these components.

**Count the values available to each component**

For every source index, find its component representative and increment that component's counter for `source[index]`. These counters describe exactly the multiset of values that can be assigned among the component's positions; the order in which swaps realize a permutation does not matter.

**Consume target requests component by component**

Scan target positions. If the position's component still has an unused copy of `target[index]`, consume one and match that position. Otherwise, no value from another component can be imported, so this position must contribute one mismatch. Greedy consumption is correct because equal values are interchangeable, and only their multiplicity within the same component affects how many requests can be satisfied.

## Complexity detail
Disjoint-set operations over $n$ indices and $m$ swap edges take $O((n+m)\alpha(n))$ amortized time, where $\alpha$ is the inverse Ackermann function. Building and consuming all component counters adds $O(n)$ expected time. Parent, size, and frequency structures use $O(n)$ space.

## Alternatives and edge cases
- **Depth-first component traversal:** Building adjacency lists and visiting every component once gives $O(n+m)$ traversal plus the same frequency accounting, with $O(n+m)$ graph storage.
- **Sort values within components:** Sorting each component's source and target values also reveals unmatched multiplicities but raises the bound to $O(n\log n)$ in the largest component.
- **Rediscover a component per position:** Repeating DFS or BFS for every target index is correct when matches are consumed carefully, but can take $O(n(n+m))$ time.
- **No allowed swaps:** Every index is its own component, so the answer is the ordinary Hamming distance.
- **Duplicate values:** Counters must preserve multiplicity; a set would incorrectly reuse one available copy.
- **Redundant edges and cycles:** Union-find safely ignores unions between indices already in the same component.
- **Equal global multisets:** A zero answer still requires each needed value to occur in the correct connected component, not merely somewhere in `source`.
