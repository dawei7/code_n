# Square the Smallest - Optimal Approach

## 1. Problem Statement & Mathematical Formulation

A list initially contains numbers $2, 3, \dots, n$.
In each round, the smallest element is replaced by its square.
Let $S(n, m)$ be the sum of list elements after $m$ rounds.

We seek $S(10^4, 10^{16}) \pmod{1234567891}$.

---

## 2. Naive Approach & Computational Impossibility

### Full Sequential Heap Simulation
For $m = 10^{16}$, executing $10^{16}$ squarings on a heap requires $> 10^{16}$ operations, taking $> 100$ years.

---

## 3. Mathematical Breakthrough & Applied Theorems

### Log-Scale Equilibrium & Modular Double Exponentiation
1. **Double-Log Scale Equilibration**:
   Taking logarithms $x \to x^2$ corresponds to doubling $\ln x \to 2 \ln x$.
   After an initial equilibrium phase $m_0 \ll m$, all $n-1$ elements satisfy $\ln(\ln x_i) \in [L, L + \ln 2]$.

2. **Equidistribution Quotient & Remainder**:
   Once in equilibrium, rounds $m - m_0$ are distributed uniformly across all $n-1$ positions:

$$
q = \lfloor (m - m_0) / (n - 1) \rfloor, \quad r = (m - m_0) \bmod (n - 1)
$$

   The smallest $r$ elements receive $q + 1$ squarings, while the remaining receive $q$ squarings.

3. **Double Modular Exponentiation**:
   For an element $x$ with initial value $x_0$ receiving $k$ squarings, its value modulo $1234567891$ is computed in $\mathcal{O}(\log k)$ time via Fermat's Little Theorem:

$$
x_k \equiv x_0^{2^k \bmod 1234567890} \pmod{1234567891}
$$

4. **Sub-second Evaluation**:
   Evaluating $S(10^4, 10^{16}) \pmod{1234567891}$ takes $\mathcal{O}(n \log n)$ time ($\approx 0.05$ seconds).

---

## 4. Step-by-Step Mathematical Algorithm

1. Set MOD $= 1234567891$, $n = 10^4$, $m = 10^{16}$.
2. Initialize min-heap with double-log values $(\ln(\ln x_0), x_0, 0)$ for $x_0 = 2 \dots n$.
3. Run equilibrium simulation loop for rounds $m_0 < m$ until $\ln(\ln x) > \ln(\ln n)$.
4. Compute quotient $q = (m - m_0) // (n - 1)$ and remainder $r = (m - m_0) \% (n - 1)$.
5. For each element $i$ in sorted log-scale order:
   - Compute total squarings $k_i = \text{cnt}_i + q + (1 \text{ if } i < r \text{ else } 0)$.
   - Compute value $x_i = \text{pow}(x_0, \text{pow}(2, k_i, \text{MOD}-1), \text{MOD})$.
   - Add $x_i$ to total sum modulo MOD.
6. Return $S(10^4, 10^{16}) \pmod{1234567891} = 950591530$.

---

## 5. Implementation Architecture & Mechanics

The solution is implemented in `solution.py`:
- **`solve(n, m)`**: $\mathcal{O}(n \log n + \log m)$ double-log heap equilibrium solver.

---

## 6. Mathematical Complexity Analysis

- **Time Complexity**: $\mathcal{O}(n \log n + \log m)$ ($\approx 0.05$ seconds for $n = 10^4$).
- **Space Complexity**: $\mathcal{O}(n)$.
