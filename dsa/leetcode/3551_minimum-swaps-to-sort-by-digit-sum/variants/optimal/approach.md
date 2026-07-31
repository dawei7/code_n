## General

Sorting by digit sum alone is insufficient because equal sums are ordered by the values themselves. Associate every value with the key `(digit_sum(value), value)` and sort by that key. Since all input values are distinct, this produces one unambiguous target permutation.

Maintain a map from each value to its current array position. Visit target positions from left to right. If the correct value is already at the current position, no action is needed. Otherwise, the map identifies exactly where that value currently sits; swap it into place and update the two affected map entries. The fixed prefix never changes again.

Every nontrivial permutation cycle of length $k$ needs at least $k-1$ swaps: one swap can place at most one additional cycle element into its final position. The left-to-right repairs use exactly $k-1$ swaps for that cycle. Summed over all cycles, the greedy repairs therefore attain the global minimum.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$. Each value has at most ten decimal digits under the stated bound, so all digit sums take $O(n)$ total time. Sorting dominates at $O(n \log n)$ time. Building and maintaining the position map takes $O(n)$ additional space; the sorted target also occupies $O(n)$ space.

## Alternatives and edge cases

- **Explicit cycle decomposition:** Map every original position to its target position, mark visited positions, and add $k-1$ for each cycle of length $k$. It has the same asymptotic bounds but needs a separate visited array.
- **Repeated linear searches:** Finding each desired value by scanning the remaining suffix is correct but degrades to $O(n^2)$ time.
- **Tie handling:** Equal digit sums must be resolved by smaller numeric value, not by original position or stable input order.
- **Already sorted input:** Every map lookup returns the current index, so the result remains zero.
- **Single value:** The only permutation is a fixed point and requires no swap.
- **Large values:** `1000000000` has digit sum $1$; decimal magnitude does not determine the sorting key.
- **Input mutation:** The reference adapter rearranges its local array while counting swaps; the required output is only the count.
