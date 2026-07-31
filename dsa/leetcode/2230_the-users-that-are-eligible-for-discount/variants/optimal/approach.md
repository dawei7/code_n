## General

**Apply both eligibility conditions to one purchase**

Cross-join the single parameter row to the purchase data in the app-local fixture. Retain a purchase only when its timestamp lies between `startDate` and `endDate`, inclusively, and its amount is at least `minAmount`. The conditions must hold for the same row; one in-range low purchase and one out-of-range expensive purchase do not combine.

Date parameters compare as midnight timestamps. Thus `BETWEEN` correctly includes the exact start and end instants while excluding activity later on the end date.

**Return users rather than purchases**

Project `user_id`, use `DISTINCT` because one user may have several eligible purchases, and order numerically. Every output ID has a retained row satisfying both predicates. Every user with such a purchase contributes at least one retained row, and deduplication preserves one copy, so the result is exact.

## Complexity detail

Let $r$ be the number of purchase rows. Filtering is $O(r)$ without a supporting index, while distinct ordered output can take $O(r\log r)$ time, giving $O(r\log r)$ in the general case.

Deduplication and ordering may retain $O(r)$ values. Exact index use and temporary storage are database-engine dependent.

## Alternatives and edge cases

- **Group conditional counts:** Grouping by user and testing whether any row qualifies is correct but does more aggregation than direct filtering needs.
- **Separate user-level predicates:** Checking date and amount in separate rows incorrectly combines two nonqualifying purchases.
- **End-of-day expansion:** Extending `endDate` through `23:59:59` violates the stated midnight boundary.
- **Boundary timestamps:** Purchases exactly at either midnight endpoint qualify.
- **Minimum amount:** Equality with `minAmount` qualifies.
- **Repeated eligible purchases:** `DISTINCT` emits the user once.
- **No eligible rows:** The result is an empty table with the `user_id` column.
