## General

Start from `Products` because every product must appear in the result. Left-join `Discounts` on equal `category`; this attaches the one applicable percentage when it exists while retaining products whose categories have no discount row.

For an unmatched row, the joined discount is `NULL`. `COALESCE(d.discount, 0)` treats that absence as a zero-percent discount. Multiplying `price` by the remaining percentage and dividing by 100 then handles matched, zero-percent, full-price, and 100-percent discounts with one expression. Finally, sort by `product_id` ascending as required.

## Complexity detail

Let $P$ and $D$ be the row counts of `Products` and `Discounts`. With ordinary indexed, hash, or sort-based relational operators, joining and ordering require at most $O((P+D)\log(P+D))$ time and $O(P+D)$ working space. Exact access paths and constants depend on the database engine and available indexes.

## Alternatives and edge cases

- **Inner join:** This incorrectly removes every product whose category has no discount.
- **Correlated scalar subquery:** Looking up the discount separately for each product is expressible but can repeat work when many products share a category.
- **Missing discount:** `COALESCE` converts the joined `NULL` to zero, preserving the original price.
- **Zero or full discount:** Percentages 0 and 100 naturally produce the original price and zero, respectively.
- **Decimal arithmetic:** The percentage expression retains decimal price semantics and must not truncate fractional prices prematurely.
- **Output order:** The explicit `ORDER BY` is necessary because relational results otherwise have no guaranteed order.
