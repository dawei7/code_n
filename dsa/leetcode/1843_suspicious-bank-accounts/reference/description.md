## Description

`Accounts` assigns each bank account a maximum expected monthly income. `Transactions` records deposits and withdrawals: a `Creditor` row adds money to an account, whereas a `Debtor` row removes money and does not count as income.

For every account and calendar month, total only its creditor amounts. An account is suspicious when that monthly income is strictly greater than its own `max_income` during at least two consecutive calendar months. Report the identifiers of all accounts satisfying that condition.
