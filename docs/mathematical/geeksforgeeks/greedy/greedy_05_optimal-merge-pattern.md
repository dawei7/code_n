# Formal Mathematical Specification: Optimal Merge Pattern

## 1. Definitions and Notation

Let $S = \{s_1, s_2, \dots, s_n\}$ be a multiset of $n$ positive integers, where each $s_i \in \mathbb{Z}^+$ represents the size of a file. 

We define the state of the system at any time $t$ as a multiset $\mathcal{M}_t$. Initially, $\mathcal{M}_0 = S$. A merge operation $\phi$ on two elements $a, b \in \mathcal{M}_t$ produces a new multiset $\mathcal{M}_{t+1} = (\mathcal{M}_t \setminus \{a, b\}) \cup \{a + b\}$. The cost of this operation is defined by the function $c(\phi) = a + b$.

The objective is to reach a terminal state $\mathcal{M}_{n-1} = \{\sum_{i=1}^n s_i\}$ through a sequence of $n-1$ merge operations $\Phi = (\phi_1, \phi_2, \dots, \phi_{n-1})$. The total cost $C(\Phi)$ is the sum of the costs of individual operations:
$$C(\Phi) = \sum_{j=1}^{n-1} c(\phi_j)$$

## 2. Algebraic Characterization

The problem is isomorphic to constructing a binary tree where the leaves are the elements of $S$. Let $T$ be a binary tree with $n$ leaves, where each leaf $l_i$ corresponds to an element $s_i \in S$. Let $d_i$ denote the depth of leaf $l_i$ (the number of edges on the path from the root to the leaf).

The total cost of merging is given by the weighted path length of the tree:
$$C(T) = \sum_{i=1}^n s_i \cdot d_i$$

**Theorem (Greedy Optimality):** To minimize $C(T)$, we must minimize the depth $d_i$ for the largest values of $s_i$. This is achieved by the Huffman coding construction, which satisfies the following recurrence for the minimum cost $f(\mathcal{M})$:
$$f(\mathcal{M}) = \min_{a, b \in \mathcal{M}} \{ (a + b) + f((\mathcal{M} \setminus \{a, b\}) \cup \{a + b\}) \}$$
where the base case is $f(\{x\}) = 0$.

**Loop Invariant:** At the start of each iteration of the algorithm, the total cost accumulated is the sum of all internal nodes of the binary tree constructed thus far, and the priority queue contains the roots of the subtrees formed by the elements of the current multiset $\mathcal{M}_t$.

## 3. Complexity Analysis

### Time Complexity
The algorithm utilizes a Min-Heap (priority queue) to maintain the multiset $\mathcal{M}_t$.

1. **Initialization:** Constructing the heap from $n$ elements using `heapify` takes $T_{init} = O(n)$.
2. **Iteration:** The algorithm performs $n-1$ iterations. In each iteration:
   - Two `heappop` operations are performed: $2 \times O(\log n)$.
   - One `heappush` operation is performed: $1 \times O(\log n)$.
   - The total work per iteration is $O(\log n)$.
3. **Total Time:**
   $$T(n) = O(n) + \sum_{i=1}^{n-1} O(\log n) = O(n) + O(n \log n) = O(n \log n)$$
Thus, the time complexity is $\Theta(n \log n)$.

### Space Complexity
1. **Auxiliary Space:** The Min-Heap stores exactly $n$ elements at the start. During the merge process, the number of elements in the heap decreases by 1 in each step. The maximum space required is $O(n)$ to store the elements of the multiset $\mathcal{M}_t$.
2. **Total Space:** Since the algorithm operates on the multiset of size $n$, the space complexity is $\Theta(n)$. If the input array is modified in-place, the auxiliary space remains $O(n)$ due to the heap structure requirements, though the input storage is reused.