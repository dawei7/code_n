## Description

Each `Delivery` row represents a food order placed by one customer on `order_date`, together with the same-day-or-later date requested for delivery.

Classify each delivery by comparing its two dates. A delivery is **immediate** when `customer_pref_delivery_date` equals `order_date`; when the preferred date is later, the delivery is **scheduled**.

Find what percentage of all rows in `Delivery` are immediate. Round the percentage to two decimal places and report it in the format demonstrated by the example.
