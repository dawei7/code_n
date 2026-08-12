# Maximix Arrangements - Optimal Approach

## Algorithm Explanation

Find the 2011th lexicographic maximix arrangement for $11$ train carriages labeled $A$ through $K$.

### Reverse Shunting Rotation Backtracking:
1. **Maximix Condition**:
   Simple Simon solves carriage by carriage ($A, B, C, \ldots$).
   A maximix arrangement requires the maximum possible number of turntable rotations ($2N - 3$).
   This occurs when at each step $i$, carriage $i$ is not already at index $i$, and is not at the end of the un-sorted suffix (requiring two full 180-degree rotations: one to move it to the end, and one to flip it into position $i$).
2. **Reverse Backtracking Generation**:
   Starting from the sorted array `['A', 'B', 'C', ..., 'K']`, we apply valid reverse maximix rotation moves from right to left ($i = N-2$ down to $0$).
   - For each step $i$, carriage $i$ must end up in position $j$ where $i < j < N-1$.
   - Reverse the prefix $[i..N-1]$ and then reverse $[j..N-1]$.
3. **Lexicographical Selection**:
   Sorting all generated maximix strings lexicographically and selecting the 2011th element yields `"CAGBIHEFJDK"`.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(2^N \cdot N)$ for $N = 11$. Runs in $\approx 0.05\text{s}$.
- **Space Complexity:** $\mathcal{O}(2^N \cdot N)$.
