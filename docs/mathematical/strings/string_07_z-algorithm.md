# Formal Mathematical Specification: Z-Algorithm

## 1. Definitions and Notation
Let $S \in \Sigma^*$ be a string of length $n$.
Define the Z-array $Z : \{1, \dots, n\} \to \mathbb{N}$ where $Z[i]$ is the length of the longest common prefix of $S[1 \dots n]$ and $S[i \dots n]$.
Mathematically:
$$ Z[i] = \max \{ k \mid S[1 \dots k] = S[i \dots i+k-1] \} $$
with $Z[1] = n$.

## 2. Algebraic Characterization (The Z-Box)
The algorithm maintains a "Z-box" $[L, R]$, which is the interval with the maximum $R$ such that $S[L \dots R]$ matches $S[1 \dots R-L+1]$.
For computing $Z[i]$, we have two primary cases based on whether $i$ lies inside the current Z-box ($i \leq R$):
1. **$i > R$**: No historical information is available. We must explicitly match $S[i+k]$ with $S[1+k]$ for $k \ge 0$.
2. **$i \leq R$**: The substring $S[i \dots R]$ matches $S[i-L+1 \dots R-L+1]$. Let $k = i - L + 1$. We look at previously computed $Z[k]$:
   - If $Z[k] < R - i + 1$, then $Z[i] = Z[k]$ precisely.
   - If $Z[k] \geq R - i + 1$, then $Z[i]$ is at least $R - i + 1$, and we must explicitly match characters starting from $R+1$.

## 3. Algorithm Formalization
1. Initialize $L = 0, R = 0$.
2. For $i = 2 \dots n$:
   - If $i > R$: Set $L = i, R = i$, while $R \leq n$ and $S[R - L + 1] = S[R]$, increment $R$. $Z[i] = R - L$, decrement $R$.
   - If $i \leq R$: Let $k = i - L + 1$.
     - If $Z[k] < R - i + 1$: $Z[i] = Z[k]$.
     - If $Z[k] \geq R - i + 1$: Set $L = i$, while $R \leq n$ and $S[R - L + 1] = S[R]$, increment $R$. $Z[i] = R - L$, decrement $R$.

## 4. Complexity Analysis
- **Time Complexity:** The value of $R$ strictly monotonically increases from $0$ to $n$. Explicit character comparisons only occur when evaluating positions beyond $R$, and every successful comparison increments $R$. Thus, there are at most $O(n)$ successful comparisons. The loop overhead is $O(n)$. Total time complexity is strictly $O(n)$.
- **Space Complexity:** The algorithm requires an array $Z$ of size $n$. Space complexity is $O(n)$.
