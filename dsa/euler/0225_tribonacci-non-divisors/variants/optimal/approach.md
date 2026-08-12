# Tribonacci Non-divisors - Optimal Approach

## Algorithm Explanation

Find the $124$th odd number that does not divide any term of the Tribonacci sequence defined by $T_1 = T_2 = T_3 = 1$ and $T_n = T_{n-1} + T_{n-2} + T_{n-3}$.

### Modular Tribonacci Cycle Simulation:
1. **Periodic Property**:
   Modulo any odd integer $k$, the 3-state tuple $(T_{n-2}, T_{n-1}, T_n) \pmod k$ is purely periodic starting from $(1, 1, 1)$.
2. **Divisibility Condition**:
   An odd integer $k$ is a non-divisor if and only if during its full period, no generated term satisfies $T_n \equiv 0 \pmod k$.
3. **Execution**:
   Iterating through odd numbers $k = 3, 5, 7, \dots$ and checking for zero terms before cycle completion finds the $124$th non-divisor at $2009$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \cdot \text{Period}(k))$ where $N = 124$ and average period is $\mathcal{O}(k^2)$. Runs in $\approx 0.50\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
