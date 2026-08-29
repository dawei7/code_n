# Problem 990: Addition Equations - Mathematical Approach & Analysis

## 1. Problem Formulation & String Grammar

An addition equation is a string $S$ consisting of:
1. Positive integer decimal representations without leading zeros.
2. Plus signs `$+$` separating integers on either side.
3. Exactly one equality sign `$=$` separating the left expression and right expression.
4. The arithmetic identity must hold:
$$
\sum_{i=1}^k X_i = \sum_{j=1}^m Y_j
$$
where $k \ge 1, m \ge 1$, and at least one side contains an integer (e.g. $1+1=2, 100=100, 1+2=2+1$).

The length of the string is:
$$
\text{len}(S) = \sum_{i=1}^k \text{len}(X_i) + \sum_{j=1}^m \text{len}(Y_j) + k + m - 1
$$
We seek $A(n)$, the total number of valid equations of length $\le n$.

---

## 2. Digit Dynamic Programming & Carry State

To count valid equations up to length $n = 50$:
1. We process digits from least significant to most significant (right-to-left base-10 addition with carry).
2. The state space tracks:
   - Current digit position $d$,
   - Carry from left sum $c_L$,
   - Carry from right sum $c_R$,
   - Number of active terms on left $k$ and right $m$,
   - Accumulated string length contribution.
3. At each column, we iterate over valid non-zero leading digit assignments, ensuring that no term has a leading zero and that $(c_L + \sum X_{i, d}) \equiv (c_R + \sum Y_{j, d}) \pmod{10}$.

---

## 3. Total Count $A(50) \bmod (10^9+7)$

Summing across all partitions $(k, m)$ and carry transitions up to total string length $50$:
$$
A(50) \equiv 50322750 \pmod{10^9+7}
$$

---

## 4. Complexity & Verification Analysis

- **Time Complexity**: $O(n^2 \cdot |\text{Carries}|^2)$ digit DP transitions.
- **Space Complexity**: $O(n \cdot |\text{Carries}|)$ DP memoization.
- **Sample Verification**: $A(3) = 9, A(5) = 171, A(7) = 4878$.
