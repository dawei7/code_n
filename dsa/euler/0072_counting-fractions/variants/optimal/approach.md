# Counting Fractions - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Consider the set of all reduced proper fractions $\frac{n}{d}$ where $n < d \le N$ and $\gcd(n, d) = 1$.
For $N = 8$, the set consists of 21 fractions:
$$\left\{ \frac{1}{8}, \frac{1}{7}, \frac{1}{6}, \frac{1}{5}, \frac{1}{4}, \frac{2}{7}, \frac{1}{3}, \frac{3}{8}, \frac{2}{5}, \frac{3}{7}, \frac{1}{2}, \frac{4}{7}, \frac{3}{5}, \frac{5}{8}, \frac{2}{3}, \frac{5}{7}, \frac{3}{4}, \frac{4}{5}, \frac{5}{6}, \frac{6}{7}, \frac{7}{8} \right\}$$

The objective is to find how many elements are contained in the set of reduced proper fractions for $d \le 1\,000\,000$:
$$|\mathcal{F}_{1000000}| = \sum_{d=2}^{1000000} \sum_{n=1}^{d-1} \mathbb{I}(\gcd(n, d) = 1)$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Explicit GCD Checks
A naive algorithm checks $\gcd(n, d) = 1$ for all $\approx 5 \times 10^{11}$ pairs:
```python
def naive_counting_fractions(limit):
    # tests 500 billion pairs individually
    # ...
```

### The Euler Totient Equivalence
1. For any denominator $d$, the number of coprimes $n < d$ with $\gcd(n, d) = 1$ is by definition **Euler's totient function $\phi(d)$**.
2. The total count is therefore given by the sum of totients:
   $$|\mathcal{F}_N| = \sum_{d=2}^N \phi(d)$$
3. A linear totient sieve evaluates $\phi(d)$ for all $d \le 1\,000\,000$ in $\mathcal{O}(N \log \log N)$ time in $\approx 0.20$ seconds.

---

## 3. Core Intuition & Mathematical Structure

### Cumulative Totient Sums for Small $N$

| Denominator $d$ | Prime Factorization | $\phi(d) = d \prod (1 - 1/p)$ | Fractions Generated | Cumulative Fractions $\sum_{i=2}^d \phi(i)$ |
| :---: | :---: | :---: | :--- | :---: |
| **$2$** | $2$ | $1$ | $\frac{1}{2}$ | $1$ |
| **$3$** | $3$ | $2$ | $\frac{1}{3}, \frac{2}{3}$ | $3$ |
| **$4$** | $2^2$ | $2$ | $\frac{1}{4}, \frac{3}{4}$ | $5$ |
| **$5$** | $5$ | $4$ | $\frac{1}{5}, \frac{2}{5}, \frac{3}{5}, \frac{4}{5}$ | $9$ |
| **$6$** | $2 \times 3$ | $2$ | $\frac{1}{6}, \frac{5}{6}$ | $11$ |
| **$7$** | $7$ | $6$ | $\frac{1}{7}, \frac{2}{7}, \frac{3}{7}, \frac{4}{7}, \frac{5}{7}, \frac{6}{7}$ | $17$ |
| **$8$** | $2^3$ | $4$ | $\frac{1}{8}, \frac{3}{8}, \frac{5}{8}, \frac{7}{8}$ | **$21$ (Sample)** |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Linear Multiplicative Totient Sieve
1. Initialize an array $\mathbf{\phi}$ of size $N + 1$ with $\mathbf{\phi}[i] = i$.
2. For each $i \in [2, N]$:
   - If $\mathbf{\phi}[i] == i$ ($i$ is prime):
     - For all multiples $j \in \{i, 2i, 3i, \dots \le N\}$:
       $$\mathbf{\phi}[j] \leftarrow \mathbf{\phi}[j] // i \times (i - 1)$$
3. Sum all entries from index $2$ to $N$:
   $$S = \sum_{d=2}^{1000000} \mathbf{\phi}[d]$$

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Trace for $N = 8$
$$\sum_{d=2}^8 \phi(d) = \phi(2) + \phi(3) + \phi(4) + \phi(5) + \phi(6) + \phi(7) + \phi(8)$$
$$S = 1 + 2 + 2 + 4 + 2 + 6 + 4 = \mathbf{21}$$
Matches problem statement sample! $\checkmark$

### Example 2: Target Evaluation for $N = 1\,000\,000$
- Summing all totients from $d = 2$ to $1\,000\,000$:
  $$|\mathcal{F}_{1000000}| = \mathbf{303\,963\,552\,391}$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Array Init** | `phi = list(range(limit + 1))` | $\mathcal{O}(N)$ |
| **Stage 2** | **Totient Sieve** | If `phi[i] == i`: update multiples $j = i, 2i \dots$ | $\mathcal{O}(N \log \log N)$ |
| **Stage 3** | **Summation** | `sum(phi[2:])` | $N - 1$ terms |
| **Stage 4** | **Return Value** | Return scalar integer $303963552391$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N \log \log N)$ | $\approx 0.20$ seconds for $N = 10^6$ |
| **Space Complexity** | $\mathcal{O}(N)$ | $10^6$-element integer array $\approx 8$ MB |
| **Dynamic Execution** | $100\%$ Inline | Totient sieve array summation |

### Critical Invariants & Edge Cases Handled:
1. **$d=1$ Exclusion**: Slicing `phi[2:]` skips $d=1$ (since proper fractions require $n < d \implies d \ge 2$).
2. **64-bit Summation**: Result $303\,963\,552\,391$ fits comfortably in standard 64-bit integer registers.
