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

### Required Complexity

- **Time:** $O(S+T)$
- **Space:** $O(T)$

<details>
<summary>Approach</summary>

#### General

**Identify subscriptions that touch the target year.** An interval overlaps
2021 when `start_date <= '2021-12-31'` and
`end_date >= '2021-01-01'`. This includes subscriptions that begin earlier,
finish later, or touch either boundary date.

**Build the set of accounts that streamed during 2021.** Filter `Streams` to
the inclusive target dates and deduplicate `account_id`. Left join this set to
the overlapping subscriptions, then retain rows whose joined account is
missing. Counting those rows returns the requested value, including zero when
no account qualifies.

The overlap predicate selects exactly the subscriptions active on at least one
target-year date. The filtered stream relation contains an account exactly
when it has at least one disqualifying session. Therefore, a missing joined
row is equivalent to satisfying both required conditions, and each primary-key
subscription contributes at most once.

#### Complexity detail

Here $S$ and $T$ are the input row counts. With ordinary hash aggregation and
join execution, filtering and deduplicating streams plus scanning
subscriptions takes $O(S+T)$ expected time. The target-year account set uses
$O(T)$ space in the worst case. A database may instead use indexed
$O((S+T)\log T)$ operations while preserving the same relational plan.

#### Alternatives and edge cases

- **Correlated `NOT EXISTS`:** This is concise and MySQL can optimize it into
  an anti-join, but an engine without a suitable index may rescan all streams
  per subscription and take $O(ST)$ time.
- **`NOT IN` subquery:** It can express the exclusion but requires careful
  null semantics; an explicit anti-join is clearer.
- Streams before or after 2021 do not disqualify an account.
- Subscriptions spanning either year boundary still overlap 2021.
- The aggregate must return one row with zero when every account streamed or
  no subscription overlaps the year.

</details>
