# Monthly Transactions II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1205 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/monthly-transactions-ii/) |

## Problem Description

### Goal

The `Transactions` table records incoming transactions. Each row has a unique `id`, a `country`, an `amount`, a transaction date, and a `state` that is either `"approved"` or `"declined"`.

The `Chargebacks` table records incoming chargebacks for transactions in `Transactions`; `trans_id` refers to the original transaction's `id`. A chargeback may correspond to a transaction that was declined as well as one that was approved, and its own `trans_date` may fall in a later month than the original transaction.

For every month-country combination having relevant activity, report the count and total amount of approved transactions in their transaction month, together with the count and total amount of chargebacks in their chargeback month. Omit any month-country row for which all four reported values would be zero. Return the result rows in any order.

### Function Contract

**Input tables**

- `Transactions(id, country, state, amount, trans_date)`: `id` is unique and `state` is either `"approved"` or `"declined"`.
- `Chargebacks(trans_id, trans_date)`: `trans_id` references `Transactions.id`; its date is the chargeback date.
- Let $t$ be the number of transaction rows, $c$ the number of chargeback rows, and $g$ the number of reported month-country groups.

**Return value**

- One row per relevant month-country group with columns `month`, `country`, `approved_count`, `approved_amount`, `chargeback_count`, and `chargeback_amount`.
- `month` is represented as `YYYY-MM`; approved metrics use the original transaction date, while chargeback metrics use the chargeback date.

### Examples

**Example 1**

`Transactions`

| id | country | state | amount | trans_date |
|---:|---|---|---:|---|
| 101 | US | approved | 1000 | 2019-05-18 |
| 102 | US | declined | 2000 | 2019-05-19 |
| 103 | US | approved | 3000 | 2019-06-10 |
| 104 | US | declined | 4000 | 2019-06-13 |
| 105 | US | approved | 5000 | 2019-06-15 |

`Chargebacks`

| trans_id | trans_date |
|---:|---|
| 102 | 2019-05-29 |
| 101 | 2019-06-30 |
| 105 | 2019-09-18 |

Output:

| month | country | approved_count | approved_amount | chargeback_count | chargeback_amount |
|---|---|---:|---:|---:|---:|
| 2019-05 | US | 1 | 1000 | 1 | 2000 |
| 2019-06 | US | 2 | 8000 | 1 | 1000 |
| 2019-09 | US | 0 | 0 | 1 | 5000 |

**Example 2**

A declined transaction contributes no approved metrics, but a later chargeback for it still contributes one chargeback and its full amount.

**Example 3**

A month-country pair containing only declined transactions with no chargebacks is omitted because every requested metric would be zero.

### Required Complexity

- **Time:** $O(t+c)$
- **Space:** $O(g)$

<details>
<summary>Approach</summary>

#### General

**Turn each relevant fact into an event.** Select approved transaction rows as events keyed by the month of `Transactions.trans_date` and by `country`. Each contributes `1` and `amount` to the approved fields and zeros to the chargeback fields. Declined transactions do not create approved events.

**Attach chargebacks to their transaction attributes.** Join each `Chargebacks.trans_id` to `Transactions.id` to recover the transaction's `country` and `amount`. Key this event by the month of `Chargebacks.trans_date`, not the original transaction date, and contribute only to the chargeback fields. This join works identically for approved and declined original transactions.

**Aggregate the unified stream.** Combine the two event sets with `UNION ALL`, then group by `month` and `country` and sum all four numeric contributions. Every event has at least one nonzero count, so only groups with approved or chargeback activity are created; declined-only groups with no chargeback never enter the stream. A deterministic `ORDER BY` is useful for local fixtures even though the platform permits any row order.

#### Complexity detail

With an indexed or hash lookup from each of the $c$ chargebacks to its transaction, the event construction processes $t+c$ rows. Hash aggregation adds constant expected work per event, for $O(t+c)$ logical time. The aggregation stores one fixed record for each of the $g$ reported keys, requiring $O(g)$ auxiliary space. Physical database plans may choose sorting or different join strategies.

#### Alternatives and edge cases

- **Correlated aggregates per month-country key:** Recomputing each of the four metrics for every key is correct but can take $O(g(t+c))$ time.
- **Redundant cross-product aggregation:** Repeating every event once per transaction and dividing the resulting sums by the transaction count preserves the metrics but creates quadratically many intermediate rows.
- **Full outer join of monthly summaries:** Separately aggregating approved transactions and chargebacks and then full-joining the summaries works on engines that support it, but requires careful key coalescing and zero filling.
- **Use the original date for chargebacks:** This incorrectly attributes a later chargeback to the transaction month rather than the chargeback month.
- **Declined transaction with a chargeback:** It adds zero approved activity and still contributes its amount to chargeback metrics.
- **Declined-only month:** Without a chargeback, it produces no output row because all four requested values are zero.
- **Chargeback-only month:** It must appear with approved count and amount equal to zero.
- **Multiple countries:** Equal calendar months remain separate when their countries differ.
- **Any output order:** Ordering is not part of the platform contract, though the app-local query sorts the keys for stable verification.

</details>
