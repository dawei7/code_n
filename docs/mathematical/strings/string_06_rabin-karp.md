# Formal Mathematical Specification: Rabin-Karp Algorithm

## 1. Definitions and Notation
Let $T \in \Sigma^*$ be a text of length $n$ and $W \in \Sigma^*$ be a pattern of length $m$.
Let $b$ be the radix (e.g., $b = 256$) and $q$ be a large prime modulus.

## 2. Polynomial Rolling Hash Function
For a string $S$ of length $m$, define its hash value $H(S) \in \mathbb{Z}_q$:
$$ H(S) = \left( \sum_{i=1}^m S[i] \cdot b^{m-i} \right) \pmod q $$

## 3. Algebraic Characterization (Rolling Hash Property)
The hash value for the next shift $s+1$ in $T$ can be computed from shift $s$ in $O(1)$ time:
$$ H(T[s+2 \dots s+m+1]) = \left( (H(T[s+1 \dots s+m]) - T[s+1] \cdot b^{m-1}) \cdot b + T[s+m+1] \right) \pmod q $$
where all arithmetic operations are taken in $\mathbb{Z}_q$.

## 4. Algorithm Formalization
1. Precompute $h_M = b^{m-1} \pmod q$.
2. Compute $H(W)$ and $H_0 = H(T[1 \dots m])$.
3. For $s = 0, \dots, n-m$:
   - If $H_s = H(W)$, perform a deterministic verification $T[s+1 \dots s+m] \stackrel{?}{=} W[1 \dots m]$.
   - If verification passes, shift $s$ is valid.
   - If $s < n-m$, compute $H_{s+1}$ using the rolling hash formula.

## 5. Complexity Analysis
- **Time Complexity:** Precomputation takes $O(m)$ time. Hash rolling takes $O(n-m)$ time. The deterministic verification takes $O(m)$ time but is executed only when $H_s = H(W)$. Assuming a uniform hash distribution over $\mathbb{Z}_q$, the expected number of spurious hits is $O(n/q)$. Thus, the expected time complexity is $O(n + m)$. The worst-case time complexity (all hashes collide) is $O(nm)$.
- **Space Complexity:** The algorithm maintains integer hash variables. Space is strictly $O(1)$.
