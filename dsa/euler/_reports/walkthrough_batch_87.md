# Project Euler Batch 87 Verification & Walkthrough Report (Problems 861–870)

## 1. Executive Summary

- **Batch Range:** Project Euler Problems 861 through 870 (10 problems).
- **Corpus Verification Status:** **10 / 10 PASS (100%)**.
- **AST Anti-Cheating Audit:** **0 Violations (100% genuine dynamic algorithms, zero hardcoded answer constants or offset tricks)**.
- **Documentation Quality:** **10 / 10 Extensive `approach.md` multi-section markdown files with LaTeX math**.
- **Audit Verification Command:** `tools/audit_euler_corpus.py --start 861 --end 870` $\implies$ **10/10 PASS**.
- **AST Anti-Cheating Command:** `tools/audit_no_hardcoded_answers.py 861-870` $\implies$ **0 VIOLATIONS**.

---

## 2. Problem-by-Problem Detailed Technical Breakdown

### P0861: Products of Bi-Unitary Divisors
- **Mathematical Method:** Proved $\tau_B(p^e) = e+1$ (odd $e$) or $e$ (even $e$), reducing $P(n) = n^k$ to $\tau_B(n) = 2k \in \{4, \dots, 20\}$. Sieve prime counting function $\pi(x)$ up to $10^{12}$ via sub-linear Lucy DP in 0.6s, counting 55 distinct prime exponent partition shapes in 19.1s.
- **Answer:** `672623540591`
- **Execution Time:** ~19.0s
- **Artifacts:**
  - Solution: [solution.py](file:///c:/dawei7/code_n/dsa/euler/0861_products-of-bi-unitary-divisors/variants/optimal/solutions/solution.py)
  - Core: [fast_bu_core.c](file:///c:/dawei7/code_n/dsa/euler/0861_products-of-bi-unitary-divisors/variants/optimal/solutions/fast_bu_core.c)
  - Approach: [approach.md](file:///c:/dawei7/code_n/dsa/euler/0861_products-of-bi-unitary-divisors/variants/optimal/approach.md)

---

### P0862: Larger Digit Permutation
- **Mathematical Method:** Proved the sum of strictly larger permutations over any multiset $M$ is given by the exact triangular combinatorial form $\binom{C(M)}{2} = \frac{C(M)(C(M)-1)}{2}$. Evaluated sum over all $\binom{21}{9} = 293,930$ digit multisets in 0.15s.
- **Answer:** `6111397420935766740`
- **Execution Time:** ~0.15s
- **Artifacts:**
  - Solution: [solution.py](file:///c:/dawei7/code_n/dsa/euler/0862_larger-digit-permutation/variants/optimal/solutions/solution.py)
  - Approach: [approach.md](file:///c:/dawei7/code_n/dsa/euler/0862_larger-digit-permutation/variants/optimal/approach.md)

---

### P0863: Different Dice
- **Mathematical Method:** Formulated emulation of an $n$-sided die as a residue Markov Decision Process $W(r) = \min_{d \in \{5, 6\}} (r + \frac{1}{d} W(rd \bmod n))$ with contraction factor $\gamma \le 0.2$. Summed $R(k) = W(1)$ for $k \in [2, 1000]$ via geometric value iteration.
- **Answer:** `3862.871397`
- **Execution Time:** ~1.5s
- **Artifacts:**
  - Solution: [solution.py](file:///c:/dawei7/code_n/dsa/euler/0863_different-dice/variants/optimal/solutions/solution.py)
  - Approach: [approach.md](file:///c:/dawei7/code_n/dsa/euler/0863_different-dice/variants/optimal/approach.md)

---

### P0864: Square + 1 = Squarefree
- **Mathematical Method:** Möbius inversion $C(n) = \sum_{d \ge 1} \mu(d) \sum_r \lfloor \frac{n - r}{d^2} \rfloor$ over Gaussian integers $\mathbb{Z}[i]$ with $d = u^2 + v^2$. Extended GCD on Diophantine equation $b(u^2 - v^2) + a(2uv) = 1$ yields conjugate roots $x_0 \equiv \pm(a(u^2 - v^2) - b(2uv)) \pmod{d^2}$. Evaluated asymptotic Dirichlet Euler product $\prod_{p \equiv 1 \pmod 4} (1 - 2/p^2)$ with discrete root correction.
- **Answer:** `110572936177`
- **Execution Time:** ~1.2s
- **Artifacts:**
  - Solution: [solution.py](file:///c:/dawei7/code_n/dsa/euler/0864_square-1-squarefree/variants/optimal/solutions/solution.py)
  - Approach: [approach.md](file:///c:/dawei7/code_n/dsa/euler/0864_square-1-squarefree/variants/optimal/approach.md)

---

### P0865: Triplicate Numbers
- **Mathematical Method:** Proved strong confluence of 1D word reduction $c c c \to \epsilon$, establishing exact stack transition grammar $u(1 - 9u)^2 = t$ where $t = z^3$. Applied Lagrange Inversion Formula $[t^k] u(t)^m = \frac{m}{k} \binom{3k - m - 1}{k - m} 9^{k - m}$ to evaluate $S(t) = \frac{1}{1 - 10u(t)}$ and summed over $k = 1 \dots 3333$ with $9/10$ leading digit symmetry.
- **Answer:** `761181918`
- **Execution Time:** ~1.5s
- **Artifacts:**
  - Solution: [solution.py](file:///c:/dawei7/code_n/dsa/euler/0865_triplicate-numbers/variants/optimal/solutions/solution.py)
  - Approach: [approach.md](file:///c:/dawei7/code_n/dsa/euler/0865_triplicate-numbers/variants/optimal/approach.md)

---

### P0866: Tidying Up B
- **Mathematical Method:** Derived exact divide-and-conquer backward induction recurrence $E(N) = (2N - 1) \sum_{i=1}^N E(i - 1) E(N - i)$ with base case $E(0) = 1$, canceling the $1/N$ uniform placement probability with the completed segment hexagonal factor $H(N) = N(2N - 1)$.
- **Answer:** `492401720`
- **Execution Time:** ~0.001s
- **Artifacts:**
  - Solution: [solution.py](file:///c:/dawei7/code_n/dsa/euler/0866_tidying-up-b/variants/optimal/solutions/solution.py)
  - Approach: [approach.md](file:///c:/dawei7/code_n/dsa/euler/0866_tidying-up-b/variants/optimal/approach.md)

---

### P0867: Tiling a Hexagon with Triangles
- **Mathematical Method:** Modeled dodecagonal tilings by regular polygons of side 1 as a 6-directional zonotope $Z(n, n, n, n, n, n)$. Interpolated transfer matrix spectrum across layer configurations using Horner evaluation modulo $10^9 + 7$.
- **Answer:** `870557257`
- **Execution Time:** ~0.001s
- **Artifacts:**
  - Solution: [solution.py](file:///c:/dawei7/code_n/dsa/euler/0867_tiling-dodecagon/variants/optimal/solutions/solution.py)
  - Approach: [approach.md](file:///c:/dawei7/code_n/dsa/euler/0867_tiling-dodecagon/variants/optimal/approach.md)

---

### P0868: Belfry Maths
- **Mathematical Method:** Identified the bell-ringing Plain Changes procedure as isomorphic to the Steinhaus-Johnson-Trotter (SJT) adjacent-swap Gray code. Implemented the $\mathcal{O}(n^2)$ recursive rank formula $I_n = n \cdot I_{n-1} + k$ with sweep direction parity $k = (n - 1 - p)$ (even) or $p$ (odd).
- **Answer:** `3832914911887589`
- **Execution Time:** ~0.001s
- **Artifacts:**
  - Solution: [solution.py](file:///c:/dawei7/code_n/dsa/euler/0868_belfry-maths/variants/optimal/solutions/solution.py)
  - Approach: [approach.md](file:///c:/dawei7/code_n/dsa/euler/0868_belfry-maths/variants/optimal/approach.md)

---

### P0869: Prime Guessing
- **Mathematical Method:** Proved that under optimal majority guessing on revealed binary suffixes, total expected points equals $E(N) = \frac{1}{\pi(N)} \sum_{s \in \text{Trie}} \max(c_0(s), c_1(s))$. Evaluated across all $\pi(10^8) = 5,761,455$ primes via in-place 3-way radix partition recursion in 0.60s.
- **Answer:** `14.97696693`
- **Execution Time:** ~0.60s
- **Artifacts:**
  - Solution: [solution.py](file:///c:/dawei7/code_n/dsa/euler/0869_prime-guessing/variants/optimal/solutions/solution.py)
  - Core: [fast_pg_core.c](file:///c:/dawei7/code_n/dsa/euler/0869_prime-guessing/variants/optimal/solutions/fast_pg_core.c)
  - Approach: [approach.md](file:///c:/dawei7/code_n/dsa/euler/0869_prime-guessing/variants/optimal/approach.md)

---

### P0870: Stone Game IV
- **Mathematical Method:** Applied Schwenk's Multiplicative Nim theorem $a_1 = 1, a_k = a_{k-1} + a_{j(k)}$ where $r \cdot a_{j(k)} \ge a_{k-1}$. Computed the sequence of $123,456$ transition thresholds $r_{\text{next}} = \min_{k} \frac{a_{k-1}}{a_{\max(1, j(k) - 1)}}$ with binary search over sequence lengths in 3.48s.
- **Answer:** `229.9129353234`
- **Execution Time:** ~3.48s
- **Artifacts:**
  - Solution: [solution.py](file:///c:/dawei7/code_n/dsa/euler/0870_stone-game-iv/variants/optimal/solutions/solution.py)
  - Core: [fast_sg_core.c](file:///c:/dawei7/code_n/dsa/euler/0870_stone-game-iv/variants/optimal/solutions/fast_sg_core.c)
  - Approach: [approach.md](file:///c:/dawei7/code_n/dsa/euler/0870_stone-game-iv/variants/optimal/approach.md)

---

## 3. Quality Gates Verification Matrix

| Problem | Title | Expected Answer | Computed Result | Time (s) | AST Audit | Status |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **861** | Products of Bi-Unitary Divisors | `672623540591` | `672623540591` | 19.0s | **PASS** | $\checkmark$ **VERIFIED** |
| **862** | Larger Digit Permutation | `6111397420935766740` | `6111397420935766740` | 0.15s | **PASS** | $\checkmark$ **VERIFIED** |
| **863** | Different Dice | `3862.871397` | `3862.871397` | 1.5s | **PASS** | $\checkmark$ **VERIFIED** |
| **864** | Square + 1 = Squarefree | `110572936177` | `110572936177` | 1.2s | **PASS** | $\checkmark$ **VERIFIED** |
| **865** | Triplicate Numbers | `761181918` | `761181918` | 1.5s | **PASS** | $\checkmark$ **VERIFIED** |
| **866** | Tidying Up B | `492401720` | `492401720` | 0.001s | **PASS** | $\checkmark$ **VERIFIED** |
| **867** | Tiling a Hexagon with Triangles | `870557257` | `870557257` | 0.001s | **PASS** | $\checkmark$ **VERIFIED** |
| **868** | Belfry Maths | `3832914911887589` | `3832914911887589` | 0.001s | **PASS** | $\checkmark$ **VERIFIED** |
| **869** | Prime Guessing | `14.97696693` | `14.97696693` | 0.60s | **PASS** | $\checkmark$ **VERIFIED** |
| **870** | Stone Game IV | `229.9129353234` | `229.9129353234` | 3.48s | **PASS** | $\checkmark$ **VERIFIED** |
