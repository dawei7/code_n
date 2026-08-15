# Totient Maximum - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Euler's totient function $\phi(n)$ counts the number of positive integers $k \le n$ that are relatively prime to $n$ ($\gcd(k, n) = 1$).

For example, for $n \le 10$:
- $n = 6 \implies \phi(6) = 2 \implies \frac{n}{\phi(n)} = \frac{6}{2} = 3$ (maximum for $n \le 10$).

The objective is to find the value of $n \le 1\,000\,000$ for which $\frac{n}{\phi(n)}$ is maximized:
$$n_{\text{max}} = \operatorname*{arg\,max}_{2 \le n \le 1000000} \frac{n}{\phi(n)}$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Full Range Totient Sieve
A naive approach computes $\phi(n)$ for all $n \le 1\,000\,000$ using a linear sieve and scans for the maximum ratio:
```python
def naive_totient_max():
    # builds 1,000,000-element totient sieve array
    # ...
```

### Analytical Inversion via Euler's Product Formula
By Euler's totient product formula:
$$\phi(n) = n \prod_{p \mid n} \left( 1 - \frac{1}{p} \right) = n \prod_{p \mid n} \frac{p - 1}{p}$$
Inverting both sides:
$$\frac{n}{\phi(n)} = \prod_{p \mid n} \frac{p}{p - 1}$$

1. Each prime factor $p$ contributes a factor $\frac{p}{p - 1} > 1$.
2. Smaller primes contribute strictly larger multipliers:
   $$\frac{2}{1} = 2.0 > \frac{3}{2} = 1.5 > \frac{5}{4} = 1.25 > \frac{7}{6} \approx 1.167 > \dots$$
3. Therefore, to maximize $\frac{n}{\phi(n)}$ under the constraint $n \le 1\,000\,000$, $n$ MUST be the product of the smallest consecutive primes (a **primorial number** $p_k\#$).

---

## 3. Core Intuition & Mathematical Structure

### Primorial Number Sequence & Totient Ratio Growth

| Primorial $p_k\#$ | Product Formulation | Numerical Value | Totient Ratio $\frac{n}{\phi(n)} = \prod \frac{p}{p-1}$ | Under $1\,000\,000$? |
| :---: | :--- | :---: | :---: | :---: |
| **$p_1\#$** | $2$ | $2$ | $\frac{2}{1} = 2.000$ | Yes $\checkmark$ |
| **$p_2\#$** | $2 \times 3$ | $6$ | $2 \times 1.5 = \mathbf{3.000}$ | **Yes (Max for $n \le 10$)** |
| **$p_3\#$** | $2 \times 3 \times 5$ | $30$ | $3 \times 1.25 = 3.750$ | Yes $\checkmark$ |
| **$p_4\#$** | $30 \times 7$ | $210$ | $3.75 \times \frac{7}{6} = 4.375$ | Yes $\checkmark$ |
| **$p_5\#$** | $210 \times 11$ | $2\,310$ | $4.375 \times \frac{11}{10} = 4.8125$ | Yes $\checkmark$ |
| **$p_6\#$** | $2310 \times 13$ | $30\,030$ | $4.8125 \times \frac{13}{12} \approx 5.2135$ | Yes $\checkmark$ |
| **$p_7\#$** | $30030 \times 17$ | **$510\,510$** | $5.2135 \times \frac{17}{16} \approx \mathbf{5.5394}$ | **Yes (Global Max)** |
| **$p_8\#$** | $510510 \times 19$ | $9\,699\,690$ | $\approx 5.8471$ | No ($> 10^6$) |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Primorial Product Algorithm
1. Initialize $n = 1$.
2. Iterate through consecutive primes $p \in (2, 3, 5, 7, 11, 13, 17, 19, \dots)$:
   - If $n \cdot p > 1\,000\,000$, break.
   - $n \leftarrow n \cdot p$.
3. The resulting product is $n_{\text{max}} = 510\,510$, evaluated in 7 multiplications in $\mathcal{O}(1)$ time.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Trace for $n \le 10$
- $p_1\# = 2 \implies \frac{2}{\phi(2)} = 2$.
- $p_2\# = 2 \times 3 = 6 \implies \frac{6}{\phi(6)} = \mathbf{3}$.
- $p_3\# = 6 \times 5 = 30 > 10$.
- $n = 6$ maximizes ratio for $n \le 10$. Matches problem statement sample! $\checkmark$

### Example 2: Target Evaluation for $n \le 1\,000\,000$
- $n = 2 \times 3 \times 5 \times 7 \times 11 \times 13 \times 17 = \mathbf{510\,510}$.
- Next prime is $19 \implies 510510 \times 19 = 9699690 > 10^6$.
- Maximum Ratio Integer:
  $$n_{\text{max}} = \mathbf{510\,510}$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Primes List** | `primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]` | $\mathcal{O}(1)$ |
| **Stage 2** | **Product Loop** | For $p$ in primes: if $n \cdot p > 10^6$, break; $n *= p$ | $7$ multiplications |
| **Stage 3** | **Return Value** | Return scalar integer $510510$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(1)$ | $\approx 0.0000$ seconds |
| **Space Complexity** | $\mathcal{O}(1)$ | Scalar integer registers |
| **Dynamic Execution** | $100\%$ Inline | Primorial product accumulation |

### Critical Invariants & Edge Cases Handled:
1. **Multiplicity Invariance**: Prime powers $p^k$ do not increase the ratio $\frac{p^k}{\phi(p^k)} = \frac{p}{p-1}$, proving that distinct square-free primes are strictly optimal.
2. **Consecutive Primorial Maximality**: Any replacement of a small prime with a larger prime strictly reduces the ratio product.
