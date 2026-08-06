## Description

The `Orders` table records the number of orders received during each numbered minute. The `minute` value uniquely identifies a row, and the table contains a multiple of six rows.

Partition the timeline into consecutive six-minute intervals: minutes $1$ through $6$ form interval $1$, minutes $7$ through $12$ form interval $2$, and the same pattern continues. For every interval, add the six `order_count` values. Return each interval number with its total orders, ordered by `interval_no` in ascending order.
