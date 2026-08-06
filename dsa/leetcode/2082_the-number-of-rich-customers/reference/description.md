## Description

The `Store` table records individual bills. Each row has a unique bill identifier, the customer responsible for that bill, and its integer amount. A customer is considered rich when at least one of their bills has an amount strictly greater than 500.

Report how many distinct customers satisfy that condition. Multiple qualifying bills from the same customer must contribute only once, an amount equal to 500 does not qualify, and the result must be a single row with column name `rich_count`.
