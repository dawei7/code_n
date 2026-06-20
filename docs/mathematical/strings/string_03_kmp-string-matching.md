# Formal Mathematical Specification: Knuth-Morris-Pratt Algorithm

## 1. Definitions and Notation
Let $T \in \Sigma^*$ be a text of length $n$ and $W \in \Sigma^*$ be a word (pattern) of length $m$.
We seek the set of all valid shifts $s$ such that $0 \leq s \leq n - m$ and $T[s+1 \dots s+m] = W[1 \dots m]$.

## 2. The Prefix Function (Failure Array)
Define the prefix function $\pi : \{1, \dots, m\} \to \mathbb{N}$ as the length of the longest proper prefix of $W[1 \dots q]$ that is also a proper suffix of $W[1 \dots q]$.
Mathematically:
$$ \pi(q) = \max \{ k < q \mid W[1 \dots k] = W[q - k + 1 \dots q] \} $$
with $\pi(1) = 0$.

## 3. Algebraic Characterization
If a mismatch occurs at $T[i] \neq W[q+1]$ after $q$ characters have matched (i.e., $T[i-q \dots i-1] = W[1 \dots q]$), the next possible valid shift must match at least $\pi(q)$ characters.
The KMP algorithm guarantees that no potential match is skipped by shifting the pattern by exactly $q - \pi(q)$ positions.

## 4. Algorithm Formalization
**Phase 1: Compute $\pi$**
State $k$ denotes the length of the current matched prefix.
For $q = 2 \dots m$:
1. While $k > 0 \land W[k+1] \neq W[q]$, update $k \leftarrow \pi(k)$.
2. If $W[k+1] = W[q]$, update $k \leftarrow k + 1$.
3. Set $\pi(q) = k$.

**Phase 2: Match against $T$**
State $q$ denotes the number of matched characters.
For $i = 1 \dots n$:
1. While $q > 0 \land W[q+1] \neq T[i]$, update $q \leftarrow \pi(q)$.
2. If $W[q+1] = T[i]$, update $q \leftarrow q + 1$.
3. If $q = m$, a valid shift is found at $i - m$. Update $q \leftarrow \pi(q)$.

## 5. Complexity Analysis
- **Time Complexity:** In both phases, the value of $k$ (or $q$) increases by at most 1 in each iteration of the outer loop. Since $k$ is strictly bounded below by 0, the total number of decrements (the `while` loops) cannot exceed the total number of increments. Thus, the amortized cost of the inner loops is $O(1)$. Total time is mathematically strictly bounded by $O(n + m)$.
- **Space Complexity:** The algorithm maintains the prefix function array $\pi$ of size $m$. Space complexity is exactly $O(m)$.
