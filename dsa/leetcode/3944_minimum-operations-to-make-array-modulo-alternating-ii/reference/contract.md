## Function Contract

**Inputs**

- `nums`: A nonempty integer array. Indices are zero-based, so index `0` belongs to the even-index group.
- `k`: The modulus. Every selected target residue lies in `[0, k)`, and the even-index and odd-index target residues must be different.

Let $n = \lvert\texttt{nums}\rvert$. Increasing or decreasing one element by `1` costs one operation; any element may be changed repeatedly. Only each final value's remainder modulo `k` matters to the alternating condition.

**Return value**

Return the minimum total number of unit increment or decrement operations needed to make all even-index elements share one residue and all odd-index elements share a different residue.

