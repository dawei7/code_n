# Formal Mathematical Specification: Naive Pattern Search

## 1. Definitions and Notation
Let $T \in \Sigma^*$ be a text of length $n$ and $W \in \Sigma^*$ be a pattern of length $m$.
We seek all shifts $s \in \{0, \dots, n-m\}$ such that $T[s+1 \dots s+m] = W[1 \dots m]$.

## 2. Objective Function
Define an indicator function $\mathcal{I}(s)$ for a valid shift:
$$ \mathcal{I}(s) = \prod_{j=1}^m \mathbb{I}(T[s+j] = W[j]) $$
The goal is to find the set $\mathcal{S} = \{ s \mid \mathcal{I}(s) = 1 \}$.

## 3. Algorithm Formalization
For each $s \in \{0, 1, \dots, n-m\}$:
1. Initialize $j = 1$.
2. While $j \leq m$ and $T[s+j] = W[j]$:
   - $j \leftarrow j + 1$.
3. If $j = m + 1$, append $s$ to $\mathcal{S}$.

## 4. Complexity Analysis
- **Time Complexity:** In the worst-case scenario (e.g., $T = a^{n}$, $W = a^{m-1}b$), the inner loop executes exactly $m$ times for each of the $n-m+1$ possible shifts. The mathematically worst-case time complexity is $O((n - m + 1)m)$. If $m \ll n$, this asymptotically behaves as $O(nm)$.
- **Space Complexity:** The algorithm requires only scalar index variables $s$ and $j$. Space is strictly $O(1)$.
