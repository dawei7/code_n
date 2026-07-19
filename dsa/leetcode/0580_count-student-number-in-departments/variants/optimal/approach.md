## General
**Start from the complete department catalog**

Use `Department` as the left side of a left join to `Student`. This preserves a department even when no student row matches its identifier.

**Count a nullable student column**

Group by the department identifier and name. Count `student_id`, not `COUNT(*)`: an empty department still produces one null-extended joined row, and counting all rows would incorrectly report one student. `COUNT(student_id)` ignores that null and returns zero.

**Apply both ordering keys**

Sort by the aggregate count descending so larger departments appear first. Then sort equal counts by department name ascending, as required.

**Why every department receives the right count**

The left join creates one joined row for each matching student and retains one null-extended row only when there are no matches. Counting non-null student identifiers therefore equals the number of students for populated departments and zero for empty ones. Grouping produces exactly one output row for every preserved department.

## Complexity detail
For `D` departments and `S` students, joining and grouping process $O(D + S)$ rows with suitable hashing or indexes. Ordering the `D` result groups costs $O(D \log D)$, for $O((D + S) \log D)$ time in the general bound and $O(D + S)$ working space.

## Alternatives and edge cases
- **Preaggregate students before joining:** count students by `dept_id`, left join those totals to departments, and replace a missing total with zero; it has the same asymptotic behavior.
- **Correlated count per department:** is concise but may scan all students for each department and take $O(DS)$ time.
- **Inner join:** omits empty departments and violates the contract.
- **`COUNT(*)` after a left join:** reports one for an empty department because it counts the null-extended row.
- **Empty department:** must appear with `student_number = 0`.
- **Equal counts:** use ascending department name as the tie-breaker.
- **Duplicate department names:** group by identifier as well as name so distinct departments are not merged.
- **Student attributes:** names and genders do not affect the count.
