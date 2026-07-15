# Last Person to Fit in the Bus

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1204 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/last-person-to-fit-in-the-bus/) |

## Problem Description

### Goal

The `Queue` table describes every person waiting to board a bus. Both `person_id` and `turn` contain each integer from 1 through the number of rows exactly once. A smaller `turn` means that the person boards earlier, and `weight` records that person's weight in kilograms. Only one person boards at each turn.

The bus has a weight limit of 1000 kilograms, so boarding stops before the first person whose addition would make the accumulated weight exceed that limit. Find the `person_name` of the last person who can board. The test data guarantees that the first person fits.

### Function Contract

**Input table**

- `Queue(person_id, person_name, weight, turn)`: `person_id` is unique; `person_id` and `turn` are both permutations of the integers from 1 through $n$.
- Let $n$ be the number of people in the queue.

**Return value**

- One row with the column `person_name`, identifying the last person whose cumulative weight in `turn` order is at most 1000 kilograms.

### Examples

**Example 1**

`Queue`

| person_id | person_name | weight | turn |
|---:|---|---:|---:|
| 5 | Alice | 250 | 1 |
| 4 | Bob | 175 | 5 |
| 3 | Alex | 350 | 2 |
| 6 | John Cena | 400 | 3 |
| 1 | Winston | 500 | 6 |
| 2 | Marie | 200 | 4 |

Output:

| person_name |
|---|
| John Cena |

In boarding order, the cumulative weights are 250, 600, and 1000 through John Cena. Adding Marie would raise the total to 1200, so John Cena is the last person who fits.

**Example 2**

If the first person's weight is exactly 1000, that person is returned and nobody later in the queue can board.

**Example 3**

The physical row order of `Queue` does not determine boarding order; only `turn` does.

### Required Complexity

- **Time:** $O(n\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Express the boarding process as a prefix sum.** Order the rows by `turn` and use a windowed `SUM(weight)` from the first row through the current row. The resulting value is precisely the bus weight immediately after that person boards because every earlier turn contributes once.

**Keep only feasible prefixes.** Positive passenger weights make cumulative weight non-decreasing. Rows whose running total is at most 1000 are exactly the people who can board before the capacity would be exceeded. The platform guarantee that the first person fits ensures this filtered set is nonempty.

**Choose the final feasible turn.** Sort the feasible rows by `turn` in descending order and take one row. It has the greatest boarding position whose prefix remains within the limit, so its `person_name` is the requested last passenger.

#### Complexity detail

Without relying on an index for `turn`, ordering the $n$ rows for the window calculation costs $O(n\log n)$ time; the window scan and final selection are linear. The ordered window state may use $O(n)$ auxiliary space. A database engine with a suitable physical order or index may execute the scan more cheaply, but the stated bound does not assume one.

#### Alternatives and edge cases

- **Correlated prefix subquery:** Summing all rows with `turn <= current.turn` for every candidate is correct, but it can rescan the table $n$ times and take $O(n^2)$ time.
- **Self-join and aggregation:** Joining each row to all preceding turns and grouping by the candidate row also computes prefixes, but materializes up to quadratically many pairs.
- **Recursive CTE:** Simulating boarding turn by turn is possible, though more verbose and less direct than a window sum.
- **Exact capacity:** A cumulative weight equal to 1000 is allowed because boarding must not exceed the limit.
- **First person only:** The guarantee that turn 1 fits means the query always has a feasible row, even if turn 2 crosses the limit.
- **All people fit:** The row with the largest `turn` is returned.
- **Unordered storage:** Window ordering must use `turn`; neither insertion order nor `person_id` determines boarding order.

</details>
