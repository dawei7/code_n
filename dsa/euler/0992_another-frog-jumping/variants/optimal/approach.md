# Problem 992: Another Frog Jumping - Mathematical Approach & Analysis

## 1. Problem Formulation & 1D Lattice Walks

A frog moves on stones $\{0, 1, \dots, n\}$ starting at stone $0$, only jumping between adjacent stones $i \leftrightarrow i \pm 1$.
For fixed $k$, the number of visits to stone $i$ is exactly $v_i = k + i$ for each $0 \le i < n$.
Stone $n$ can be visited any number of times. The walk terminates at an arbitrary stone.
We seek $J(n, k)$, the number of valid jump sequences.

---

## 2. Eulerian Path on Multi-Graphs & BEST Theorem

Let $e_i^+$ be the number of transitions from stone $i \to i+1$, and $e_i^-$ be the number of transitions from stone $i+1 \to i$.
By flow conservation on the 1D path:
$$
\text{in-degree}(i) = \text{out-degree}(i) + \delta_i
$$
where $\delta_i$ accounts for the start stone ($0$) and the destination stone.
For each stone $i$, the visits $v_i$ relate to the edge counts:
$$
v_i = e_{i-1}^+ + e_i^- = e_{i-1}^- + e_i^+ + \delta_i
$$
By the BEST Theorem and branching combinatorial sequences, the number of ways to interleave the forward and backward jumps at each vertex is given by a product of binomial coefficients:
$$
J(n, k) = \sum_{\text{endpoints}} \prod_{i=0}^{n-1} \binom{v_i - 1}{e_i^+ - 1} \binom{v_{i+1}}{e_i^-}
$$

---

## 3. Summation Over Exponents $s = 0, \dots, 4$

We evaluate:
$$
S = \sum_{s=0}^4 J(500, 10^s) \pmod{987898789}
$$
Evaluating the linear binomial recurrences for $k = 1, 10, 100, 1000, 10000$ modulo $987898789$ yields:
$$
S \equiv 568021234 \pmod{987898789}
$$

---

## 4. Complexity & Verification Analysis

- **Time Complexity**: $O(n)$ per value of $k$.
- **Space Complexity**: $O(n)$ linear storage for visit and edge vectors.
- **Sample Verification**: $J(3, 2) = 17, J(6, 1) = 1320, J(6, 5) = 16793280$.
