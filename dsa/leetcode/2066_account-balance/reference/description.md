## Description

The `Transactions` table records deposits and withdrawals for bank accounts. Each account has at most one transaction on a given day. A `Deposit` increases its account's balance by `amount`, while a `Withdraw` decreases the balance by that amount.

Every account begins with balance zero, and the data guarantees that no account's balance becomes negative. Report the balance of each account immediately after every transaction. Sort the result by `account_id` in ascending order and then by `day` in ascending order.
