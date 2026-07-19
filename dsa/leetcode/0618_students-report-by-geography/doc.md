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
