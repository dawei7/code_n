## General
**Reduce each row to its trailing-zero capacity**

At final row position `i`, all columns after `i` are above the diagonal and must be zero. Therefore, that row needs at least `n - i - 1` trailing zeros. The rest of its contents do not affect validity, so first record one trailing-zero count per row.

**Choose the earliest feasible row greedily**

Process target positions from top to bottom. Find the first row at or below the current position whose trailing-zero count meets the requirement, then move it upward by adjacent swaps. If no such row exists, no later rearrangement can fill this position and the answer is `-1`.

Choosing the earliest feasible row is optimal. Any valid arrangement must bring some feasible remaining row to the current position. A row farther down costs at least as many swaps and passes over every row crossed by the earliest candidate; using the earliest candidate preserves all other rows in their relative order and cannot make a later requirement harder.

The implementation moves only trailing-zero counts, not matrix rows. Adding the candidate's displacement gives exactly the number of adjacent swaps needed to perform the same stable row move.

## Complexity detail
Counting trailing zeros inspects at most $n^2$ cells. For each of $n$ positions, searching for a feasible row and shifting the capacity list can take $O(n)$ time, for $O(n^2)$ total.

The capacity list contains $n$ integers, giving $O(n)$ auxiliary space. The input grid need not be modified.

## Alternatives and edge cases
- **Physical row bubbling:** produces the same minimum but copying full rows during each swap can cost $O(n^3)$ time.
- **Try every row permutation:** guarantees a minimum but requires factorial time.
- **Sort by trailing zeros:** unrestricted sorting does not directly account for the adjacent-swap cost or stable minimum movement.
- **Single-cell grid:** there are no cells above the diagonal, so zero swaps are needed.
- **Already valid:** every position immediately finds its current row and contributes zero.
- **Impossible top row:** absence of any row with at least $n-1$ trailing zeros proves impossibility immediately.
- **Extra trailing zeros:** a row may exceed its current requirement and remains feasible.
- **Duplicate capacities:** rows with equal trailing-zero counts are interchangeable for validity; choosing the first minimizes movement.
