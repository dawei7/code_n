# Smallest Multiple - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Let $\mathcal{S}_N = \{ 1, 2, 3, \dots, N \}$ denote the set of consecutive natural numbers up to $N \in \mathbb{N}$.

The objective is to evaluate the Least Common Multiple (LCM) across all elements in $\mathcal{S}_N$:

$$
L(N) = \operatorname{lcm}(\mathcal{S}_N) = \operatorname{lcm}(1, 2, 3, \dots, N)
$$

Formally, $L(N)$ is the unique minimal positive integer divisible by every $k \in \mathcal{S}_N$:

$$
L(N) = \min \{ m \in \mathbb{N}^+ \mid \forall k \in [1, N], \, k \mid m \}
$$

We must compute $L(20)$.

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Naive Multiples Testing
A naive algorithm increments candidate multiples of $N$ ($x = N, 2N, 3N, \dots$) and checks divisibility by every $k \in [1, N]$:
```python
def naive_smallest_multiple(n):
    x = n
    while True:
        if all(x % k == 0 for k in range(1, n + 1)):
            return x
        x += n
```

### Computational Inefficiencies
1. **Astronomic Search Space**: For $N = 20$, $L(20) = 232\,792\,560$, requiring over $11.6$ million iterations and $>1.5 \times 10^8$ modulo operations.
2. **Exponential Blowup**: For $N = 50$, $L(50) \approx 3.09 \times 10^{19}$, causing naive candidate testing to take billions of CPU years.

---

## 3. Core Intuition & Mathematical Structure

By the Fundamental Theorem of Arithmetic, every integer has a unique prime factorization. The LCM of a set of integers is the product of each prime raised to its **maximum exponent** present in any number in the set.

For $k \le N$, the highest power of prime $p$ that does not exceed $N$ is:

$$
a_p = \max \{ e \in \mathbb{N} \mid p^e \le N \} = \lfloor \log_p N \rfloor
$$

### Prime Exponent Decomposition for $N = 20$

| Prime $p$ | Formula $a_p = \lfloor \log_p 20 \rfloor$ | Exponent $a_p$ | Maximal Prime Power $p^{a_p}$ |
| :---: | :---: | :---: | :---: |
| **$2$** | $\lfloor \log_2 20 \rfloor = \lfloor 4.32 \rfloor$ | $4$ | $2^4 = 16$ |
| **$3$** | $\lfloor \log_3 20 \rfloor = \lfloor 2.73 \rfloor$ | $2$ | $3^2 = 9$ |
| **$5$** | $\lfloor \log_5 20 \rfloor = \lfloor 1.86 \rfloor$ | $1$ | $5^1 = 5$ |
| **$7$** | $\lfloor \log_7 20 \rfloor = \lfloor 1.54 \rfloor$ | $1$ | $7^1 = 7$ |
| **$11$** | $\lfloor \log_{11} 20 \rfloor = \lfloor 1.25 \rfloor$ | $1$ | $11^1 = 11$ |
| **$13$** | $\lfloor \log_{13} 20 \rfloor = \lfloor 1.17 \rfloor$ | $1$ | $13^1 = 13$ |
| **$17$** | $\lfloor \log_{17} 20 \rfloor = \lfloor 1.06 \rfloor$ | $1$ | $17^1 = 17$ |
| **$19$** | $\lfloor \log_{19} 20 \rfloor = \lfloor 1.02 \rfloor$ | $1$ | $19^1 = 19$ |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### A. Prime Power Product Formula
The global LCM is given exactly by:

$$
\begin{aligned}
L(N) = \prod_{\substack{p \le N \\ p \in \mathbb{P}}} p^{\lfloor \log_p N \rfloor}
\end{aligned}
$$

### B. Associative Iteration via Euclidean GCD
Alternatively, using the associativity of the binary LCM operator:

$$
\operatorname{lcm}(a_1, a_2, \dots, a_k) = \operatorname{lcm}(\operatorname{lcm}(a_1, \dots, a_{k-1}), a_k)
$$

where binary LCM is computed via the Euclidean Greatest Common Divisor (GCD):

$$
\operatorname{lcm}(a, b) = \frac{a \cdot b}{\gcd(a, b)}
$$

Using the Euclidean Algorithm, each step executes in $\mathcal{O}(\log(\min(a, b)))$ arithmetic operations.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Evaluation for $N = 10$
- Primes $\le 10$: $\{2, 3, 5, 7\}$.
- Powers: $2^{\lfloor \log_2 10 \rfloor} = 2^3 = 8$, $3^{\lfloor \log_3 10 \rfloor} = 3^2 = 9$, $5^1 = 5$, $7^1 = 7$.
- Product: $L(10) = 8 \times 9 \times 5 \times 7 = \mathbf{2520}$. Matches sample! $\checkmark$

### Example 2: Exact Evaluation for $N = 20$
Evaluating the product of maximal prime powers:

$$
L(20) = 16 \times 9 \times 5 \times 7 \times 11 \times 13 \times 17 \times 19 = \mathbf{232\,792\,560}
$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Accumulator Initialization** | Set $\text{ans} = 1$ | $\mathcal{O}(1)$ |
| **Stage 2** | **Sequential Reduction** | For $k = 2 \dots N$: $\text{ans} \leftarrow (\text{ans} \cdot k) // \gcd(\text{ans}, k)$ | $\mathcal{O}(N \log N)$ |
| **Stage 3** | **Return Value** | Return scalar integer $\text{ans}$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N \log N)$ | $\approx 0.00002$ seconds for $N = 20$ |
| **Space Complexity** | $\mathcal{O}(1)$ | Single integer accumulator |
| **Dynamic Execution** | $100\%$ Inline | Euclidean reduction loop |

### Critical Invariants & Edge Cases Handled:
1. **Exact Divisibility Guarantee**: Division by $\gcd(\text{ans}, k)$ always yields a remainder of 0.
2. **Arbitrary Precision**: Python handles arbitrarily large values of $L(N)$ without 64-bit integer overflow.