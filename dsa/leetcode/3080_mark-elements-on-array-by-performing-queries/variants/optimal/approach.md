## General

**Turn the repeated minimum rule into one global order.** Every automatic mark chooses the smallest pair `(value, index)` among the currently unmarked elements. Sort all such pairs once. Their lexicographic order exactly matches the rule: smaller values come first, and equal values are ordered by smaller indices.

Maintain a Boolean `marked` array and a cursor into the sorted pairs. For each query, mark its explicit index only if it is not already marked, subtracting that value from `remaining_sum` exactly once.

**Advance one persistent cursor.** To perform the query's $k$ automatic marks, inspect pairs from the cursor onward. A pair whose index was already marked is stale, so skip it. Otherwise mark its index, subtract its value, and decrement $k$. If the cursor reaches the end, every element is marked and the remaining sum is zero.

The cursor never moves backward. Consequently, each sorted pair is inspected at most once across the entire sequence of queries, including pairs made stale by earlier explicit marks.

At every automatic selection, all pairs before the cursor are already marked or have just been consumed. The first unmarked pair at or after the cursor is therefore the globally smallest eligible `(value, index)` pair, exactly as required. Explicit marks update the same `marked` state, and `remaining_sum` subtracts an element precisely when that state changes from unmarked to marked. Thus the recorded value after each query is the sum of exactly the elements that remain unmarked.

## Complexity detail

Sorting the $n$ pairs takes $O(n \log n)$ time. The $m$ queries take $O(m)$ outside the cursor loop, and the cursor performs at most $n$ inspections in total. The overall time is therefore $O(n \log n + m)$. The sorted pairs, marked flags, and answer storage use $O(n + m)$ total space; excluding the required output, the auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Min-heap:** A heap of `(value, index)` pairs with lazy deletion also implements the ordering in $O((n+m)\log n)$ time. Sorting once is simpler because no new values are ever inserted.
- **Rescan for every automatic mark:** Searching the full array for the next eligible minimum is direct and correct, but may take $O(n^2)$ time over the query sequence.
- **Equal values:** Pair ordering must include the index; comparing values alone violates the required smaller-index tie break.
- **Repeated explicit indices:** Check `marked[index]` before subtraction so the running sum changes only once per element.
- **Zero k:** The explicit index is still processed, but no automatic selections are made.
- **Too few remaining elements:** Reaching the end of the sorted pairs naturally marks every available element and leaves zero.
- **Large sums:** The maximum unmarked total can exceed 32-bit signed range, so fixed-width languages need a 64-bit accumulator.
