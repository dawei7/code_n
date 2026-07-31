## Function Contract

**Inputs**

- `nums`: An array of distinct integers containing both endpoints of the original consecutive range.

The input order is arbitrary. Let $L=\min(\texttt{nums})$ and $H=\max(\texttt{nums})$; only absent integers in the inclusive range $[L,H]$ belong in the result.

**Return value**

Return a list containing each integer in $[L,H]$ that does not occur in `nums`, ordered from smallest to largest.
