# Formal Mathematical Specification: Word Break

## 1. Definitions and Notation
String $S$, dictionary $\mathcal{D}$. Return True if $S$ can be segmented into words $\in \mathcal{D}$.

## 2. Algebraic Characterization (Recurrence Relation)
$$ W(i) = \bigvee_{j=0}^{i-1} \left( W(j) \land (S[j+1 \dots i] \in \mathcal{D}) \right) $$

## 3. Complexity Analysis
- **Time Complexity:** $O(n^3)$ worst case for string slicing, $O(n^2)$ with Trie.
- **Space Complexity:** $O(n)$.
