## Function Contract

**Inputs**

- `grid`: A nonempty rectangular array of equal-length strings containing only `'.'` and `'#'`.
- `d`: The inclusive Euclidean-distance limit for every move.

The bottom and top rows coincide when `grid` has one row. In that case, selecting one available starting cell already forms a route; one legal same-row move may also be the final move. A move must change cells, so remaining at the same coordinate is not an additional route step.

**Return value**

Return the number of cell sequences satisfying the start, finish, availability, distance, row-direction, and consecutive-same-row rules, reduced modulo $1{,}000{,}000{,}007$.
