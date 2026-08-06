## Description

The `Orders` table stores a compressed distribution of order sizes. Each
unique `order_id` row says that an order containing `item_count` items occurs
`order_occurrences` times; the row therefore represents that many individual
orders rather than one order.

Calculate the average number of items per represented order and round it to
two decimal places. Return the single value under the column name
`average_items_per_order`; row ordering is irrelevant because the result has
one row.
