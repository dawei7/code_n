# Product's Worth Over Invoices

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1677 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/products-worth-over-invoices/) |

## Problem Description
### Goal

The `Product` table identifies products by primary-key `product_id` and gives each one a unique lowercase name. The `Invoice` table records invoices for products. Each invoice has four independent monetary amounts: `rest` remains due, `paid` has been paid, `canceled` was canceled, and `refunded` was returned.

Produce one row for every product, including products that have no invoice. For each product, total each of the four amount columns over all of its invoices; an absent invoice history contributes zero to every total. Return the product name as `name` together with `rest`, `paid`, `canceled`, and `refunded`, ordered by `name` in ascending lexicographic order.

### Function Contract
**Inputs**

- `Product(product_id, name)`: $P$ products, where `product_id` is the primary key and every `name` is unique
- `Invoice(invoice_id, product_id, rest, paid, canceled, refunded)`: $I$ invoices, where `invoice_id` is the primary key and `product_id` identifies the invoiced product

**Return value**

A relation with columns `name`, `rest`, `paid`, `canceled`, and `refunded`, containing every product exactly once in ascending `name` order.

### Examples
**Example 1**

- Input: `Product = [(0, "ham"), (1, "bacon")]`, `Invoice = [(23,0,2,0,5,0), (12,0,0,4,0,3), (1,1,1,1,0,1), (2,1,1,0,1,1), (3,1,0,1,1,1), (4,1,1,1,1,0)]`
- Output: `[("bacon",3,3,3,3), ("ham",2,4,5,3)]`

**Example 2**

- Input: `Product = [(7, "empty")]`, `Invoice = []`
- Output: `[("empty",0,0,0,0)]`

**Example 3**

- Input: `Product = [(9, "zero")]`, `Invoice = [(2,9,0,0,0,0)]`
- Output: `[("zero",0,0,0,0)]`

### Required Complexity

- **Time:** $O(I + P \log P)$
- **Space:** $O(P)$

<details>
<summary>Approach</summary>

#### General

**Keep the complete product catalog**

Start from `Product` and left-join `Invoice` on `product_id`. The outer join is essential: an inner join would discard a product with no matching invoice, contradicting the requirement to report every product.

**Aggregate all four measures together**

Group by the product key and name, then apply `SUM` independently to `rest`, `paid`, `canceled`, and `refunded`. Each joined invoice contributes once to exactly one product group, so every aggregate is the requested total. For a product without invoices, the left join supplies a single null-extended row; `SUM` of that missing value is null, so wrap each aggregate in `COALESCE(..., 0)`.

Grouping by the primary key keeps products distinct, while including `name` makes the selected nonaggregate column explicit and portable across strict SQL grouping modes. Finally, `ORDER BY p.name` establishes the required ascending output order. Because names are unique, no tie rule is needed.

#### Complexity detail

A standard hash join and grouped aggregation inspect the $P$ product rows and $I$ invoice rows in $O(P + I)$ expected work while retaining at most one aggregate state per product. Sorting the $P$ result groups by arbitrary unique names costs $O(P \log P)$ comparison time. The combined bound is $O(I + P \log P)$ time and $O(P)$ auxiliary space.

#### Alternatives and edge cases

- **Aggregate invoices before joining:** a grouped invoice subquery can reduce the join input to one row per invoiced product, but it still needs a left join and zero replacement for products without invoices.
- **Inner join:** is shorter but incorrectly omits catalog products whose invoice history is empty.
- **Correlated aggregate subqueries:** one subquery per amount is readable in isolation but may rescan invoices repeatedly without effective indexing.
- **No invoices for a product:** all four totals must be numeric zero, not null, and the product must remain present.
- **Zero-valued invoices:** they still belong to their product group and leave the corresponding sums at zero.
- **Input row order and identifiers:** neither invoice order nor gaps in either primary key affect grouping; only `name` controls final order.

</details>
