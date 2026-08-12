# Prize Strings - Optimal Approach

## Algorithm Explanation

Count the number of valid $n$-day attendance strings using $\{O, L, A\}$ such that:
1. The student is late ($L$) on **at most one** occasion.
2. The student is absent ($A$) for **fewer than three consecutive** days (no $AAA$).

### Dynamic Programming State & Transitions:
1. **DP State**:
   Let `dp[lates][consec_absent]` be the number of valid strings after $d$ days with:
   - `lates` $\in \{0, 1\}$ (total $L$ count so far).
   - `consec_absent` $\in \{0, 1, 2\}$ (streak of trailing $A$'s).
   Base case: `dp[0][0] = 1` for $0$ days.
2. **Transitions for Day $d+1$**:
   For each state `(lates, consec_absent)` with count $C$:
   - Append 'O': transitions to `(lates, 0)` with $+C$.
   - Append 'L': if `lates == 0`, transitions to `(1, 0)` with $+C$.
   - Append 'A': if `consec_absent < 2`, transitions to `(lates, consec_absent + 1)` with $+C$.
3. **Execution**:
   After $30$ days, summing all $6$ state entries gives $1,918,080,160$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\text{days})$ - $6$ states and constant operations per day. Runs in $\approx 0.000\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Two $2 \times 3$ DP tables.
