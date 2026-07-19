## General
**Keep the employee table on the preserved side.** Start from `Employees` and left join `EmployeeUNI` on their shared `id`. A matching mapping contributes its `unique_id`; when no match exists, left-join semantics retain the employee row and supply `NULL` for mapping columns.

Select only `unique_id` and `name`. Because each internal ID is unique in both tables, the join produces exactly one output row per employee: either the single matching identifier or one null-extended row. An inner join would incorrectly discard unmapped employees.

## Complexity detail
With a hash table or index for the $U$ mappings, building or reading that lookup and probing it for all $E$ employees takes $O(E + U)$ time and $O(U)$ working space. Physical database plans may use an equivalent indexed join.

## Alternatives and edge cases
- **Correlated scalar lookup:** Query `EmployeeUNI` separately for every employee. It is correct but can take $O(EU)$ time without an index.
- **Inner join:** It returns correct values only for mapped employees and violates the requirement to retain everyone else.
- **No mapping:** An employee absent from `EmployeeUNI` must still appear with `NULL`, not be omitted or assigned a fabricated identifier.
- **All mapped:** The result has no null identifiers when every employee has a corresponding row.
- **Duplicate names:** Join by `id`, since names need not identify employees uniquely.
- **Output order:** The problem permits any row order; the local query orders by internal ID only to keep tests deterministic.
