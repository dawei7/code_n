# Distinct Primes Factors - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Let $\omega(n)$ denote the prime omega function, which counts the number of distinct prime factors of an integer $n \in \mathbb{N}$:
$$\omega(n) = \sum_{\substack{p \mid n \\ p \in \mathbb{P}}} 1 = |\mathcal{P}(n)|$$
where $\mathcal{P}(n)$ is the set of prime divisors of $n$.

The objective is to find the first of four consecutive integers to each have four distinct prime factors:
$$x_{\text{min}} = \min \{ x \in \mathbb{N} \mid \omega(x) = \omega(x + 1) = \omega(x + 2) = \omega(x + 3) = 4 \}$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Individual Integer Factorization
A naive algorithm factors each integer $k = 2, 3, 4, \dots$ independently with trial division:
```python
def naive_distinct_prime_factors():
    # factors each integer individually
    # ...
```

### Computational Inefficiencies
1. **Redundant Factorizations $\mathcal{O}(N \sqrt{N})$**: Factoring every integer independently takes several seconds.
2. **Superiority of Omega Sieve**: Sieve-based accumulation computes $\omega(n)$ for all $n \le 200\,000$ simultaneously in $\mathcal{O}(N \log \log N)$ time ($\approx 0.03$ seconds).

---

## 3. Core Intuition & Mathematical Structure

### Small Consecutive Runs Comparison Table

| Consecutive Count $K$ | Target Factors $\omega(n)$ | Starting Term $x_{\text{min}}$ | Consecutive Terms & Prime Factorizations |
| :---: | :---: | :---: | :--- |
| **$2$** | $2$ | **$14$** | $14 = 2 \times 7$ ($\omega=2$)<br>$15 = 3 \times 5$ ($\omega=2$) |
| **$3$** | $3$ | **$644$** | $644 = 2^2 \times 7 \times 23$ ($\omega=3$)<br>$645 = 3 \times 5 \times 43$ ($\omega=3$)<br>$646 = 2 \times 17 \times 19$ ($\omega=3$) |
| **$4$** | **$4$** | **$134\,043$** | **Four Consecutive Terms** (detailed below) |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Additive Omega Sieve Algorithm
1. Allocate an array $\mathbf{\omega}$ of size $L = 200\,000$ initialized with $0$.
2. For each $i \in [2, L-1]$:
   - If $\mathbf{\omega}[i] == 0$ ($i$ is prime):
     - For all multiples $j \in \{i, 2i, 3i, \dots < L\}$:
       $$\mathbf{\omega}[j] \leftarrow \mathbf{\omega}[j] + 1$$
3. Scan indices $x \in [2, L-4]$ with a sliding counter:
   - If $\mathbf{\omega}[x] == 4$, increment `count`.
   - When `count == 4`, the first number of the 4-consecutive run is $x - 3$.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Evaluation for $K = 2$ and $K = 3$
- $K = 2 \implies 14$ ($14=2\times 7, 15=3\times 5$). Matches sample! $\checkmark$
- $K = 3 \implies 644$ ($644=2^2\times 7\times 23, 645=3\times 5\times 43, 646=2\times 17\times 19$). Matches sample! $\checkmark$

### Example 2: Target Evaluation for $K = 4$
The first 4 consecutive integers with $\omega(n) = 4$ start at $x = \mathbf{134\,043}$:
1. $134\,043 = 3 \times 7 \times 13 \times 491 \implies \omega = \mathbf{4}$
2. $134\,044 = 2^2 \times 23 \times 31 \times 47 \implies \omega = \mathbf{4}$
3. $134\,045 = 5 \times 17 \times 19 \times 83 \implies \omega = \mathbf{4}$
4. $134\,046 = 2 \times 3^2 \times 11 \times 677 \implies \omega = \mathbf{4}$

Starting Term:
$$x_{\text{min}} = \mathbf{134\,043}$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Omega Array Allocation** | `factors = [0] * limit` ($L = 200\,000$) | $\mathcal{O}(L)$ |
| **Stage 2** | **Omega Sieve** | If `factors[i] == 0`: increment multiples $j = i, 2i, \dots$ | $\mathcal{O}(L \log \log L)$ |
| **Stage 3** | **Run-Length Scan** | `if factors[i] == 4: count += 1; if count == 4: return i - 3` | $\mathcal{O}(L)$ |
| **Stage 4** | **Return Value** | Return scalar integer $134043$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(L \log \log L)$ | $\approx 0.03$ seconds for $L = 200\,000$ |
| **Space Complexity** | $\mathcal{O}(L)$ | $200\,000$-element integer array $\approx 1.5$ MB |
| **Dynamic Execution** | $100\%$ Inline | Prime omega sieve + run-length scanner |

### Critical Invariants & Edge Cases Handled:
1. **Prime Power Multiplicities**: Repeated prime factors (e.g. $2^2, 3^2$) increment $\mathbf{\omega}$ only once, correctly measuring distinct prime factors rather than total prime factors.
2. **Consecutive Reset**: If $\mathbf{\omega}[x] \neq 4$, the counter resets immediately to $0$, ensuring strict consecutiveness.
