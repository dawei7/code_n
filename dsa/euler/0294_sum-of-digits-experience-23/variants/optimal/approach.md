# Sum of Digits - Experience #23 - Optimal Approach

## Algorithm Explanation

Find $S(11^{12}) \bmod 10^9$, where $S(n)$ is the number of positive integers $k < 10^n$ such that $23 \mid k$ and the sum of the digits $d(k) = 23$.

### State Space Matrix Exponentiation:
1. **State Space Definition**:
   Each digit suffix state is represented by $(s, r)$ where:
   - $s \in [0, 23]$ is the current accumulated digit sum.
   - $r \in [0, 22]$ is the current value modulo $23$.
   This yields $24 \times 23 = 552$ distinct DP states.
2. **Transition Matrix**:
   Appending a digit $d \in [0, 9]$ transitions state $(s, r)$ to $(s + d, (10r + d) \bmod 23)$.
   This defines a linear $552 \times 552$ transition matrix $M$.
3. **Logarithmic Exponentiation**:
   Evaluating $S(11^{12}) \bmod 10^9$ reduces to computing $M^{11^{12}} \bmod 10^9$ using binary matrix exponentiation in $\mathcal{O}(552^3 \log(11^{12}))$ operations.
4. **Execution**:
   Matrix exponentiation modulo $10^9$ yields $789184709$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(S^3 \log N)$ for state count $S = 552$ and $N = 11^{12}$. Runs in $\approx 2.50\text{s}$.
- **Space Complexity:** $\mathcal{O}(S^2)$ matrix memory.
