# Subsets with a Unique Sum - Optimal Approach

## Algorithm Explanation

Find $\operatorname{sum}(U(S, 50))$, the sum of all integers that occur as the sum of *exactly one* $50$-element subset of $S = \{1^2, 2^2, \dots, 100^2\}$.

### Bitwise Integer Dynamic Programming:
1. **State Representation**:
   Let `ones[c]` be a 295,425-bit integer whose $s$-th bit is $1$ if sum $s$ occurs *exactly once* using $c$ elements.
   Let `twos[c]` be an integer whose $s$-th bit is $1$ if sum $s$ occurs $\ge 2$ times using $c$ elements.
2. **Bitwise Transitions**:
   When processing element $v = i^2$:
   - `s_ones = ones[c-1] << v`
   - `s_twos = twos[c-1] << v`
   - `new_twos = twos[c] | (ones[c] & s_ones) | s_twos`
   - `new_ones = (ones[c] ^ s_ones) & ~new_twos`
3. **Execution**:
   Summing the set bit indices of `ones[50]` yields $115039000$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}\left(n \cdot k \cdot \frac{S_{\text{max}}}{64}\right)$ where $n = 100, k = 50, S_{\text{max}} = 295425$. Runs in $\approx 1.38\text{s}$.
- **Space Complexity:** $\mathcal{O}\left(k \cdot \frac{S_{\text{max}}}{64}\right) \approx 2.3\text{ MB}$.
