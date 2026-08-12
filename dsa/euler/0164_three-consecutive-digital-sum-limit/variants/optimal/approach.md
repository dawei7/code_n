# Three Consecutive Digital Sum Limit - Optimal Approach

## Algorithm Explanation

Find the total number of $20$-digit numbers (without leading zero) for which no three consecutive digits have a sum greater than $9$.

### Dynamic Programming State Transition:
Construct the number digit by digit from left to right for lengths $L = 1 \dots 20$.

1. **State Definition**:
   Maintain DP state `dp[(d1, d2)]` representing the number of valid prefixes ending with the last two digits $(d_1, d_2)$ where $d_1, d_2 \in [0, 9]$.
2. **Base Case ($L = 2$)**:
   For $d_1 \in [1, 9]$ (no leading zero) and $d_2 \in [0, 9 - d_1]$, initialize `dp[(d1, d2)] = 1`.
3. **Transition Step ($L = 3 \dots 20$)**:
   For each state $(d_1, d_2)$ and next digit $d_3 \in [0, 9 - d_1 - d_2]$:
   $$\text{new\_dp}[(d_2, d_3)] += \text{dp}[(d_1, d_2)]$$
4. **Final Result**:
   Sum all counts in `dp` after $20$ steps.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(L \cdot 10^3)$ where $L = 20$ (at most $550$ state transitions per step). Runs in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(10^2) = \mathcal{O}(100)$ - Number of active DP states.
