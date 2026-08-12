# Magic 5-gon Ring - Optimal Approach

## Algorithm Explanation

Find the maximum 16-digit string representation for a magic 5-gon ring filled with integers $1 \dots 10$.

### Structure & Constraints:
- Outer nodes: $o_0, o_1, o_2, o_3, o_4$.
- Inner nodes: $i_0, i_1, i_2, i_3, i_4$.
- 5 triplet lines: $(o_0, i_0, i_1), (o_1, i_1, i_2), (o_2, i_2, i_3), (o_3, i_3, i_4), (o_4, i_4, i_0)$.
- **16-Digit Constraint**: For the concatenated string to have length $16$, number $10$ must belong to the outer nodes (since inner nodes appear twice).
- **Canonical Ordering**: Start at $o_0 = \min(o_0, o_1, o_2, o_3, o_4)$.

### Strategy:
1. Permute all $10! = 3,628,800$ node assignments.
2. Enforce canonical start condition $o_0 = \min(o_k)$.
3. Check equal line sums $S = o_k + i_k + i_{(k+1)\%5}$.
4. Concatenate triplets into integer string and record maximum 16-digit result.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(10!)$ with early pruning. Runs in $< 0.3\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Auxiliary memory is constant.
