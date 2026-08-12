# Kakuro - Optimal Approach

## Algorithm Explanation

Find the sum of the 10-digit decrypted answers for all 200 cryptic Kakuro puzzles in `kakuro200.txt`.

### Cryptic Letter Decryption & Constraint Propagation:
1. **Kakuro Rules & Cryptic Mapping**:
   Each puzzle grid ($5 \times 5$ or $6 \times 6$) contains cryptic sum labels written using letters $A \dots J$, representing a bijection to digits $0 \dots 9$.
   White cells must be filled with distinct digits $1 \dots 9$ in each horizontal and vertical run such that the run sum equals the decrypted cryptic sum.
2. **Constraint Satisfaction DFS Backtracking**:
   For each puzzle:
   - We iterate over digit permutations of $A \dots J \in \{0, \dots, 9\}$.
   - We check valid digit sum combinations for each run length.
   - Forward checking and domain reduction prune invalid letter mappings early.
3. **Execution**:
   Solving all 200 Kakuro puzzles and summing their 10-digit answers yields $1075555621404$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\text{Puzzles} \cdot 10!)$ pruned constraint search. Runs in $\approx 0.50\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
