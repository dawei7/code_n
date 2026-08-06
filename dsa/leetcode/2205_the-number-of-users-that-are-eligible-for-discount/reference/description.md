## Description

The `Purchases` table records the user, timestamp, and amount of every purchase. A user is eligible for a discount when at least one of their purchases both falls within a requested inclusive time interval and reaches a requested minimum amount.

Count the distinct eligible users. The supplied `startDate` and `endDate` values are dates interpreted at the start of their respective days. Consequently, a purchase exactly at midnight on `endDate` is included, while a purchase later during that calendar date is after the interval.
