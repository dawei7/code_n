## Function Contract

**Input table**

- `restaurant_orders`: One row per order, with the six columns defined in the Description. `order_id` is unique; `order_rating` may be `NULL`.

Peak-hour membership depends only on the time component of `order_timestamp`. Both endpoints of each peak interval are included. An unrated order contributes to `total_orders` and the peak-hour ratio but not to `AVG(order_rating)` or `COUNT(order_rating)`.

**Result table**

Return exactly these columns:

- `customer_id`
- `total_orders`
- `peak_hour_percentage`, rounded to the nearest whole percentage point
- `average_rating`, rounded to two decimal places over rated orders only

Apply the four eligibility thresholds to their exact aggregate values, then order the retained rows by `average_rating DESC, customer_id DESC`.
