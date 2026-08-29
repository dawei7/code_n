## General

**Generate the bounded candidate domain**

The largest customer ID is guaranteed not to exceed 100. The recursive common table expression `t` generates integers from one through 100:

- the anchor row is `SELECT 1 AS n`;
- the recursive member selects `n + 1` while `n < 100`.

When `n = 99`, it generates 100. When `n = 100`, the condition fails and recursion stops. The CTE therefore provides a complete fixed candidate domain without requiring a permanent numbers table.

**Keep only values below the current maximum**

The first outer predicate is:

`n < (SELECT MAX(customer_id) FROM Customers)`.

The requested range includes the maximum itself, but that maximum is necessarily present in `Customers` by definition. It can never be a missing ID. Excluding it with strict `<` rather than generating it for a later membership rejection does not change the missing-ID set.

Values greater than the maximum are excluded because they lie outside the requested interval.

**Remove identifiers that exist**

The second predicate is:

`n NOT IN (SELECT customer_id FROM Customers)`.

For every generated candidate below the maximum, this keeps it only when no customer row has that identifier. Since `customer_id` is the table’s unique identifier and is treated as a concrete key, each present ID is removed regardless of customer name.

The query selects `n AS ids` to give the single output column its required name.

**A sample walk-through**

For customer IDs one, four, and five, `MAX(customer_id)` is five. The CTE candidates satisfying `n < 5` are one, two, three, and four.

`NOT IN` removes one and four because they appear in the table. Two and three remain and are returned as `ids`.

Five is not tested by the strict maximum predicate, but it is known present and therefore could never belong in the output.

**Why the returned set is correct**

Take any returned `n`. It comes from one through 100, is below the maximum customer ID, and is absent from `Customers`. It is therefore a missing ID within the requested range.

Conversely, take any missing ID `x` between one and the maximum. It cannot equal the maximum because that value exists, so `x < max`. The maximum bound of 100 means the CTE generates `x`. Its absence makes `NOT IN` true, so the query returns it.

Thus the query computes exactly the required set of IDs.

**Null semantics**

`NOT IN` can behave unexpectedly if its subquery contains `NULL`: comparisons become unknown and candidates may be filtered out. The source relies on `customer_id` being a non-null unique identifier, as intended by the schema.

If nullable IDs were possible in a different database, `NOT EXISTS` would be safer.

**Ordering limitation in the exact source**

The problem requires ascending `ids`, but the checked-in query contains no `ORDER BY` clause. The recursive CTE is generated from one upward, and MySQL will often display the filtered rows in that apparent order, but SQL does not guarantee result order without explicit ordering.

Therefore, the logical missing-ID set is correct, while strict presentation-order compliance is not guaranteed by the exact source. Adding `ORDER BY ids ASC` would make that requirement explicit. This documentation describes the source as written rather than claiming an ordering guarantee it does not state.

**Why hard-coding 100 is valid here**

The recursive upper limit comes directly from the constraint that the maximum customer ID never exceeds 100. If that bound changed, the CTE would need to derive its stopping value from `MAX(customer_id)` or use a reusable numbers table.

The current source still scans candidates up to 100 even when the actual maximum is small; the outer predicate removes extras.

## Complexity detail

Let $C$ be the number of customer rows and $M=\max(\texttt{customer\_id})$, with $M\le100$.

The CTE creates 100 rows, a constant under the contract. The maximum subquery scans customer IDs unless an index supplies it directly. Membership can be materialized or indexed by the optimizer. A general sort/materialization bound consistent with the manifest is $O((M+C)\log(C+1))$, while an indexed or hashed plan can approach $O(M+C)$.

The generated number rows and membership structure use $O(M+C)$ working space in a general materialized plan. Since $M\le100$, the number-series portion is tightly bounded.

Physical SQL costs remain optimizer-dependent and should be inspected with `EXPLAIN`.

## Alternatives and edge cases

- **Recursive CTE stopping at the actual maximum:** Seed one and recurse while `n < MAX(customer_id)` through a prepared bound, avoiding generation beyond the needed range.
- **Permanent numbers table:** It is efficient and reusable in production schemas but adds an external dependency.
- **`NOT EXISTS`:** A correlated anti-join avoids `NOT IN` null hazards and expresses absence directly.
- **Left anti-join:** Left-join candidates to customers and keep rows with a null matched key.
- **Window-gap expansion:** Use `LEAD` to identify gaps and a number generator to expand them; this is more complex for a maximum of only 100.
- **Maximum ID equals one:** The strict `n < max` predicate keeps no candidates, correctly returning an empty set.
- **No gaps:** Every candidate below the maximum is removed by membership, producing no rows.
- **Gap immediately before maximum:** It is below the maximum and absent, so it is returned.
- **ID 100 as maximum:** The CTE includes 100, though the strict predicate tests only one through 99; 100 is known present.
- **Maximum itself:** It never needs to be returned because being the maximum proves it exists.
- **Nullable IDs:** `NOT IN` would be unsafe; the key contract is required.
- **Empty customer table:** `MAX` would be null and no candidate would pass. The task’s notion of a present maximum implicitly assumes data exists.
- **Missing explicit ordering:** Add `ORDER BY ids ASC` for guaranteed compliance; generation order alone is not a SQL ordering contract.
- **Hard-coded domain bound:** It is valid only because the reference guarantees a maximum no larger than 100.
