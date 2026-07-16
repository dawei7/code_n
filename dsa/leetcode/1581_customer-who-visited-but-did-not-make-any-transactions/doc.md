# Customer Who Visited but Did Not Make Any Transactions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1581 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/) |

## Problem Description
### Goal

The `Visits` table records each store visit and the customer who made it. The `Transactions` table records purchases, with every transaction linked to the visit during which it occurred.

Identify visits for which no transaction was made. A visit with several transactions is still a transactional visit and must contribute nothing, while multiple transaction-free visits by the same customer must all be counted.

Return each customer who has at least one transaction-free visit together with the number of such visits. Result rows may appear in any order.

### Function Contract
**Inputs**

- `Visits(visit_id, customer_id)`: visit records keyed by `visit_id`.
- `Transactions(transaction_id, visit_id, amount)`: transaction records keyed by `transaction_id`; `visit_id` identifies the associated visit.

**Return value**

Return columns `customer_id` and `count_no_trans`, with one row per customer and the count of that customer's visits having no matching transaction.

### Examples
**Example 1**

- Input: visits by customers 23, 9, 30, 54, and 96, with transactions attached only to visit IDs 1, 2, and 5
- Output: customer 30 has one transaction-free visit, customer 54 has two, and customer 96 has one

**Example 2**

- Input: one visit with no transaction
- Output: that customer with `count_no_trans = 1`

**Example 3**

- Input: every visit has at least one transaction
- Output: an empty result

### Required Complexity

- **Time:** $O((V+T)\log(V+T))$
- **Space:** $O(V+T)$

<details>
<summary>Approach</summary>

#### General

**Preserve visits that have no match**

Start from `Visits` and left-join `Transactions` on `visit_id`. The outer join retains one row for a visit even when no transaction matches it. In that unmatched row, columns from `Transactions`, including its non-null key `transaction_id`, are `NULL`.

Filter for `transactions.transaction_id IS NULL`. Testing the transaction key is important: it distinguishes the join-generated absence marker from nullable business fields and removes every matched visit regardless of how many transactions it has.

**Aggregate unmatched visits by customer**

Group the remaining rows by `visits.customer_id` and apply `COUNT(*)`. Each retained row corresponds to exactly one transaction-free visit, so the count is the required number for that customer. Alias it as `count_no_trans`.

Customers with only transactional visits have no retained row and therefore do not appear. Multiple unmatched visits for one customer enter the same group and are counted separately.

#### Complexity detail

Let $V$ and $T$ be the row counts of `Visits` and `Transactions`. With indexed or hash-assisted joining and grouping, execution can approach $O(V+T)$; a portable sort-based upper bound is $O((V+T)\log(V+T))$.

Join and grouping workspace may retain $O(V+T)$ row or hash state.

#### Alternatives and edge cases

- **`NOT EXISTS` anti-join:** filter each visit by the absence of a matching transaction. It is logically equivalent and efficient when `Transactions.visit_id` is indexed.
- **Correlated transaction count:** require a per-visit subquery count to equal zero. It is correct but can rescan all transactions for every visit and take $O(VT)$ time.
- **Inner join:** this keeps exactly the visits that did transact, reversing the required condition.
- **Count a nullable transaction column:** after filtering unmatched rows it works, but `COUNT(*)` states the retained-visit meaning directly.
- **Several transactions in one visit:** the visit contributes zero, not a negative value or several exclusions.
- **Several transaction-free visits:** each visit contributes one to its customer's aggregate.
- **Mixed visits for one customer:** count only that customer's unmatched visit IDs.
- **No qualifying visit:** return no rows.
- **Output order:** no ordering is required.

</details>
