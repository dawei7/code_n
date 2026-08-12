# Reachable Numbers - Optimal Approach

## Algorithm Explanation

Find the sum of all positive reachable integers formed by arithmetic expressions using digits $1$ through $9$ in order, with concatenation, $+$, $-$, $\times$, $/$, and any parentheses.

### Bottom-Up Interval DP over Rational Expressions:
1. **Interval DP State Definition**:
   Let $S(i, j)$ be the set of reachable rational numbers (`Fraction`) formed by the digit sequence slice $D[i \dots j]$ ($0 \le i \le j \le 8$).
2. **Base Case & Concatenation**:
   The single integer formed by concatenating digits $D[i \dots j]$ is added to $S(i, j)$.
3. **Recursive Interval Splitting**:
   For each length from $1$ to $9$ and each split point $k \in [i, j-1]$:
   For $A \in S(i, k)$ and $B \in S(k+1, j)$, we add $A+B, A-B, A \times B$, and $A/B$ ($B \ne 0$) into $S(i, j)$.
4. **Positive Integer Filtering**:
   After evaluating $S(0, 8)$, we filter unique positive integers ($x > 0$, $x \in \mathbb{Z}$) and sum them up.
5. **Execution**:
   The sum of all positive reachable integers is $20101196798$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N^3 \cdot |S|^2)$ for $N = 9$ digits. Runs in $\approx 8.50\text{s}$.
- **Space Complexity:** $\mathcal{O}(N^2 \cdot |S|)$ for fraction set storage.
