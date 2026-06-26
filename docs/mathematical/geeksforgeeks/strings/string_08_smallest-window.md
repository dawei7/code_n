# Formal Mathematical Specification: Smallest Window

## 1. Definitions and Notation
Let $S \in \Sigma^*$ and $P \in \Sigma^*$ be two strings of lengths $n$ and $m$.
We seek indices $i^*, j^*$ such that $1 \leq i^* \leq j^* \leq n$, the multiset of characters in $P$ is a subset of the multiset of characters in $S[i^* \dots j^*]$, and the length $(j^* - i^* + 1)$ is minimized.

## 2. Formalization via Sliding Window
Let $H_P : \Sigma \to \mathbb{N}$ be the frequency mapping of $P$.
Let $H_W : \Sigma \to \mathbb{N}$ be the frequency mapping of the current window $S[L \dots R]$.
A window is valid if $\forall c \in \Sigma, H_W(c) \geq H_P(c)$.
Define the defect function $\mathcal{D}(H_W) = \sum_{c \in \Sigma} \max(0, H_P(c) - H_W(c))$.
The window is valid iff $\mathcal{D}(H_W) = 0$.

## 3. Algorithm State Transitions
Maintain pointers $L, R \in \{1 \dots n\}$ starting at 1.
- **Expansion (Increase $R$)**: Add $S[R]$ to $H_W$. If $H_W(S[R]) \leq H_P(S[R])$, decrement the defect.
- **Contraction (Increase $L$)**: If $\mathcal{D}(H_W) = 0$, record window size $(R - L + 1)$. Remove $S[L]$ from $H_W$. If $H_W(S[L]) < H_P(S[L])$, increment the defect.

## 4. Complexity Analysis
- **Time Complexity:** The pointers $L$ and $R$ each traverse the string $S$ exactly once monotonically. Thus, there are $O(n)$ pointer updates. Hash map updates are $O(1)$. Total time complexity is strictly $O(n)$.
- **Space Complexity:** The algorithm maintains frequency maps mapping elements of $\Sigma$ to integers. Space complexity is $O(|\Sigma|)$, which is $O(1)$ constant overhead relative to $n$.
