## General
**Aggregate one output group per employee**

Group all membership rows by `employee_id`. This guarantees one result row for every employee regardless of how many departments they have.

**Extract the explicit primary when it exists**

Inside each group, use a conditional expression that returns `department_id` only when `primary_flag = 'Y'`, and aggregate it with `MAX`. A multi-department employee has one such row, so the aggregate yields that department. If no row is flagged, the conditional aggregate is `NULL`.

**Fall back only for the single-department rule**

Also compute `MAX(department_id)` across the group. `COALESCE` returns the conditional primary when present. Otherwise the contract guarantees that the employee has one membership, so the fallback aggregate returns that sole department.

The conditional branch selects every explicit primary exactly, and the fallback applies precisely when no explicit primary exists. Under the membership guarantees, that absence means the single row is the required department, so every employee receives exactly the correct result.

## Complexity detail
A hash aggregation examines each of the $R$ membership rows once and performs constant work for its employee group, giving $O(R)$ expected logical time. The aggregation stores two scalar values for each of the $M$ employee groups, using $O(M)$ space.

## Alternatives and edge cases
- **Window count plus filter:** Count memberships per employee and keep rows that are flagged or belong to a one-row partition. This is clear but may require partition sorting.
- **`UNION` of flagged and singleton rows:** Combine all `'Y'` rows with groups having count one. It is correct but scans or groups the source in separate branches and may require duplicate elimination unless `UNION ALL` is used carefully.
- **Correlated membership count:** Testing the row count separately for every source row can degrade to quadratic work without an appropriate index.
- **Single department with `'N'`:** It must be returned; filtering only for `'Y'` loses this employee.
- **Several departments:** Use the flagged row even when its department ID is not an extremum.
- **Input row order:** The primary row may occur before, after, or between nonprimary memberships.
- **Interleaved employees:** Grouping uses identifiers rather than relying on adjacent source rows.
- **Output order:** The platform accepts any order. The app-local query sorts by `employee_id` only for deterministic fixtures.
