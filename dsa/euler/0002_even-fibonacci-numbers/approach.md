# Even Fibonacci Numbers - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Let the Fibonacci sequence $(F_n)_{n \ge 1}$ be defined by the initial conditions and recurrence:

$$
F_1 = 1, \quad F_2 = 2, \quad F_n = F_{n-1} + F_{n-2} \quad \text{for } n \ge 3
$$

Define the set of even-valued Fibonacci terms not exceeding an upper bound $N \in \mathbb{N}$:

$$
\mathcal{E}_N = \{ F_k \mid k \in \mathbb{N}, \, F_k \le N, \, 2 \mid F_k \}
$$

The objective is to compute the sum of all elements in $\mathcal{E}_N$:

$$
\begin{aligned}
S(N) = \sum_{x \in \mathcal{E}_N} x = \sum_{\substack{k \ge 1 \\ F_k \le N}} F_k \cdot \mathbb{I}(2 \mid F_k)
\end{aligned}
$$

where $\mathbb{I}(P) \in \{0, 1\}$ is the indicator function of proposition $P$.

We must evaluate $S(4\,000\,000)$.

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Element-Wise Parity Testing
A naive algorithm generates every standard Fibonacci number sequentially and filters by testing $F_k \bmod 2 == 0$:
```python
def naive_S(limit):
    a, b = 1, 2
    total = 0
    while a <= limit:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    return total
```

### Computational Inefficiencies
1. **Redundant Parity Computations**: The parity of Fibonacci numbers follows a strict period of 3:

$$
\text{Odd}, \text{Even}, \text{Odd}, \text{Odd}, \text{Even}, \text{Odd}, \dots
$$

2. **Unnecessary Branching**: Testing modulo on every element wastes two-thirds of all loop cycles on odd numbers.

---

## 3. Core Intuition & Mathematical Structure

Because every third Fibonacci term is even, we can define the pure subsequence of even terms:

$$
E_n = F_{3n-1} \quad (\text{or } F_{3n} \text{ under } F_1=1, F_2=1 \text{ indexing})
$$

Specifically: $E_1 = 2, E_2 = 8, E_3 = 34, E_4 = 144, \dots$

### Fibonacci Parity & Subsequence Table

| Index $k$ | $F_k$ | Parity | Subsequence Term $E_n$ | Formula $E_n = 4E_{n-1} + E_{n-2}$ |
| :---: | :---: | :---: | :---: | :--- |
| **1** | $1$ | Odd | — | — |
| **2** | $2$ | **Even** | $E_1 = 2$ | Initial value |
| **3** | $3$ | Odd | — | — |
| **4** | $5$ | Odd | — | — |
| **5** | $8$ | **Even** | $E_2 = 8$ | Initial value |
| **6** | $13$ | Odd | — | — |
| **7** | $21$ | Odd | — | — |
| **8** | $34$ | **Even** | $E_3 = 34$ | $4(8) + 2 = 34$ |
| **9** | $55$ | Odd | — | — |
| **10** | $89$ | Odd | — | — |
| **11** | $144$ | **Even** | $E_4 = 144$ | $4(34) + 8 = 144$ |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Direct Recurrence for Even Terms
Let $E_n$ denote the $n$-th even Fibonacci term. Expanding $F_{3n}$:

$$
\begin{aligned}
F_{3n} &= F_{3n-1} + F_{3n-2} \\
&= (F_{3n-2} + F_{3n-3}) + F_{3n-2} = 2F_{3n-2} + F_{3n-3} \\
&= 2(F_{3n-3} + F_{3n-4}) + F_{3n-3} = 3F_{3n-3} + 2F_{3n-4} \\
&= 3F_{3n-3} + 2(F_{3n-3} - F_{3n-6}) = 4F_{3n-3} + F_{3n-6}
\end{aligned}
$$

Translating to $E_n$:

$$
\boxed{E_n = 4E_{n-1} + E_{n-2} \quad \text{for } n \ge 3}
$$

with base conditions $E_1 = 2, E_2 = 8$.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Evaluation for $N = 100$
- $E_1 = 2$
- $E_2 = 8$
- $E_3 = 4(8) + 2 = 34$
- $E_4 = 4(34) + 8 = 144 > 100$ (Terminates)
- Sum $S(100) = 2 + 8 + 34 = \mathbf{44}$. Matches sample! $\checkmark$

### Example 2: Exact Evaluation for $N = 4\,000\,000$

| Term $n$ | Recurrence Calculation | Value $E_n$ | Running Sum $S$ |
| :---: | :--- | :---: | :---: |
| **1** | Initial condition | $2$ | $2$ |
| **2** | Initial condition | $8$ | $10$ |
| **3** | $4(8) + 2$ | $34$ | $44$ |
| **4** | $4(34) + 8$ | $144$ | $188$ |
| **5** | $4(144) + 34$ | $610$ | $798$ |
| **6** | $4(610) + 144$ | $2\,584$ | $3\,382$ |
| **7** | $4(2584) + 610$ | $10\,946$ | $14\,328$ |
| **8** | $4(10946) + 2584$ | $46\,368$ | $60\,696$ |
| **9** | $4(46368) + 10946$ | $196\,440$ | $257\,136$ |
| **10** | $4(196440) + 46368$ | $832\,040$ | $1\,089\,176$ |
| **11** | $4(832040) + 196440$ | $3\,524\,576$ | **$4\,613\,732$** |
| **12** | $4(3524576) + 832040$ | $14\,930\,344 > 4 \times 10^6$ | *Stop* |

Total Sum: $S(4\,000\,000) = \mathbf{4\,613\,732}$.

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **State Initialization** | Set $e_1 = 2, e_2 = 8, \text{total} = 0$ | $\mathcal{O}(1)$ |
| **Stage 2** | **Guarded Loop** | Iterate while $e_1 \le \text{limit}$ | $\approx 11$ steps |
| **Stage 3** | **Accumulation** | $\text{total} \leftarrow \text{total} + e_1$ | $\mathcal{O}(1)$ |
| **Stage 4** | **State Transition** | $(e_1, e_2) \leftarrow (e_2, 4e_2 + e_1)$ | $\mathcal{O}(1)$ |
| **Stage 5** | **Return Value** | Return exact scalar integer $\text{total}$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(\log_\psi N)$ where $\psi = \phi^3 \approx 4.236$ | Exactly 11 iterations for $4\,000\,000$ |
| **Space Complexity** | $\mathcal{O}(1)$ | 3 integer variables |
| **Dynamic Execution** | $100\%$ Inline | Direct linear recurrence |

### Critical Invariants & Edge Cases Handled:
1. **Upper Bound Strictness ($e_1 \le N$)**: Excludes terms exceeding $N$ before accumulation.
2. **Small Limits ($N < 2$)**: Correctly returns $0$ if limit is below the first even term.