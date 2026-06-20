# Formal Mathematical Specification: String to Integer (atoi)

## 1. Definitions and Notation
Let $S$ be a string. Let $\sigma \in \{1, -1\}$ be the sign.
Let $\mathcal{D} = S[i \dots j]$ be the contiguous sequence of numeric digits $d_k \in \{0 \dots 9\}$.

## 2. Algebraic Characterization
The integer representation is a polynomial evaluation in base 10:
$$ N = \sigma \sum_{k=0}^{|D|-1} d_{|D|-1-k} \cdot 10^k $$
To prevent overflow, evaluating iteratively $N_{k} = 10 \cdot N_{k-1} + d_k$ requires checking:
$$ N_{k-1} > \lfloor \frac{INT\_MAX}{10} \rfloor \implies \text{Overflow} $$

## 3. Complexity Analysis
- **Time Complexity:** Parsing is deterministic $O(n)$.
- **Space Complexity:** $O(1)$.
