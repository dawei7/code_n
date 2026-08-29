# Twenty-Two Foolish Primes - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

A set of $100$ disks numbered $1$ to $100$ are arranged in a random line (a uniform permutation of $\{1, 2, \dots, 100\}$).
- There are $\pi(100) = 25$ prime numbers $\le 100$.
- A prime disk is called **foolish** if it is **not** in its original natural position (i.e. disk $p$ is not at position $p$).
- Non-prime disks may be in any position.

Find the probability that **exactly $22$ prime disks are foolish** (meaning exactly $25 - 22 = 3$ prime disks are in their natural positions, and the other 22 are displaced).
Give your answer rounded to $12$ decimal places in the form `0.abcdefghijkl`.

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Monte Carlo Permutation Sampling
A naive simulation samples random permutations of $100$ items:
```python
def naive_monte_carlo_primes():
    # 100! approx 9.33 * 10^157 total permutations
    # Measuring a probability of order 10^-3 to 12 decimal places requires > 10^24 samples
    # ...
```

### Generalized Partial Derangements via Inclusion-Exclusion
1. **Selection of Fixed Primes:**
   There are $\binom{25}{3}$ ways to choose which $3$ prime disks remain in their natural positions.
2. **Constrained Permutations of the Remaining 97 Positions:**
   The remaining $22$ prime disks must all be displaced from their natural positions among the $97$ available slots.
   Let $A_i$ be the event that the $i$-th remaining prime disk is at its natural position ($i = 1 \dots 22$).
   By the Principle of Inclusion-Exclusion:

$$
N_{\text{deranged}} = \sum_{m=0}^{22} (-1)^m \binom{22}{m} (97 - m)!
$$

3. **Exact Probability Ratio:**

$$
\text{Prob} = \frac{\binom{25}{3} \sum_{m=0}^{22} (-1)^m \binom{22}{m} (97 - m)!}{100!}
$$

   Evaluating with 50-digit `Decimal` arithmetic gives the exact 12-decimal value in $< 0.001$ seconds.

---

## 3. Core Intuition & Mathematical Structure

### Inclusion-Exclusion Term Decomposition ($m = 0 \dots 4$)

| $m$ (Extra Fixed Primes) | Sign $(-1)^m$ | Combination $\binom{22}{m}$ | Factorial $(97 - m)!$ | Term Value $(-1)^m \binom{22}{m} (97-m)!$ |
| :---: | :---: | :---: | :---: | :---: |
| **$m = 0$** | $+1$ | $1$ | $97!$ | $+97!$ |
| **$m = 1$** | $-1$ | $22$ | $96!$ | $-22 \times 96!$ |
| **$m = 2$** | $+1$ | $231$ | $95!$ | $+231 \times 95!$ |
| **$m = 3$** | $-1$ | $1540$ | $94!$ | $-1540 \times 94!$ |
| **$m = 4$** | $+1$ | $7315$ | $93!$ | $+7315 \times 93!$ |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Master Inclusion-Exclusion Probability Formula
```python
def solve(total_disks: int = 100, num_primes: int = 25, foolish: int = 22) -> str:
    fixed_primes = num_primes - foolish  # 3
    ways_choose_fixed = math.comb(num_primes, fixed_primes)

    sum_terms = sum(
        ((-1) ** m)
        * math.comb(foolish, m)
        * math.factorial(total_disks - fixed_primes - m)
        for m in range(foolish + 1)
    )

    prob = (ways_choose_fixed * sum_terms) / math.factorial(total_disks)
    return f"{prob:.12f}"
```

Evaluating for $100$ disks:

$$
\text{Probability} = \mathbf{0.001887854841}
$$

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Combinatorial Multiplier
- $\binom{25}{3} = \frac{25 \times 24 \times 23}{3 \times 2 \times 1} = 2300$ ways to choose the $3$ fixed primes.

### Example 2: Normalization by $100!$
- Dividing by $100! = 100 \times 99 \times 98 \times 97!$:

$$
\frac{97!}{100!} = \frac{1}{100 \times 99 \times 98} = \frac{1}{970\,200}
$$

- $\frac{2300}{970\,200} = \frac{23}{9702} \approx 0.002370645$.
- Multiplied by the derangement alternating series $\sum_{m=0}^{22} \frac{(-1)^m \binom{22}{m}}{97 \times 96 \dots (98-m)} \approx 0.796345$:

$$
\text{Prob} = \mathbf{0.001887854841} \quad (\checkmark)
$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Combinations** | Compute $\binom{25}{3} = 2300$ | $\mathcal{O}(1)$ |
| **Stage 2** | **Alternating Sum** | Sum $m = 0 \dots 22$ of $(-1)^m \binom{22}{m} (97 - m)!$ | $23$ terms |
| **Stage 3** | **Decimal Division**| `prob = (2300 * sum_terms) / 100!` | $\mathcal{O}(1)$ |
| **Stage 4** | **Format Result** | Return `f"{prob:.12f}"` | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(\text{foolish}) = 23$ iterations | $< 0.001$ seconds |
| **Space Complexity** | $\mathcal{O}(1)$ | High-precision Decimal |
| **Dynamic Execution** | $100\%$ Inline | Inclusion-exclusion restricted derangement formula |

### Critical Invariants & Edge Cases Handled:
1. **Strict 3-Fixed Primes Invariant**: The inclusion-exclusion over the remaining 22 primes guarantees that *no other* prime disk is fixed.
2. **Arbitrary Non-Prime Placement**: Non-primes have no positional constraints, captured by the unrestricted factorial $(97 - m)!$.