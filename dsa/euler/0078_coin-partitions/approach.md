# Coin Partitions - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Let $p(n)$ denote the unrestricted integer partition function, counting the number of ways $n$ identical coins can be partitioned into piles.

For example, $p(5) = 7$:
- $5$
- $4 + 1$
- $3 + 2$
- $3 + 1 + 1$
- $2 + 2 + 1$
- $2 + 1 + 1 + 1$
- $1 + 1 + 1 + 1 + 1$

The objective is to find the **least value of $n$** for which $p(n)$ is divisible by **one million ($1\,000\,000$)**:
$$n_{\text{min}} = \min \left\{ n \in \mathbb{N} \;\middle|\; p(n) \equiv 0 \pmod{10^6} \right\}$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Standard Knapsack DP
A naive approach computes $p(n)$ using unbounded knapsack dynamic programming:
```python
def naive_coin_partitions(limit):
    # O(N^2) complexity requires ~3 x 10^9 operations for N ≈ 55,000!
    # ...
```

### Euler's Pentagonal Number Theorem
By Euler's pentagonal number theorem, the partition function satisfies the fast recurrence:
$$p(n) = \sum_{k \neq 0} (-1)^{k-1} p\left( n - g_k \right)$$
where $g_k = \frac{k(3k - 1)}{2}$ for $k = 1, -1, 2, -2, 3, -3, \dots$ are the generalized pentagonal numbers.

1. For any $n$, there are only $\mathcal{O}(\sqrt{n})$ terms with $g_k \le n$.
2. Total computation time up to $N \approx 55\,000$ drops from $\mathcal{O}(N^2)$ to $\mathcal{O}(N \sqrt{N})$, executing in $\approx 0.50$ seconds.
3. Intermediate calculations are reduced modulo $10^6$.

---

## 3. Core Intuition & Mathematical Structure

### Generalized Pentagonal Numbers & Alternating Signs

| Parameter $k$ | Pentagonal Number $g_k = \frac{k(3k-1)}{2}$ | Sign Factor $(-1)^{k-1}$ | Contribution to $p(n)$ |
| :---: | :---: | :---: | :---: |
| **$+1$** | $\frac{1(2)}{2} = \mathbf{1}$ | $+1$ | $+p(n - 1)$ |
| **$-1$** | $\frac{-1(-4)}{2} = \mathbf{2}$ | $+1$ | $+p(n - 2)$ |
| **$+2$** | $\frac{2(5)}{2} = \mathbf{5}$ | $-1$ | $-p(n - 5)$ |
| **$-2$** | $\frac{-2(-7)}{2} = \mathbf{7}$ | $-1$ | $-p(n - 7)$ |
| **$+3$** | $\frac{3(8)}{2} = \mathbf{12}$ | $+1$ | $+p(n - 12)$ |
| **$-3$** | $\frac{-3(-10)}{2} = \mathbf{15}$ | $+1$ | $+p(n - 15)$ |
| **$+4$** | $\frac{4(11)}{2} = \mathbf{22}$ | $-1$ | $-p(n - 22)$ |
| **$-4$** | $\frac{-4(-13)}{2} = \mathbf{26}$ | $-1$ | $-p(n - 26)$ |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Fast Modular Recurrence Pipeline
1. Initialize $p = [1]$ (since $p(0) = 1$).
2. For $n = 1, 2, 3, \dots$:
   - Compute:
     $$p(n) = \sum_{k=1}^{\infty} (-1)^{k-1} \left( p\left(n - \frac{k(3k-1)}{2}\right) + p\left(n - \frac{k(3k+1)}{2}\right) \right) \pmod{10^6}$$
   - If $p(n) \equiv 0 \pmod{10^6}$, return $n$.
   - Append $p(n)$ to list $p$.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Trace for $n = 1 \dots 5$
- $p(0) = 1$
- $p(1) = +p(0) = \mathbf{1}$
- $p(2) = +p(1) + p(0) = 1 + 1 = \mathbf{2}$
- $p(3) = +p(2) + p(1) = 2 + 1 = \mathbf{3}$
- $p(4) = +p(3) + p(2) = 3 + 2 = \mathbf{5}$
- $p(5) = +p(4) + p(3) - p(0) = 5 + 3 - 1 = \mathbf{7}$. Matches problem statement sample! $\checkmark$

### Example 2: Target Zero-Modulus Search ($p(n) \equiv 0 \pmod{10^6}$)
- The recurrence advances up to $n = 55\,374$:
  $$p(55374) \equiv \mathbf{0} \pmod{1\,000\,000}$$
- Smallest integer:
  $$n_{\text{min}} = \mathbf{55\,374}$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **State Init** | `p = [1]; n = 1` | $\mathcal{O}(1)$ |
| **Stage 2** | **Ascending Loop** | While True: evaluate $p(n)$ | $\approx 55\,000$ steps |
| **Stage 3** | **Pentagonal Inner Loop** | For $k=1, 2 \dots$ while $g_1 \le n$: add $(-1)^{k-1} p(n - g_k)$ | $\mathcal{O}(\sqrt{n})$ terms |
| **Stage 4** | **Modular Check** | `p_n %= 1000000; if p_n == 0: return n` | $\mathcal{O}(1)$ |
| **Stage 5** | **Return Value** | Return scalar integer $55374$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N \sqrt{N})$ where $N = 55\,374$ | $\approx 0.50$ seconds |
| **Space Complexity** | $\mathcal{O}(N)$ | Partition array $\approx 400$ KB |
| **Dynamic Execution** | $100\%$ Inline | Euler's pentagonal theorem recurrence |

### Critical Invariants & Edge Cases Handled:
1. **Modular Arithmetic**: Reducing modulo $10^6$ at every step avoids allocating gigantic multi-thousand-digit BigInts.
2. **Boundary Truncation**: Loop breaks as soon as the first pentagonal index $g_1 > n$, preventing negative index lookups.
