## Function Contract

**Inputs**

- `nums`: a non-empty array of unique integers in ascending order.
- `k`: the one-based position of the requested missing number.

Let $N = \lvert\texttt{nums}\rvert$. Missing values are counted strictly after `nums[0]`, first through the gaps between stored values and then beyond `nums[N - 1]` if necessary.

**Return value**

- The $k$th missing integer in that increasing sequence.
