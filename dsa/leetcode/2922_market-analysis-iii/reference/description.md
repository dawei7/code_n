## Description

The marketplace records sellers in `Users`, product brands in `Items`, and
individual sales in `Orders`. For each seller, consider only orders whose
item brand differs from that seller's favorite brand. Count the number of
distinct item IDs among those qualifying orders, so repeated sales of the same
item contribute once.

Find the largest such count and return every seller attaining it. The result
must contain `seller_id` and the count as `num_items`, ordered by
`seller_id` in ascending order. Sellers without a qualifying sale do not
produce a grouped count.
