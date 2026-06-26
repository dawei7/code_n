# Formal Mathematical Specification: Maximal Rectangle

## 1. Definitions and Notation

Let $M$ be a binary matrix of dimensions $m \times n$, where $M_{i,j} \in \{0, 1\}$ for $0 \le i < m$ and $0 \le j < n$. We define the set of all possible sub-rectangles $R$ as the set of quadruplets $(r_1, c_1, r_2, c_2)$ such that $0 \le r_1 \le r_2 < m$ and $0 \le c_1 \le c_2 < n$.

A sub-rectangle is considered "valid" if and only if:
$$\forall r \in [r_1, r_2], \forall c \in [c_1, c_2] : M_{r,c} = 1$$

The objective is to find the maximum area $\mathcal{A}^*$ defined as:
$$\mathcal{A}^* = \max_{(r_1, c_1, r_2, c_2) \in \mathcal{R}_{valid}} (r_2 - r_1 + 1) \times (c_2 - c_1 + 1)$$

We define a state vector $H^{(i)} \in \mathbb{N}^n$, representing the "histogram" of consecutive ones ending at row $i$:
$$H^{(i)}_j = \begin{cases} 0 & \text{if } M_{i,j} = 0 \\ H^{(i-1)}_j + 1 & \text{if } M_{i,j} = 1 \end{cases}$$
where $H^{(-1)}_j = 0$ for all $j$.

## 2. Algebraic Characterization

The problem is decomposed into $m$ independent instances of the "Largest Rectangle in Histogram" problem. For a fixed row $i$, let $f(H^{(i)})$ be the area of the largest rectangle in the histogram defined by the vector $H^{(i)}$.

### Recurrence Relation
The global maximum area is given by the supremum over all row-wise histogram solutions:
$$\mathcal{A}^* = \max_{0 \le i < m} f(H^{(i)})$$

### Histogram Invariant
For a fixed row $i$, let $S$ be a monotonic stack containing indices $k$ such that $H^{(i)}_{S_t} \le H^{(i)}_{S_{t+1}}$. For any index $k$ being processed:
1. If $H^{(i)}_k < H^{(i)}_{S_{top}}$, we pop $S_{top}$ and calculate the area of the rectangle with height $H^{(i)}_{S_{top}}$.
2. The width $W$ of this rectangle is determined by the nearest indices to the left and right that are strictly smaller than $H^{(i)}_{S_{top}}$. Specifically:
   $$W = k - S_{top-1} - 1$$
3. The area contribution is $\mathcal{A}_{pop} = H^{(i)}_{S_{top}} \times (k - S_{top-1} - 1)$.

The correctness relies on the invariant that for any bar $H^{(i)}_j$, the stack maintains the boundaries of the largest rectangle of height $H^{(i)}_j$ that includes column $j$.

## 3. Complexity Analysis

### Time Complexity
The algorithm consists of two nested processes:
1. **Histogram Construction:** For each row $i \in \{0, \dots, m-1\}$, we update $n$ elements. This requires $\sum_{i=0}^{m-1} n = O(mn)$ operations.
2. **Monotonic Stack Processing:** For each row, we perform a linear scan of $n$ elements. Each index $j \in \{0, \dots, n-1\}$ is pushed onto the stack exactly once and popped at most once. The amortized cost per row is $O(n)$.

Total time complexity $T(m, n)$ is:
$$T(m, n) = \sum_{i=0}^{m-1} (O(n) + O(n)) = O(mn)$$
Thus, $T(m, n) \in \Theta(mn)$.

### Space Complexity
The space complexity $S(m, n)$ is dominated by the auxiliary structures:
1. **Histogram Array:** $H$ requires $O(n)$ space.
2. **Monotonic Stack:** In the worst case (a strictly increasing histogram), the stack stores $O(n)$ indices.

Total space complexity $S(m, n)$ is:
$$S(m, n) = O(n) + O(n) = O(n)$$
The space complexity is independent of the number of rows $m$, provided the matrix is processed row-by-row, yielding $S(m, n) \in \Theta(n)$.