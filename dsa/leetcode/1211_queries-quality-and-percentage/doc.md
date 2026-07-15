# Queries Quality and Percentage

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1211 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/queries-quality-and-percentage/) |

## Problem Description

### Goal

The `Queries` table contains collected database-query results and may include duplicate rows. Each row has a `query_name`, a result value, its `position` from 1 through 500, and its `rating` from 1 through 5. A row is a poor query result when its rating is less than 3.

For each distinct `query_name`, compute its quality as the average of $\texttt{rating}/\texttt{position}$ across all rows with that name. Also compute its poor query percentage as 100 times the fraction of those rows whose rating is less than 3. Round both metrics to two decimal places and return the groups in any order.

### Function Contract

**Input table**

- `Queries(query_name, result, position, rating)`: Duplicate rows are allowed; $1\le\texttt{position}\le500$ and $1\le\texttt{rating}\le5$.
- Let $n$ be the row count and $g$ the number of distinct query names.

**Return value**

- One row per query name with columns `query_name`, `quality`, and `poor_query_percentage`, with both numeric metrics rounded to two decimal places.

### Examples

**Example 1**

`Queries`

| query_name | result | position | rating |
|---|---|---:|---:|
| Dog | Golden Retriever | 1 | 5 |
| Dog | German Shepherd | 2 | 5 |
| Dog | Mule | 200 | 1 |
| Cat | Shirazi | 5 | 2 |
| Cat | Siamese | 3 | 3 |
| Cat | Sphynx | 7 | 4 |

Output:

| query_name | quality | poor_query_percentage |
|---|---:|---:|
| Cat | 0.66 | 33.33 |
| Dog | 2.50 | 33.33 |

**Example 2**

A group in which no rating is below 3 has a poor query percentage of `0.00`.

**Example 3**

Duplicate table rows each contribute separately to both averages.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(g)$

<details>
<summary>Approach</summary>

#### General

**Group at the requested reporting grain.** Group every row by `query_name`. Duplicate rows remain separate inputs to the aggregates, as required by the table semantics.

**Average the quality contribution directly.** Convert `rating` and `position` to a non-integer numeric ratio before applying `AVG`. This prevents integer division from truncating values such as $5/2$. Round the resulting group average to two decimal places only after aggregation.

**Turn the poor predicate into an indicator.** Map `rating < 3` to 1 and every other rating to 0. Its group average is the fraction of poor rows; multiplying by 100 converts that fraction to a percentage. Rounding after multiplication produces the requested two-decimal result.

Each aggregate sees exactly the rows belonging to its query name, so the two formulas match their definitions independently. A local `ORDER BY query_name` makes fixture output deterministic even though the platform allows any row order.

#### Complexity detail

With hash aggregation, the database scans all $n$ rows once and performs constant work per row, for $O(n)$ logical time. It maintains one fixed aggregate record for each of the $g$ query names, using $O(g)$ auxiliary space. A physical engine may choose a sort-based plan with different costs.

#### Alternatives and edge cases

- **Correlated aggregate per name:** Recomputing the averages by rescanning `Queries` for every distinct name can take $O(gn)$ time.
- **Redundant cross join:** Repeating every source row once per table row leaves averages unchanged but creates $O(n^2)$ intermediate rows.
- **Integer division:** Dividing two integers may truncate the quality contribution and produce a wrong average.
- **Rating exactly three:** It is not poor because the definition uses strictly less than 3.
- **No poor rows:** Averaging zero indicators produces `0.00` rather than `NULL`.
- **All poor rows:** The poor query percentage is `100.00`.
- **Duplicate rows:** Every occurrence contributes to the numerator and denominator.
- **Rounding order:** Round the final averages, not each individual ratio before averaging.

</details>
