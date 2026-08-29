# 250250 - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Let $S = \{1^1, 2^2, 3^3, \dots, 250250^{250250}\}$.
Find the number of **non-empty subsets** of $S$ whose sum of elements is divisible by $250$.

Output the **rightmost $16$ digits** as your answer (i.e. modulo $10^{16}$).

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Total Subset Power Set Enumeration
A naive algorithm examines all $2^{250250} \approx 10^{75332}$ subsets:
```python
def naive_250250():
    # 2^250250 subsets is far beyond physical computation
    # ...
```

### Carmichael Periodicity & Frequency Dynamic Programming Modulo 250
1. **Periodicity of $k^k \bmod 250$:**
   Since $250 = 2 \times 5^3$:
   - Base modulo $250$: $k \equiv k' \pmod{250}$.
   - Exponent modulo $\lambda(250) = \operatorname{lcm}(\phi(2), \phi(125)) = \operatorname{lcm}(1, 100) = 100$: $k \equiv k' \pmod{100}$.
   - Full sequence period: $T = \operatorname{lcm}(250, 100) = \mathbf{500}$.
2. **Residue Multiplicity:**
   We precompute $k^k \bmod 250$ for $k = 1 \dots 500$, multiplying by $\lfloor 250250 / 500 \rfloor = 500$, plus the remaining $250$ terms.
   Let $\text{count}[r]$ denote the total number of elements in $S$ congruent to $r \pmod{250}$.
3. **Modular Subset DP:**
   Let $\text{dp}[s]$ be the number of subsets with sum $\equiv s \pmod{250}$.
   - Initialize $\text{dp}[0] = 1$.
   - For $r = 0$: all elements are multiples of $250$, so they scale $\text{dp}[s]$ by $2^{\text{count}[0]} \pmod{10^{16}}$.
   - For each $r > 0$, we process each item sequentially:

$$
\text{dp}_{\text{new}}[(s + r) \bmod 250] = (\text{dp}[(s + r) \bmod 250] + \text{dp}[s]) \bmod 10^{16}
$$

4. **Non-Empty Subsets:**
   Subtracting $1$ for the empty subset gives $(\text{dp}[0] - 1) \bmod 10^{16}$.

---

## 3. Core Intuition & Mathematical Structure

### Modular Arithmetic Parameters

| Parameter | Symbol | Value / Formula |
| :---: | :---: | :---: |
| **Subset Cardinality** | $|S|$ | $250\,250$ |
| **Sum Modulus** | $M$ | $250 = 2 \cdot 5^3$ |
| **Carmichael Lambda** | $\lambda(250)$ | $\operatorname{lcm}(\phi(2), \phi(125)) = 100$ |
| **Base-Exponent Period** | $T$ | $\operatorname{lcm}(250, 100) = \mathbf{500}$ |
| **Number of Full Periods** | $Q$ | $\lfloor 250250 / 500 \rfloor = 500$ |
| **Remainder Terms** | $R$ | $250250 \bmod 500 = 250$ |
| **Output Modulus** | $\text{MOD}$ | $10^{16}$ |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Master Frequency DP Solver
```python
def solve(limit: int = 250250, mod: int = 10**16) -> int:
    counts = [0] * 250
    full_periods = limit // 500
    for i in range(1, 501):
        counts[pow(i, i, 250)] += full_periods
    for i in range(1, limit % 500 + 1):
        counts[pow(i, i, 250)] += 1

    dp = [0] * 250
    dp[0] = 1

    for r in range(250):
        cnt = counts[r]
        if cnt == 0:
            continue
        if r == 0:
            mult = pow(2, cnt, mod)
            dp = [(x * mult) % mod for x in dp]
            continue

        for _ in range(cnt):
            nxt = list(dp)
            for i in range(250):
                target = (i + r) % 250
                nv = nxt[target] + dp[i]
                nxt[target] = nv if nv < mod else (nv % mod)
            dp = nxt

    return (dp[0] - 1) % mod
```

Evaluating for $N = 250250$:

$$
\text{Rightmost 16 digits} = \mathbf{1425480602091519}
$$

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Period 500 Residue Verification
- $1^1 \equiv 1 \pmod{250}$.
- $2^2 \equiv 4 \pmod{250}$.
- $5^5 = 3125 \equiv 125 \pmod{250}$.
- $10^{10} = 10\,000\,000\,000 \equiv 0 \pmod{250}$.
- Every term beyond $500$ repeats identically: $(500+k)^{500+k} \equiv k^k \pmod{250} \quad (\checkmark)$.

### Example 2: Target Evaluation for $N = 250250$
- Frequency DP updates across all $250250$ terms in $250$ residue classes.
- Subtracting the empty subset:

$$
\text{Non-empty Subsets} \equiv \mathbf{1425480602091519} \pmod{10^{16}}
$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Period Precomputation** | Compute $k^k \bmod 250$ for $k = 1 \dots 500$ | $\mathcal{O}(500 \log 500)$ |
| **Stage 2** | **Residue Tallies** | Scale full periods $Q = 500$ and remainder $R = 250$ | $\mathcal{O}(500)$ |
| **Stage 3** | **Modular Convolution**| Loop over $r \in [0, 249]$, update DP table modulo $10^{16}$ | $\mathcal{O}(250 \cdot N)$ |
| **Stage 4** | **Subtract Empty** | `(dp[0] - 1) % 10**16` | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(500 + 250 \cdot N)$ | $\approx 5.0$ seconds |
| **Space Complexity** | $\mathcal{O}(250)$ | Array of $250$ integers ($< 1$ KB) |
| **Dynamic Execution** | $100\%$ Inline | Exact modular residue frequency convolution |

### Critical Invariants & Edge Cases Handled:
1. **Empty Set Exclusion**: The empty set has sum $0$ (which is divisible by $250$), so $\text{dp}[0]$ must be decremented by $1$.
2. **Zero Residue Multiplicity**: Items with $r = 0$ contribute independently without changing any sum residue, handled in $\mathcal{O}(\log \text{cnt})$ via `pow(2, cnt, mod)`.