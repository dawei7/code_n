# Base-10 Diophantine Reciprocal - Optimal Approach

## Algorithm Explanation

Find the total number of integer solutions $(a, b, p)$ with $1 \le a \le b$ and $p \ge 1$ to the Diophantine equation:
$$\frac{1}{a} + \frac{1}{b} = \frac{p}{10^n} \quad (1 \le n \le 9)$$

### Coprime Factorization & Divisor Counting:
Let $g = \gcd(a, b)$, $a = g A, b = g B$ where $\gcd(A, B) = 1$ ($1 \le A \le B$).
Substituting into equation:
$$\frac{g(A + B)}{g^2 A B} = \frac{p}{10^n} \implies p \cdot g A B = 10^n (A + B)$$

Since $\gcd(A, A + B) = 1$ and $\gcd(B, A + B) = 1$:
1. $A \mid 10^n$ and $B \mid 10^n$ with $\gcd(A, B) = 1$.
2. For each coprime pair $(A, B)$ dividing $10^n$:
   $$p \cdot g = \frac{10^n (A + B)}{A B} = K$$
3. For $p \ge 1$ to be an integer, $g$ can be **any divisor** of $K$.
4. The number of valid $g$ (and corresponding $p = K / g$) is $d(K)$, the divisor count of $K$.

Sum $d(K)$ over all coprime divisor pairs $(A, B)$ of $10^n$ for $n \in \{1, 2, \dots, 9\}$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N_{\text{max}} \cdot d(10^N)^2 \cdot \sqrt{K})$. Runs in $< 0.005\text{s}$.
- **Space Complexity:** $\mathcal{O}(d(10^N))$ - Divisor list storage.
