## Function Contract

**Inputs**

- `nums`: A nonempty integer array.

Let $N=\lvert\texttt{nums}\rvert$. Each operation discards one prefix of length $\min(3,\text{current length})$; it never removes elements from another position or changes the relative order of survivors.

**Return value**

Return the minimum—and, because the operation is fixed, uniquely determined—number of prefix-removal operations needed until the remaining suffix is empty or has pairwise-distinct values.
