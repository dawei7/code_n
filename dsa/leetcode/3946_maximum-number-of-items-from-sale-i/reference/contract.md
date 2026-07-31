## Function Contract

**Inputs**

- `items`: A nonempty list of rows `[factor_i, price_i]`, one for each indexed item type.
- `budget`: The maximum total amount that may be spent on purchased copies.

Let $n=\lvert\texttt{items}\rvert$, let $B=\texttt{budget}$, and let $F=\max_i \texttt{factor_i}$.

**Return value**

Return the maximum number of purchased plus awarded free copies achievable with purchase cost at most `budget`.
