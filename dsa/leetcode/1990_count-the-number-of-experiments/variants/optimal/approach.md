## General

**Generate the complete category grid first**

Grouping only rows that exist in `Experiments` cannot produce categories with zero observations. The query therefore constructs the required output domain explicitly before looking at the data.

CTE `P` contains exactly the three platform literals: Android, IOS, and Web. CTE `Exp` contains exactly the three experiment-name literals: Reading, Sports, and Programming.

Each uses `UNION` to form its constant relation. The literals are distinct, so duplicate removal changes nothing, but the result is the intended three-row list.

**Take the Cartesian product**

CTE `T` selects from `P, Exp` without a join condition. In SQL, this is a cross join. Every platform row pairs with every experiment-name row, creating $3\cdot3=9$ category combinations.

This fixed nine-row table is the backbone of the solution. Even a category absent from the actual experiments already has a row that can survive to the output.

**Attach matching experiment records**

`T AS t LEFT JOIN Experiments USING (platform, experiment_name)` matches each category pair with every recorded experiment having both the same platform and experiment name.

The left join is essential. If a pair has no experiment, its `T` row remains and the columns coming from `Experiments`, including `experiment_id`, are null.

`USING` is shorthand for equality on both named columns and exposes one merged copy of each join key. It is appropriate because both tables use the exact same key names.

**Count a nonnull column rather than rows**

`COUNT(experiment_id)` counts only nonnull values. For a category with real matches, `experiment_id` is the table's unique nonnull identifier, so the count equals the number of experiment rows.

For an absent category, the left join still produces one placeholder row, but its `experiment_id` is null. `COUNT(experiment_id)` returns zero.

Using `COUNT(*)` would be wrong for zero categories because it would count the placeholder row and return one. Choosing the right counted expression is what converts missing matches into zero.

**Group by both category dimensions**

`GROUP BY 1, 2` groups by the first and second selected columns: `platform` and `experiment_name`. Each of the nine generated pairs becomes one output group.

Within a group, every joined experiment row has the same two category values, so the aggregate gives its frequency. Because `T` contains every pair exactly once, the output contains exactly nine rows.

**Trace one present and one absent pair**

If Web and Reading has two experiment rows, its generated pair joins to both records. Both IDs are nonnull, so the count is two.

If Android and Sports has no record, its generated pair survives as one left-join row with null ID. The nonnull count is zero, yet the category labels remain in the result.

**Why the query is correct**

The cross product proves completeness: every required platform-experiment combination exists before aggregation. The left join associates each generated pair with all and only input rows from that category while retaining empty categories.

Primary-key nonnullness makes counting `experiment_id` identical to counting actual matches. Grouping by the pair produces one correct count per category. Hence the result is both complete and numerically correct.

**Why hard-coded categories are appropriate here**

The contract fixes the category domains to exactly three known enum values each. Deriving platforms or experiment names from the data would omit a value when no row currently uses it, recreating the original zero-category problem.

Explicit constant CTEs encode the complete declared domains. If the schema later gained enum values, these CTEs would need to be updated, but under the stated contract they are exact.

## Complexity detail

Let $N$ be the number of rows in `Experiments`. The generated category table always has nine rows. With hashing or a single scan/group plan, matching and aggregation take $O(N)$ time.

Only nine aggregate groups and fixed constant tables are required, so logical auxiliary space is $O(1)$ with respect to $N$. A database engine may allocate plan-dependent hash or temporary structures, but the number of result categories is fixed.

## Alternatives and edge cases

- **Group `Experiments` directly:** Misses category pairs whose count should be zero.
- **Conditional aggregation:** Can count all experiment names per platform, but still needs an explicit platform domain and may produce a wide rather than requested row format.
- **Separate tables for enum domains:** Preferable in a normalized extensible schema; cross joining those tables follows the same idea.
- **`COUNT(*)`:** Incorrectly counts the null-extended placeholder as one for absent categories.
- **`COUNT(experiment_id)`:** Correct because only actual matched rows have nonnull IDs.
- **Empty `Experiments` table:** The cross product still yields all nine pairs, each with zero.
- **Many rows in one category:** Every nonnull ID is counted once.
- **Unique experiment IDs:** Prevent accidental duplication within the source table.
- **Two-key join:** Both platform and experiment name are necessary; joining on only one mixes categories.
- **Fixed enum values:** Explicit CTE literals ensure categories absent from data still appear.
- **Any output order:** No `ORDER BY` is needed.
- **Positional grouping:** `GROUP BY 1, 2` refers to the two selected category columns.
- **No mutation:** The query reads and aggregates `Experiments`.
