# Formal Mathematical Specification: Level-order Traversal

## 1. Definitions and Notation
Let $d(v)$ be the depth of node $v \in V$, defined as the number of edges from the root to $v$.
We partition $V$ into disjoint subsets $L_k = \{ v \in V \mid d(v) = k \}$ for $0 \leq k \leq \mathcal{H}(T)$.

## 2. Objective
Output the sequence of sets $(L_0, L_1, \dots, L_{\mathcal{H}(T)})$, where within each set $L_k$, elements are ordered by their relative left-to-right position in the geometric embedding of $T$.

## 3. Algorithm Formalization (BFS)
Let $Q$ be a FIFO queue.
1. Initialize $Q \leftarrow [r]$.
2. For $k = 0, 1, \dots$:
   - Let $S_k$ be the sequence of elements currently in $Q$.
   - Empty $Q$ and enqueue all children of elements in $S_k$ sequentially from left to right.
   - If $Q$ is empty, terminate.

## 4. Complexity Analysis
- **Time Complexity:** Each node is enqueued and dequeued exactly once. $O(|V|)$.
- **Space Complexity:** The maximum size of $Q$ is bounded by $\max_k |L_k|$. In the worst case (a perfectly balanced tree), the last level contains exactly $(|V|+1)/2$ nodes, yielding a space complexity of $O(|V|)$.
