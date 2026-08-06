## Description

The `Rides` table records rides by unique `ride_id`. Each row names the
`driver_id` of the person who drove that ride and the `passenger_id` of the
person who rode as its passenger. Within one row, the driver and passenger are
different people.

Report every distinct person who appears as a driver in at least one row. For
each such driver, count how many rows list that same person as the passenger.
A driver who never appears in the passenger column must still be included with
a count of zero. The result rows may be returned in any order.
