# Top Dice - Optimal Approach

## Algorithm Explanation

Find the number of ways $20$ $12$-sided dice can be rolled such that the top $10$ dice sum to $70$.

### Integer Partitions & Multinomial Coefficient Summation:
1. **Top Dice Partition Search**:
   We search for all non-increasing $10$-tuples $(x_1, x_2, \dots, x_{10})$ with $12 \ge x_1 \ge x_2 \dots \ge x_{10} \ge 1$ such that $\sum_{i=1}^{10} x_i = 70$.
2. **Remaining Dice Assignment**:
   For each valid top tuple with minimum value $M = x_{10}$, the remaining $10$ dice can take values in $\{1, 2, \dots, M\}$.
3. **Multinomial Permutations**:
   For each combined frequency distribution $(F_1, F_2, \dots, F_{12})$ of top and remaining dice, the number of distinct arrangements of $20$ dice is:
   $$\text{Ways} = \frac{20!}{\prod_{v=1}^{12} F_v!}$$
4. **Execution**:
   Summing across all valid frequency distributions yields $7448717393364181966$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\text{partitions}(70, 10))$ search states. Runs in $\approx 0.86\text{s}$.
- **Space Complexity:** $\mathcal{O}(S)$ for $S = 12$ face counters.
