# Large Non-Mersenne Prime - Optimal Approach

## Algorithm Explanation

Find the last $10$ digits of the $2,357,207$-digit prime number:
$$N = 28433 \times 2^{7830457} + 1$$

### Modular Exponentiation:
To compute the last $10$ digits, we evaluate $N \pmod{10^{10}}$:
$$\text{Last } 10 \text{ Digits} = (28433 \times (2^{7830457} \bmod 10^{10}) + 1) \bmod 10^{10}$$

Using binary exponentiation `pow(2, 7830457, 10**10)` executes in $\log_2(7830457) \approx 23$ modular multiplications.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\log E)$ where $E = 7830457$. Runs in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary memory is constant.
