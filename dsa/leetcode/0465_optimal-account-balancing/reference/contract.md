## Function Contract

**Inputs**

- `transactions`: A list of entries `[from_i, to_i, amount_i]`, each describing one completed transfer between two distinct people.

Let $n$ be the number of input transactions, $p$ the number of distinct person identifiers in those transactions, and $k$ the number of people whose net balance is nonzero after all transactions are combined.

**Return value**

- Return the smallest number of additional transactions that can make every person's net balance zero.

Person identifiers label accounts; they need not form a contiguous range.
