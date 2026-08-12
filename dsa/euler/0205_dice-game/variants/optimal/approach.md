# Dice Game - Optimal Approach

## Algorithm Explanation

Find the probability that Pyramidal Peter ($9$ four-sided dice) beats Cubic Colin ($6$ six-sided dice), rounded to $7$ decimal places.

### Dynamic Programming Outcome Distribution:
1. **Sum Distribution**:
   - Compute probability distribution of Peter's total sum $s_p \in [9, 36]$ over $4^9 = 262144$ outcomes.
   - Compute probability distribution of Colin's total sum $s_c \in [6, 36]$ over $6^6 = 46656$ outcomes.
2. **Winning Combination**:
   $$\mathbb{P}(\text{Peter} > \text{Colin}) = \frac{1}{4^9 \cdot 6^6} \sum_{s_p=9}^{36} \operatorname{count}_P(s_p) \sum_{s_c < s_p} \operatorname{count}_C(s_c)$$
3. **Execution**:
   The exact probability rounded to $7$ decimal places is $0.5731441$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(D_1 F_1 + D_2 F_2)$ where $D_1=9, F_1=4$ and $D_2=6, F_2=6$. Runs in $\approx 0.000\text{s}$.
- **Space Complexity:** $\mathcal{O}(\text{MaxSum}) = \mathcal{O}(1)$.
