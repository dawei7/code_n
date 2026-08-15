# Generate the Invoice

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2362 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/generate-the-invoice/) |

## Problem Description

### Goal

The `Products` table maps each unique product identifier to its unit price.
The `Purchases` table records a quantity for each product appearing on an
invoice; `(invoice_id, product_id)` uniquely identifies a purchase row.

Find the invoice having the greatest total value, where each line contributes
`quantity * unit price`. If several invoices share that greatest total, choose
the smallest `invoice_id`. Return every purchase line from the chosen invoice
with its `product_id`, `quantity`, and computed line `price`, in any order.

### Function Contract

**Input tables**

- `Products(product_id, price)`: One unit price per unique product.
- `Purchases(invoice_id, product_id, quantity)`: Unique invoice-product lines.

Let $P$ and $R$ be the row counts of `Products` and `Purchases`.

**Return value**

Return the selected invoice's lines with columns `product_id`, `quantity`, and
`price`, where `price` equals that line's quantity times its product unit
price. The result need not include `invoice_id`, and row order is unrestricted.

### Examples

#### Example 1

Invoice 2 and invoice 4 both total 1000, so invoice 2 wins the identifier
tie-break. Its two returned lines are `(2, 3, 600)` and `(1, 4, 400)`.
