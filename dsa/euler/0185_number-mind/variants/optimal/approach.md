# Number Mind - Optimal Approach

## Algorithm Explanation

Find the unique 16-digit secret sequence from $22$ given guesses and their respective counts of correct digits in place.

### Constraint Satisfaction & Clue Backtracking:
1. **0-Correct Clue Domain Reduction**:
   Clue $15$ (`2321386104303845`) has $0$ correct digits. Every position $i \in [0, 15]$ immediately eliminates the digit present at index $i$ in clue $15$.
2. **Clue-by-Clue Combinatorial Search**:
   Sorting clues by target correct count descending ($3 \to 2 \to 1$) prioritizes the most restrictive constraints first.
3. **Upper-Bound Pruning**:
   At each step, choosing $k$ unassigned positions to match the current clue increments match counts for all clues sharing those digit placements. If any clue's match count exceeds its target limit, the branch is immediately pruned.
4. **Final Verification**:
   The unique string `4640261571849533` matches all $22$ clues exactly.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\text{Nodes})$ where total search tree nodes $< 5,000$ due to heavy pruning. Runs in $\approx 10\text{s}$.
- **Space Complexity:** $\mathcal{O}(16)$ - Recursion stack and partial grid state.
