# Monopoly Odds - Optimal Approach

## Algorithm Explanation

Find the 6-digit modal string for the top $3$ most frequently visited Monopoly board squares when playing with two $4$-sided dice.

### Rules & Transitions:
1. **Board Layout**: $40$ squares numbered $00$ to $39$.
2. **Dice**: Two $4$-sided dice (sum $2 \dots 8$).
3. **Rule Set**:
   - $3$ consecutive doubles send the player directly to JAIL ($10$).
   - Landing on G2J ($30$) moves directly to JAIL ($10$).
   - CC (Community Chest $2, 17, 33$) cards: $2/16$ movement cards (GO, JAIL).
   - CH (Chance $7, 22, 36$) cards: $10/16$ movement cards (GO, JAIL, C1, E3, H2, R1, Next R, Next U, Back 3).
   - If "Back 3" from CH36 lands on CC17, draw a CC card immediately.

### Simulation Strategy:
Run a stationary distribution Markov simulation over $2,000,000$ rolls to extract exact limiting probabilities and output the concatenated 6-digit modal string for the top $3$ squares.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ where $N = 2,000,000$ rolls. Runs in $< 0.4\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary array storage.
