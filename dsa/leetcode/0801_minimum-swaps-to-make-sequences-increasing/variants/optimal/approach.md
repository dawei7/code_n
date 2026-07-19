## General
**Keep only the previous swap decision**

At index `i`, later feasibility depends on which values occupy index `i`, not on the full history. Maintain `keep`, the minimum cost through the previous index when it was not swapped, and `swap`, the minimum cost when it was swapped. Initially these costs are `0` and `1`.

**Test the two possible alignments**

If `nums1[i] > nums1[i - 1]` and `nums2[i] > nums2[i - 1]`, using the same decision at both indices preserves increasing order: `keep` can follow `keep`, and a new swapped state can follow `swap` with one additional swap.

If `nums1[i] > nums2[i - 1]` and `nums2[i] > nums1[i - 1]`, changing orientation between the indices is valid: a kept current pair can follow a swapped previous pair, while a swapped current pair can follow a kept previous pair with one additional swap. When both conditions hold, take the cheaper predecessor for each state.

These transitions examine every possible valid decision for index `i` from each possible valid decision at $i - 1$. By induction, the two stored costs are the minima for their respective current orientations. The smaller final state therefore gives the global minimum among all valid swap patterns.

## Complexity detail
Each of the `n` index pairs is processed once with constant work, giving $O(n)$ time. Four scalar state values replace the full dynamic-programming table, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Two-column DP table:** Store keep/swap costs for every index; it uses the same recurrence and $O(n)$ time but requires $O(n)$ space.
- **Memoized recursion:** State `(index, previous-swapped)` also gives $O(n)$ states, though recursion and memo storage are unnecessary.
- **Enumerate swap subsets:** Trying all $2^{n}$ choices is correct for small lists but exponential.
- **Both alignments valid:** Take minima from both predecessor orientations rather than committing greedily.
- **Only cross alignment valid:** The decision must flip between the two adjacent indices.
- **Strict comparison:** Equal adjacent values are not increasing and must not use `>=`.
- **Single pair:** Both length-one sequences are already increasing, so zero swaps are optimal.
