## Function Contract

**Inputs**

- `arr`: The remaining arithmetic-progression values in their original order.

Let $n = \lvert\texttt{arr}\rvert$. The original progression contained $n+1$ values, and exactly one interior value was removed. The input guarantee covers increasing, decreasing, and constant progressions.

**Return value**

Return the removed integer value. Because neither original endpoint was removed, `arr[0]` and `arr[-1]` are the original first and last values.
