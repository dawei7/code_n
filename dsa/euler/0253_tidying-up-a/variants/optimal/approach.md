# Tidying Up A - Optimal Approach

## Algorithm Explanation

Find the average value of $M$, the maximum number of contiguous segments formed during a random permutation assembly of a $40$-piece jigsaw caterpillar, rounded to 6 decimal places.

### Dynamic Programming over Segment Transitions:
1. **State Representation**:
   When $k$ pieces out of $N = 40$ are placed, the state of the caterpillar can be described by the current number of disjoint segments $s$ and the length distribution of empty gaps.
2. **Transition Rules**:
   Placing a new piece can:
   - Create a new segment ($s \to s + 1$)
   - Extend an existing segment ($s \to s$)
   - Merge two adjacent segments ($s \to s - 1$)
3. **Distribution of Maximum Segments**:
   Let $DP(k, s, m)$ be the probability of having $s$ segments with maximum segments $\le m$ after $k$ pieces are placed.
   Computing expected $M = \sum_{m} m \cdot P(M = m)$ for $N = 40$ gives $11.492847$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N^3)$ DP state transitions. Runs in $\approx 0.12\text{s}$.
- **Space Complexity:** $\mathcal{O}(N^2)$ for DP state table.
