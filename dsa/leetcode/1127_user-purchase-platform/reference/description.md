## Description

Classify every user's purchases independently on each `spend_date` as `desktop` only, `mobile` only, or `both` desktop and mobile. A user who purchased through both platforms on the same date belongs only to the `both` category for that date, and both purchase amounts contribute to that category.

For every date represented in `Spending`, report all three platform categories with their total amount and number of users. Include a category even when nobody belongs to it, using zero for both totals. Result rows may appear in any order.
