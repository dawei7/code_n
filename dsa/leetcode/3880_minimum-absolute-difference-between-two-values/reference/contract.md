## Function Contract

**Inputs**

- `nums`: An array containing only the integers `0`, `1`, and `2`.

Let $n=\lvert\texttt{nums}\rvert$. Indices are zero-based. A valid pair is ordered by value—its first component indexes a `1` and its second indexes a `2`—but its distance is symmetric.

**Return value**

Return $\min \lvert i-j\rvert$ over all indices satisfying `nums[i] == 1` and `nums[j] == 2`. Return `-1` when that set of pairs is empty.
