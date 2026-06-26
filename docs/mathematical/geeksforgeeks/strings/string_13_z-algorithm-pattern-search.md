# Formal Mathematical Specification: Z-Algorithm Pattern Search

## 1. Definitions and Notation
Let $T$ be text of length $n$, $W$ be pattern of length $m$. Let $\$$ be a sentinel character such that $\$ \notin \Sigma$.
Construct $S = W \cdot \$ \cdot T$ with length $n + m + 1$.

## 2. Algebraic Characterization
Apply the Z-algorithm (from `string_07`) to $S$. For any index $i > m+1$, if $Z[i] = m$, it implies that $S[i \dots i+m-1] = S[1 \dots m] = W$. Thus, a valid shift exists at index $i - (m + 1)$ in $T$.

## 3. Complexity Analysis
- **Time Complexity:** Z-array construction on $S$ takes strictly $O(n + m)$.
- **Space Complexity:** Maintaining the Z-array for $S$ requires $O(n + m)$ space.
