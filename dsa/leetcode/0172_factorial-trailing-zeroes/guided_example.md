# Guided Example: Factorial Trailing Zeroes

We trace the step-by-step prime factor counting via Legendre's Formula for prime 5 on representative integer factorial instances:

- **Input:** $n = 28$
- **Required output:** $6$ ($28!$ has 6 trailing zeroes, contributed by factors of 5 from $5, 10, 15, 20,$ and double factor from $25$)
- **Base Power-of-Five Instance:** $n = 25 \implies 6$ ($\lfloor 25/5 \rfloor + \lfloor 25/25 \rfloor = 5 + 1 = 6$)
- **Single Unit Instance:** $n = 5 \implies 1$ ($5! = 120$)
- **Zero Result Instance:** $n = 3 \implies 0$ ($3! = 6$)

This instance demonstrates Legendre's Formula for prime multiplicity in factorials ($E_p(n!) = \sum_{k=1}^\infty \lfloor n / p^k \rfloor$), proves why prime 5 is strictly scarcer than prime 2, avoids computing massive factorials directly, and achieves $O(\log_5 N)$ logarithmic runtime in $O(1)$ space.

---

## 1. Instance & Teaching Goal

Given an integer $n = 28$:
Determine the number of trailing zeroes at the end of the decimal representation of $28!$.
The factorial value is:
$$
28! = 304,888,344,611,713,860,501,504,000,000 \implies \mathbf{6 \text{ trailing zeroes}}
$$

Calculating $n!$ directly is computationally intractable for large $n$ (e.g. $n = 10^4$ has over $35,000$ digits!).
A decimal trailing zero is created if and only if the number contains a factor of $10 = 2 \times 5$:
- In any factorial $n! = 1 \times 2 \times 3 \times \dots \times n$, every 2nd number is divisible by 2, while only every 5th number is divisible by 5.
- Factors of 2 are vastly more abundant than factors of 5.
- Therefore, the prime factor **5 is the strictly limiting factor**: each factor of 5 pairs with an available factor of 2 to create a trailing zero.
The number of trailing zeroes in $n!$ is precisely equal to the total power of 5 in the prime factorization of $n!$.

---

## 2. Conceptual Foundation & Invariants

### Legendre's Multiplicity Theorem
The exponent of a prime $p$ in the prime factorization of $n!$ is given by Legendre's Formula:
$$
E_p(n!) = \sum_{k=1}^{\infty} \left\lfloor \frac{n}{p^k} \right\rfloor = \left\lfloor \frac{n}{p} \right\rfloor + \left\lfloor \frac{n}{p^2} \right\rfloor + \left\lfloor \frac{n}{p^3} \right\rfloor + \dots
$$

For $p = 5$:
1. $\lfloor n / 5 \rfloor$ counts numbers $\le n$ that contribute at least one factor of 5 ($\{5, 10, 15, 20, 25, \dots\}$).
2. $\lfloor n / 25 \rfloor$ counts numbers $\le n$ that contribute a *second* factor of 5 ($\{25, 50, 75, \dots\}$).
3. $\lfloor n / 125 \rfloor$ counts numbers $\le n$ that contribute a *third* factor of 5 ($\{125, 250, \dots\}$).

Summing these terms accounts for the total multiplicity of 5.
The loop terminates as soon as $5^k > n$.

### Iterative Quotient Reduction Protocol
Instead of calculating large powers $5^k$, iteratively divide $n$ by 5:
Initialize $\text{zeroes} = 0$.

While $n > 0$:
$$
\text{zeroes} \leftarrow \text{zeroes} + \left\lfloor \frac{n}{5} \right\rfloor
$$
$$
n \leftarrow \left\lfloor \frac{n}{5} \right\rfloor
$$

Return $\text{zeroes}$.

> **Invariant.** At iteration $k$, the added quantity $\lfloor n / 5^k \rfloor$ counts all integers $\le N$ that contain at least $k$ prime factors of 5.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $n = 28$:

### Initialization
- $n = 28$.
- $\text{zeroes} = 0$.

---

