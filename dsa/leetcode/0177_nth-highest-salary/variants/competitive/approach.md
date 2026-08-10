## General

**Define rank by counting greater distinct salaries**

The competitive function does not sort salary levels explicitly. For each
candidate row `Emp1`, its correlated subquery counts how many distinct
`Emp2.Salary` values are strictly greater.

A salary is the $N$th highest distinct value exactly when:

$$
\#\{\text{distinct salaries greater than it}\}=N-1.
$$

The source expresses this equality in the outer `WHERE` clause. The strict
greater-than comparison is important: equal salaries belong to the same dense
rank and must not count above one another.

**Understand the two aliases**

`Employee Emp1` supplies the current candidate salary. For that row, the inner
query scans `Employee Emp2` and evaluates:

`Emp2.Salary > Emp1.Salary`.

`COUNT(DISTINCT(Emp2.Salary))` collapses all employees at the same greater
salary level. The count is therefore the number of ranks above the candidate,
not the number of higher-paid employees.

The aliases are necessary because the same table participates in both query
levels. They tell SQL which salary is the inner scanned value and which is the
outer candidate.

**Collapse duplicate qualifying candidates with `MAX`**

If several employees earn the requested salary, every corresponding `Emp1` row
satisfies the same greater-count predicate. The outer query applies
`MAX(Salary)` to these duplicates.

Since all qualifying rows at a valid dense rank have the same salary value,
`MAX` returns that value once. If no candidate satisfies the predicate,
aggregate `MAX` over the empty set returns SQL `NULL`.

This aggregate behavior gives the stored function a scalar value for both the
found and missing-rank cases.

**Trace rank two**

For salaries 100, 200, and 300 with `N = 2`:

- candidate 300 has zero distinct greater salaries;
- candidate 200 has one distinct greater salary, 300;
- candidate 100 has two.

The predicate `N - 1 = 1` retains only 200, and outer `MAX` returns 200.

With salaries `[500,500,300,200]`, each 500 row has greater-count zero. Salary
300 has one greater distinct value—500, counted once despite two employees.
Thus rank two is 300.

**Trace first and missing ranks**

For `N = 1`, the required greater count is zero. All rows at the maximum salary
qualify, and outer `MAX` returns that maximum.

If `N` exceeds the number of distinct salary levels, no candidate has exactly
`N - 1` greater values. The outer aggregate sees no row and returns null.
An empty table behaves the same way.

**Why this implements dense ranking**

For any numeric salary $s$, the number of distinct values greater than $s$ is
fixed regardless of how often $s$ occurs. Its descending dense rank is that
count plus one.

The predicate is therefore necessary and sufficient for rank `N`. `MAX`
does not choose among different valid rank values; there can be only one
distinct numeric value with a given count of greater distinct levels.

**Null salary semantics**

If `Emp1.Salary` is null, the comparison
`Emp2.Salary > Emp1.Salary` is unknown for every row, so the inner count is
zero. A null candidate could interact unexpectedly with `N = 1`, although
outer `MAX` ignores null when a numeric maximum also qualifies.

The classic dataset assumes meaningful numeric salaries. A production version
should add `Salary IS NOT NULL` if null values are possible and should not
participate in ranks.

**Stored function behavior**

`RETURN (SELECT MAX(...))` yields one scalar integer or null. The source uses
MySQL hash comments and routine syntax. It does not mutate `N`, so the
one-based rank remains visible as `N - 1` in the predicate.

**Correlated work may repeat for duplicate outer rows**

Logically, the inner count is evaluated for each candidate row from `Emp1`.
Two employees with the same salary ask the same greater-salary question, yet a
naive executor may repeat that work. Grouping outer candidates by salary first
would reduce evaluations to the number of distinct levels. A salary index can
also accelerate the greater-than range, but neither optimization is stated in
the query, so correctness must not depend on it.

This repeated-work issue does not change the returned value: duplicate outer
rows share one salary, one greater-distinct count, and one dense rank. It
changes only physical performance.

## Complexity detail

In a naive correlated execution, the inner query can inspect $n$ employee rows
for each of $n$ outer candidates. Time is $O(n^2)$, as the source comment says,
not the manifest's $O(n\log n)$.

Counting distinct greater salaries may require $O(u)$ state for up to $u=n$
distinct values, giving $O(n)$ worst-case working space. An optimizer or index
may transform or accelerate the query, but the text does not guarantee a
sort-like $O(n\log n)$ plan.

## Alternatives and edge cases

- **Distinct sort plus offset:** Usually clearer and has $O(n\log n)$ straightforward behavior, matching the optimal variant.
- **`DENSE_RANK` window function:** Calculates the same greater-distinct rank directly.
- **Duplicate salaries:** `COUNT(DISTINCT ...)` prevents employees from inflating the rank.
- **`N = 1`:** Candidates with zero greater salaries are the maximum.
- **Missing rank:** Outer `MAX` over no qualifiers returns null.
- **Empty table:** Returns null without a special branch.
- **Strict comparison:** `>` is required; `>=` would count the candidate's own salary level.
- **Positive `N`:** The contract prevents the nonsensical negative target count.
- **Nullable salaries:** Exclude them explicitly if the data model allows them.
- **Manifest mismatch:** Naive correlated evaluation is quadratic, not $O(n\log n)$.
