# Running Total for Different Genders

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1308 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/running-total-for-different-genders/) |

## Problem Description
### Goal
The `Scores` table records a player's score on a competition day and identifies whether the player belongs to the female team (`F`) or male team (`M`). The pair `(gender, day)` is unique, so each gender has at most one recorded score on a given date.

For every recorded gender-and-day row, compute that gender's cumulative score from its earliest recorded day through the current day, inclusive. Return the gender, day, and running total, ordering the rows first by gender and then by day in ascending order.

### Function Contract
**Inputs**

The database contains one table:

- `Scores(player_name, gender, day, score_points)`
- `player_name` is the player's name.
- `gender` is either `F` or `M`.
- `day` is the score date.
- `score_points` is the number of points recorded on that row.
- `(gender, day)` is the primary key.

Let $n$ be the number of rows in `Scores`.

**Return value**

A relation with columns `gender`, `day`, and `total`. For a row with gender $g$ and date $d$,

$$
\texttt{total}
=
\sum_{r:\,r.\texttt{gender}=g\,\land\,r.\texttt{day}\le d}
r.\texttt{score_points}.
$$

Sort the output by `gender` and then `day`, both ascending.

### Examples
**Example 1**

- Input rows for `F`: `("Priyanka","F","2019-12-30",17)`, `("Priya","F","2019-12-31",23)`, `("Aron","F","2020-01-01",17)`
- Output rows: `("F","2019-12-30",17)`, `("F","2019-12-31",40)`, `("F","2020-01-01",57)`

**Example 2**

- Input rows: `("Jose","M","2019-12-18",2)`, `("Khali","M","2019-12-25",11)`
- Output rows: `("M","2019-12-18",2)`, `("M","2019-12-25",13)`

**Example 3**

- Input rows: `("Ada","F","2024-04-10",9)`
- Output: `("F","2024-04-10",9)`

### Required Complexity
- **Time:** $O(n\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Partition the running sum by gender**

Use `SUM(score_points)` as a window aggregate. `PARTITION BY gender` starts an independent accumulation for each team, and `ORDER BY day` establishes chronological prefix order inside that partition.

Because `(gender, day)` is unique, the ordered window has one row per position. An explicit `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` frame states the intended prefix exactly: the frame for a row contains every earlier row of the same gender plus that row itself. Its sum is therefore precisely the required cumulative score.

**Separate calculation order from display order**

Window ordering determines which rows contribute to each total, but SQL does not guarantee final presentation order from a window clause alone. Add an outer `ORDER BY gender, day` so the returned relation follows the required gender-first chronological order.

#### Complexity detail

The database partitions and orders $n$ rows for the window computation, which takes $O(n\log n)$ time under the standard comparison-sorting model. The ordered window operation and result materialization can use $O(n)$ space.

#### Alternatives and edge cases

- **Correlated prefix subquery:** Summing all same-gender rows with `day <= current_day` for every outer row is correct, but without relying on a special index plan it performs $O(n^2)$ row comparisons.
- **Self-join and group:** Joining each row to all earlier same-gender rows and grouping produces the same totals, while also materializing a potentially quadratic intermediate relation.
- **Independent partitions:** The female and male running totals must never contribute to one another, even on the same date.
- **First date:** The earliest row for a gender has a total equal to its own `score_points`.
- **Missing dates:** Cumulative totals advance only on dates present in the table; no synthetic calendar rows are returned.
- **Input order:** Physical insertion order is irrelevant because both the window and final result use explicit date ordering.

</details>
