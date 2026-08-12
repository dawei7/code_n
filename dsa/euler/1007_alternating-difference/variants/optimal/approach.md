# Alternating Difference - Optimal Approach

## Algorithm Explanation

Find $A(10^7) \bmod (10^9 + 9)$ where $A(n)$ is the sum of values of all valid parenthesizations of alternating differences over Fibonacci numbers $F_0, \dots, F_n$.

Using Catalan / Dyck path combinatorics to aggregate coefficient signs of each $F_k$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ linear scan.
- **Space Complexity:** $\mathcal{O}(1)$ - Memory overhead is constant.
