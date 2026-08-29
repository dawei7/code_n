# Amicable Numbers - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Let $d(n)$ denote the sum of the proper divisors of $n$ (divisors strictly less than $n$):

$$
\begin{aligned}
d(n) = \sum_{\substack{k \mid n \\ 1 \le k < n}} k = \sigma_1(n) - n
\end{aligned}
$$

where $\sigma_1(n)$ is the sum of all positive divisors of $n$.

Two distinct positive integers $a, b \in \mathbb{N}$ form an **amicable pair** $(a, b)$ if:

$$
d(a) = b \quad \land \quad d(b) = a \quad \text{with } a \neq b
$$

Each number in an amicable pair is called an **amicable number**.

The objective is to compute the sum of all amicable numbers strictly less than $10\,000$:

$$
S(10\,000) = \sum_{a=2}^{9999} a \cdot \mathbb{I}\left( d(a) \neq a \land d(a) < 10\,000 \land d(d(a)) = a \right)
$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Individual Factorization of Every Integer
A naive algorithm computes proper divisor sums independently for each candidate $a$ and recomputes for $b = d(a)$:
```python
def naive_proper_sum(n):
    return sum(i for i in range(1, n) if n % i == 0)
```

### Computational Inefficiencies
1. **Redundant Iterations $\mathcal{O}(N^2)$**: Trial division across all $N$ numbers evaluates millions of modulo operations.
2. **Superiority of Sieve Method**: Sieve-based accumulation computes $d(n)$ for all $n < N$ simultaneously in harmonic $\mathcal{O}(N \log N)$ time ($\approx 0.002$ seconds).

---

## 3. Core Intuition & Mathematical Structure

Instead of factoring each number $n$, we turn the operation inside out:
For each potential divisor $i \in [1, N-1]$, we add $i$ to all of its strictly larger multiples:

$$
j \in \{2i, 3i, 4i, \dots < N\}
$$

By the harmonic series identity:

$$
\sum_{i=1}^N \frac{N}{i} = N \sum_{i=1}^N \frac{1}{i} = \mathcal{O}(N \ln N)
$$

### Amicable Pairs Under $10\,000$

| Pair $(a, b)$ | $d(a)$ Calculation | $d(b)$ Calculation | Pair Sum $a + b$ |
| :---: | :---: | :---: | :---: |
| **$(220, 284)$** | $d(220) = 1+2+4+5+10+11+20+22+44+55+110 = 284$ | $d(284) = 1+2+4+71+142 = 220$ | $504$ |
| **$(1184, 1210)$** | $d(1184) = 1210$ | $d(1210) = 1184$ | $2394$ |
| **$(2620, 2924)$** | $d(2620) = 2924$ | $d(2924) = 2620$ | $5544$ |
| **$(5020, 5564)$** | $d(5020) = 5564$ | $d(5564) = 5020$ | $10584$ |
| **$(6232, 6368)$** | $d(6232) = 6368$ | $d(6368) = 6232$ | $12600$ |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Harmonic Divisor Sieve
1. Allocate an array $D$ of size $N = 10\,000$ initialized with $0$.
2. For each $i = 1 \dots N-1$:

$$
D[j] \leftarrow D[j] + i \quad \text{for } j \in \{2i, 3i, \dots, N-1\}
$$

3. After completing the sieve, each $D[a]$ contains the exact sum of proper divisors $d(a)$.
4. For each $a \in [2, N-1]$, let $b = D[a]$. If $b \neq a$, $b < N$, and $D[b] == a$, then $a$ is an amicable number.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Trace for Amicable Pair $(220, 284)$
- Divisors of $220$: $1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110 \implies \text{Sum} = 284$.
- Divisors of $284$: $1, 2, 4, 71, 142 \implies \text{Sum} = 220$.
- Because $d(220) = 284$, $d(284) = 220$, and $220 \neq 284$, both are amicable! $\checkmark$

### Example 2: Target Evaluation Under $10\,000$
Summing all elements in the 5 amicable pairs under $10\,000$:

$$
S(10\,000) = (220 + 284) + (1184 + 1210) + (2620 + 2924) + (5020 + 5564) + (6232 + 6368) = \mathbf{31\,626}
$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Array Allocation** | `d = [0] * limit` | $\mathcal{O}(N)$ |
| **Stage 2** | **Harmonic Sieve** | For $i = 1 \dots N-1$: add $i$ to multiples $2i \dots N-1$ | $\mathcal{O}(N \log N)$ |
| **Stage 3** | **Amicability Check** | For $a = 2 \dots N-1$: test $b \neq a \land b < N \land d[b] == a$ | $\mathcal{O}(N)$ |
| **Stage 4** | **Return Sum** | Return scalar integer $31626$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N \log N)$ | $\approx 0.002$ seconds for $N = 10\,000$ |
| **Space Complexity** | $\mathcal{O}(N)$ | $10\,000$-element integer array $\approx 80$ KB |
| **Dynamic Execution** | $100\%$ Inline | Harmonic divisor sieve |

### Critical Invariants & Edge Cases Handled:
1. **Self-Amicable (Perfect Numbers) Exclusion**: Condition $b \neq a$ explicitly excludes perfect numbers where $d(a) = a$ (such as $6, 28, 496, 8128$).
2. **Boundary Protection**: Condition $b < \text{limit}$ ensures no out-of-bounds indexing occurs when $d(a) \ge 10\,000$.