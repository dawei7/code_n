# Formal Mathematical Specification: Build Max Heap (Heapify)

## 1. Definitions and Notation

Let $A = [a_0, a_1, \dots, a_{n-1}]$ be an array of $n$ elements drawn from a totally ordered set $(\mathcal{X}, \leq)$. We define the structure as a complete binary tree $T$ mapped to the array indices $I = \{0, 1, \dots, n-1\}$.

*   **Parent-Child Mapping:** For any index $i \in I$, the left child $L(i)$ and right child $R(i)$ are defined as:
    $L(i) = 2i + 1$
    $R(i) = 2i + 2$
    provided $L(i), R(i) < n$.
*   **Max-Heap Property:** A sequence $A$ satisfies the Max-Heap property if and only if for all $i$ such that $0 \leq i < \lfloor n/2 \rfloor$:
    $a_i \geq a_{L(i)}$ (if $L(i) < n$)
    $a_i \geq a_{R(i)}$ (if $R(i) < n$)
*   **State Space:** The algorithm operates on the space of all permutations of the input array, $\mathcal{S} = \text{Perm}(A)$. The goal is to reach a state $A^* \in \mathcal{S}$ such that $A^*$ satisfies the Max-Heap property.

## 2. Algebraic Characterization

The algorithm utilizes the `sift_down` procedure, denoted as $\text{SD}(i, n)$, which restores the heap property for a subtree rooted at $i$, assuming the subtrees rooted at $L(i)$ and $R(i)$ are already valid Max-Heaps.

**Loop Invariant:**
For the main loop iterating $k$ from $\lfloor n/2 \rfloor - 1$ down to $0$:
At the start of each iteration $k$, the subarray $A[k+1 \dots n-1]$ forms a forest of valid Max-Heaps. Specifically, for all $j > k$, the subtree rooted at $j$ satisfies the Max-Heap property.

**Recursive Definition of `sift_down`:**
Let $m$ be the index of the largest element in the set $\{i, L(i), R(i)\} \cap I$.
If $m \neq i$:
1. Swap $a_i$ and $a_m$.
2. $\text{SD}(m, n)$ is called recursively.
If $m = i$, the property is satisfied for index $i$, and the recursion terminates.

**Correctness:**
By induction on $k$, since the base case $k = \lfloor n/2 \rfloor - 1$ starts with all nodes $j > k$ being leaves (which trivially satisfy the property), and each $\text{SD}(k, n)$ preserves the property for the subtree rooted at $k$, the final state at $k=0$ ensures the entire tree is a Max-Heap.

## 3. Complexity Analysis

### Time Complexity
The time complexity is determined by the sum of the costs of $\text{SD}(i, n)$ for all $i$ from $\lfloor n/2 \rfloor - 1$ down to $0$. 
Let $h$ be the height of the tree, $h = \lfloor \log_2 n \rfloor$. A node at height $d$ (where leaves are at $d=0$) can perform at most $d$ swaps. 

The number of nodes at height $d$ is at most $\lceil n / 2^{d+1} \rceil$. The total work $W(n)$ is:
$$W(n) = \sum_{d=0}^{\lfloor \log_2 n \rfloor} \lceil \frac{n}{2^{d+1}} \rceil \cdot O(d)$$
$$W(n) = O\left( n \sum_{d=0}^{\infty} \frac{d}{2^d} \right)$$

Using the arithmetico-geometric series identity $\sum_{d=0}^{\infty} d x^d = \frac{x}{(1-x)^2}$ for $|x| < 1$, with $x = 1/2$:
$$\sum_{d=0}^{\infty} \frac{d}{2^d} = \frac{1/2}{(1 - 1/2)^2} = \frac{1/2}{1/4} = 2$$
Thus, $W(n) = O(2n) = O(n)$.

### Space Complexity
*   **Auxiliary Space:** The iterative implementation of `sift_down` requires only a constant number of pointers and temporary variables for swapping, resulting in $O(1)$ auxiliary space.
*   **Total Space:** The algorithm operates in-place on the input array $A$, requiring $O(n)$ total space to store the data. If the recursive implementation is used, the call stack adds $O(\log n)$ space, but this is not required for the optimal $O(1)$ auxiliary space bound.