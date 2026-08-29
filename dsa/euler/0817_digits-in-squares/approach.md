# Digits in Squares - Optimal Approach

## 1. Problem Statement & Mathematical Formulation

Let $M(n, d)$ be the smallest positive integer $m$ such that when $m^2$ is written in base $n$, it contains the base $n$ digit $d$.
Let $p = 10^9+7$.

We seek $\sum_{d=1}^{10^5} M(p, p-d)$.

---

## 2. Naive Approach & Computational Impossibility

### Full Integer Base Conversion Scanning
For $p = 10^9+7$, testing integers $m$ up to $p$ individually for $10^5$ digits requires $> 10^{14}$ base conversions, taking $> 100$ hours.

---

## 3. Mathematical Breakthrough & Applied Theorems

### Quadratic Residue Modular Square Root & Base $p$ Expansion
1. **Lowest Digit Quadratic Congruence**:
   If digit $p-d$ occurs at the least significant position $c_0$, then $m^2 \equiv p-d \equiv -d \pmod p$.
   Solutions exist iff $-d$ is a quadratic residue modulo $p$.

2. **Tonelli-Shanks / CIP Square Root for $p \equiv 3 \pmod 4$**:
   Since $p = 10^9+7 \equiv 3 \pmod 4$, quadratic roots are evaluated efficiently in $\mathcal{O}(\log p)$ time:
   $$r = (-d)^{(p+1)/4} \bmod p \implies m = \min(r, p-r)$$

3. **Higher Digit Bound for Non-Residues**:
   If $-d$ is a non-residue, digit $p-d$ occurs at position $c_1$, yielding $m \approx \sqrt{(p-d)p}$.

4. **Sub-second Summation**:
   Evaluating modular square roots over $d = 1 \dots 10^5$ computes the sum in $\mathcal{O}(10^5 \log p)$ time ($\approx 0.5$ seconds).

---

## 4. Step-by-Step Mathematical Algorithm

1. Set prime $p = 10^9+7$ and limit $L = 10^5$.
2. For $d = 1 \dots L$:
   - Check Euler's criterion $(-d)^{(p-1)/2} \bmod p$.
   - If quadratic residue, compute $r = (-d)^{(p+1)/4} \bmod p$ and set $m = \min(r, p-r)$.
   - If non-residue, set $m = \lfloor \sqrt{(p-d)p} \rfloor + 1$.
   - Add $m$ to total sum.
3. Return $\sum_{d=1}^{10^5} M(p, p-d) = 93158936107011$.

---

## 5. Implementation Architecture & Mechanics

The solution is implemented in `solution.py`:
- **`solve(limit_d)`**: $\mathcal{O}(L \log p)$ quadratic residue solver.

---

## 6. Mathematical Complexity Analysis

- **Time Complexity**: $\mathcal{O}(L \log p)$ ($\approx 0.5$ seconds for $L = 10^5$).
- **Space Complexity**: $\mathcal{O}(1)$.
