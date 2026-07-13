# Students Report By Geography

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 618 |
| Difficulty | Hard |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/students-report-by-geography/) |

## Problem Description
### Goal
Given a `Student` table whose rows contain a student's name and one of the continents `America`, `Asia`, or `Europe`, rearrange the names into a report with exactly three columns named for those continents.

Sort the names belonging to each continent in ascending alphabetical order. Place the first name from each continent in the first row, the second name in the second row, and so on. Continue until the longest continent list is exhausted, using `NULL` when another continent has no name at a rank that still exists elsewhere.

### Function Contract
**Inputs**

- `Student(name, continent)`: student names labeled with exactly one of `America`, `Asia`, or `Europe`

**Return value**

- Columns named `America`, `Asia`, and `Europe`
- Row one contains the first alphabetic name from each continent, row two the second, and so on
- When a continent has no name at a rank that exists for another continent, its cell is null

### Examples
**Example 1**

- Input: America has Jane and Jack; Asia has Xi; Europe has Pascal
- Output rows: `(Jack, Xi, Pascal)`, `(Jane, null, null)`

**Example 2**

- Input: Asia has Bo and Ada; the other continents are empty
- Output rows: `(null, Ada, null)`, `(null, Bo, null)`

### Required Complexity

- **Time:** $O(R \log R)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

**Assign an independent alphabetic rank**

Use `ROW_NUMBER()` partitioned by `continent` and ordered by `name`. Each continent starts at rank one, so equal ranks identify names that belong on the same output row.

**Pivot each rank with conditional aggregation**

Group the ranked relation by its row number. For each target continent, a `CASE` expression exposes that continent's name and nulls the others; `MAX` selects the one nonnull value for the group. If no student from a continent has that rank, all corresponding values are null and the output cell remains null.

**Why every name appears in the correct cell**

Within one continent, `ROW_NUMBER` assigns every name one unique position in alphabetic order. Grouping equal positions places exactly the kth name from every available continent together. Conditional aggregation sends a name only to its own continent column, so no name is duplicated, omitted, or moved across continents.

#### Complexity detail

For `R` students, partition ordering costs $O(R \log R)$ time and $O(R)$ execution space. The grouped pivot is linear after ranking, and ordering the at most `R` result ranks does not increase the bound.

#### Alternatives and edge cases

- **Rank three filtered lists and join them:** separately number each continent and outer-join by rank; it is explicit but repeats similar logic and needs full-outer-join emulation in MySQL.
- **Session variables:** older MySQL solutions can maintain one counter per continent, but evaluation-order dependencies make them fragile compared with window functions.
- **Correlated rank count:** count preceding names for every student; it is correct for unique names but can take $O(R^2)$ time.
- A missing continent produces an entirely null column while other names still appear.
- Unequal continent sizes produce nulls only after the shorter list is exhausted.
- Input row order is irrelevant; names are ordered within each continent.
- The number of output rows equals the largest continent population.

</details>