### Iteration 1: Power $5^1 = 5$
- Compute multiples of 5:
  $$
  \text{count}_1 = \left\lfloor \frac{28}{5} \right\rfloor = \mathbf{5}
  $$
  *(Multiples in range: $5, 10, 15, 20, 25$)*.
- Accumulate:
  $$
  \text{zeroes} \leftarrow 0 + 5 = 5
  $$
- Update $n$:
  $$
  n \leftarrow \left\lfloor \frac{28}{5} \right\rfloor = \mathbf{5}
  $$

---

### Iteration 2: Power $5^2 = 25$
- Compute multiples of 25:
  $$
  \text{count}_2 = \left\lfloor \frac{5}{5} \right\rfloor = \mathbf{1}
  $$
  *(Multiple in range: $25$ contributes a second factor of 5)*.
- Accumulate:
  $$
  \text{zeroes} \leftarrow 5 + 1 = \mathbf{6}
  $$
- Update $n$:
  $$
  n \leftarrow \left\lfloor \frac{5}{5} \right\rfloor = \mathbf{1}
  $$

---

### Iteration 3: Power $5^3 = 125$
- Compute multiples of 125:
  $$
  \text{count}_3 = \left\lfloor \frac{1}{5} \right\rfloor = \mathbf{0}
  $$
- Accumulate: $\text{zeroes} = 6 + 0 = 6$.
- Update $n$:
  $$
  n \leftarrow \left\lfloor \frac{1}{5} \right\rfloor = \mathbf{0}
  $$
- $n == 0$. Loop terminates.

Final trailing zero count: $\mathbf{6}$.

---

## 4. Complete Execution Trace

```text
Input: n = 28

Iter 1: count += 28 // 5  = 5.  (numbers: 5, 10, 15, 20, 25)   total = 5
Iter 2: count += 5  // 5  = 1.  (number 25 gives extra 5)       total = 6
Iter 3: count += 1  // 5  = 0.  (n becomes 0, stop)

Result: 6 trailing zeroes
```

| Iteration $k$ | Incoming $n$ | Prime Power $5^k$ | Quotient $\lfloor n / 5 \rfloor$ | Numbers Generating This Factor | Cumulative $\text{zeroes}$ |
|:---:|:---:|:---:|:---:|:---|:---:|
| 1 | 28 | $5$ | 5 | $5, 10, 15, 20, 25$ | 5 |
| **2** | **5** | **$25$** | **1** | **$25$ (2nd factor)** | **6** |
| 3 | 1 | $125$ | 0 | None ($125 > 28$) | 6 |
| **End** | **0** | - | - | **Terminated ($n == 0$)** | **6 (Final)** |

---

## 5. Algorithmic Correctness

**Soundness.** Every trailing zero corresponds to a unique pair of prime factors $(2, 5)$. By de Polignac's / Legendre's formula, the exact exponent of prime $p$ in $n!$ is $\sum_{k=1}^\infty \lfloor n / p^k \rfloor$. Since $E_2(n!) > E_5(n!)$ for all $n \ge 1$, the number of trailing zeroes is bounded strictly by $E_5(n!)$.

**Completeness.** Dividing $n$ repeatedly by 5 computes each term $\lfloor n / 5^k \rfloor$ in order. The sequence strictly decreases and terminates when $5^k > n$. No factors of 5 can be omitted.

---

## 6. Traps This Instance Exposes

- **Missing Powers of 5:** Naively counting only $\lfloor n / 5 \rfloor$ misses the extra factors from $25, 125, 625, \dots$, undercounting $25!$ as 5 instead of 6.
- **Computing $n!$ Directly:** Attempting `math.factorial(n)` will exceed memory and time limits or crash with integer size limits in languages with fixed-width integers.
- **Base Case $n = 0$:** $0! = 1$, which has 0 trailing zeroes. The loop condition `while n > 0` handles $n = 0$ immediately, returning 0.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log_5 n)$. At each iteration, $n$ is divided by 5. For $n \le 10^4$, the loop runs at most $\lfloor \log_5(10000) \rfloor = 5$ times.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory, using only a single scalar accumulator `zeroes`.
