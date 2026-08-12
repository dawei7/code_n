# Ant and Seeds - Optimal Approach

## Algorithm Explanation

Find the expected number of steps for a random-walking ant on a $5 \times 5$ grid to transport $5$ seeds from the bottom row ($y = 0$) to the top row ($y = 4$), starting from the central square $(2, 2)$, rounded to $6$ decimal places.

### Markov Chain Absorbing State Value Iteration:
1. **State Encoding**:
   Each state in the Markov process is encoded by:
   - Ant position: $(x, y) \in [0, 4] \times [0, 4]$ ($25$ positions).
   - Bottom row seed bitmask: $b \in [0, 31]$ ($5$ bits).
   - Top row seed bitmask: $t \in [0, 31]$ ($5$ bits).
   - Carrying status: $c \in \{0, 1\}$.
2. **Transition Rules**:
   - Equal-probability random walk to grid neighbors.
   - If $c = 0$, $y = 0$, and bottom square has seed: pick up seed ($c \to 1$, bit cleared).
   - If $c = 1$, $y = 4$, and top square is empty: drop seed ($c \to 0$, bit set).
3. **Absorbing Expected Value Linear System**:
   We solve $E(s) = 1 + \frac{1}{\text{deg}(s)} \sum_{s'} E(s')$ via Gauss-Seidel value iteration until convergence.
4. **Execution**:
   Evaluating the expected steps from start state $(2, 2, \text{bottom}=31, \text{top}=0, c=0)$ yields $430.088247$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\text{Reachable\_States} \cdot \text{Iterations})$ where reachable states $\approx 6400$. Runs in $\approx 0.45\text{s}$.
- **Space Complexity:** $\mathcal{O}(\text{Reachable\_States})$ state table memory.
