## Function Contract

**Input tables**

- `Product(product_id, product_name, unit_price)`: the product catalog used to resolve names.
- `Sales(seller_id, product_id, buyer_id, sale_date, quantity, price)`: the purchase history associated with buyers.

The output grain is one row per qualifying `buyer_id`. Eligibility depends only on whether the buyer's joined purchase history contains at least one `S8` name and contains no `iPhone` name. Seller, date, quantity, price, unit price, and purchases of other product names do not alter those two existence conditions.

Repeated `Sales` rows are permitted but do not create repeated output buyers. If `Sales` is empty, or if every buyer either lacks an `S8` purchase or has an `iPhone` purchase, the result is empty.

**Return value**

- One column named `buyer_id`.
- One row for every buyer with at least one `S8` purchase and zero `iPhone` purchases.
- Result order is unrestricted.
