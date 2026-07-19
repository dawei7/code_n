## General
**Separate magnitudes from sign parity**

Every operation changes two signs and never changes an absolute value.
Because the grid's adjacency graph is connected, sign changes can be moved
along paths: two negative signs can be brought together and eliminated.
Consequently, an even number of negative entries permits every magnitude to
be positive.

If the negative count is odd and no zero is available, an odd negative count
must remain because every operation changes that count by an even amount.
To maximize the sum, assign the unavoidable negative sign to the entry with
the smallest absolute value. A zero has magnitude zero, so the same formula
also handles it without a separate branch.

**Compute the best sum in one scan**

Accumulate the sum of every absolute value, count negative entries, and track
the smallest magnitude. With an even negative count, return the absolute-value
sum. With an odd count, changing the smallest magnitude from positive to
negative reduces that sum by twice its magnitude, so return

$$
\sum_{i,j}\lvert\texttt{matrix[i][j]}\rvert
-2\min_{i,j}\lvert\texttt{matrix[i][j]}\rvert.
$$

The construction argument shows this bound is reachable, while parity shows
that no arrangement can avoid the stated loss when the negative count is odd.

## Complexity detail
There are $M=n^2$ cells. The algorithm reads each cell once and performs
constant work, giving $O(M)$ time. The accumulated sum, negative count, and
smallest magnitude use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Simulate sign-flip operations:** Searching sequences of adjacent flips
  creates an enormous state space and is unnecessary once the parity invariant
  is identified.
- **Sort all magnitudes:** Sorting reveals the smallest magnitude but costs
  $O(M\log M)$ time and $O(M)$ storage when a running minimum suffices.
- **Repeated minimum scans:** Recomputing the global minimum while processing
  every cell remains correct but takes $O(M^2)$ time.
- Zero absorbs the unavoidable odd sign at no sum cost because `-0 == 0`.
- With an even negative count, every entry can contribute its full absolute
  value regardless of where those negatives initially occur.
- With an odd negative count, the smallest magnitude is sacrificed even when
  that entry was initially positive.
- Large values require a return type capable of holding sums beyond 32-bit
  signed range.
