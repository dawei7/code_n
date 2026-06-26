# Formal Mathematical Specification: Pow(x, n) (Fast Exponentiation)

## 1. Definitions and Notation

Let $x \in \mathbb{R}$ be the base and $n \in \mathbb{Z}$ be the exponent. We define the function $f: \mathbb{R} \times \mathbb{Z} \to \mathbb{R}$ such that $f(x, n) = x^n$.

The domain of the algorithm is defined by the set of pairs $(x, n) \in \mathbb{R} \times \mathbb{Z}$. We define the following subsets and operations:
*   **Base Case:** $x^0 = 1$ for all $x \neq 0$.
*   **Reciprocal Property:** For $n < 0$, $x^n = (x^{-1})^{-n} = \frac{1}{x^{-n}}$.
*   **Binary Representation:** Let $n$ be represented in binary form as $n = \sum_{i=0}^{k} b_i 2^i$, where $b_i \in \{0, 1\}$ and $k = \lfloor \log_2 |n| \rfloor$.

## 2. Algebraic Characterization

The algorithm relies on the principle of **Exponentiation by Squaring**, which is derived from the following recurrence relation:

$$
f(x, n) = 
\begin{cases} 
1 & \text{if } n = 0 \\
(f(x, n/2))^2 & \text{if } n > 0, n \equiv 0 \pmod 2 \\
x \cdot (f(x, (n-1)/2))^2 & \text{if } n > 0, n \equiv 1 \pmod 2 \\
\frac{1}{f(x, |n|)} & \text{if } n < 0 
\end{cases}
$$

### Loop Invariant
For the iterative implementation, let $r_i$ be the result, $b_i$ be the base, and $e_i$ be the exponent at iteration $i$. The algorithm maintains the invariant:
$$x^n = r_i \cdot b_i^{e_i}$$
Initially, $r_0 = 1, b_0 = x, e_0 = n$. At each step $i$, the exponent $e_i$ is halved ($e_{i+1} = \lfloor e_i / 2 \rfloor$). If $e_i$ is odd, the result is updated $r_{i+1} = r_i \cdot b_i$, and the base is squared $b_{i+1} = b_i^2$. The invariant holds because:
$$r_i \cdot b_i^{e_i} = (r_i \cdot b_i) \cdot (b_i^2)^{(e_i-1)/2} = r_i \cdot b_i^{e_i}$$

## 3. Complexity Analysis

### Time Complexity
The time complexity is determined by the number of iterations required to reduce the exponent $n$ to 0. Since the algorithm performs a right-shift operation on $n$ (equivalent to $n \leftarrow \lfloor n/2 \rfloor$) in each iteration, the number of iterations $T(n)$ is governed by the recurrence:
$$T(n) = T(\lfloor n/2 \rfloor) + O(1)$$
By the Master Theorem (Case 2), where $a=1, b=2, f(n)=O(1)$, we have:
$$T(n) = \Theta(\log_2 n)$$
Thus, the time complexity is $O(\log n)$.

### Space Complexity
*   **Recursive Implementation:** The space complexity is determined by the depth of the call stack. Since the problem size is halved at each recursive step, the depth of the recursion tree is $\lceil \log_2 n \rceil$. Therefore, the auxiliary space complexity is $O(\log n)$.
*   **Iterative Implementation:** The iterative approach utilizes a constant number of variables ($r, b, e$) regardless of the magnitude of $n$. Consequently, the auxiliary space complexity is $O(1)$. 

*Note: In the context of the provided algorithm, the iterative approach is preferred for space optimality, though the recursive definition remains the standard for theoretical divide-and-conquer analysis.*