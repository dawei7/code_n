## General
**Make every chosen slot as light as possible.** Sort the apple weights in ascending order. For any target count $c$, the $c$ lightest apples have no greater total weight than any other selection of $c$ apples. Consequently, if that lightest prefix does not fit, no selection of the same size can fit; if it does fit, it is a valid selection.

**Grow the feasible prefix greedily.** Traverse the sorted weights while maintaining the current total. Add the next apple when the new total is at most 5000. The first weight that would exceed capacity proves that the current prefix count is maximal by the lightest-prefix argument, so return it immediately. If no weight causes overflow, every apple fits and the answer is $n$.

## Complexity detail
Sorting $n$ weights costs $O(n\log n)$ time, and the prefix scan costs $O(n)$, for an overall $O(n\log n)$ bound. Python's sorted copy may use $O(n)$ auxiliary space; the running total and count themselves require $O(1)$ space.

## Alternatives and edge cases
- **Repeated minimum selection:** Finding and removing the lightest remaining apple on every step is correct but can take $O(n^2)$ time.
- **Counting by weight:** Because weights lie between 1 and 1000, a fixed frequency array can avoid comparison sorting and run in $O(n+1000)$ time, at the cost of a less general implementation.
- **All apples fit:** Exhausting the sorted list returns its full length.
- **Exact capacity:** A cumulative weight of exactly 5000 is valid; only a strictly larger sum stops selection.
- **Single apple:** Its weight is at most 1000, so it always fits.
- **Duplicate weights:** Equal-weight apples are interchangeable, and each occurrence still contributes one to the count.
- **Input order:** Heavy apples appearing first must not prevent lighter later apples from being selected.
- **Positive weights:** Since every weight is at least 1, adding another apple never decreases the cumulative weight.
