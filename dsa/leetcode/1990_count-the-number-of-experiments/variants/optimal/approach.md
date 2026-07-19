## General
**Materialize the complete category domain**

Create one constant three-row relation for the platforms and another for the
experiment names. Their Cartesian product contains exactly the nine required
output combinations, independent of which categories appear in the data.

**Left join observations onto every pair**

Left join `Experiments` to that nine-row domain using both category columns.
Existing rows attach to their matching pair. A missing pair still retains one
domain row with null experiment columns, which is necessary for reporting a
zero.

**Count a nullable input identifier**

Group by platform and experiment name, then apply `COUNT(experiment_id)`.
`COUNT` ignores the null placeholder produced by an unmatched left join, so a
missing pair yields `0`; matched rows contribute one apiece because
`experiment_id` is unique and non-null.

The domain contains every valid pair exactly once, and every experiment joins
to exactly one pair, proving that the nine grouped counts are complete and
non-overlapping.

## Complexity detail
The platform-and-name domain has a fixed size of nine. Scanning and grouping
$N$ experiments therefore takes $O(N)$ time. The query maintains only nine
groups, so its auxiliary grouping and output state is $O(1)$ with respect to
$N$.

## Alternatives and edge cases
- **Nine `UNION ALL` count queries:** Compute one filtered scalar count for
  every fixed pair. This is correct but may scan `Experiments` nine times and
  repeats nearly identical SQL.
- **Group only the input table:** A direct `GROUP BY` reports observed pairs
  correctly but omits every required zero-count combination.
- **Conditional aggregation plus domain expansion:** Aggregate the input once,
  then left join those counts to the nine constants. This has the same
  asymptotic complexity and can also be clear.
- `COUNT(*)` is wrong after the left join because it counts the preserved
  placeholder row as one; count a nullable column from `Experiments`.
- Several experiment rows may share the same categories and must all be
  counted.
- A category absent from the input still participates in three zero-count
  output rows.
- Output order is not part of the contract.
