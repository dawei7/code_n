## General

**Convert all balance effects into one signed ledger**

Each user's current balance equals initial credit plus incoming transaction amounts minus outgoing transaction amounts.

The derived table `t` creates rows with a uniform schema `(user_id, credit)` for all three components:

- A payer receives `-amount` because sending money decreases balance.
- A recipient receives `amount` because receiving money increases balance.
- Every user receives one row containing their initial `credit`.

Once all effects have the same two columns, the final balance is simply their sum per user.

**Why UNION ALL is essential**

The query combines the three streams with `UNION ALL`, which preserves every row.

Ordinary `UNION` removes duplicate rows. Two legitimate transactions can have the same user and amount, and deduplicating them would lose a real balance effect. An initial-credit row could also numerically match a transaction effect. Those are separate facts and must all contribute.

`UNION ALL` expresses ledger addition rather than set union.

**Guarantee that users without transactions remain**

The third branch selects `user_id, credit` from every `Users` row. Therefore every user appears in `t` at least once even when they never paid or received money.

For such a user, the group sum contains only the initial credit and returns it unchanged. No outer join or missing-value replacement is needed.

**Join the ledger back to user names**

`t` contains identifiers and signed amounts but not names. The query joins `Users AS u` on equal `user_id` to attach `user_name`.

The user identifier is the primary key, so each ledger row matches at most one user row. Under the bank schema, payer and recipient identifiers refer to users, and the initial rows certainly match.

The final group is keyed by `t.user_id`. In MySQL, `user_name` is functionally determined by that primary-key user identifier, allowing it to be selected alongside the aggregate.

**Aggregate the current credit**

`SUM(t.credit) AS credit` adds initial credit and every signed transaction effect.

For user one in the example, the ledger includes initial one hundred, outgoing negative four hundred, and incoming positive two hundred. Their sum is negative one hundred.

For user four, only initial eight hundred exists, so the sum remains eight hundred.

The date and transaction identifier are irrelevant to current-balance arithmetic. Every transaction contributes exactly once on the payer side and once on the recipient side regardless of when it occurred.

**Classify a breached limit**

The limit is breached only when final credit is strictly below zero.

`IF(SUM(t.credit) < 0, 'Yes', 'No')` applies that rule to the same aggregate used for the displayed credit. A balance of zero is not negative and therefore produces `"No"`.

The sum expression appears twice, but both occurrences refer to the same group of ledger rows and produce the same current balance.

**Conservation across the bank**

Every transaction contributes `-amount` to one user and `+amount` to another. These effects cancel in the bank-wide total.

Thus transactions redistribute credit but do not change the sum of all users' balances. This is a useful conceptual check on the signed-union construction, although the query does not need a separate validation step.

A self-transfer would generate both signs for the same user and cancel within that user's group, also matching the real net effect.

**Why the query is correct**

For a fixed user, `t` contains one initial-credit row, one negative row for every payment made, and one positive row for every payment received. No fact is deduplicated.

Summing that group exactly implements the balance equation. Joining supplies the correct name, and the conditional label is yes exactly for a negative sum. Because every user has an initial row, this argument covers users both with and without transactions.

The contract allows any output order, so the absence of `ORDER BY` is intentional and valid.

## Complexity detail

Let $U$ be user count and $T$ transaction count. The unioned ledger has $U+2T$ rows.

Creating ledger streams and joining them requires linear row processing under ordinary indexed or hash-join plans. Grouping may use hashing in expected $O(U+T)$ time or comparison sorting in $O((U+T)\log(U+T))$ time.

The manifest's $O(N\log N)$ time is a conservative sort-based summary for total input-derived ledger size $N$. Actual SQL cost depends on indexes, grouping strategy, and the optimizer.

The derived ledger and grouping state can require $O(N)$ intermediate storage, matching the manifest. A database may stream, materialize, or spill portions of this work according to its physical plan.

## Alternatives and edge cases

- **Separate incoming and outgoing aggregates:** Aggregate each transaction side by user and left join both to users. It is correct but needs null handling and more join logic.
- **Conditional aggregation after joins:** Joining users to transactions in both roles can create multiplicative rows unless designed carefully.
- **UNION instead of UNION ALL:** It is incorrect because equal-looking ledger effects are distinct financial events.
- **User with no transactions:** The initial-credit branch guarantees one group row and preserves the balance.
- **Only outgoing transactions:** All effects beyond initial credit are negative.
- **Only incoming transactions:** All effects beyond initial credit are positive.
- **Balance exactly zero:** The breach label is `"No"` because the test is strictly less than zero.
- **Negative balance:** It produces `"Yes"` regardless of how many transactions caused it.
- **Self-transfer:** Positive and negative rows cancel for the same user.
- **Repeated equal amounts:** `UNION ALL` preserves every occurrence.
- **Transaction dates:** They do not affect an all-time current-balance summary and are intentionally ignored.
- **Any output order:** No sorting clause is required.
- **Functional dependency:** Selecting `user_name` while grouping by primary-key `user_id` relies on MySQL recognizing that dependency.
