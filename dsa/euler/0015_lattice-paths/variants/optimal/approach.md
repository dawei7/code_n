# Lattice Paths - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Starting in the top-left vertex $(0, 0)$ of an $n \times n$ square grid ($n = 20$), with movement restricted strictly to right ($\text{R}$) and down ($\text{D}$), we seek the total number of distinct routes $L(n)$ to reach the bottom-right vertex $(n, n)$.

Formally:
$$L(n) = \left| \{ \mathbf{w} \in \{\text{R}, \text{D}\}^{2n} \mid \operatorname{count}(\text{R}) = n \land \operatorname{count}(\text{D}) = n \} \right|$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Recursive Path Exploration
A naive backtracking algorithm traverses the tree of paths recursively:
```python
def naive_paths(x, y, n):
    if x == n and y == n:
        return 1
    paths = 0
    if x < n:
        paths += naive_paths(x + 1, y, n)
    if y < n:
        paths += naive_paths(x, y + 1, n)
    return paths
```

### Computational Inefficiencies
1. **Exponential Explosion $\Theta(4^n / \sqrt{n})$**: The recursive call tree for $n = 20$ performs over $1.37 \times 10^{11}$ calls ($\approx 25$ minutes).
2. **Combinatorial Exactness**: The problem has a direct closed-form combinatorial formula computable in $\mathcal{O}(n)$ time ($\approx 0.0000$ seconds).

---

## 3. Core Intuition & Mathematical Structure

Every valid path in an $n \times n$ grid consists of exactly $n$ horizontal moves ($\text{R}$) and $n$ vertical moves ($\text{D}$).
The total length of the sequence is fixed at:
$$2n = n + n \text{ steps}$$

Choosing which $n$ positions in the $2n$-step sequence are down moves ($\text{D}$) uniquely determines the path.

### Central Binomial Coefficient Sequence

| Grid Size $n$ | Total Moves $2n$ | Move Formula $\binom{2n}{n}$ | Distinct Routes $L(n)$ |
| :---: | :---: | :---: | :---: |
| **$1 \times 1$** | $2$ | $\binom{2}{1} = \frac{2!}{1! 1!}$ | **$2$** ($\text{RD}, \text{DR}$) |
| **$2 \times 2$** | $4$ | $\binom{4}{2} = \frac{4 \times 3}{2 \times 1}$ | **$6$** |
| **$3 \times 3$** | $6$ | $\binom{6}{3} = \frac{6 \times 5 \times 4}{3 \times 2 \times 1}$ | **$20$** |
| **$4 \times 4$** | $8$ | $\binom{8}{4} = \frac{8 \times 7 \times 6 \times 5}{4 \times 3 \times 2 \times 1}$ | **$70$** |
| **$20 \times 20$** | $40$ | $\binom{40}{20} = \prod_{k=1}^{20} \frac{20 + k}{k}$ | **$137\,846\,528\,820$** |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Central Binomial Theorem
By bijection with binary strings of length $2n$ having Hamming weight $n$:
$$L(n) = \binom{2n}{n} = \frac{(2n)!}{(n!)^2}$$

### Product Formulation
To compute the binomial coefficient without evaluating large factorial products directly:
$$L(n) = \prod_{k=1}^n \frac{n + k}{k}$$

Each intermediate division by $k$ is exact in integer arithmetic.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Evaluation for $2 \times 2$ Grid ($n = 2$)
- Total steps: $2 \times 2 = 4$.
- Number of routes:
  $$\binom{4}{2} = \frac{4 \times 3}{2 \times 1} = \mathbf{6}$$
- The 6 valid sequences are: $\text{RRDD}, \text{RDRD}, \text{RDDR}, \text{DRRD}, \text{DRDR}, \text{DDRR}$. Matches sample! $\checkmark$

### Example 2: Exact Target Evaluation for $20 \times 20$ Grid ($n = 20$)
- Evaluating $\binom{40}{20}$:
  $$L(20) = \frac{40 \times 39 \times 38 \times \dots \times 21}{20 \times 19 \times 18 \times \dots \times 1} = \mathbf{137\,846\,528\,820}$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Accumulator Setup** | Set `ans = 1` | $\mathcal{O}(1)$ |
| **Stage 2** | **Multiplicative Loop** | For $k = 1 \dots n$: `ans = ans * (n + k) // k` | $n$ steps |
| **Stage 3** | **Return Value** | Return scalar integer `ans` | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(n)$ | $\approx 0.00001$ seconds for $n = 20$ |
| **Space Complexity** | $\mathcal{O}(1)$ | Single integer register |
| **Dynamic Execution** | $100\%$ Inline | Multiplicative binomial evaluation |

### Critical Invariants & Edge Cases Handled:
1. **Integer Divisibility**: Because $\prod_{i=1}^k (n + i)$ represents $k$ consecutive integers, it is strictly divisible by $k!$, ensuring exact integer division at every step.
2. **Boundary $n=0$**: For $n=0$, the formula correctly yields $L(0) = \binom{0}{0} = 1$.
