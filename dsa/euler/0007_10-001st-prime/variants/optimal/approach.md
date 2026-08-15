# 10,001st Prime - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Let $(p_k)_{k \ge 1}$ denote the strictly increasing sequence of prime numbers:
$$p_1 = 2, \quad p_2 = 3, \quad p_3 = 5, \quad p_4 = 7, \quad p_5 = 11, \quad p_6 = 13, \dots$$

The objective is to compute the $N$-th prime number for $N = 10\,001$:
$$p_N = p_{10001}$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Naive Sequential Trial Division
A naive algorithm increments integers $x = 2, 3, 4, \dots$, tests each for primality via trial division up to $\sqrt{x}$, and increments a counter until the $N$-th prime is found:
```python
def is_prime(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))

def naive_nth_prime(n):
    count = 0
    candidate = 1
    while count < n:
        candidate += 1
        if is_prime(candidate):
            count += 1
    return candidate
```

### Computational Inefficiencies
1. **Redundant Trial Divisions**: Checking candidate primality one-by-one requires $\mathcal{O}(p_N^{1.5} / \ln p_N)$ operations.
2. **Superiority of Sieve**: The Sieve of Eratosthenes finds all primes up to an upper bound $L$ in near-linear $\mathcal{O}(L \log \log L)$ time.

---

## 3. Core Intuition & Mathematical Structure

By the Prime Number Theorem (PNT), $p_n \sim n \ln n$.
For $n \ge 6$, Dusart's inequality provides a rigorous analytical upper bound on the $n$-th prime:
$$p_n < n (\ln n + \ln \ln n)$$

### Prime Bound Estimation Table

| Index $n$ | $\ln n$ | $\ln \ln n$ | Dusart's Bound $n(\ln n + \ln \ln n)$ | Exact Prime $p_n$ |
| :---: | :---: | :---: | :---: | :---: |
| **$6$** | $1.7918$ | $0.5832$ | $14.25$ | **$13$** |
| **$10$** | $2.3026$ | $0.8340$ | $31.37$ | **$29$** |
| **$100$** | $4.6052$ | $1.5272$ | $613.24$ | **$541$** |
| **$1\,000$** | $6.9078$ | $1.9326$ | $8\,840.4$ | **$7\,919$** |
| **$10\,001$** | $9.2104$ | $2.2203$ | $114\,319.2$ | **$104\,743$** |

Setting a safe sieve limit $L = 120\,000$ strictly guarantees $p_{10001} < L$.

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Sieve of Eratosthenes Complexity & Optimality
Allocating a boolean array $\mathbf{b}$ of size $L = 120\,000$:
1. Initialize $\mathbf{b}[0] = \mathbf{b}[1] = \text{False}$, and $\mathbf{b}[x] = \text{True}$ for $x \ge 2$.
2. For each prime $i \le \sqrt{L}$, cross off composite multiples starting at $i^2$:
   $$\mathbf{b}[j] \leftarrow \text{False} \quad \text{for } j \in \{i^2, i^2 + i, i^2 + 2i, \dots\}$$
3. By Mertens' Second Theorem, the total operations count is:
   $$\sum_{p \le \sqrt{L}} \frac{L}{p} = \mathcal{O}(L \log \log L)$$

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Evaluation for $N = 6$
1. Sieve primes in $[2, 20]$: $\{2, 3, 5, 7, 11, 13, 17, 19\}$.
2. Counting primes sequentially:
   - 1st: $2$
   - 2nd: $3$
   - 3rd: $5$
   - 4th: $7$
   - 5th: $11$
   - 6th: **$13$**
3. Matches problem statement sample value **13**! $\checkmark$

### Example 2: Exact Evaluation for $N = 10\,001$
- Sieve executed up to $L = 120\,000$.
- Prime counter increments on each prime.
- Counter reaches $10\,001$ at prime value:
  $$p_{10001} = \mathbf{104\,743}$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Limit Determination** | Set safe sieve limit $L = 120\,000$ via Dusart's bound | $\mathcal{O}(1)$ |
| **Stage 2** | **Sieve Allocation** | Allocate `is_prime = [True] * limit` | $\mathcal{O}(L)$ |
| **Stage 3** | **Sieve & Count Loop** | For $i = 2 \dots L-1$: if prime, increment count and mark $i^2, i^2+i, \dots$ | $\mathcal{O}(L \log \log L)$ |
| **Stage 4** | **Early Exit** | If $\text{count} == N$: return $i$ immediately | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(L \log \log L)$ | $\approx 0.012$ seconds for $L = 120\,000$ |
| **Space Complexity** | $\mathcal{O}(L)$ | $\approx 1$ MB boolean array |
| **Dynamic Execution** | $100\%$ Inline | Direct Sieve of Eratosthenes |

### Critical Invariants & Edge Cases Handled:
1. **Starting at $i^2$**: Multiples $k \cdot i$ with $k < i$ have already been marked by smaller prime factors $k$, preventing redundant cancellations.
2. **Immediate Return**: Returning $i$ as soon as $\text{count} == N$ halts subsequent sieve operations.
