## Description

The `Delivery` table records food orders. Each row has a unique delivery identifier, a customer, the date on which the order was placed, and the customer's preferred delivery date. The preferred date is never earlier than the order date.

An order is **immediate** when `customer_pref_delivery_date` equals `order_date`; otherwise it is **scheduled**. For every distinct order date, compute the percentage of that date's orders that were immediate. Round each percentage to two decimal places and return the rows in ascending `order_date` order.
