# Formal Mathematical Specification: Run Length Encoding

## 1. Definitions and Notation
Let $S \in \Sigma^*$ be a string of length $n$.
A string can be uniquely decomposed into a sequence of runs $(c_k, L_k)$ for $1 \leq k \leq r$, where $c_k \in \Sigma$, $L_k \in \mathbb{N}^+$, $c_k \neq c_{k+1}$, and $S = \prod_{k=1}^r c_k^{L_k}$.

## 2. Algorithm Formalization
The RLE function $f : \Sigma^* \to (\Sigma \times \mathbb{N}^*)^*$ is computed via a single pass deterministic finite automaton (DFA) or a procedural loop:
1. Initialize a counter $C = 1$.
2. For $i = 2 \dots n$:
   - If $S[i] = S[i-1]$, $C \leftarrow C + 1$.
   - If $S[i] \neq S[i-1]$, output $(S[i-1], C)$ and reset $C \leftarrow 1$.
3. Output $(S[n], C)$.

## 3. Complexity Analysis
- **Time Complexity:** The sequence is iterated exactly once. Time is $O(n)$.
- **Space Complexity:** The output requires $O(r)$ space, where $r$ is the number of runs. In-place tracking requires $O(1)$ space overhead.
