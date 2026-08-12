# Few Repeated Digits - Optimal Approach

## Algorithm Explanation

Find the total number of $18$-digit numbers (without leading zero) such that no digit occurs more than $3$ times.

### Exponential Generating Function / Multiset Permutations:
Let $(c_0, c_1, \dots, c_9)$ be the counts of digits $0 \dots 9$ appearing in the $18$-digit number.
Each count satisfies $0 \le c_d \le 3$, with $\sum_{d=0}^9 c_d = 18$.

1. **Total Multiset Permutations**:
   The number of distinct $18$-digit permutations allowing leading zero is:
   $$P_{\text{total}} = \frac{18!}{c_0! c_1! \dots c_9!}$$
2. **Excluding Leading Zeroes**:
   The number of permutations starting with digit $0$ is:
   $$P_{\text{zero}} = \frac{17!}{(c_0 - 1)! c_1! \dots c_9!} = \frac{c_0}{18} P_{\text{total}}$$
3. **Valid $18$-Digit Permutations**:
   $$P_{\text{valid}} = P_{\text{total}} - P_{\text{zero}} = \frac{17!}{c_0! c_1! \dots c_9!} \times (18 - c_0)$$

Sum $P_{\text{valid}}$ across all valid digit count vectors $(c_0, c_1, \dots, c_9)$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(4^{10})$ multiset states ($\le 4^{10} = 1,048,576$, pruned to $\sum c_d = 18$). Runs in $\approx 0.05\text{s}$.
- **Space Complexity:** $\mathcal{O}(L)$ - Recursion stack depth ($L = 18$).
