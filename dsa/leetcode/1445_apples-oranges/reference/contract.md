## Function Contract

**Input**

- `Sales(sale_date, fruit, sold_num)` records a daily quantity for `apples` or `oranges`;
- (`sale_date`, `fruit`) uniquely identifies a row.

Let $R$ be the number of rows in `Sales`, and let $D$ be the number of distinct sale dates.

**Return value**

Return `sale_date` and `diff` for every recorded date, where

$$
\texttt{diff}=\text{apples sold}-\text{oranges sold}.
$$

Order the $D$ result rows by `sale_date` ascending.
