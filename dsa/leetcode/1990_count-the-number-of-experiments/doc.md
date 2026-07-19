# Count the Number of Experiments

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1990 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/count-the-number-of-experiments/) |

## Problem Description
### Goal
The `Experiments` table records individual experiments by unique identifier.
Every row uses one of three platforms—`Android`, `IOS`, or `Web`—and one of
three experiment names—`Reading`, `Sports`, or `Programming`.

Report the number of recorded experiments for every one of the nine possible
platform-and-name combinations. A combination must still appear with count `0`
when no input row uses it. Return the result rows in any order.

### Function Contract
**Inputs**

- `Experiments(experiment_id, platform, experiment_name)`: `experiment_id` is
  unique; `platform` belongs to `{Android, IOS, Web}` and `experiment_name`
  belongs to `{Reading, Sports, Programming}`.
- Let $N$ be the number of rows in `Experiments`.

**Return value**

- A nine-row table with columns `platform`, `experiment_name`, and
  `num_experiments`.
- Each platform-and-name pair occurs exactly once, and its count includes every
  matching input row.
- Result-row order is irrelevant.

### Examples
**Example 1**

For experiments `(IOS, Programming)`, `(IOS, Sports)`,
`(Android, Reading)`, two copies of `(Web, Reading)`, and
`(Web, Programming)`, the output is:

| platform | experiment_name | num_experiments |
|---|---|---:|
| Android | Reading | 1 |
| Android | Sports | 0 |
| Android | Programming | 0 |
| IOS | Reading | 0 |
| IOS | Sports | 1 |
| IOS | Programming | 1 |
| Web | Reading | 2 |
| Web | Sports | 0 |
| Web | Programming | 1 |

**Example 2**

- Input: one `(Android, Sports)` row
- Output: count `1` for `(Android, Sports)` and `0` for the other eight pairs.

**Example 3**

- Input: three `(Web, Programming)` rows
- Output: count `3` for that pair and `0` for every other pair.

### Required Complexity
- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

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

#### Complexity detail

The platform-and-name domain has a fixed size of nine. Scanning and grouping
$N$ experiments therefore takes $O(N)$ time. The query maintains only nine
groups, so its auxiliary grouping and output state is $O(1)$ with respect to
$N$.

#### Alternatives and edge cases

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

</details>
