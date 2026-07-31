## General

A legal swap moves a one left, never right, and swaps do not change the relative order of the ones. Consequently, for every suffix, the final arrangement may contain no more ones in that suffix than the original string contains there: ones can leave a suffix by moving left, but none can enter it from the left.

Scan positions from right to left. Let `suffix_capacity` be the number of original ones seen so far. Among all score positions in the current suffix, retain the largest `suffix_capacity` values in a min-heap. Add the current `nums[i]`; if the heap exceeds the permitted number of selected positions, discard its smallest value.

After processing a suffix, the heap is the maximum-weight selection satisfying that suffix's capacity. When the scan extends one position left, either the capacity stays fixed or grows by one, so adding the new value and dropping only the smallest excess value preserves optimality. These nested suffix limits are exactly the reachability limits imposed by leftward swaps. At the end, the heap contains one score position for every original one and represents a reachable maximum-score arrangement.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. Each value is inserted once and removed at most once from a heap containing at most $N$ entries, so the running time is $O(N\log N)$. The heap uses $O(N)$ auxiliary space.

## Alternatives and edge cases

- **Prefix max-heap:** Scan left to right, add every available position, and whenever the original string supplies a one, assign it the greatest unused prefix value. This equivalent greedy is the exact native Accepted formulation.
- **Repeated prefix maximum:** Searching and removing the largest available prefix value separately for every one is correct but can take $O(N^2)$ time.
- **No ones:** The heap's final capacity is zero, so the score is `0`.
- **All ones:** No one can cross another one, and there are no zeros to swap; every position remains selected and the score is `sum(nums)`.
- **Zero operations:** Keeping a one in its original position is always legal, so an unfavorable leftward move is never required.
- **Directionality:** The allowed `"01" -> "10"` swap moves a one left only; treating swaps as bidirectional changes the problem.
- **Large score:** Up to $N$ values as large as $10^9$ may contribute, so the sum can exceed 32-bit range.
