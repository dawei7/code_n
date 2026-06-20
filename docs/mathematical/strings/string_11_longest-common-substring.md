# Formal Mathematical Specification: Longest Common Substring (Horizontal Scanning)

*(Note: string_11 covers Longest Common Substring via the same mechanisms as string_05, but may represent an alternative approach like Horizontal Scanning for Longest Common Prefix. Assuming LCP here due to typical duplicate naming issues.)*

## 1. Definitions and Notation
Let $\mathcal{A} = \{S_1, S_2, \dots, S_N\}$ be a set of $N$ strings.
Let $\text{LCP}(S_a, S_b)$ denote the longest common prefix of two strings.
The goal is to find $\text{LCP}(\mathcal{A}) = \bigcap_{k=1}^N S_k[1 \dots c]$ for maximum $c$.

## 2. Algebraic Characterization
The LCP operation is associative and commutative:
$$ \text{LCP}(\mathcal{A}) = \text{LCP}(S_1, \text{LCP}(S_2, \dots \text{LCP}(S_{N-1}, S_N))) $$

## 3. Complexity Analysis
- **Time Complexity:** Iteratively accumulating the LCP across all $N$ strings bounds character comparisons to the length of the shortest string. $O(N \cdot \min |S_i|)$.
- **Space Complexity:** $O(1)$ beyond the input array.
