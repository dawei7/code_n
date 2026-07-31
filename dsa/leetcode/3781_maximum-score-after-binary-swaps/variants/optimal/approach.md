## General

A legal swap moves a one left, never right, and swaps do not change the relative order of the ones. Thus, when the scan reaches an original one, that one may finish at any still-unused position in the prefix seen so far.

Scan positions from left to right and insert each corresponding `nums` value into a max-heap. Whenever the current bit is `'1'`, remove the greatest available prefix value and add it to the score. Heap entries not yet removed remain available for later ones farther to the right.

For the first $j$ original ones, the algorithm chooses the maximum-weight matching between those ones and legal, distinct prefix positions. When the next one is reached, assigning it the greatest unused eligible value cannot hurt any later one, because every later one can use every position currently available plus additional positions. An exchange with any solution that assigns a smaller current value preserves feasibility and never decreases the score. Repeating this argument proves that the accumulated choices are globally optimal and reachable by leftward swaps.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. Each value is inserted once and removed at most once from a heap containing at most $N$ entries, so the running time is $O(N\log N)$. The heap uses $O(N)$ auxiliary space.

## Alternatives and edge cases

- **Suffix capacity heap:** Scan right to left and retain the largest number of suffix values allowed by the number of original ones in that suffix. This is an equivalent greedy formulation with the same asymptotic bounds.
- **Repeated prefix maximum:** Searching and removing the largest available prefix value separately for every one is correct but can take $O(N^2)$ time.
- **No ones:** The heap's final capacity is zero, so the score is `0`.
- **All ones:** No one can cross another one, and there are no zeros to swap; every position remains selected and the score is `sum(nums)`.
- **Zero operations:** Keeping a one in its original position is always legal, so an unfavorable leftward move is never required.
- **Directionality:** The allowed `"01" -> "10"` swap moves a one left only; treating swaps as bidirectional changes the problem.
- **Large score:** Up to $N$ values as large as $10^9$ may contribute, so the sum can exceed 32-bit range.
