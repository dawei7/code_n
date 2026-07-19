## General
**Form one group per class**

Group enrollment rows by the `class` value. Each group then contains exactly the student associations relevant to that class.

**Count students and apply the threshold**

Use `COUNT(DISTINCT student)` and retain groups with a count of at least five through `HAVING`. Distinct counting states the semantic quantity directly and prevents repeated enrollment data from inflating a total.

**Why every returned class qualifies**

All rows for one class enter the same group, and no row from another class can enter it. The distinct aggregate therefore equals that class's enrolled-student count. The inclusive `HAVING` predicate keeps exactly counts five or greater.

**Order only for deterministic local output**

The platform permits any row order. Sorting class names stabilizes local fixtures without changing which groups qualify.

## Complexity detail
For `n` enrollments and `c` classes, grouping and distinct counting generally use hashing or sorting in $O(n \log c)$ time and up to $O(n)$ working space. The final ordering of at most `c` class names fits within that bound.

## Alternatives and edge cases
- **Deduplicate enrollments in a subquery first:** then use `COUNT(*)` per class; it has the same general complexity.
- **Correlated count per enrollment:** can rescan all courses for many rows and take $O(n^2)$ time.
- **Filter with `WHERE COUNT(...)`:** is invalid because aggregate filters belong in `HAVING`.
- **Exactly five students:** qualifies because the threshold is inclusive.
- **Four students:** does not qualify.
- **Student in several classes:** contributes independently to each class group.
- **Distinct counting:** prevents duplicate associations from changing the semantic count.
- **Several qualifying classes:** return every one of them.
