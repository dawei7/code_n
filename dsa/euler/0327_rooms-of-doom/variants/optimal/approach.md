# Rooms of Doom - Optimal Approach

## Algorithm Explanation

Find $\sum_{C=3}^{40} M(C, 30)$, where $M(C, R)$ is the minimum number of security cards required from a dispensing machine to travel through $R$ rooms carrying at most $C$ cards at any time.

### Backward Dynamic Programming Recurrence:
1. **Room State Transition**:
   To pass through room $r$, let $K$ be the required number of cards needed at the entrance of room $r$.
   - If $K < C$, a single direct step is taken: $K_{\text{prev}} = K + 1$.
   - If $K \ge C$, multiple round-trips are required to deposit cards into room $r$'s storage box before the final move.
     Each round trip yields a net storage of $C - 2$ cards and costs $2$ cards for return.
     The required number of round trips is:
     $$\text{trips} = \left\lceil \frac{K - C + 1}{C - 2} \right\rceil$$
     $$K_{\text{prev}} = K + 2 \cdot \text{trips} + 1$$
2. **Execution**:
   Iterating $R = 30$ room steps for each $3 \le C \le 40$ and summing $M(C, 30)$ yields $34315549139516$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(R \cdot (C_{\max} - C_{\min}))$ for $R = 30$ and $C \le 40$. Runs in $\approx 0.00\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
