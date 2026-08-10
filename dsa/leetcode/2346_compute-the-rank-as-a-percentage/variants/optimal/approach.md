## General

**Compute rank and department size as window values**

Each student's percentage depends on other rows in the same department but must still return one row per student. Window functions are designed for this: they calculate partition-level information without collapsing rows through grouping.

The query uses two window expressions partitioned by `department_id`:

- `RANK()` supplies the student's descending-mark rank;
- `COUNT(1)` supplies the department's total student count.

Every source row remains in the output with its own `student_id` and `department_id`.

**Rank marks from highest to lowest**

`RANK() OVER (PARTITION BY department_id ORDER BY mark DESC)` restarts ranking for every department and places higher marks first.

The highest mark receives rank one. Equal marks receive the same rank because `RANK` assigns ties identically. Ranks after a tie contain gaps, matching the positional definition of rank. For example, marks `90,90,80` receive ranks `1,1,3`.

Using `DENSE_RANK` would be wrong when a lower mark follows a tie because it would produce `1,1,2` and a different percentage.

This distinction is part of the formula rather than a cosmetic display choice. The numerator measures how many ranking positions precede the student, including positions occupied by tied students. After two students tie for first, the next student is in the third positional slot, so `rank - 1` must be two. Compressing that student to dense rank two would incorrectly claim that only one position precedes them and would understate their percentage.

**Translate the rank into the requested scale**

The formula is

`(rank - 1) * 100 / (department_count - 1)`.

Subtracting one makes the highest rank zero. Dividing by one less than the group size spreads positional ranks across a scale whose last unique position is 100.

The multiplication by 100 occurs before division in the expression, producing a percentage rather than a fraction. MySQL performs the numeric calculation and `ROUND(..., 2)` rounds it to two decimal places.

Students tied on a mark share a rank and therefore share the same percentage.

**Handle a one-student department**

If a department contains one student, both `rank - 1` and `count - 1` are zero, producing division by zero. MySQL yields `NULL` for that expression rather than a meaningful percentage.

`COALESCE(rounded_expression, 0)` replaces the null with zero. A sole student is the highest-ranked student, so percentage zero is the natural result.

For normal departments with at least two students, the calculation is non-null and `COALESCE` preserves it.

**Why window partitions are independent**

Both rank and count use the same `PARTITION BY department_id`. A student's numerator and denominator therefore refer to the same department. Marks in another department cannot affect their rank, and students elsewhere cannot inflate the denominator.

The result has no required order, so the query does not add an outer `ORDER BY`. The ordering inside `RANK` defines ranking logic only; it does not guarantee final row presentation.

**A tie trace**

For a two-student department where both marks are 650, both receive rank one and the count is two. Each percentage is

`(1-1) * 100 / (2-1) = 0`.

For marks 920, 610, and 530, ranks are one, two, and three with count three, producing zero, 50, and 100.

**Why the result is correct**

For every row, the rank window gives exactly the department position required by descending marks and shared ties. The count window gives the exact department size. Substituting those values into the stated formula and rounding produces the requested percentage. The only undefined denominator case is explicitly mapped to zero.

No row is lost or duplicated because window functions annotate rather than group the source.

## Complexity detail

Let `n` be the number of students. Ranking generally requires ordering rows within departments, giving `O(n \log n)` time under comparison sorting. Counting partitions and evaluating expressions add linear work.

The database may buffer or sort `O(n)` rows for window evaluation, so the manifest gives `O(n)` working space. Actual memory versus temporary-disk use depends on MySQL's execution plan and configuration.

The output contains exactly `n` rows. Required result storage is normally excluded from auxiliary-space analysis.

## Alternatives and edge cases

- **MySQL `PERCENT_RANK`:** This window function directly computes `(rank-1)/(rows-1)` and could be multiplied by 100, often with the single-row case already defined as zero.
- **Correlated subqueries:** Count higher marks and department size per student. This can repeat scans and requires careful tie handling.
- **`DENSE_RANK`:** It removes gaps after ties and does not match the specified rank formula.
- **`ROW_NUMBER`:** It gives different ranks to tied marks, violating the tie rule.
- **Global rank without partition:** Students from different departments would compete incorrectly.
- **Global count denominator:** Percentages must use department size, not total table size.
- **One student:** Division by zero becomes null and `COALESCE` returns zero.
- **All students tied:** Everyone has rank one and percentage zero.
- **Tie below the top:** Tied students share the same percentage, and later ranks skip positions.
- **Negative or unusual marks:** Descending numeric ordering still defines rank; the schema uses integers without requiring positivity.
- **Rounding:** `ROUND(...,2)` is applied after the full percentage calculation.
- **Any output order:** No final sort is necessary.
- **Unique student IDs:** Each source row corresponds to one output student.
