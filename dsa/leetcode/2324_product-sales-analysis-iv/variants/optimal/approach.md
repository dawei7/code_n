## General

The comparison is between a user's total spending on products, not between individual sale rows. First join each sale to its product price, multiply `quantity` by `price`, and sum those amounts for every `(user_id, product_id)` pair.

The resulting relation has one cumulative amount per user-product pair. Apply `DENSE_RANK()` within each user, ordering amounts from greatest to least. Every maximum receives position 1, including all equal maximums, while every smaller total receives a later position.

Filtering to position 1 returns exactly the requested ties. Only the two identifier columns are selected, and no final sort is added because the contract permits any row order.

## Complexity detail

Let $s$ be the number of sales rows and $p$ the number of product rows. In a general database execution model, joining and reading the relations plus grouping and ranking take $O((s+p)\log s)$ time. Hash tables, grouped intermediates, and ranking workspace can require $O(s+p)$ space. Indexes and optimizer choices may improve the physical plan without weakening these conservative bounds.

## Alternatives and edge cases

- **Rank raw sales:** Ranking before aggregation compares individual purchases and fails when several smaller purchases of one product form the largest cumulative spend.
- **Maximum plus join:** Computing each user's maximum total and joining it back is valid, but requires the same grouped spending relation and careful preservation of ties.
- **`ROW_NUMBER()` instead of `DENSE_RANK()`:** Row numbering would arbitrarily keep only one product when several share the maximum.
- **Repeated user-product sales:** Their quantities must contribute to one cumulative amount.
- **Unrestricted output order:** Adding an order is harmless but unnecessary; validation treats the result as an unordered table.
