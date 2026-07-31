## General

**Group at the requested reporting grain.** The output needs one row for each
teacher, so group the `Teacher` rows by `teacher_id`. This creates exactly the
reporting groups required by the result and does not invent teachers that are
absent from the input.

**Count subjects rather than assignments.** A teacher may have several rows
with the same `subject_id` when that subject is taught in different
departments. `COUNT(DISTINCT subject_id)` removes those within-teacher
repetitions before counting, while identical subject identifiers belonging to
different teacher groups remain independent. Alias the aggregate as `cnt` to
match the output contract.

The grouping assigns every input row to its teacher's single group. Within
that group, the distinct aggregate establishes a one-to-one correspondence
between counted values and unique subjects taught by that teacher. Therefore
each output count is exact, and every represented teacher appears once.

## Complexity detail

Let $R$ be the number of assignments. A conservative sort-based execution
groups and deduplicates in $O(R\log R)$ time and uses $O(R)$ auxiliary space.
A database engine may instead choose hashing or exploit indexes, but those
physical-plan choices do not change the query's result.

## Alternatives and edge cases

- **Distinct-pair subquery:** First select distinct `(teacher_id, subject_id)`
  pairs, then group by teacher and use `COUNT(*)`; this is equivalent but more
  verbose.
- **Correlated distinct count:** Selecting teachers and running a distinct
  subject subquery for each one is correct, but can repeatedly scan the table
  and approach $O(R^2)$ work.
- **Self-join before aggregation:** Joining all rows belonging to the same
  teacher preserves the final distinct count, but may materialize quadratically
  many intermediate rows.
- **Repeated subject across departments:** Department differences do not
  increase `cnt` when `subject_id` is unchanged for the same teacher.
- **Shared identifiers across teachers:** Distinctness is scoped to each
  `teacher_id` group, so one subject can count once for every teacher who
  teaches it.
- **Result order:** No `ORDER BY` clause is required because the contract
  accepts the teacher rows in any order.
