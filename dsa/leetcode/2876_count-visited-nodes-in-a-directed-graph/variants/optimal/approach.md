## General

**Recognize the functional-graph structure**

Every node has exactly one outgoing edge. Consequently, each weak component consists of one directed cycle with zero or more directed trees feeding into that cycle. A walk starting on a cycle visits exactly the cycle length. A walk starting outside a cycle visits its tail and then every node of the cycle it reaches.

**Peel away every tail**

Compute the indegree of each node and place every zero-indegree node in a queue. Repeatedly remove a queued node, record it in `removed_order`, decrease the indegree of its unique successor, and enqueue that successor if its indegree becomes zero.

No cycle node can be removed: inside a directed cycle, every node retains the incoming edge from its predecessor. Conversely, every non-cycle node is eventually removed because its component has a finite tail leading to a cycle. After the queue is exhausted, exactly the cycle nodes have positive indegree.

**Assign cycles, then restore tails backward**

For each unassigned node with positive indegree, follow edges until returning to that node. Those encountered nodes form one complete cycle, so assign their common cycle length to every one of them.

Process `removed_order` in reverse. The successor of each removed node is either a cycle node or a tail node whose answer has already been restored. Therefore

$$
\texttt{answer[node]} = 1 + \texttt{answer[edges[node]]}.
$$

Cycle counts are exact by construction, and the reverse recurrence adds precisely one distinct tail node at a time. Together these steps assign the correct visited-node count to every starting node.

## Complexity detail

Let $n = \lvert\texttt{edges}\rvert$. Building indegrees, pruning tails, traversing the disjoint cycles, and restoring removed nodes each process every node or edge only a constant number of times. The total running time is $O(n)$.

The indegree array, queue, removal order, cycle lists, and answer array contain at most $O(n)$ values, so auxiliary space is $O(n)$.

The benchmark uses $n$ as `size` and forms one cycle containing all nodes at sizes 16, 64, and 256. Every expected answer is $n$. The pruning method identifies and assigns the cycle in linear time. A correct baseline that starts a fresh walk with a new visited set from every node returns the same arrays but exhibits quadratic scaling.

## Alternatives and edge cases

- **Path memoization with local positions:** Following each unresolved path and detecting a cycle with a per-path index map also achieves $O(n)$ time and $O(n)$ space, but its cycle and resolved-suffix bookkeeping is more intricate.
- **Fresh traversal from every node:** Simulating each starting point independently is straightforward but takes $O(n^2)$ time on a long cycle or a long shared tail.
- **Recursive DFS:** Three-color DFS can distinguish active paths from resolved nodes, but a chain of length $10^5$ risks exceeding the language recursion limit.
- **Multiple components:** Each component owns exactly one cycle; cycle lengths must be computed independently.
- **Merging tails:** Different nodes may share a successor, and reverse propagation safely reuses that successor's already-known count.
- **No self-loops:** The source contract excludes `edges[i] == i`, although cycles of length two or more still require full handling.
- **Entire graph is one cycle:** The initial queue is empty, and every node immediately receives $n$.
