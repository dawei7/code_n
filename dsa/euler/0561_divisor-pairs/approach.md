# Divisor Pairs - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Let $S(n)$ be the number of pairs $(a, b)$ of distinct divisors of $n$ such that $a \mid b$.
Let $p_m\# = \prod_{i=1}^m p_i$ be the primorial of the first $m$ primes.
Let $E(m, n) = v_2(S((p_m\#)^n))$ be the 2-adic valuation of $S((p_m\#)^n)$.
Let $Q(n) = \sum_{i=1}^n E(904961, i)$.

We are given:
- $S(6) = 5 \implies E(2, 1) = 0$
- $Q(8) = 2714886$

We seek to evaluate:

$$
Q(10^{12})
$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Direct Iteration over $10^{12}$ Terms
Evaluating $E(m, i)$ sequentially for each $i \le 10^{12}$ would take millions of seconds.

---

## 3. Core Intuition & Mathematical Structure

### Divisor Pair Formula & 2-Adic Valuation
1. **Combinatorial Divisor Pair Formula**:
   For $N = (p_m\#)^n$, each prime factor has multiplicity $n$.
   The number of pairs $(a, b)$ with $a \mid b$ is $\binom{n+2}{2}^m$, so:

$$
S((p_m\#)^n) = \frac{(n+1)^m}{2^m} \left( (n+2)^m - 2^m \right)
$$

2. **2-Adic Splitting**:
   - **For odd $n$**: $(n+2)^m$ is odd and $2^m$ is even, so $(n+2)^m - 2^m$ is odd.

$$
E(m, n) = m(v_2(n+1) - 1)
$$

   - **For even $n = 2k$**: by the Lifting the Exponent Lemma (LTE) with odd $m = 904961$:

$$
v_2((2k+2)^m - 2^m) = m + v_2((k+1)^m - 1) = m + v_2(k)
$$

$$
E(m, 2k) = v_2(k) = v_2(n/2)
$$

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Legendre's $O(1)$ Summation Identity
1. **Sum of 2-Adic Valuations**:
   By Legendre's formula, the sum of $v_2(k)$ over $k \in [1, K]$ is:

$$
\sum_{k=1}^K v_2(k) = v_2(K!) = K - s_2(K)
$$

   where $s_2(K)$ is the binary popcount (number of 1s in the binary representation of $K$).
2. **Closed-Form Formula for $Q(N)$**:
   Let $K_1 = \lfloor (N+1)/2 \rfloor$ and $K_2 = \lfloor N/2 \rfloor$.

$$
Q(N) = m (K_1 - s_2(K_1)) + (K_2 - s_2(K_2))
$$

This evaluates $Q(10^{12})$ in **$O(1)$ time (< 1 microsecond)**!

---

## 5. Concrete Step-by-Step Example Walkthrough

### Verification of Small Samples
- $n = 8 \implies K_1 = 4, K_2 = 4$.
- $s_2(4) = 1$.
- $Q(8) = 904961 \times (4 - 1) + (4 - 1) = 3(904961) + 3 = 2714886$ ($\checkmark$).
- $Q(10^{12}) = 452480999988235494$ ($\checkmark$).

---

## 6. Implementation Architecture & Algorithmic Blueprint

```
[Define K1 = (n + 1) // 2 and K2 = n // 2]
                   │
                   ▼
[Evaluate Legendre valuations: odd_sum = m * (K1 - popcount(K1)), even_sum = K2 - popcount(K2)]
                   │
                   ▼
[Return odd_sum + even_sum = 452480999988235494]
```

---

## 7. Mathematical Complexity & Edge Case Invariants

### Complexity Analysis
- **Domain Size**: $n = 10^{12}, m = 904961$.
- **Time Complexity**: $O(1) \approx 0.000001\text{ seconds}$ in pure Python.
- **Space Complexity**: $O(1)$ memory.

### Invariants Handled
- **Exact LTE Invariance**: The algebraic identity $v_2((k+1)^m - 1) = v_2(k)$ holds identically for all odd integers $m$.
- **100% Dynamic Execution**: Pure Python $O(1)$ Legendre popcount reduction with zero hardcoded literals.
