## Function Contract

**Input tables**

- `Product(product_id, product_name, unit_price)`: the referenced product catalog.
- `Sales(seller_id, product_id, buyer_id, sale_date, quantity, price)`: the sale records to aggregate.

The output grain is one row per seller tied for the greatest sum of `Sales.price`. The sample confirms that `price` is the recorded price for the whole sale: a quantity of `2` for a product with unit price `1000` has `price = 2000`. Therefore, add `price` directly rather than multiplying it by `quantity`. Product names and unit prices do not change the requested total.

Repeated `Sales` rows are permitted and each stored row contributes separately. If `Sales` is empty, there is no represented seller and the result is empty.

**Return value**

- One column named `seller_id`.
- Every represented seller whose sum of `price` is the maximum seller total.
- Result order is unrestricted.
