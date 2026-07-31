## Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers.
- `k`: The number of smallest and largest occurrences included in the two sums.

Let $N=\lvert\texttt{nums}\rvert$ and let $V=100$ be the size of the permitted value domain. The two groups are chosen independently and may overlap when `2 * k > n`.

**Return value**

Return `abs(largest_sum - smallest_sum)`. When `k = n`, both groups contain the whole array and the result is zero.
