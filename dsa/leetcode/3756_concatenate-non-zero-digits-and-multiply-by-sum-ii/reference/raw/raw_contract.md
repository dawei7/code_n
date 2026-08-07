## Function Contract

**Inputs**

- `s`: A nonempty string whose characters are decimal digits.
- `queries`: An array of inclusive index pairs `[l_i, r_i]` into `s`.

Let $m = \lvert\texttt{s}\rvert$ and $q = \lvert\texttt{queries}\rvert$. Each query is evaluated independently against the original string; removing zeros does not modify `s` or shift later query indices.

**Return value**

Return an array of $q$ integers. For each query, concatenate its nonzero digits in order, multiply that value by their digit sum, and return the product modulo $10^9+7$.
