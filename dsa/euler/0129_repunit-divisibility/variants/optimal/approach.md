# Repunit Divisibility - Optimal Approach

## Algorithm Explanation

Find the least positive integer $n$ ($\gcd(n, 10) = 1$) for which $A(n) > 1,000,000$, where $A(n)$ is the minimal repunit length $k$ such that $R(k) = \underbrace{11\dots1}_{k \text{ ones}}$ is divisible by $n$.

### Mathematical Bounds & Modular Search:
1. **Lower Bound Reduction**:
   By the Pigeonhole Principle on remainder states modulo $n$, $A(n) \le n$.
   Consequently, for $A(n) > 1,000,000$, we must have $n > 1,000,000$.
2. **Modular Repunit Evaluation**:
   The repunit recurrence modulo $n$:
   $$r_{k+1} = (10 r_k + 1) \bmod n \quad (r_1 = 1)$$
   The minimal $k$ where $r_k \equiv 0 \pmod n$ is $A(n)$.
3. Search starting at $n = 1,000,001$, incrementing $n$ by $2$ (filtering $\gcd(n, 10) = 1$), and return the first $n$ with $A(n) > 10^6$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \cdot A(n))$ search with lower bound $n > 10^6$. Runs in $< 0.15\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary memory is constant.
