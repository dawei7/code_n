# Maximum Product of Parts - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Let $N$ be a positive integer and let $N$ be split into $k$ equal parts, $r = N/k$, so that $N = r + r + \dots + r$.
Let $P = r^k = \left(\frac{N}{k}\right)^k$ be the product of the parts.

For a given $N$, let $M(N) = \max_{k \ge 1} \left(\frac{N}{k}\right)^k$ be the maximum product that can be obtained by splitting $N$ into $k$ equal parts.

We define:
$$D(N) = \begin{cases} -N & \text{if } M(N) \text{ is a terminating decimal} \\ +N & \text{if } M(N) \text{ is a non-terminating decimal} \end{cases}$$

For example, for $N = 11$:
- $k = 4 \implies P(11, 4) = (11/4)^4 = 2.75^4 = 57.19140625$ (terminating) $\implies D(11) = -11$.
For $N = 8$:
- $k = 3 \implies P(8, 3) = (8/3)^3 = 512/27 = 18.96296296\dots$ (non-terminating) $\implies D(8) = +8$.

The objective is to find **$\sum_{N=5}^{10\,000} D(N)$**:
$$S_{\text{parts}} = \sum_{N=5}^{10\,000} D(N)$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Exhaustive Float Comparison
A naive approach computes $P(N, k)$ using high-precision floats for all $k \in [1, N]$:
```python
def naive_max_product():
    # Arbitrary precision float arithmetic for 10,000 values takes tens of seconds
    # ...
```

### Continuous Calculus & Base-10 Prime Reduction
1. **Continuous Maximization of $P(N, k)$:**
   Consider $f(k) = \ln P(N, k) = k(\ln N - \ln k)$.
   Differentiating with respect to $k$:
   $$f'(k) = (\ln N - \ln k) + k \cdot \left(-\frac{1}{k}\right) = \ln\left(\frac{N}{k}\right) - 1$$
   Setting $f'(k) = 0 \implies \ln(N / k) = 1 \implies \mathbf{k = \frac{N}{e}}$ where $e \approx 2.718281828\dots$
2. **Integer Candidates:**
   The optimal integer $k$ is either $k_1 = \lfloor N / e \rfloor$ or $k_2 = k_1 + 1 = \lceil N / e \rceil$.
   We simply compare $k_1 \ln(N / k_1)$ with $k_2 \ln(N / k_2)$.
3. **Terminating Decimal Criterion:**
   $\left(\frac{N}{k}\right)^k$ is a terminating decimal in base 10 iff the denominator of the reduced fraction $\frac{N}{k}$ has no prime factors other than $2$ and $5$:
   $$d = \frac{k}{\gcd(N, k)}$$
   Dividing out all factors of 2 and 5:
   - If $d = 1 \implies$ terminating $\implies D(N) = -N$.
   - If $d > 1 \implies$ non-terminating $\implies D(N) = +N$.
4. Evaluating $N \in [5, 10\,000]$ takes $\approx 0.01$ seconds.

---

## 3. Core Intuition & Mathematical Structure

### Optimal Parts Count $k \approx N/e$ and Decimal Type for Sample Integers

