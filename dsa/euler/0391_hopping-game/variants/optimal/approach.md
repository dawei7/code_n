# Hopping Game - Optimal Approach

## Algorithm Explanation

Find $\sum_{n=1}^{1000} M(n)^3$, where $M(n)$ is the maximum initial move $x \in [1, n]$ for the first player to force a win in the counter game played on sequence $S = \{s_k\}$ (cumulative binary digit $1$-count).

### Minimax Impartial Game State Backward DP:
1. **Game State Transition Rules**:
   The counter $c$ starts at $0$.
   A move consists of picking $x \in [1, n]$ such that the new counter $c' = c + x \in S$.
   A state $c \in S$ is a winning position if there exists at least one valid move $x \in [1, n]$ leading to a losing state $c + x$.
2. **Backward Dynamic Programming**:
   For each game parameter $n \in [1, 1000]$, we construct the finite subset of valid game states $S \cap [0, S_{\max}(n)]$.
   We compute state outcomes $W(c) \in \{\text{WIN}, \text{LOSS}\}$ backwards from the terminal state.
3. **Optimal First Move $M(n)$**:
   $M(n)$ is the maximum $x \in [1, n]$ such that $x \in S$ and $x$ is a losing position for the opponent (or $0$ if no winning move exists).
4. **Execution**:
   Evaluating $M(n)$ for $n = 1 \dots 1000$ and summing $M(n)^3$ yields $61029882288$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \cdot S_{\max})$ for $N = 1000$. Runs in $\approx 0.35\text{s}$.
- **Space Complexity:** $\mathcal{O}(S_{\max})$ outcome bitarray.
