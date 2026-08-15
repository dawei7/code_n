# Different Dice - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Using fair 5-sided and 6-sided dice, we emulate an $n$-sided fair die using a predetermined sequence of dice $(d_1, d_2, \dots)$ where $d_i \in \{5, 6\}$.
Let $R(n)$ be the minimum expected number of dice rolls needed.
Define $S(n) = \sum_{k=2}^n R(k)$.
Given:
- $R(8) = 25/12 \approx 2.083333$
- $R(28) \approx 2.142476$
- $S(30) \approx 56.054622$

Find $S(1000)$ rounded to 6 decimal places.

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Infinite Sequence Exploration
- The set of all infinite binary sequences $\{5, 6\}^\infty$ is uncountable.
- Branch-and-bound tree searches over sequences suffer from non-local cycle dependencies.

---

## 3. Core Intuition & Mathematical Structure

### Residue State Space Markov Decision Process
At any point in the emulation, if we have $r \in \{0, 1, \dots, n - 1\}$ leftover equiprobable outcomes ($r_0 = 1$ initially):
- Rolling a die of size $d \in \{5, 6\}$ produces $r \cdot d$ total outcomes.
- We accept $\lfloor (r \cdot d) / n \rfloor \cdot n$ outcomes and carry over $r' = (r \cdot d) \bmod n$ leftover states.
- If $r' = 0$, the process halts immediately.

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Bellman Optimality Equation
Let $V(r)$ be the expected future rolls per state with $r$ leftover outcomes.
Scaling by $r$, let $W(r) = r \cdot V(r)$.
The Dynamic Programming Bellman equation is:
$$W(r) = \min_{d \in \{5, 6\}} \left( r + \frac{1}{d} W((r \cdot d) \bmod n) \right)$$
with terminal condition $W(0) = 0$.
The expected rolls for an $n$-sided die is:
$$R(n) = V(1) = W(1)$$

### Exponential Contraction Mapping
Because $\gamma = \max(1/5, 1/6) = 0.2 < 1$:
- The Bellman operator is a strict $\gamma$-contraction in the $L_\infty$ norm.
- $k$ iterations reduce maximum error by $5^{-k}$.
- Machine epsilon precision is reached within $35$ iterations.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Walkthrough for $n = 8$:
- Residues $r \in \{1, \dots, 7\}$:
  - $(1 \times 5) \bmod 8 = 5$
  - $(5 \times 5) \bmod 8 = 1$
  - Cycle between residues $1$ and $5$ with $d = 5$:
    - $W(1) = 1 + \frac{1}{5} W(5)$
    - $W(5) = 5 + \frac{1}{5} W(1)$
    - Solving the linear system: $W(1) = 1 + \frac{1}{5}(5 + \frac{1}{5} W(1)) = 2 + \frac{1}{25} W(1) \implies \frac{24}{25} W(1) = 2 \implies W(1) = \frac{50}{24} = \frac{25}{12} \approx \mathbf{2.083333}$. (Matches problem specification! $\checkmark$)

---

## 6. Implementation Architecture & Algorithmic Blueprint

| Stage | Operation | Description | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **State Space Allocation** | Initialize $W[0 \dots n-1]$ with $W[0] = 0$ | $\mathcal{O}(n)$ |
| **Stage 2** | **Value Iteration Loop** | Iterate $W[r] \leftarrow \min_{d \in \{5, 6\}} (r + \frac{1}{d} W[rd \bmod n])$ | $\mathcal{O}(n)$ per iteration |
| **Stage 3** | **Convergence Check** | Halt when $\max |\Delta W| < 10^{-13}$ ($\approx 35$ steps) | $\mathcal{O}(35n)$ |
| **Stage 4** | **Summation & Rounding** | Sum $R(k) = W[1]$ for $k \in [2, 1000]$ and format to 6 decimals | $\mathcal{O}(N^2) \approx 1.5\text{ s}$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(K \cdot N^2) \approx 1.5\text{ s}$ | Real-time execution in pure Python |
| **Space Complexity** | $\mathcal{O}(N) \le 1\text{ MB}$ | Small 1D array of floats |
| **Implementation Standard** | $100\%$ Pure Python | Zero external dependencies |

### Critical Invariants Handled:
1. **Contraction Guarantee**: The factor $\gamma \le 0.2$ guarantees monotonic geometric convergence regardless of initial values.
2. **Optimal Predetermined Policy**: The greedy choice $\arg\min_{d \in \{5, 6\}}$ at residue $r$ identifies the unique optimal stationary predetermined sequence.
