# Passcode Derivation - Optimal Approach

## Algorithm Explanation

Determine the shortest secret passcode from $50$ successful login attempts recorded in `keylog.txt`.

### Topological Sort Graph Strategy:
Each $3$-character entry $c_1 c_2 c_3$ establishes strict precedence constraints: $c_1 \to c_2$ and $c_2 \to c_3$.

1. Parse all $50$ login entries into a Directed Acyclic Graph (DAG) $(V, E)$.
2. Calculate in-degrees for all unique characters.
3. Perform **Kahn's Topological Sort Algorithm**:
   - Maintain a queue of nodes with `in_degree == 0`.
   - Process nodes sequentially, decrementing neighbor in-degrees.
4. Join ordered characters into the passcode integer.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(V + E)$ where $V \le 10$ digits and $E \le 50$ edges. Runs in $< 0.05\text{s}$.
- **Space Complexity:** $\mathcal{O}(V + E)$ - Graph adjacency structure.
