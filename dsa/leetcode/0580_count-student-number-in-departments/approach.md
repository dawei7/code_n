## General

The phrase “all departments, even ones with no current students” determines the shape of the query. `Department` is the complete catalog and must be the preserved side of a left join. `Student` supplies zero or more matching rows for each catalog entry.

**Why the query starts from `Department`**

The join

```sql
Department
LEFT JOIN Student USING (dept_id)
```

retains every `Department` row. For a department with students, it produces one joined row for each matching student. For a department without students, it still produces one placeholder joined row, with every column supplied by `Student` set to `NULL`.

An inner join would lose empty departments completely. Starting from `Student` would also make it awkward to recover departments that have no student row. The left join expresses the requirement directly: every department survives, while student data is optional.

`USING (dept_id)` is shorthand for equality between the same-named join columns, conceptually `Department.dept_id = Student.dept_id`. The foreign-key guarantee says every student’s department exists in the catalog. The primary key on `Department.dept_id` says each student matches exactly one department.

**Why `COUNT(student_id)` gives zero correctly**

After the join, `GROUP BY dept_id` gathers the joined rows for each department. The selected aggregate is `COUNT(student_id)`, not `COUNT(*)`. That distinction is the heart of the solution.

`COUNT(expression)` counts only rows where its expression is not `NULL`. `Student.student_id` is a primary key and is therefore non-`NULL` on every real student row. Each matched student contributes exactly one to the count.

For an empty department, the left join creates a placeholder row whose `student_id` is `NULL`. `COUNT(student_id)` ignores that placeholder, producing zero. `COUNT(*)` would count the placeholder itself and incorrectly report one student. The query deliberately counts a non-nullable column from the optional, right-hand table so that “no match” contributes zero.

**Why grouping by the ID is sound**

`GROUP BY dept_id` creates one result group per department identifier. The selected `dept_name` is functionally determined by that identifier because `Department.dept_id` is unique. In MySQL, selecting the corresponding name is valid under this primary-key dependency. Spelling the group as `GROUP BY Department.dept_id, Department.dept_name` would be more portable across SQL systems with stricter grouping rules, but it represents the same groups.

Grouping by the ID rather than only by the name also avoids accidentally combining two departments if names were not guaranteed unique. Identity comes from `dept_id`; `dept_name` is display data.

**Producing the requested order**

The query finishes with:

```sql
ORDER BY 2 DESC, 1
```

Ordinal 2 refers to the second selected expression, `COUNT(student_id) AS student_number`. Descending order places departments with more students first. Ordinal 1 refers to `dept_name`. Its omitted direction defaults to ascending, giving alphabetical name order when counts tie.

For the sample, Engineering’s joined group contains Jack and Jane, so its count is two. Science has Mark, so its count is one. Law receives only the null placeholder and therefore counts zero. Sorting by count yields Engineering, Science, then Law.

**Why the query is correct**

Take any department. The left join guarantees at least one joined row for it, so it cannot disappear. Every real student assigned to that department matches it by `dept_id` and yields one joined row with a non-`NULL` primary key. No student from another department can enter the group because the join equality rejects it.

After grouping, `COUNT(student_id)` counts all and only those real matching students. If there are none, the only joined row has a null student ID and contributes zero. Thus, each department produces exactly one result row with its exact number of students.

Ordering first by that count descending and then by name ascending matches both ranking rules. The selected aliases give the requested two-column result.

Several SQL details reinforce the reasoning. The count must use a right-table column, because left-table columns remain non-`NULL` even in an unmatched placeholder. The chosen right-table column must itself be guaranteed non-`NULL` for real matches, which `student_id` is. And the left/right orientation must preserve `Department`, because it is the universe of required outputs.

## Complexity detail

Let $D$ be the number of departments and $S$ the number of students. A standard hash join can build or probe join structures in expected $O(D+S)$ time. Group aggregation then processes at most $S+D$ joined rows: one per student plus one placeholder for each empty department. It stores one count per department.

Sorting the $D$ result groups by count and name costs $O(D\log D)$ time. A conservative combined expression is $O(D+S+D\log D)$, which is covered by the manifest’s $O((D+S)\log D)$ bound. The join, group state, and result sorting can use $O(D+S)$ working space in a general plan, matching the declared space bound.

An actual database may use indexes, sort-merge joining, or streaming aggregation, so physical costs vary. The result itself has exactly $D$ rows.

## Alternatives and edge cases

- **Pre-aggregate students, then join:** Count students per `dept_id` in a subquery and left-join those counts to `Department`, using `COALESCE(count, 0)`. This can reduce join output size before the catalog join and is equally valid.
- **Correlated count:** A subquery can count students separately for each department. With a suitable index it may perform well, but without one it can repeatedly scan `Student`.
- **Inner join:** Incorrect because departments with zero students vanish.
- **`COUNT(*)`:** Incorrect after a left join because the synthetic unmatched department row is still a row and would be counted as one.
- **Counting `Department.dept_id`:** Also incorrect for empty departments because the preserved left-side ID remains non-`NULL` in the placeholder.
- **No students at all:** Every department remains and receives count zero; alphabetical department name breaks the all-zero tie.
- **No departments:** Foreign-key-valid student data must also be empty, and the output is empty.
- **Equal student counts:** The second key must sort `dept_name` alphabetically ascending.
- **Duplicate department names:** Grouping by unique `dept_id` keeps distinct departments separate even if their displayed names happen to match.
- **Unique student IDs:** Each real student contributes exactly one because `student_id` is a non-`NULL` primary key.
- **Ordinal ordering:** `ORDER BY 2 DESC, 1` is concise, but naming `student_number` and `dept_name` explicitly can be easier to maintain if the select-list order changes.
- **Portability of grouping:** Some database modes require `dept_name` in the `GROUP BY` despite its functional dependency on the primary key. Adding it does not change the algorithm.
