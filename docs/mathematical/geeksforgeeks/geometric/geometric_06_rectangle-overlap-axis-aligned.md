# Formal Mathematical Specification: Rectangle Overlap (Axis-Aligned)

## 1. Definitions and Notation

Let $\mathcal{R}$ be the set of all axis-aligned rectangles in the Euclidean plane $\mathbb{R}^2$. A rectangle $R \in \mathcal{R}$ is uniquely defined by its bottom-left coordinate $(x_1, y_1)$ and its top-right coordinate $(x_2, y_2)$, where $x_1 < x_2$ and $y_1 < y_2$. We denote a rectangle as an ordered tuple:
$$R = \langle x_1, y_1, x_2, y_2 \rangle \in \mathbb{R}^4 \mid x_1 < x_2, y_1 < y_2$$

The interior of a rectangle $R$, denoted $\text{int}(R)$, is the open set:
$$\text{int}(R) = \{ (x, y) \in \mathbb{R}^2 \mid x_1 < x < x_2 \land y_1 < y < y_2 \}$$

The problem asks to determine the existence of a non-empty intersection between the interiors of two rectangles $R_A$ and $R_B$. We define the overlap predicate $\Phi: \mathcal{R} \times \mathcal{R} \to \{0, 1\}$ as:
$$\Phi(R_A, R_B) = \begin{cases} 1 & \text{if } \text{int}(R_A) \cap \text{int}(R_B) \neq \emptyset \\ 0 & \text{otherwise} \end{cases}$$

## 2. Algebraic Characterization

To characterize $\Phi(R_A, R_B)$, we utilize the property that the intersection of two axis-aligned rectangles is itself an axis-aligned rectangle (or empty). The intersection $\mathcal{I} = \text{int}(R_A) \cap \text{int}(R_B)$ is non-empty if and only if the projections of the rectangles onto the $x$-axis and $y$-axis both have non-empty intersections.

Let $I_x(R) = (x_1, x_2)$ and $I_y(R) = (y_1, y_2)$ be the open intervals representing the projections of $R$ onto the coordinate axes. The intersection of two open intervals $(a, b)$ and $(c, d)$ is non-empty if and only if $\max(a, c) < \min(b, d)$.

Thus, $\Phi(R_A, R_B) = 1$ if and only if:
$$\max(x_{A,1}, x_{B,1}) < \min(x_{A,2}, x_{B,2}) \quad \land \quad \max(y_{A,1}, y_{B,1}) < \min(y_{A,2}, y_{B,2})$$

By applying De Morgan's Laws to the negation of the overlap condition, we define the non-overlap condition $\neg \Phi(R_A, R_B)$. The rectangles are disjoint if any of the following hold:
1. $R_A$ is to the left of $R_B$: $x_{A,2} \leq x_{B,1}$
2. $R_A$ is to the right of $R_B$: $x_{A,1} \geq x_{B,2}$
3. $R_A$ is below $R_B$: $y_{A,2} \leq y_{B,1}$
4. $R_A$ is above $R_B$: $y_{A,1} \geq y_{B,2}$

Formally, $\Phi(R_A, R_B) = 1 \iff \neg (x_{A,2} \leq x_{B,1} \lor x_{A,1} \geq x_{B,2} \lor y_{A,2} \leq y_{B,1} \lor y_{A,1} \geq y_{B,2})$.

## 3. Complexity Analysis

### Time Complexity
The algorithm evaluates a boolean expression consisting of a fixed number of arithmetic comparisons. Let $n$ be the number of rectangles (here $n=2$). The computational work $W$ is defined by the number of primitive operations:
$$W = \sum_{i=1}^{k} c_i$$
where $k=8$ (the number of comparisons in the disjunction) and $c_i$ is the constant time required for a floating-point or integer comparison. Since $k$ is independent of the input values and the number of rectangles, the time complexity is:
$$T(n) \in O(1)$$

### Space Complexity
The algorithm requires a constant amount of auxiliary memory to store the input coordinates and the boolean result of the comparisons. No dynamic data structures or recursive calls are utilized. Let $S$ be the space required:
$$S = \text{const} \implies S \in O(1)$$
The space complexity is therefore $O(1)$, as the memory footprint does not scale with the magnitude of the coordinates or the input size.