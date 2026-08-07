## Function Contract

**Inputs**

- `nums`: the integer array to test.

Let $n = \lvert\texttt{nums}\rvert$. A valid result requires three ordered separator indices with at least one array
element before, between, and after them. Inputs with $n < 7$ are legal under the source constraints but cannot contain
such a split. Values may be positive, zero, or negative, and the separator values never contribute to a section sum.

**Return value**

Return `True` if some valid `(i, j, k)` makes the four retained subarray sums equal; otherwise return `False`. Only
feasibility is returned, not the indices or shared sum.
