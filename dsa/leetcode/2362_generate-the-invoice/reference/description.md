## Description

The `Products` table maps each unique product identifier to its unit price.
The `Purchases` table records a quantity for each product appearing on an
invoice; `(invoice_id, product_id)` uniquely identifies a purchase row.

Find the invoice having the greatest total value, where each line contributes
`quantity * unit price`. If several invoices share that greatest total, choose
the smallest `invoice_id`. Return every purchase line from the chosen invoice
with its `product_id`, `quantity`, and computed line `price`, in any order.
