# Sum Square Difference - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

For $N \in \mathbb{N}$, define the sum of the first $N$ natural numbers:

$$
S_1(N) = \sum_{k=1}^N k
$$

Define the sum of the squares of the first $N$ natural numbers:

$$
S_2(N) = \sum_{k=1}^N k^2
$$

The objective is to compute the difference between the square of the sum and the sum of the squares:

$$
\Delta(N) = \left( \sum_{k=1}^N k \right)^2 - \sum_{k=1}^N k^2 = (S_1(N))^2 - S_2(N)
$$

We must evaluate $\Delta(100)$.

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Iterative Element-Wise Accumulation
A naive algorithm loops $k = 1 \dots N$, accumulating $\sum k$ and $\sum k^2$:
```python
def naive_sum_square_difference(n):
    sum_n = sum(range(1, n + 1))
    sum_squares = sum(k * k for k in range(1, n + 1))
    return sum_n**2 - sum_squares
```

### Computational Inefficiencies
1. **Linear Time $\mathcal{O}(N)$**: Looping $N$ times performs $2N$ arithmetic operations.
2. **Unnecessary Loops**: Both series admit exact closed-form algebraic expressions in $\mathcal{O}(1)$ time.

---

## 3. Core Intuition & Mathematical Structure

Both partial sums are well-known classical series whose formulas derive from telescoping and induction:

### Closed-Form Component Breakdown

| Series | Notation | Closed-Form Formula | Value for $N = 10$ | Value for $N = 100$ |
| :--- | :---: | :--- | :---: | :---: |
| **Sum of Numbers** | $S_1(N)$ | $\frac{N(N+1)}{2}$ | $55$ | $5\,050$ |
| **Square of the Sum** | $(S_1(N))^2$ | $\frac{N^2(N+1)^2}{4}$ | $55^2 = 3\,025$ | $5050^2 = 25\,502\,500$ |
| **Sum of Squares** | $S_2(N)$ | $\frac{N(N+1)(2N+1)}{6}$ | $385$ | $338\,350$ |
| **Difference** | $\Delta(N)$ | $\frac{N(N+1)(N-1)(3N+2)}{12}$ | **$2\,640$** | **$25\,164\,150$** |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### A. Closed-Form Algebra
Subtracting $S_2(N)$ from $(S_1(N))^2$:

$$
\begin{aligned}
\Delta(N) &= \frac{N^2(N+1)^2}{4} - \frac{N(N+1)(2N+1)}{6} \\
&= \frac{N(N+1)}{12} \left[ 3N(N+1) - 2(2N+1) \right] \\
&= \frac{N(N+1)}{12} \left[ 3N^2 + 3N - 4N - 2 \right] \\
&= \frac{N(N+1)(3N^2 - N - 2)}{12} \\
&= \frac{N(N+1)(N-1)(3N+2)}{12}
\end{aligned}
$$

Factoring reveals that $\Delta(N)$ is a degree-4 polynomial:

$$
\boxed{\Delta(N) = \frac{(N^2 - 1) N (3N + 2)}{12}}
$$

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Evaluation for $N = 10$
1. Sum of first 10 numbers: $S_1(10) = \frac{10 \times 11}{2} = 55$.
2. Square of sum: $55^2 = 3025$.
3. Sum of squares: $S_2(10) = \frac{10 \times 11 \times 21}{6} = 385$.
4. Difference: $\Delta(10) = 3025 - 385 = \mathbf{2640}$. Matches sample! $\checkmark$

### Example 2: Exact Evaluation for $N = 100$
1. $S_1(100) = \frac{100 \times 101}{2} = 5050 \implies (S_1(100))^2 = 25\,502\,500$.
2. $S_2(100) = \frac{100 \times 101 \times 201}{6} = 338\,350$.
3. Difference:

$$
\Delta(100) = 25\,502\,500 - 338\,350 = \mathbf{25\,164\,150}
$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Sum of Integers** | `sum_n = n * (n + 1) // 2` | $\mathcal{O}(1)$ |
| **Stage 2** | **Sum of Squares** | `sum_squares = n * (n + 1) * (2*n + 1) // 6` | $\mathcal{O}(1)$ |
| **Stage 3** | **Difference** | `sum_n * sum_n - sum_squares` | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(1)$ | $\approx 0.00001$ seconds |
| **Space Complexity** | $\mathcal{O}(1)$ | In-place integer arithmetic |
| **Dynamic Execution** | $100\%$ Inline | Closed-form scalar evaluation |

### Critical Invariants & Edge Cases Handled:
1. **Exact Integer Division**: The product $(N-1)N(N+1)(3N+2)$ is always divisible by 12 for all $N \ge 1$.
2. **Boundary $N=1$**: For $N=1$, $\Delta(1) = 1^2 - 1^2 = 0$, which cleanly matches the formula.