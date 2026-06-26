# Formal Mathematical Specification: Counting Sort

## 1. Definitions and Notation

Let $A = [a_1, a_2, \dots, a_n]$ be an input sequence of $n$ integers, where each element $a_i \in \mathbb{Z}_{\ge 0}$. Let $k = \max(A)$ denote the maximum value in the sequence. The domain of the input elements is the set $\mathcal{D} = \{0, 1, \dots, k\}$.

We define the following auxiliary structures:
*   **Frequency Array:** A mapping $C: \mathcal{D} \to \{0, 1, \dots, n\}$, where $C[v]$ represents the cardinality of the set $\{a_i \in A \mid a_i = v\}$.
*   **Prefix Sum Array:** A mapping $P: \mathcal{D} \to \{0, 1, \dots, n\}$, defined as the cumulative distribution function of the frequencies:
    $$P[j] = \sum_{i=0}^{j} C[i]$$
*   **Output Array:** A sequence $B = [b_1, b_2, \dots, b_n]$ which is a permutation of $A$ such that $b_1 \le b_2 \le \dots \le b_n$.

## 2. Algebraic Characterization

The correctness of Counting Sort relies on the transformation of frequencies into positional indices. The algorithm proceeds through three formal phases:

**Phase 1: Frequency Counting**
The frequency array $C$ is constructed such that:
$$C[v] = \sum_{i=1}^{n} \mathbb{I}(a_i = v)$$
where $\mathbb{I}(\cdot)$ is the indicator function.

**Phase 2: Prefix Summation**
The array $P$ is computed via the recurrence:
$$P[j] = \begin{cases} C[0] & \text{if } j = 0 \\ P[j-1] + C[j] & \text{if } 0 < j \le k \end{cases}$$
For any value $v$, $P[v]$ represents the total number of elements in $A$ that are less than or equal to $v$. Consequently, the elements equal to $v$ occupy the indices in the range $(P[v-1], P[v]]$ in the sorted output $B$ (using 1-based indexing).

**Phase 3: Stable Placement**
To maintain stability, we iterate through the input $A$ in reverse order ($i = n$ down to $1$). For each $a_i$, the element is placed in $B$ at the position determined by the current prefix sum:
$$B[P[a_i]] = a_i$$
Following the placement, the prefix sum is decremented to account for the consumed position:
$$P[a_i] \leftarrow P[a_i] - 1$$
The invariant maintained at each step $t$ (where $t$ is the number of elements placed) is that the elements $\{b_{P[v]-t+1}, \dots, b_{P[v]}\}$ are exactly the instances of value $v$ processed thus far, preserving their relative order from $A$.

## 3. Complexity Analysis

### Time Complexity
The algorithm consists of three distinct linear passes:
1.  **Counting:** A single pass over $A$ to populate $C$, requiring $\sum_{i=1}^n 1 = n$ operations.
2.  **Prefix Sums:** A single pass over $C$ of size $k+1$, requiring $\sum_{j=0}^k 1 = k+1$ operations.
3.  **Placement:** A single pass over $A$ (in reverse), requiring $n$ operations.

The total time complexity $T(n, k)$ is given by:
$$T(n, k) = \Theta(n) + \Theta(k) + \Theta(n) = \Theta(n + k)$$
Since the algorithm performs no comparisons between elements, it avoids the $\Omega(n \log n)$ lower bound established for comparison-based sorting models.

### Space Complexity
The algorithm requires auxiliary space for the frequency/prefix-sum array $C$ and the output array $B$.
*   **Auxiliary Space:** The array $C$ requires $k+1$ units of space.
*   **Output Space:** The array $B$ requires $n$ units of space.

The total space complexity $S(n, k)$ is:
$$S(n, k) = \Theta(n + k)$$
This demonstrates a space-time trade-off: the algorithm achieves linear time complexity at the cost of memory proportional to the range of the input values. If $k \gg n$, the space complexity becomes the dominant constraint, rendering the algorithm inefficient.