# Investigating Ulam Sequences - Optimal Approach

## Algorithm Explanation

Find $\sum_{n=2}^{10} U(2, 2n+1)_k$, where $k = 10^{11}$ and $U(a,b)$ is the Ulam sequence starting with $a, b$.

### Structure of Ulam Sequences $U(2, 2n+1)$:
By the Knuth-Finch-Schmerl theorem for $U(2, v)$ ($v \ge 5$ odd):
1. **Exactly Two Even Terms**:
   $U(2, v)$ contains only two even terms: $2$ and $E = 2v + 2 = 4n + 4$.
2. **All Subsequent Terms are Odd**:
   For any odd integer $x > E$, the sum of two odd numbers is always even. Thus, an odd number $x > E$ cannot be formed as a sum of two odd terms.
   $x \in U(2, v)$ if and only if **exactly one** of $(x - 2)$ or $(x - E)$ is in $U(2, v)$.
3. **Linear Feedback Shift Register (LFSR) Recurrence**:
   Represent odd terms $2m+1$ by a boolean sequence $B[m]$. For $m \ge e = E / 2$:
   $$B[m] = B[m - 1] \oplus B[m - e]$$
4. **State Machine Period Detection**:
   The sliding window state of $e$ bits repeats after period $P_{\text{bits}}$. We track the $e$-bit integer state starting at $m = e$ to detect the exact period $P_{\text{terms}}$ and sum $P_{\text{sum}} = 2 \times P_{\text{bits}}$ in $\mathcal{O}(P_{\text{bits}})$ steps.
5. **$k$-th Term Formula**:
   With $P_{\text{terms}}$ terms per period and period sum $P_{\text{sum}}$, $U(2, v)_k$ is computed in $\mathcal{O}(1)$ time after period detection.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(P(v))$ per sequence where $P(v)$ is the LFSR period length ($P \le 2.1 \times 10^6$). Total execution time $\approx 3.0\text{s}$.
- **Space Complexity:** $\mathcal{O}(2^e)$ hash map / state history array.
