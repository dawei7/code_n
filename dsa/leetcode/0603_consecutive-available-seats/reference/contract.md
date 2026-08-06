## Function Contract

**Input**

`Cinema(seat_id, free)` contains the seat availability rows. Let $n$ be its row count.

**Return value**

Return a one-column table containing each free `seat_id` that has a free seat at `seat_id - 1` or `seat_id + 1`. Sort the result by `seat_id` in ascending order.
