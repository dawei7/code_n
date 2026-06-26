# Formal Mathematical Specification: The Power Sum

## 1. Definitions and Notation

Let $X \in \mathbb{Z}^+$ be the target integer and $N \in \mathbb{Z}^+$ be the exponent. We define the set of candidate natural numbers as $\mathcal{C} = \{i \in \mathbb{Z}^+ \mid i^N \leq X\}$. The cardinality of this set is $M = \lfloor X^{1/N} \rfloor$.

The problem seeks to find the number of subsets $S \subseteq \mathcal{C}$ such that the sum of the $N$-th powers of the elements in $S$ equals $X$. Formally, we define the solution space as:
$$\mathcal{F} = \left\{ S \subseteq \mathcal{C} : \sum_{s \in S} s^N = X \right\}$$
The objective is to compute the cardinality $|\mathcal{F}|$.

We define the state of our recursive process as a tuple $(t, i)$, where:
*   $t \in \mathbb{Z}_{\geq 0}$ is the remaining target sum.
*   $i \in \mathbb{Z}^+$ is the current candidate base being considered for inclusion in the subset.

## 2. Algebraic Characterization

The algorithm is defined by the function $f(t, i)$, which returns the number of ways to express $t$ as a sum of unique $N$-th powers using a subset of $\{i, i+1, \dots, M\}$. The recurrence relation is defined as:

$$f(t, i) = 
\begin{cases} 
1 & \text{if } t = 0 \\
0 & \text{if } t < 0 \lor i^N > t \\
f(t - i^N, i + 1) + f(t, i + 1) & \text{otherwise}
\end{cases}$$

**Correctness Invariants:**
1.  **Completeness:** The branching factor $f(t - i^N, i + 1) + f(t, i + 1)$ represents the partition of the power set of $\mathcal{C}$ into two disjoint sets: those containing $i$ and those not containing $i$.
2.  **Termination:** Since $i$ is strictly increasing in every recursive call ($i \to i+1$), and the domain is bounded by $M = \lfloor X^{1/N} \rfloor$, the recursion depth is finite, ensuring the algorithm terminates.
3.  **Uniqueness:** The constraint $i+1$ in the recursive step ensures that each element $i \in \mathcal{C}$ is considered at most once, satisfying the requirement for unique natural numbers.

## 3. Complexity Analysis

### Time Complexity
The algorithm explores a binary recursion tree. Let $T(i)$ be the number of nodes in the recursion tree starting at index $i$. The recurrence for the number of operations is:
$$T(i) = 1 + T(i+1) + T(i+1) = 2T(i+1) + 1$$
Given the base case $T(M+1) = 1$, this is a linear non-homogeneous recurrence. Expanding this, we find:
$$T(1) = \sum_{k=0}^{M} 2^k = 2^{M+1} - 1$$
Substituting $M = \lfloor X^{1/N} \rfloor$, the time complexity is $O(2^{X^{1/N}})$. This represents the total number of subsets of $\mathcal{C}$ evaluated in the worst case.

### Space Complexity
The space complexity is determined by the maximum depth of the recursion stack. In the worst-case scenario, the algorithm traverses the tree to a depth of $M$. 
*   **Auxiliary Space:** The stack frame stores the current parameters $(t, i)$ and the return address. Since each frame occupies $O(1)$ space, the total auxiliary space is proportional to the maximum depth of the recursion tree.
*   **Total Space:** 
$$\text{Space} = O(\text{depth}) = O(M) = O(X^{1/N})$$
Thus, the space complexity is $O(X^{1/N})$, corresponding to the height of the recursion tree.