| Integer $N$ | Real Peak $N/e$ | Candidate $k$ | Maximum Product $M(N) = (N/k)^k$ | Reduced Denominator $d$ | Decimal Type | $D(N)$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$N = 5$** | $5/e \approx 1.84$ | $k = 2$ | $(5/2)^2 = 2.5^2 = 6.25$ | $2 / \gcd(5, 2) = 2 \implies 1$ | Terminating | **$-5$** |
| **$N = 6$** | $6/e \approx 2.21$ | $k = 2$ | $(6/2)^2 = 3^2 = 9$ | $2 / \gcd(6, 2) = 1$ | Terminating | **$-6$** |
| **$N = 7$** | $7/e \approx 2.58$ | $k = 3$ | $(7/3)^3 = 343/27 = 12.\overline{703}$ | $3 / \gcd(7, 3) = 3$ | Non-Terminating | **$+7$** |
| **$N = 8$** | $8/e \approx 2.94$ | $k = 3$ | $(8/3)^3 = 512/27 = 18.\overline{962}$ | $3 / \gcd(8, 3) = 3$ | Non-Terminating | **$+8$ (Sample)** |
| **$N = 9$** | $9/e \approx 3.31$ | $k = 3$ | $(9/3)^3 = 3^3 = 27$ | $3 / \gcd(9, 3) = 1$ | Terminating | **$-9$** |
| **$N = 10$** | $10/e \approx 3.68$ | $k = 4$ | $(10/4)^4 = 2.5^4 = 39.0625$ | $4 / \gcd(10, 4) = 2 \implies 1$ | Terminating | **$-10$** |
| **$N = 11$** | $11/e \approx 4.05$ | $k = 4$ | $(11/4)^4 = 2.75^4 = 57.19140625$ | $4 / \gcd(11, 4) = 4 \implies 1$ | Terminating | **$-11$ (Sample)** |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Master Optimization Pipeline
```python
def solve(max_n: int = 10000) -> int:
    E = math.e
    total = 0
    for N in range(5, max_n + 1):
        k1 = int(N / E)
        k2 = k1 + 1
        k = k1 if k1 * math.log(N / k1) > k2 * math.log(N / k2) else k2

        d = k // math.gcd(N, k)
        while d % 2 == 0:
            d //= 2
        while d % 5 == 0:
            d //= 5

        total += -N if d == 1 else N
    return total
```
Evaluating for $N \le 10\,000$:
$$S_{\text{parts}} = \mathbf{48\,861\,552}$$

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Sample Verification for $N = 11$
- $11 / e \approx 4.0467$.
- $k_1 = 4 \implies 4 \ln(11/4) = 4 \ln(2.75) \approx 4.0464$.
- $k_2 = 5 \implies 5 \ln(11/5) = 5 \ln(2.2) \approx 3.9423$.
- Optimal $k = 4$.
- $\gcd(11, 4) = 1 \implies d = 4$.
- Dividing factors of 2: $4 \to 2 \to 1 \implies$ Terminating!
- $D(11) = -11$. Matches problem statement sample! $\checkmark$

### Example 2: Target Evaluation for $5 \le N \le 10\,000$
- Summing over all $N \in [5, 10\,000]$:
  $$S_{\text{parts}} = \mathbf{48\,861\,552}$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Integer Loop** | For $N \in [5, 10\,000]$ | $9996$ values |
| **Stage 2** | **Continuous Peak** | $k_1 = \lfloor N/e \rfloor, k_2 = k_1 + 1$ | $\mathcal{O}(1)$ |
| **Stage 3** | **Log Comparison** | `k1 * log(N/k1) vs k2 * log(N/k2)` | $\mathcal{O}(1)$ |
| **Stage 4** | **GCD Reduction** | $d = k // \gcd(N, k)$ | $\mathcal{O}(\log N)$ |
| **Stage 5** | **2 and 5 Sieve** | `while d%2 == 0: d//=2; while d%5 == 0: d//=5` | $\mathcal{O}(\log d)$ |
| **Stage 6** | **Tally Sign** | `total += -N if d == 1 else N` | $\mathcal{O}(1)$ |
| **Stage 7** | **Return Sum** | Return scalar integer $48861552$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N \log N)$ where $N = 10^4$ | $\approx 0.01$ seconds |
| **Space Complexity** | $\mathcal{O}(1)$ | Constant variables |
| **Dynamic Execution** | $100\%$ Inline | Continuous calculus optimization with 2-adic and 5-adic fraction reduction |

### Critical Invariants & Edge Cases Handled:
1. **Unambiguous Peak Comparison**: Using log products $k \ln(N/k)$ avoids power overflow ($N^k$ exceeds standard double precision float ranges).
2. **Exact Base-10 Divisibility**: Checking $d=1$ after stripping 2 and 5 is mathematically equivalent to testing whether the decimal representation terminates.
