## Description

The `Transactions` table records a transaction identifier, its customer, the calendar date of the transaction, and its amount. A customer has at most one transaction on any particular date.

Find every maximal period in which the same customer made transactions on at least three consecutive calendar days and each day's `amount` was strictly greater than the preceding day's amount. A customer may have more than one qualifying period when a missing date or a non-increasing amount separates the periods.

For each qualifying period, report the customer and its first and last dates. Sort the rows by `customer_id`, then `consecutive_start`, then `consecutive_end`, all in ascending order.
