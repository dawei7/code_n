# Reversible Numbers - Optimal Approach

## Algorithm Explanation

Find the total number of reversible positive integers $n < 10^9$, where $n$ is reversible if $n + \operatorname{reverse}(n)$ consists entirely of odd decimal digits and contains no leading zeroes.

### Combinatorial Digit Analysis by Length $L$:
Analyzing digit addition carry propagation for length $L$:

1. **$L \equiv 1 \pmod 4$ ($L = 1, 5, 9$)**:
   - The central digit $d_{\text{mid}}$ adds to itself ($2 d_{\text{mid}}$). For the sum to be odd, it requires a carry from the right, which forces asymmetric carry propagation that creates an even digit.
   - Count: **$0$**.
2. **$L \equiv 0, 2 \pmod 4$ ($L = 2, 4, 6, 8$)**:
   - No central digit. Every outer digit pair $(d_i, d_{L+1-i})$ adds without carry.
   - Outer pair choices: $20$ options ($d_1 + d_L \in \{3, 5, 7, 9\}$ with non-zero $d_1, d_L$).
   - Inner pair choices: $30$ options ($d_i + d_{L+1-i} \in \{1, 3, 5, 7, 9\}$).
   - Count: $20 \times 30^{L/2 - 1}$.
3. **$L \equiv 3 \pmod 4$ ($L = 3, 7$)**:
   - Requires carry from outer digits to make the central digit sum odd ($d_1 + d_L \ge 10$).
   - Count: $100 \times 500^{(L-3)/4}$.

### Combinatorial Sum Below $10^9$:
- $L = 2$: $20$
- $L = 3$: $100$
- $L = 4$: $600$
- $L = 6$: $18,000$
- $L = 7$: $50,000$
- $L = 8$: $540,000$

Total count below $10^9 = 608,720$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(L)$ where $L = 9$. Evaluates in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Constant space.
