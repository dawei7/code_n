## Description

The `Orders` table records purchases. Each row has a unique `order_id`, the
ordered `product_id`, a `quantity`, and the order's `purchase_date`. An order
counts once for this task regardless of its quantity.

Report the IDs of products that have at least three orders in one calendar
year and at least three orders again in the immediately following calendar
year. A product may qualify through any pair of consecutive years, and it must
appear only once in the result. The rows may be returned in any order.
