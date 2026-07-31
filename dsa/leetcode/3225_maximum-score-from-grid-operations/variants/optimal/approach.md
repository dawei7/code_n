## General

Represent column $j$ by a height $h_j\in[0,n]$, the number of cells colored black from its top. A white cell in column $j$ scores when its row is at least $h_j$ but below $h_{j-1}$ or $h_{j+1}$. If $P_j(h)$ is the sum of the first $h$ values in column $j$, its completed contribution is

$$
\max\left(0,\;P_j\!\left(\max(h_{j-1},h_{j+1})\right)-P_j(h_j)\right).
$$

**Keep the two boundary heights.** A DP state `dp[left][center]` stores the best score after all columns before `center` have been finalized, with the last two chosen heights equal to `left` and `center`. Choosing the next height `right` finalizes the center column. The direct transition over all three heights would take $O(n^4)$ total time.

**Compress the left-height transition.** For fixed `center`, split possible `left` heights around `right`. When `left <= right`, the center contribution depends only on `right`, so a prefix maximum of `dp[left][center]` supplies the best predecessor. When `left > right`, the contribution depends only on `left`, so a suffix maximum of `dp[left][center]` plus that left-side contribution supplies the best predecessor. Building both arrays and evaluating every `right` takes $O(n)$ for one center height instead of $O(n^2)$.

Initialize states by finalizing the first column from its right neighbor. Process each interior column, then add the last column's contribution from its left neighbor. Column prefix sums make every vertical segment value available in constant time. The state examines every height sequence, while the prefix/suffix compression preserves the maximum of the exact direct transitions.

## Complexity detail

There are $n+1$ possible black-prefix heights. Each of $n$ columns processes $O(n^2)$ height states with constant-time amortized transitions after prefix/suffix maxima, giving $O(n^3)$ time. The rolling DP matrices and column prefix sums use $O(n^2)$ space.

## Alternatives and edge cases

- **Enumerate the previous height for every transition:** This is the same exact DP without prefix/suffix compression and takes $O(n^4)$ time.
- **Assume the heights are unimodal:** The operation imposes no such restriction; arbitrary column-prefix heights are legal.
- A white cell adjacent to black cells on both sides is counted once, not twice.
- A black cell never contributes its own value.
- Boundary columns have only one horizontal neighbor.
- For $n=1$, the answer is always zero.
- Zero-valued cells can be exposed without changing the score and must not invalidate a height choice.
