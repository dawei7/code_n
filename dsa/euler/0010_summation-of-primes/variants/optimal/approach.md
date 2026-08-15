# Summation of Primes - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Let $\mathbb{P}_{<N} = \{ p \in \mathbb{P} \mid p < N \}$ denote the set of prime numbers strictly less than an upper bound $N \in \mathbb{N}$ ($N = 2\,000\,000$).

The objective is to compute the sum of all primes in $\mathbb{P}_{<N}$:
$$S(N) = \sum_{p \in \mathbb{P}_{<N}} p = \sum_{k=2}^{N-1} k \cdot \mathbb{I}(k \in \mathbb{P})$$
where $\mathbb{I}(k \in \mathbb{P}) \in \{0, 1\}$ is the indicator function for primality.

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Individual Trial Division
A naive approach iterates through every integer $k \in [2, N-1]$ and tests primality by dividing by all numbers up to $\sqrt{k}$:
```python
def is_prime(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))

def naive_sum_primes(limit):
    return sum(k for k in range(2, limit) if is_prime(k))
```

### Computational Inefficiencies
1. **High Asymptotic Complexity $\mathcal{O}(N^{1.5})$**: Trial division on $2 \times 10^6$ numbers performs nearly $2 \times 10^9$ division operations ($\approx 20$ seconds).
2. **Sieve Superiority**: The Sieve of Eratosthenes filters composite multiples across the entire interval in $\mathcal{O}(N \log \log N)$ operations ($\approx 0.08$ seconds).

---

## 3. Core Intuition & Mathematical Structure

By the Fundamental Theorem of Arithmetic, any composite integer $m < N$ has at least one prime factor $p \le \lfloor \sqrt{N} \rfloor$.
For $N = 2\,000\,000$, $\lfloor \sqrt{N} \rfloor = 1414$.

We only need to sieve multiples of primes $p \le 1414$. Every uncancelled number remaining in $[2, N-1]$ is guaranteed to be prime.

### Sieve Parameter Breakdown for $N = 2\,000\,000$

| Parameter | Mathematical Expression | Value |
| :--- | :--- | :--- |
| **Upper Bound $N$** | Domain limit $[0, N-1]$ | $2\,000\,000$ |
| **Sieve Outer Bound** | $\lfloor \sqrt{N} \rfloor$ | $1\,414$ |
| **Primes Sieved** | $\pi(\sqrt{N}) = \pi(1414)$ | $226$ primes |
| **Total Primes Summed** | $\pi(N) = \pi(2\,000\,000)$ | $148\,933$ primes |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### A. Memory-Efficient Byte-Array Sieving
Allocating a dense `bytearray` of size $N = 2\,000\,000$ takes only $2$ MB of memory.
For each prime $i \le 1414$:
1. Mark all multiples starting at $i^2$:
   $$j \in \{i^2, i^2 + i, i^2 + 2i, \dots, N-1\}$$
2. In Python, slice assignment `is_prime[i*i:limit:i] = bytearray([0]) * count` runs in underlying C loops.

### B. Summation via Enumeration
After sieving up to $\sqrt{N}$, sum all indices $i$ where $\text{is\_prime}[i] == 1$:
$$S(N) = \sum_{i=2}^{N-1} i \cdot \text{is\_prime}[i]$$

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Evaluation for $N = 10$
1. Domain: $[2, 9]$.
2. Outer bound: $\lfloor \sqrt{10} \rfloor = 3$.
3. Primes sieved:
   - $p = 2$: Mark multiples $4, 6, 8$.
   - $p = 3$: Mark multiple $9$.
4. Remaining primes: $\{2, 3, 5, 7\}$.
5. Sum: $2 + 3 + 5 + 7 = \mathbf{17}$. Matches sample! $\checkmark$

### Example 2: Exact Target Evaluation for $N = 2\,000\,000$
- Sieve executed up to $N = 2\,000\,000$.
- Identifies all $148\,933$ primes.
- Accumulated sum:
  $$S(2\,000\,000) = \mathbf{142\,913\,828\,922}$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Bytearray Allocation** | `is_prime = bytearray([1]) * limit` | $\mathcal{O}(N)$ |
| **Stage 2** | **Base Masking** | Set `is_prime[0] = is_prime[1] = 0` | $\mathcal{O}(1)$ |
| **Stage 3** | **C-Slice Sieving** | For $i = 2 \dots \lfloor \sqrt{N} \rfloor$: slice cancel $i^2 \dots N-1$ | $\mathcal{O}(N \log \log N)$ |
| **Stage 4** | **Index Summation** | `sum(i for i, p in enumerate(is_prime) if p)` | $\mathcal{O}(N)$ |
| **Stage 5** | **Return Value** | Return scalar integer sum | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N \log \log N)$ | $\approx 0.08$ seconds for $N = 2\,000\,000$ |
| **Space Complexity** | $\mathcal{O}(N)$ | $2$ MB `bytearray` |
| **Dynamic Execution** | $100\%$ Inline | Full Sieve of Eratosthenes |

### Critical Invariants & Edge Cases Handled:
1. **Starting at $i^2$**: Avoids redundant cancellations of multiples $k \cdot i$ with $k < i$.
2. **64-bit Accumulation**: Native Python long integers automatically handle sums exceeding $2^{31}-1$ without overflow.
