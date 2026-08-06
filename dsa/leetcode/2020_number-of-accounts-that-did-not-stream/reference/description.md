## Description

`Subscriptions` stores one date interval for each account, and `Streams`
records individual streaming sessions associated with those accounts.

Count accounts whose subscription overlaps calendar year 2021 but that have no
stream session dated from January 1 through December 31, 2021. A subscription
may begin before 2021 or end after it and still qualify through overlap.
Likewise, streams outside 2021 do not disqualify the account. Return the count
in a column named `accounts_count`.
