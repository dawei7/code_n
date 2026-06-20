# Formal Mathematical Specification: Max Points on a Line

## 1. Definitions and Notation

Let $P = \{p_1, p_2, \dots, p_n\}$ be a set of $n$ distinct points in the Euclidean plane $\mathbb{R}^2$, where each point $p_i$ is represented by the coordinate pair $(x_i, y_i) \in \mathbb{Z}^2$.

*   **Collinearity:** A subset of points $S \subseteq P$ is collinear if there exists a line $L \subset \mathbb{R}^2$ such that $S \subseteq L$.
*   **Slope Representation:** For any two distinct points $p_i, p_j \in P$, the slope $m_{ij}$ is defined by the vector $\vec{v} = (x_j - x_i, y_j - y_i) = (\Delta x, \Delta y)$. To avoid floating-point representation, we define the canonical slope as the reduced fraction:
    $$\sigma(p_i, p_j) = \left( \frac{\Delta y}{g}, \frac{\Delta x}{g} \right) \quad \text{where } g = \gcd(|\Delta x|, |\Delta y|)$$
    To ensure a unique representation for a line, we enforce a sign convention: if $\Delta x < 0$, we negate both components; if $\Delta x = 0$, we set the slope to $(1, 0)$ (vertical).
*   **Objective:** Find the cardinality of the largest subset $S \subseteq P$ such that all $p \in S$ are collinear. Let $\mathcal{L}$ be the set of all lines passing through at least two points in $P$. We seek:
    $$\max_{L \in \mathcal{L}} |\{p \in P : p \in L\}|$$

## 2. Algebraic Characterization

For a fixed anchor point $p_i \in P$, let $S_i$ be the set of all lines passing through $p_i$ and at least one other point $p_j \in P \setminus \{p_i\}$. We define a mapping $f_i: P \setminus \{p_i\} \to \mathbb{Z}^2$ such that $f_i(p_j) = \sigma(p_i, p_j)$.

The number of points collinear with $p_i$ along a specific slope $\vec{s} \in \mathbb{Z}^2$ is given by:
$$N(p_i, \vec{s}) = 1 + \sum_{j \neq i, p_j \neq p_i} \mathbb{I}(f_i(p_j) = \vec{s})$$
where $\mathbb{I}(\cdot)$ is the indicator function. Including points coincident with $p_i$ (duplicates), let $D_i = \{p_j \in P : p_j = p_i, j \neq i\}$. The total count of points on a line passing through $p_i$ with slope $\vec{s}$ is:
$$C(p_i, \vec{s}) = |D_i| + 1 + \sum_{j \neq i, p_j \neq p_i} \mathbb{I}(f_i(p_j) = \vec{s})$$

The algorithm computes the global maximum:
$$\text{Result} = \max_{p_i \in P} \left( \max_{\vec{s} \in \text{Im}(f_i)} C(p_i, \vec{s}) \right)$$

**Loop Invariant:** At the start of each iteration $i$ of the outer loop, the variable `best` stores $\max_{k < i} (\text{max collinear points through } p_k)$. Within the inner loop $j$, the hash map `slopes` maintains the frequency distribution of the canonical slopes $\sigma(p_i, p_j)$, ensuring that all points $p_j$ sharing the same slope relative to $p_i$ are correctly aggregated.

## 3. Complexity Analysis

### Time Complexity
The algorithm consists of a nested loop structure. The outer loop iterates $n$ times. The inner loop iterates $n-1$ times.
1.  **GCD Computation:** The Euclidean algorithm for $\gcd(\Delta x, \Delta y)$ takes $O(\log(\min(|\Delta x|, |\Delta y|)))$ time. Let $M$ be the maximum coordinate value, such that $\log M$ bounds the GCD operation.
2.  **Hash Map Operations:** Insertion and lookup in the hash map are $O(1)$ on average.
3.  **Total Work:** The total time complexity is:
    $$T(n) = \sum_{i=1}^{n} \sum_{j=1, j \neq i}^{n} O(\log M) = O(n^2 \log M)$$
Given that $\log M$ is typically treated as a constant in fixed-precision arithmetic, the complexity is $O(n^2)$.

### Space Complexity
The space complexity is dominated by the storage of the hash map for each anchor point $p_i$.
1.  **Auxiliary Space:** For a fixed $i$, the hash map stores at most $n-1$ distinct slopes. Thus, the space required is $O(n)$.
2.  **Total Space:** Since the hash map is re-initialized for each $i$, the peak auxiliary space complexity is $O(n)$. The input storage is $O(n)$, resulting in a total space complexity of $O(n)$.