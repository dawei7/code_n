## Description

The `Users` table stores each bank user's current starting credit. Every row in `Transactions` records money transferred from `paid_by` to `paid_to`: the amount must be subtracted from the payer's credit and added to the recipient's credit.

Report every user with the resulting balance after all transactions and indicate whether the credit limit has been breached. A limit is breached only when the final credit is strictly below zero, producing `"Yes"`; zero or a positive balance produces `"No"`. Users without any transaction must still appear with their original credit. Result order is unrestricted.
