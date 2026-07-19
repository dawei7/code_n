## General
**Accept both permitted referee states**

A customer qualifies when the stored referee identifier is not 2. A null referee also qualifies because no customer referred that row, but SQL does not treat `NULL <> 2` as true. Express the filter as `referee_id <> 2 OR referee_id IS NULL`.

**Why the filter is complete**

Every row has either a concrete referee identifier or null. Concrete identifier 2 is the only forbidden state. Every other concrete identifier satisfies the inequality, and the explicit null branch retains customers with no referee, so exactly the requested rows remain.

**Order only for deterministic local output**

The platform permits any row order. Ordering by name and identifier makes local fixtures stable without changing which customers qualify.

## Complexity detail
Filtering examines `n` customer rows in $O(n)$ time. The deterministic output sort costs $O(n \log n)$ time and $O(n)$ working space; without an ordering requirement, the semantic query itself is linear.

## Alternatives and edge cases
- **`COALESCE(referee_id, 0) <> 2`:** is concise when valid referee identifiers are positive, but the explicit null branch states the contract more directly.
- **Correlated anti-existence test:** can identify rows not marked with referee 2, but may rescan the customer table for every row and take $O(n^2)$ time.
- **`referee_id <> 2` alone:** incorrectly drops null referees because the comparison evaluates to unknown.
- **Referee exactly 2:** must be excluded.
- **Different referee:** qualifies regardless of that referee's own row details.
- **No referee:** must be included.
- **Customer with identifier 2:** is not automatically excluded; qualification depends on that customer's `referee_id`.
- **Duplicate names:** each qualifying customer row remains a separate result row.
