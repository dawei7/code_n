## General

**Choose the table that defines which rows must appear**

The required output asks for every employee's name, along with that employee's unique identifier when one exists. Therefore `Employees` is the table whose rows must all survive. `EmployeeUNI` is optional lookup information: it can add `unique_id`, but the absence of a matching lookup row must not remove an employee.

That requirement determines the join direction:

`Employees LEFT JOIN EmployeeUNI USING (id)`.

A left join keeps every row from the table on its left. For each employee ID, it searches the right table for matching rows. If a match exists, the joined row contains the matching `unique_id`. If none exists, SQL still emits the employee row and fills columns contributed by `EmployeeUNI` with `NULL`.

An inner join would be wrong because it would keep only employees that already have unique identifiers. Alice and Bob in the example would disappear instead of appearing with null values.

**What `USING (id)` means**

Both tables contain a column named `id`. The `USING (id)` syntax is a concise equality join: it matches rows for which `Employees.id = EmployeeUNI.id`. It also presents the shared join column as one combined column in a full joined projection, avoiding two separately named `id` columns.

The exact query does not need to return `id`, so its final projection is only:

`SELECT unique_id, name`.

`name` comes from the preserved `Employees` row. `unique_id` comes from the optional matching `EmployeeUNI` row and is automatically null when the match is absent. No `CASE`, `COALESCE`, or literal replacement is necessary: the null-extension behavior of the left join already implements the requirement.

**Following the sample row by row**

Employee ID 11 finds a matching lookup row `(11, 2)`, so the projection yields unique identifier 2 and name Meir. ID 90 similarly yields 3 and Winston, while ID 3 yields 1 and Jonathan.

Employee IDs 1 and 7 have no right-side match. The left join nevertheless produces one joined row for each, with `EmployeeUNI.unique_id` equal to `NULL`. Projecting the requested columns yields null with Alice and null with Bob.

Rows in `EmployeeUNI` whose ID does not occur in `Employees` would not appear. The query is not being asked to list identifier assignments independently; it is being asked to annotate the employee list.

**Why no explicit ordering appears**

The contract allows the result in any order. SQL does not guarantee a particular row order without `ORDER BY`, but no deterministic order is required here. Omitting sorting avoids unnecessary work and remains correct even if the database happens to return sample-like order.

**Why the query is correct**

Fix an arbitrary row in `Employees`. Left-join semantics guarantee that it produces joined output. If a lookup row with the same `id` exists, equality matching attaches its `unique_id`. If none exists, null extension supplies exactly the requested null. Selecting `unique_id` and `name` therefore produces the correct requested pair for this employee.

Because this reasoning applies to every preserved employee and no unmatched right-only row is introduced, the result contains precisely the annotated employee rows required by the problem, subject to the intended assumption that each employee has at most one identifier mapping.

**The importance of right-side key uniqueness**

The local table text states that `(id, unique_id)` is a composite primary key. That prevents the exact same pair from repeating, but by itself it does not prevent one `id` from appearing with several different unique IDs. If that were legal, a single employee would match several right rows and the query would output that employee several times.

The narrative says a row contains “the corresponding unique id,” and the intended problem model treats the lookup as one optional mapping per employee. The exact query relies on that one-to-zero-or-one relationship. If the stronger composite-key interpretation genuinely permits multiple mappings per ID, the required one-row-per-employee result needs an additional rule specifying which mapping to choose; SQL cannot infer one correctly.

## Complexity detail

Let $E$ be the number of `Employees` rows and $U$ the number of `EmployeeUNI` rows. Under a standard hash-join plan, the database builds a lookup structure for the right table in $O(U)$ time, scans the $E$ employee rows in $O(E)$ time, and performs expected constant-time lookups. Total time is $O(E+U)$ and working space is $O(U)$, matching the manifest.

With a suitable index on `EmployeeUNI.id`, an optimizer may instead perform indexed lookups. That plan can have a different detailed bound, such as $O(E\log U)$, while using less explicit hash memory. SQL is declarative, so the database chooses the physical plan based on indexes and statistics. The manifest describes the conventional linear hash-join model.

The result contains $E$ rows under the intended unique mapping. Required output storage is normally excluded from auxiliary-space analysis. No sorting cost is needed because the result order is unrestricted.

## Alternatives and edge cases

- **Explicit `ON` clause:** Write `ON Employees.id = EmployeeUNI.id`. It is equivalent and can be clearer when join columns have different names or when qualified names are desired.
- **Inner join:** This incorrectly removes employees without a unique identifier and therefore fails the central null requirement.
- **Correlated scalar subquery:** Select the matching unique ID separately for every employee. It can work with a unique indexed lookup but is often less direct than one left join.
- **Right join with reversed tables:** It can preserve `Employees` if table order is reversed, but left join expresses the output ownership more naturally.
- **Employee without a mapping:** The row remains and `unique_id` is `NULL` automatically.
- **Employee with a mapping:** Equality on `id` attaches the identifier while keeping the employee name.
- **Unused mapping row:** A right-side ID absent from `Employees` is omitted, which is correct because the output is employee-driven.
- **Several mappings for one ID:** The exact join duplicates the employee. Correct one-row behavior requires an actual uniqueness guarantee or an explicit selection rule.
- **Duplicate employee IDs:** `Employees.id` is a primary key, so this case is excluded and each employee source row is unique.
- **Null display:** SQL returns a database `NULL`, not the text string `"null"`.
- **Result order:** No `ORDER BY` is necessary because any order is accepted.
- **Column projection:** Selecting only `unique_id` and `name` prevents the shared internal `id` from leaking into the requested output.
