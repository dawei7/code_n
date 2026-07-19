# Number of Accounts That Did Not Stream

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2020 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-accounts-that-did-not-stream/) |

## Problem Description

### Goal

`Subscriptions` stores one date interval for each account, and `Streams`
records individual streaming sessions associated with those accounts.

Count accounts whose subscription overlaps calendar year 2021 but that have no
stream session dated from January 1 through December 31, 2021. A subscription
may begin before 2021 or end after it and still qualify through overlap.
Likewise, streams outside 2021 do not disqualify the account. Return the count
in a column named `accounts_count`.

### Function Contract

Let $S$ and $T$ be the row counts of `Subscriptions` and `Streams`.

**Inputs**

- `Subscriptions(account_id, start_date, end_date)`, where `account_id` is the
  primary key and `start_date < end_date`.
- `Streams(session_id, account_id, stream_date)`, where `session_id` is the
  primary key and `account_id` references `Subscriptions`.

**Return value**

Return one row and one column, `accounts_count`, containing the number of
qualifying accounts.

### Examples

**Example 1**

- Input: the supplied account subscriptions and stream sessions
- Output: `accounts_count = 2`
- Explanation: Accounts `4` and `9` have subscriptions active during 2021 but
  no stream in that year.

**Example 2**

- Input: a subscription ending on `2021-01-01` and no streams
- Output: `accounts_count = 1`
- Explanation: The subscription overlaps the first day of the target year.

**Example 3**

- Input: a 2021 subscription with only a stream dated in 2020
- Output: `accounts_count = 1`
- Explanation: An out-of-year stream does not exclude the account.
