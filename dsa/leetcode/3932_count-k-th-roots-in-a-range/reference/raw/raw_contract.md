## Function Contract

**Inputs**

- `l`: The inclusive lower endpoint of the nonnegative integer range.
- `r`: The inclusive upper endpoint of the range, with `r >= l`.
- `k`: The positive integer exponent in the relation $y=x^k$.

For the complexity bounds, define $R=\max(2,\texttt{r}+1)$ and $K=\max(2,\texttt{k})$. A value is counted once if there exists any integer base that produces it. Both endpoints belong to the range, so a perfect power equal to `l` or `r` is included.

**Return value**

Return the number of distinct integers `y` in `[l, r]` for which some integer `x` satisfies $y=x^k$.
