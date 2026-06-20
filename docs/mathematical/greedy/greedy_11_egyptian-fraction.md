# Formal Mathematical Specification: Egyptian Fraction

## 1. Definitions and Notation

Let the input be a rational number $r \in \mathbb{Q}$ such that $0 < r < 1$. We represent $r$ as a pair of coprime positive integers $(n, d) \in \mathbb{Z}^+ \times \mathbb{Z}^+$, where $r = \frac{n}{d}$ and $\gcd(n, d) = 1$.

*   **State Space ($\mathcal{S}$):** The state at any iteration $k$ is defined by the tuple $(n_k, d_k) \in \mathbb{Z}^+ \times \mathbb{Z}^+$.
*   **Unit Fraction:** A fraction of the form $\frac{1}{x}$ where $x \in \mathbb{Z}^+$.
*   **Output Set ($\mathcal{D}$):** A finite sequence of denominators $X = \{x_1, x_2, \dots, x_m\}$ such that:
    $$\frac{n}{d} = \sum_{i=1}^{m} \frac{1}{x_i}$$
    where $x_i \in \mathbb{Z}^+$ and $x_i < x_{i+1}$ for all $1 \le i < m$.

## 2. Algebraic Characterization

The algorithm employs a greedy strategy based on the Fibonacci-Sylvester expansion. Given the current state $(n_k, d_k)$, we define the next denominator $x_k$ as the smallest integer such that $\frac{1}{x_k} \le \frac{n_k}{d_k}$.

**The Greedy Choice:**
$$x_k = \left\lceil \frac{d_k}{n_k} \right\rceil$$

**Recurrence Relation:**
The transition from state $(n_k, d_k)$ to $(n_{k+1}, d_{k+1})$ is defined by:
$$\frac{n_{k+1}}{d_{k+1}} = \frac{n_k}{d_k} - \frac{1}{x_k} = \frac{n_k x_k - d_k}{d_k x_k}$$

To maintain the canonical representation, we define the next state by reducing the fraction:
$$g_k = \gcd(n_k x_k - d_k, d_k x_k)$$
$$n_{k+1} = \frac{n_k x_k - d_k}{g_k}, \quad d_{k+1} = \frac{d_k x_k}{g_k}$$

**Loop Invariant:**
At each step $k$, the remainder $r_k = \frac{n_k}{d_k}$ satisfies $0 \le r_k < 1$. The algorithm terminates at step $m$ when $n_m = 0$. The strict decrease of the numerator $n_{k+1} < n_k$ (for $n_k > 1$) ensures termination. Specifically, since $x_k \ge \frac{d_k}{n_k}$, it follows that $n_k x_k - d_k < n_k x_k - (n_k x_k - n_k) = n_k$.

## 3. Complexity Analysis

### Time Complexity
The time complexity is governed by the number of iterations $m$ and the cost of arithmetic operations per iteration.

1.  **Number of Iterations ($m$):** For a given $\frac{n}{d}$, the number of terms $m$ is bounded. While the worst-case for general inputs can be large, for the greedy algorithm, it is known that $m = O(n)$ in the worst case. However, for most inputs, the sequence of numerators decreases rapidly, leading to an average case of $O(\log d)$.
2.  **Cost per Iteration:** Each iteration requires:
    *   Calculation of $x_k = \lceil d/n \rceil$: $O(1)$ arithmetic operations.
    *   GCD computation: Using the Euclidean algorithm, $\gcd(n_k x_k - d_k, d_k x_k)$ takes $O(\log(\min(n_k, d_k)))$ time.
    *   Multiplication and division: $O(\log^2(\max(n_k, d_k)))$ using standard algorithms, or $O(\log(\max(n_k, d_k)))$ assuming word-size operations.

Thus, the total time complexity is $O(m \cdot \log(\text{bits}))$, which simplifies to $O(n \log d)$ in the worst case, or $O(\log d)$ under favorable conditions.

### Space Complexity
*   **Auxiliary Space:** The algorithm maintains a constant number of variables $(n, d, x, g)$ to track the current state. Thus, the auxiliary space complexity is $O(1)$.
*   **Total Space:** Including the output sequence of length $m$, the space complexity is $O(m)$, where $m$ is the number of unit fractions generated. Given the greedy choice, $m$ is typically small, but in the worst case, it is $O(n)$.