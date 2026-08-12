# A Preference for A5 - Optimal Approach

## Algorithm Explanation

Find the expected number of times during a $16$-batch week that the supervisor finds a single sheet of paper in the envelope, excluding the first and last batches of the week.

### State Representation & Cutting Rules:
Represent the envelope contents as a 4-tuple state $(c_2, c_3, c_4, c_5)$ counting available sheets of sizes A2, A3, A4, and A5.

1. **Monday Morning First Batch**:
   - Supervisor cuts A1 $\to$ 2 A2 $\to$ 1 A2 + 2 A3 $\to$ 1 A2 + 1 A3 + 2 A4 $\to$ 1 A2 + 1 A3 + 1 A4 + 2 A5.
   - Uses 1 A5 for batch 1.
   - Initial envelope state: $(1, 1, 1, 1)$ (total 4 sheets, batch 1).
2. **State Transitions**:
   - Total sheets $T = c_2 + c_3 + c_4 + c_5$.
   - Drawing size A2 (prob $c_2/T$): state $\to (c_2 - 1, c_3 + 1, c_4 + 1, c_5 + 1)$.
   - Drawing size A3 (prob $c_3/T$): state $\to (c_2, c_3 - 1, c_4 + 1, c_5 + 1)$.
   - Drawing size A4 (prob $c_4/T$): state $\to (c_2, c_3, c_4 - 1, c_5 + 1)$.
   - Drawing size A5 (prob $c_5/T$): state $\to (c_2, c_3, c_4, c_5 - 1)$.
3. **Probability Tree DFS**:
   - Whenever $T == 1$ and $\text{batch\_num} \notin \{1, 16\}$, add path probability to expected sum.
   - Format answer rounded to $6$ decimal places.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\text{State Space})$ ($< 1000$ tree states). Runs in $< 0.001\text{s}$.
- **Space Complexity:** $\mathcal{O}(\text{Max Depth})$ - Depth $16$ stack.
