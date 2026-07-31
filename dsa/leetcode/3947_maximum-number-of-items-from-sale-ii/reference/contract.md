## Function Contract

**Inputs**

- `items`: A nonempty list of rows `[factor_i, price_i]`, one for each indexed item type.
- `budget`: The maximum amount that may be spent on purchased copies.

Let $n=\lvert\texttt{items}\rvert$.

**Return value**

Return the maximum number of purchased plus awarded free copies achievable with total purchase cost at most `budget`.
