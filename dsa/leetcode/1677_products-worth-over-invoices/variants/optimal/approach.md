## General
**Keep the complete product catalog**

Start from `Product` and left-join `Invoice` on `product_id`. The outer join is essential: an inner join would discard a product with no matching invoice, contradicting the requirement to report every product.

**Aggregate all four measures together**

Group by the product key and name, then apply `SUM` independently to `rest`, `paid`, `canceled`, and `refunded`. Each joined invoice contributes once to exactly one product group, so every aggregate is the requested total. For a product without invoices, the left join supplies a single null-extended row; `SUM` of that missing value is null, so wrap each aggregate in `COALESCE(..., 0)`.

Grouping by the primary key keeps products distinct, while including `name` makes the selected nonaggregate column explicit and portable across strict SQL grouping modes. Finally, `ORDER BY p.name` establishes the required ascending output order. Because names are unique, no tie rule is needed.

## Complexity detail
A standard hash join and grouped aggregation inspect the $P$ product rows and $I$ invoice rows in $O(P + I)$ expected work while retaining at most one aggregate state per product. Sorting the $P$ result groups by arbitrary unique names costs $O(P \log P)$ comparison time. The combined bound is $O(I + P \log P)$ time and $O(P)$ auxiliary space.

## Alternatives and edge cases
- **Aggregate invoices before joining:** a grouped invoice subquery can reduce the join input to one row per invoiced product, but it still needs a left join and zero replacement for products without invoices.
- **Inner join:** is shorter but incorrectly omits catalog products whose invoice history is empty.
- **Correlated aggregate subqueries:** one subquery per amount is readable in isolation but may rescan invoices repeatedly without effective indexing.
- **No invoices for a product:** all four totals must be numeric zero, not null, and the product must remain present.
- **Zero-valued invoices:** they still belong to their product group and leave the corresponding sums at zero.
- **Input row order and identifiers:** neither invoice order nor gaps in either primary key affect grouping; only `name` controls final order.
