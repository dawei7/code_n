# Formal Mathematical Specification: Kth Smallest Element in a Sorted Matrix

## 1. Definitions and Notation

Let $M$ be an $N \times N$ matrix where $M_{i,j} \in \mathbb{R}$ for $0 \le i, j < N$. The matrix satisfies the monotonicity property:
1. $\forall i, j_1 < j_2: M_{i, j_1} \le M_{i, j_2}$ (Row-wise sorted)
2. $\forall j, i_1 < i_2: M_{i_1, j} \le M_{i_2, j}$ (Column-wise sorted)

We define the set of all elements in the matrix as $\mathcal{M} = \{M_{i,j} \mid 0 \le i, j < N\}$. Let $f: \{1, \dots, N^2\} \to \mathcal{M}$ be a bijection such that $f(1) \le f(2) \le \dots \le f(N^2)$. Our objective is to determine the value $f(K)$ for a given $K \in \{1, \dots, N^2\}$.

We define a state space $\mathcal{S} \subseteq \{0, \dots, N-1\}^2$ representing the indices of elements currently under consideration for the heap. A priority queue $\mathcal{H}$ stores tuples $(M_{i,j}, i, j)$, ordered by the value $M_{i,j}$.

## 2. Algebraic Characterization

The algorithm relies on the property that the $K$-th smallest element is the result of a $K$-step extraction from a set of $N$ sorted sequences (the rows). 

### Heap Invariant
Let $\mathcal{P}_k$ be the set of elements popped from the heap after $k$ iterations. Let $\mathcal{C}_k$ be the set of "candidate" elements currently in the heap. The following invariant holds:
1. $\forall (v, i, j) \in \mathcal{C}_k$, if $j > 0$, then $M_{i, j-1} \in \mathcal{P}_k$.
2. $\forall (v, i, j) \in \mathcal{C}_k$, if $i > 0$, then $M_{i-1, j} \in \mathcal{P}_k$.

This ensures that for any element $M_{i,j}$ to be added to the heap, all its predecessors in the partial order defined by the matrix indices must have been processed.

### Transition Function
Let $H_k$ be the heap at step $k$. The transition from $H_k$ to $H_{k+1}$ is defined by:
1. Extract minimum: $(v^*, r, c) = \text{argmin}_{(v, i, j) \in H_k} \{v\}$.
2. Successor generation: Define the set of potential successors $\mathcal{N}(r, c) = \{(r+1, c), (r, c+1)\}$.
3. Update: $H_{k+1} = (H_k \setminus \{(v^*, r, c)\}) \cup \{(M_{r', c'}, r', c') \mid (r', c') \in \mathcal{N}(r, c) \land r', c' < N \land (r', c') \notin \mathcal{P}_{k+1}\}$.

The algorithm terminates at $k=K$, where the result is $v^*$.

## 3. Complexity Analysis

### Time Complexity
The algorithm performs $K$ iterations. In each iteration:
1. **Extraction:** $\text{heappop}$ takes $O(\log |\mathcal{H}|)$. Since $|\mathcal{H}| \le N$, this is $O(\log N)$.
2. **Insertion:** At most two $\text{heappush}$ operations are performed, each taking $O(\log N)$.

The total time complexity is given by the summation:
$$T(K, N) = \sum_{k=1}^{K} O(\log (\min(k, N))) = O(K \log (\min(K, N)))$$
Given that $K \le N^2$, this is bounded by $O(K \log N)$.

### Space Complexity
The space complexity is dominated by the storage of the heap $\mathcal{H}$ and the set of visited indices $\mathcal{V}$.
1. **Heap:** The heap contains at most $\min(K, N)$ elements at any time, as we only add elements from the first column initially and expand row-wise.
2. **Visited Set:** To prevent redundant insertions, we maintain a set of visited indices $(i, j)$, which requires $O(K)$ space in the worst case.

Thus, the total auxiliary space complexity is $O(\min(K, N^2))$, which simplifies to $O(K)$ for $K < N^2$ and $O(N^2)$ in the limit. If we utilize the property that we only need to track the current column index for each row, this can be optimized to $O(N)$.