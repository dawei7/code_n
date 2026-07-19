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
