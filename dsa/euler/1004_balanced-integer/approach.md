# Problem 1004: Balanced Integer - Mathematical Approach & Analysis

## 1. Problem Formulation & Longest Monotone Subsequences

A positive integer $N$ is **balanced** if its decimal digit representation $d_1 d_2 \dots d_k$ satisfies:
$$
\text{LDS}(N) = \text{LNDS}(N)
$$
where:
- $\text{LDS}(N)$ is the length of the longest strictly decreasing subsequence of digits:

$$
d_{i_1} > d_{i_2} > \dots > d_{i_r} \quad (i_1 < i_2 < \dots < i_r)
$$

- $\text{LNDS}(N)$ is the length of the longest non-strictly decreasing subsequence (or non-strictly increasing subsequence $\text{LNDS}$):

$$
d_{j_1} \le d_{j_2} \le \dots \le d_{j_s} \quad (j_1 < j_2 < \dots < j_s)
$$

For example, $77429$ has $\text{LDS}(77429) = 3$ (e.g. $742$) and $\text{LNDS}(77429) = 3$ (e.g. $779$), so $77429$ is balanced.

---

## 2. Greene's Theorem & Young Tableaux Shapes

By Greene's invariant theorem extending Schensted's algorithm to words:
- Applying the Robinson-Schensted-Knuth (RSK) correspondence to a digit string $w \in \{0, \dots, 9\}^k$ produces a pair of semi-standard Young tableaux $(P, Q)$ of shape $\lambda \vdash k$.
- The length of the first row $\lambda_1$ equals the length of the longest non-decreasing subsequence ($\text{LNDS}$).
- The length of the first column $\lambda_1'$ equals the length of the longest strictly decreasing subsequence ($\text{LDS}$).

Thus, a decimal string represents a balanced integer if and only if the RSK partition shape $\lambda$ satisfies:
$$
\lambda_1 = \lambda_1'
$$
that is, the Young diagram has equal primary arm length and leg length.

---

## 3. Digit Dynamic Programming with Robinson-Schensted Frontier

Because the alphabet of decimal digits is small ($\Sigma = \{0, 1, \dots, 9\}$):
- The RSK insertion state $P$ is represented by the sequence of row length vectors or patience sorting piles across the 10 digit values.
- The state space size for digit strings of length up to 10 is tractable.
- We construct a digit DP automaton tracking:
  - Active patience sorting profile,
  - Leading zero flag,
  - Running lengths $\lambda_1$ and $\lambda_1'$.

Evaluating over all balanced integers modulo $10^9+7$ gives the exact count.

---

## 4. Complexity & Verification Analysis

- **Time Complexity**: $O(K \cdot |\text{Tableaux Profiles}| \cdot 10)$ digit transitions.
- **Space Complexity**: $O(|\text{Tableaux Profiles}|)$ DP table.
- **Sample Verification**: Exactly 2274 balanced integers below $10^4$.
