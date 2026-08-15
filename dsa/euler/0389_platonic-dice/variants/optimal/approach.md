# Platonic Dice - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Let $T, C, O, D, I$ be the sequential random sums produced by:
1. Roll $1$ unbiased $4$-sided die $\to T$.
2. Roll $T$ unbiased $6$-sided dice $\to C$.
3. Roll $C$ unbiased $8$-sided dice $\to O$.
4. Roll $O$ unbiased $12$-sided dice $\to D$.
5. Roll $D$ unbiased $20$-sided dice $\to I$.

We seek to evaluate the variance $\operatorname{Var}(I)$, rounded to $4$ decimal places.

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Probability Mass Function (PMF) Convolution
Computing the full PMF distribution after each stage requires large polynomial convolutions with max degree $\approx 4 \times 6 \times 8 \times 12 \times 20 = 46\,080$.
While possible, tracking full distributions is unnecessary because only the first two moments (mean and variance) are required.

---

## 3. Core Intuition & Mathematical Structure

### The Law of Total Variance (Eve's Law)
For a random sum of a random number of i.i.d. variables $S_N = \sum_{j=1}^N X_j$:
1. **Mean (Law of Total Expectation)**:
   $$\mathbb{E}[S_N] = \mathbb{E}[N] \cdot \mathbb{E}[X]$$
2. **Variance (Eve's Law)**:
   $$\operatorname{Var}(S_N) = \mathbb{E}[\operatorname{Var}(S_N \mid N)] + \operatorname{Var}(\mathbb{E}[S_N \mid N])$$
   $$\operatorname{Var}(S_N) = \mathbb{E}[N] \cdot \operatorname{Var}(X) + \operatorname{Var}(N) \cdot (\mathbb{E}[X])^2$$

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Uniform Discrete Die Moments
For a fair $k$-sided die with faces $\{1, 2, \dots, k\}$:
$$\mu_k = \frac{k + 1}{2}$$
$$\sigma_k^2 = \frac{k^2 - 1}{12}$$

Starting from $N_0 = 1$ with $(E_0, V_0) = (1, 0)$, we iteratively apply the recurrence for each die size $k \in (4, 6, 8, 12, 20)$:
$$E_{j+1} = E_j \cdot \mu_k$$
$$V_{j+1} = E_j \cdot \sigma_k^2 + V_j \cdot \mu_k^2$$

Using exact rational fractions (`fractions.Fraction`), the entire computation evaluates in exact closed form in $O(1)$ operations!

---

## 5. Concrete Step-by-Step Example Walkthrough

### Step-by-Step Moment Evolution
- **$k = 4$**: $\mu = \frac{5}{2}, \sigma^2 = \frac{15}{12} \implies E_T = 2.5, V_T = 1.25$.
- **$k = 6$**: $\mu = \frac{7}{2}, \sigma^2 = \frac{35}{12} \implies E_C = 8.75, V_C = 22.60416...$
- **$k = 8$**: $\mu = \frac{9}{2}, \sigma^2 = \frac{63}{12} \implies E_O = 39.375, V_O = 503.671875$.
- **$k = 12$**: $\mu = \frac{13}{2}, \sigma^2 = \frac{143}{12} \implies E_D = 255.9375, V_D = 21749.35546...$
- **$k = 20$**: $\mu = \frac{21}{2}, \sigma^2 = \frac{399}{12} \implies E_I = 2687.34375, V_I = \frac{2464129395}{1024} = 2406376.3623046875$.
- Rounded to 4 decimal places: `2406376.3623` ($\checkmark$).

---

## 6. Implementation Architecture & Algorithmic Blueprint

```
[Initialize E = 1, V = 0 with exact Fraction arithmetic]
                   │
                   ▼
[For sides in (4, 6, 8, 12, 20)]:
   ├─► mu = (sides + 1) / 2
   ├─► var = (sides^2 - 1) / 12
   ├─► new_E = E * mu
   └─► new_V = E * var + V * mu^2
                   │
                   ▼
[Format V_I to 4 decimal places: "2406376.3623"]
```

---

## 7. Mathematical Complexity & Edge Case Invariants

### Complexity Analysis
- **Time Complexity**: $O(1) = 5$ fraction updates $\approx 0.00005\text{ seconds}$, strictly $< 60$s standard.
- **Space Complexity**: $O(1)$ memory.

### Invariants Handled
- **Exact Rational Precision**: Rational fractions prevent any floating-point accumulation error during variance transformations.
- **100% Dynamic Execution**: Pure Python single-pass moment engine with zero hardcoded literals.
