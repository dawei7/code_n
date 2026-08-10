## General

**Begin with every student-subject combination**

The result must contain a row even when a student attended a subject's exam zero times. Starting from `Examinations` cannot naturally produce combinations that have no rows there. The query instead builds the complete set of required combinations first, then attaches matching attendance records.

In MySQL, `Students JOIN Subjects` without an `ON` or `USING` condition acts as a cross join. Every student is paired with every subject. If there are $S$ students and $U$ subjects, this stage produces exactly $S\cdot U$ rows, including pairs with no attendance.

The selected `student_name` travels with its student's primary-key row, while `subject_name` comes from the unique subject row.

**Preserve zero-attendance pairs with a left join**

The query left-joins `Examinations AS e` with `USING (student_id, subject_name)`. For a student-subject pair, every examination record with both matching fields joins to it. Because `Examinations` may contain duplicates, repeated attendance rows are deliberately preserved: each row represents one attendance.

If no examination record matches, the left join still emits the student-subject pair and fills columns from alias `e` with `NULL`. This placeholder is why an inner join would be wrong: an inner join would discard every zero-attendance combination.

**Count a nullable examination column rather than all rows**

The expression `COUNT(e.student_id)` counts only non-null values from the examination side. For a real matching attendance row, `e.student_id` is present and contributes one. For the placeholder row created by a missing match, it is `NULL` and contributes zero.

Using `COUNT(*)` in this exact join would incorrectly return one for a student-subject pair with no examination, because the preserved left-side placeholder is still a row. Qualifying the column with `e.` is equally important: the unqualified cross-product `student_id` is never null and would also count the placeholder.

For Alice and Math in the example, three matching examination rows join and the count is three. For Bob and Physics, no row matches, the left join produces one null examination placeholder, and `COUNT(e.student_id)` returns zero.

**Collapse attendance rows into one required result row**

`GROUP BY 1, 3` uses ordinal references to the first and third selected expressions: `student_id` and `subject_name`. All joined attendance rows for one student-subject pair become one group, over which the count is calculated.

The query also selects `student_name` without listing it separately in the group clause. Under this schema, `student_id` is the Students primary key, so each grouped student identifier functionally determines exactly one name. MySQL can therefore return the corresponding name consistently.

There is exactly one group for every row of the original student-subject cross product. Examination duplicates increase only the aggregate count; they do not create duplicate result rows.

**Produce the specified order**

`ORDER BY 1, 3` again refers to `student_id` and `subject_name`. It sorts identifiers numerically in ascending order and, within a student, sorts subject names in ascending lexicographic order, exactly as required.

The alias `attended_exams` gives the aggregate the required output column name. The other three columns already carry their specified names.

**Why the query is complete and exact**

Take any student and subject. The cross join creates their pair exactly once because both source keys are unique. The left join retains that pair whether it has zero, one, or many matching examination rows. `COUNT(e.student_id)` equals the number of those actual matches while ignoring only the synthetic null placeholder. Grouping returns one row for the pair.

Conversely, every output group originated from one real Students row and one real Subjects row, so no unauthorized combination appears. Its count includes exactly the examination rows with both matching identifiers. Thus the result contains every required pair with its exact attendance count.

## Complexity detail

Let $S$ be the number of students, $U$ the number of subjects, $E$ the number of examination rows, and $R=S\cdot U$ the mandatory number of result combinations. An efficient hash- or index-assisted plan can form and aggregate matches in $O(R+E)$ time before ordering. Since the output itself has $R$ rows, $\Omega(R)$ work is unavoidable.

The explicit `ORDER BY` may require sorting $R$ grouped rows, adding $O(R\log R)$ comparison work in a physical plan unless an engine can obtain the order from indexes or its chosen execution. The manifest's $O(R+E)$ time describes the relational join-and-aggregation core rather than guaranteeing every MySQL sort implementation is linear.

The cross-product groups, join state, and aggregation structures can use $O(R+E)$ logical working space in the worst case. A database may stream, hash, sort, or spill these structures, so exact memory depends on its optimizer. The result itself contains $R$ rows.

## Alternatives and edge cases

- **Pre-aggregate examinations first:** Group `Examinations` by student and subject, cross join the dimension tables, then left join the compact counts and use `IFNULL(..., 0)`. This can reduce intermediate duplicates while producing the same result.
- **Start from `Examinations`:** It omits student-subject pairs with zero attendance and cannot meet the output contract by itself.
- **Inner join examinations:** It similarly removes every zero-count pair.
- **`COUNT(*)` after a left join:** It counts the placeholder row and incorrectly reports one instead of zero.
- **Duplicate examination rows:** They represent repeated attendances and must each contribute one; the exact query preserves and counts them.
- **Student with no examinations:** The cross join still produces every subject, each with count zero.
- **Subject with no examinations:** Every student still receives a row for that subject with zero.
- **No examination rows at all:** The result remains the full student-subject product with all counts zero.
- **Ordinal grouping:** `GROUP BY 1, 3` depends on select-list positions; explicit column names can be clearer during future query edits.
- **Functional dependency:** Selecting `student_name` is safe because primary-key `student_id` uniquely determines it.
- **Required order:** Removing `ORDER BY` would leave row order unspecified and violate this problem's explicit sorting requirement.
