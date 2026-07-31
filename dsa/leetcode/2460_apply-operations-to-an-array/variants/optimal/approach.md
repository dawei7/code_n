## General

Perform the problem's two phases directly. First scan indices $0$ through $n-2$ in increasing order. Whenever the current value equals its right neighbor, double the current value and immediately replace the neighbor with zero. Writing each change at once is essential: the next iteration must observe the array produced by every earlier operation.

**Stable in-place compaction.** After the simulation, maintain a write pointer for the next nonzero destination. Read the modified array from left to right. For each nonzero value, copy it to `nums[write]` and advance `write`. Reading in original order preserves the relative order of the nonzero values. The copy is safe even when the read and write positions coincide; otherwise, the write position is strictly behind the read position and cannot destroy an unread value.

Once all values have been examined, every position before `write` contains exactly the nonzero sequence in its required order. Fill positions from `write` through $n-1$ with zero. This preserves the length and supplies exactly as many trailing zeros as the simulation produced or the input already contained.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. The operation simulation, stable compaction, and trailing-zero fill each take at most one linear pass, so total time is $O(n)$.

All changes are stored in `nums`; the algorithm uses only indices and scalar values beyond the returned input array. Auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Separate output array:** Collecting nonzero values into a new length-$n$ array is also $O(n)$ time, but it uses $O(n)$ auxiliary space instead of meeting the in-place bound.
- **Repeated deletion and insertion:** Removing each zero and appending it to the end can preserve the required result, but shifting array elements after every deletion can take $O(n^2)$ time.
- **Sequential semantics:** A mutation at index $i$ must be visible when index $i+1$ is processed; computing all equal pairs from the original array would be incorrect.
- **Three equal values:** `[2, 2, 2]` becomes `[4, 0, 2]` during simulation and `[4, 2, 0]` after compaction, rather than merging twice.
- **Equal zeros:** Applying the doubling rule to `0, 0` leaves both entries zero and does not affect later nonzero order.
- **Existing zeros:** Zeros present before the operations and zeros created by merges are treated identically during compaction.
- **No merges:** If no adjacent pair matches, only the stable zero shift can change the array.
