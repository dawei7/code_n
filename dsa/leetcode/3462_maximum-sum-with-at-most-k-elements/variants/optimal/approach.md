## General

Within any row, if a selected value is smaller than an unselected value from the same row, swapping them preserves both constraints and cannot decrease the sum. Therefore row `i` can contribute only from its largest `limits[i]` values.

Sort every row in descending order. Each allowed row prefix is then an individually sorted candidate list. Push the first value of every nonempty prefix into a max-heap, together with its row and position. Repeatedly remove the heap maximum, add it to the answer, and expose the next value from that same row when the row limit has not been reached. This is a multiway merge of descending lists, so every removal yields the greatest eligible value not yet selected anywhere.

Because all matrix values are nonnegative and `k` does not exceed total row capacity, selecting another eligible value never lowers the sum. Thus an optimum uses exactly `k` values. The exchange argument restricts every optimum to the allowed row prefixes, and the heap merge chooses the globally largest `k` values from precisely those prefixes, proving the result is optimal.

## Complexity detail

Let `grid` have $n$ rows and $m$ columns. Sorting all rows takes $O(nm\log m)$ time. The heap contains at most one entry per row, and each of the $k$ selections performs at most one removal and one insertion, taking $O(k\log n)$ additional time. The total is $O(nm\log m+k\log n)$. The heap uses $O(n)$ entries, while Python's row sort may require $O(m)$ auxiliary storage, giving $O(n+m)$ auxiliary space. The input rows are reordered in place.

## Alternatives and edge cases

- **Collect every allowed prefix and sort globally:** This is correct but stores up to $\sum_i\texttt{limits[i]}$ candidates and sorts all of them instead of maintaining only one heap entry per row.
- **Repeatedly scan all remaining candidates:** Finding the next maximum with a linear scan for each selection is correct but can take quadratic time in the number of eligible cells.
- **Take each row's limit unconditionally:** The row capacities are upper bounds; the global `k` limit may require leaving many allowed values unselected.
- **Use the first values without sorting:** Matrix order has no selection meaning, so the allowed contribution from a row must be based on value, not column position.
- **Zero row limit:** Such a row contributes no heap entry even if it contains the matrix maximum.
- **Zero global limit:** No heap removal occurs and the answer is zero.
- **Zero-valued cells:** Selecting them does not change the sum, so using exactly `k` remains safe.
- **Duplicate values:** Heap tuple fields provide deterministic ordering, while equal values remain interchangeable for optimality.
- **Large sum:** Up to $250000$ values of $10^5$ may be selected, so fixed-width implementations need a wide integer type.
