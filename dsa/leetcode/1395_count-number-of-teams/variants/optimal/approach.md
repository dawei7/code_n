## General
**Choose the middle soldier first.** For each index `j`, count four groups relative to `rating[j]`: smaller and greater ratings to its left, and smaller and greater ratings to its right.

An increasing team with middle index `j` is formed by choosing one smaller left rating and one greater right rating, giving `left_smaller * right_greater` teams. A decreasing team similarly contributes `left_greater * right_smaller`. Add both products for every possible middle index.

Every counted choice has indices in the required order because its members come from the left side, `j`, and the right side. The comparison groups enforce one of the two strict rating orders. Conversely, every valid triple has one unique middle index and belongs to exactly one of those products, so no team is omitted or counted twice.

## Complexity detail
For each of $n$ middle positions, the two side scans inspect $O(n)$ ratings, for $O(n^2)$ time. Only four counters and the total are stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Enumerate all triples:** Testing every $i < j < k$ is correct but costs $O(n^3)$ time.
- **Fenwick trees:** Coordinate-compressed prefix and suffix counts reduce time to $O(n\log n)$ but add data-structure complexity and $O(n)$ space.
- **Exactly three soldiers:** The result is either one or zero depending on their strict order.
- **Strict comparisons:** Equal ratings would not qualify, though the contract guarantees all ratings are distinct.
- **Monotone array:** Every choice of three indices is valid, so the answer is $\binom{n}{3}$.
- **Mixed directions:** A triple that rises and then falls, or falls and then rises, contributes nothing.
