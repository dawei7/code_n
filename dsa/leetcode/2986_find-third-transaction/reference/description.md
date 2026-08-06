## Description

The `Transactions` table records a user's spend and transaction timestamp. The
pair `(user_id, transaction_date)` is unique, so each user's rows have an
unambiguous chronological order.

For every user with at least three transactions, inspect exactly their third
transaction by date. Return it only when its spend is strictly greater than
the spend of each of the preceding two transactions. Later transactions do not
replace a third transaction that fails the condition. Name the output fields
`user_id`, `third_transaction_spend`, and `third_transaction_date`, and order
the result by `user_id` ascending.
