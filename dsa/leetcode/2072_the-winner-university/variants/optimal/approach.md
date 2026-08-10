## General

**Turn the scoring rule into two independent counts**

The result depends on only one fact about each university: how many of its students have a score of at least 90. Individual student names, the order of the rows, and the exact values above 90 do not affect the winner. A student with score 90 qualifies because the boundary is inclusive, and a student with score 89 does not.

The query therefore reduces each input table to a single number:

- the `NewYork` subquery evaluates `COUNT(1)` over rows satisfying `score >= 90` and names that count `cnt`;
- the `California` subquery performs the same calculation for its own table.

This is the essential simplification. The outer query does not need to retain qualifying rows or match students across universities. It needs only the two totals.

Suppose New York has scores 88, 90, and 97, while California has scores 90, 91, 72, and 84. The New York count is 2 and the California count is also 2. The outer comparison consequently returns `'No Winner'`. Notice that 97 being higher than 91 is irrelevant: the problem compares the number of qualifying students, not the universities' maximum scores or average scores.

**Why each aggregate subquery always produces one usable row**

An aggregate query containing `COUNT` and no `GROUP BY` summarizes the entire filtered input as one group. It returns exactly one row even when no source rows satisfy the condition. In that empty case, `COUNT(1)` returns 0 rather than `NULL`.

That behavior matters to the structure of the solution. If the subqueries merely selected qualifying rows, one side could produce no rows and prevent the outer query from producing a result. Here, each side is guaranteed to produce its one scalar count. Even if both university tables are empty, the derived tables contain one row each, both counts are 0, and the answer is `'No Winner'`.

The aliases `n1` and `n2` name these two one-row derived tables. Their columns are accessed as `n1.cnt` and `n2.cnt`. The comma between the derived tables is a cross join. A cross join normally pairs every row on the left with every row on the right, but each side has exactly one row, so the result has exactly one pair. The outer `SELECT` therefore also returns exactly one row.

**Choose the output with a complete three-way comparison**

The `CASE` expression checks the possible relationships between the counts in a deliberate order:

1. If `n1.cnt > n2.cnt`, New York has more qualifying students, so the returned value is `'New York University'`.
2. If `n1.cnt < n2.cnt`, California has more qualifying students, so the returned value is `'California University'`.
3. Otherwise, neither strict inequality is true. For ordinary integer counts, that means the counts are equal, so the returned value is `'No Winner'`.

These cases are mutually exclusive and exhaustive. Two integer counts cannot simultaneously be greater and less than one another, and exactly one of greater than, less than, or equal must hold. As a result, the `CASE` cannot select an incorrect university and cannot omit the tie case.

The expression is aliased as `winner` because that is the required output column name. The exact result strings are part of the contract. Returning a shortened name such as `'New York'` or changing capitalization would produce the wrong output even if the comparison itself were correct.

**Why the query is correct**

Let $Y$ be the number of rows in `NewYork` whose `score` is at least 90, and let $C$ be the corresponding number for `California`. The first subquery returns exactly $Y$: its filter includes precisely the qualifying New York rows, and `COUNT(1)` adds one for each of them. By the same reasoning, the second subquery returns exactly $C$.

The outer query compares those exact values. When $Y>C$, its first branch returns New York. When $Y<C$, its second branch returns California. When $Y=C$, both strict branches are false and `ELSE` returns no winner. Those are exactly the three outcomes specified by the problem, so the returned row is correct.

The primary-key guarantees on the university tables mean their student records are distinct according to the schema. The query does not need to use the key explicitly because it is counting qualifying rows, and each row already represents one student record. There is also no relationship that needs to be joined between the two tables: a student from one university is never paired by identity with a student from the other.

## Complexity detail

Let $N_Y$ be the number of rows in `NewYork`, let $N_C$ be the number of rows in `California`, and define $N=N_Y+N_C$.

The database must determine whether each source row satisfies `score >= 90`. In the general execution model, the first aggregate scans $N_Y$ rows and the second scans $N_C$ rows. The total work is therefore $O(N_Y+N_C)=O(N)$. The final cross join and `CASE` operate on only two scalar aggregate rows, so they add constant work.

The aggregate state contains one running count per subquery. After a qualifying row is examined, its full contents do not need to be retained. The outer query likewise holds only the two counts and the one selected result. The algorithmic auxiliary space is therefore $O(1)$.

A particular database may use an index, parallel scan, or another physical optimization, but the query does not require one and its portable worst-case explanation remains a linear scan of the two tables. The output itself is one row and one column, which is also constant in size.

## Alternatives and edge cases

- **Conditional aggregation after combining the tables:** One could label and combine both universities' rows and then compute conditional counts in one larger aggregate. That introduces unnecessary union and labeling work when two small scalar subqueries express the two independent totals directly.
- **Joining students by an identifier:** A regular join would be conceptually wrong because the task does not compare corresponding students. It compares two population counts, and there may be no meaningful cross-university key relationship.
- **Sorting qualifying scores:** Sorting cannot help decide which university has more qualifying rows. Counting alone is sufficient, so sorting would add avoidable $O(N\log N)$ work in a typical comparison-based implementation.
- **Using an average or maximum score:** The winner is based solely on how many scores meet the threshold. A university can have the highest individual score or the higher average and still lose by having fewer qualifying students.
- **Inclusive score boundary:** The predicate must be `score >= 90`. Replacing it with `score > 90` incorrectly excludes every student whose score is exactly 90.
- **Both counts equal:** Equality must return `'No Winner'` whether the shared count is large or zero. The `ELSE` branch covers every tie without needing another arithmetic test.
- **No qualifying rows:** `COUNT(1)` returns 0 rather than `NULL`. Thus one university with no qualifying students can still be compared normally, and two zero counts correctly form a tie.
- **Empty input tables:** Each ungrouped aggregate still returns one row containing 0, so the cross join and outer `SELECT` continue to return exactly one answer row.
- **Exact output literals:** The three strings and the `winner` column alias must be preserved exactly because SQL result schemas and string values are judged as part of the answer.
- **Database execution details:** An optimizer may rewrite the cross join of scalar aggregates internally. That does not change the reasoning: each table contributes one exact count, and one three-way comparison selects the result.
