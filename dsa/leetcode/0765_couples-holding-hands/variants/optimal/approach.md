## General
**Locate every partner in constant time**

Couple numbering makes the partner of person `x` equal to $x \oplus 1$: the operation changes only the final bit. Build a table from each person to their current seat, then inspect seat pairs from left to right.

**Repair a mismatched seat pair immediately**

For seats `first` and `first + 1`, let `person` occupy `first`. If the neighbor is not `person ^ 1`, find that partner through the position table and swap the partner into `first + 1`. Update both affected positions in the table and count one move. Never touch this completed seat pair again.

Any valid final seating must change a mismatched pair because its first person currently lacks their partner, so at least one future swap is unavoidable. The greedy swap uses exactly one move to finish that pair and exchanges only seats in the unprocessed suffix, leaving all earlier couples intact. It therefore meets the lower bound for the current pair without reducing the best achievable result for the suffix. Repeating this argument proves the total is minimum.

## Complexity detail
Let `n` be the number of people. Building the position table and processing $n / 2$ seat pairs take $O(n)$ time. The copied seating and position table use $O(n)$ space.

## Alternatives and edge cases
- **Union-find over couples:** Connect the two couple IDs present in each seat pair; a component of `k` couples needs $k - 1$ swaps, giving the same answer in near-linear time.
- **Graph cycle counting:** Seat pairs create a degree-two multigraph of couples, and each component contributes its vertices minus one.
- **Linear partner search after every mismatch:** The same greedy choice remains correct, but repeatedly scanning the suffix costs $O(n^2)$ time.
- **Couple already adjacent:** No swap is made, even if the higher-numbered partner sits first.
- **Single couple:** The answer is always zero.
- **One long misplacement cycle:** A component containing `k` couples requires exactly $k - 1$ swaps.
- **Input preservation:** Working on a copy avoids changing the caller's row while computing the count.
