# Largest Prime Factor - Optimal Approach

## Algorithm Explanation

To find the largest prime factor of $N = 600851475143$, we perform **trial division**:

1. Divide out $2$ completely while $N$ is even.
2. Iterate odd numbers $d = 3, 5, 7, \dots$ up to $\sqrt{N}$.
3. Whenever $d$ divides $N$, update the largest prime factor to $d$ and divide $N$ by $d$ until it is no longer divisible.
4. If $N > 1$ after the loop, the remaining value of $N$ is itself prime and is the largest prime factor.

By reducing $N$ whenever a factor is found, the loop boundary $\sqrt{N}$ shrinks dynamically, making execution almost instantaneous.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\sqrt{N})$ - At most $\sqrt{N}$ steps, practically much faster due to dynamic reduction of $N$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary memory is constant.
