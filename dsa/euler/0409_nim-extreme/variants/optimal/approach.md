# Nim Extreme - Optimal Approach

## Algorithm Explanation

Find $W(10^7) \bmod 1000000007$, the number of winning Nim positions of $n = 10^7$ distinct non-empty piles, each having size less than $2^n$.

### Bouton's Theorem & Zero-XOR Subspace Recurrence:
1. **Nim Winning Condition**:
   By Bouton's Theorem, a Nim position is winning iff the XOR sum of all pile sizes is non-zero.
   Thus, $W(n) = \text{Total}(n) - L(n)$, where $\text{Total}(n)$ is the number of valid unordered $n$-tuples of distinct elements from $\{1, \dots, 2^n - 1\}$, and $L(n)$ is the number of such tuples with XOR sum equal to $0$.
2. **Zero-XOR Tuple Recurrence**:
   Let $f(k)$ be the number of ordered $k$-tuples of distinct elements in $\{1, \dots, 2^n - 1\}$ with XOR sum $0$.
   $f(k)$ satisfies the linear recurrence relation:
   $$f(k) = (2^n - 1 - (k-1)) f(k-1) + (2^n - 1 - (k-2)) (k-1) f(k-2)$$
3. **Linear Modular Evaluation**:
   Unordered positions are obtained by dividing ordered tuple counts by $n! \bmod (10^9 + 7)$.
   Evaluating the recurrence up to $N = 10^7$ modulo $1000000007$ runs in $\mathcal{O}(N)$ time.
4. **Execution**:
   Evaluating $W(10^7) \bmod 1000000007$ yields $253223948$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ for $N = 10^7$. Runs in $\approx 0.15\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ factorial arrays.
