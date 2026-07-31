## General

Sorting meetings by start day turns the union into a left-to-right scan. Keep `current_end`, the greatest day covered by any interval processed so far, and `covered`, the number of distinct busy days already counted.

For a sorted interval `[start, end]`, nothing changes when $\texttt{end}\le\texttt{current\_end}$ because the interval is contained in the covered prefix. Otherwise, the newly covered portion begins at the later of `start` and `current_end + 1`, and ends at `end`. Add that inclusive length and move `current_end` to `end`.

Before each iteration, every busy day contributed by earlier intervals has been counted exactly once, and their rightmost covered day is `current_end`. The update adds precisely those days in the new interval that lie to its right, so the property remains true. After all intervals, `covered` is the size of their union. Subtracting it from `days` therefore leaves exactly the work days with no meeting.

## Complexity detail

Let $n = \lvert\texttt{meetings}\rvert$. Sorting takes $O(n\log n)$ time and the scan takes $O(n)$ time, for $O(n\log n)$ overall. The implementation sorts a copied list, requiring $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Explicit merged list:** Store each disjoint merged interval and sum their lengths afterward. This has the same asymptotic cost but retains more state than the running covered total needs.
- **Difference array by day:** Mark interval endpoints and scan every day. Since `days` can be $10^9$, its $O(\texttt{days})$ time and space are infeasible.
- **Repeated sorted insertion:** Insert every meeting into a maintained merged list by a linear scan. It is correct but can take $O(n^2)$ time.
- **Nested intervals:** An interval ending no later than `current_end` contributes zero additional days.
- **Overlapping endpoints:** Inclusive intervals such as `[1,3]` and `[3,5]` jointly cover five days, not six.
- **Adjacent intervals:** `[1,2]` and `[3,4]` have no free day between them; the scan counts both portions without double-counting.
- **Large timeline:** The algorithm depends on the number of meetings rather than iterating through all `days`.
