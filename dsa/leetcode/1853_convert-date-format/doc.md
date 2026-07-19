# Convert Date Format

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/convert-date-format/) |
| Frontend ID | 1853 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |

## Problem Description

### Goal

The `Days` table stores unique calendar dates in a single `DATE` column named `day`. Produce one result row for every input row, converting the stored date into a human-readable English string while preserving the date itself rather than filtering, grouping, or reordering it.

The required text has the form `"day_name, month_name day, year"`. Spell out the weekday and month with their usual capitalization, place a comma after the weekday and before the year, and write the numeric day of the month without a leading zero. The returned column must also be named `day`; row order is unrestricted.

### Function Contract

**Inputs**

- `Days(day DATE)`: one row per unique calendar date.
- Let $r$ be the number of rows in `Days`.

**Return value**

- Return one column named `day`.
- Format every source date as the case-sensitive string `weekday, month day, year`.
- Do not require a particular row order.

### Examples

**Example 1**

- Input row: `2022-04-12`
- Output row: `Tuesday, April 12, 2022`

**Example 2**

- Input row: `2021-08-09`
- Output row: `Monday, August 9, 2021`

**Example 3**

- Input row: `2020-06-26`
- Output row: `Friday, June 26, 2020`

### Required Complexity

- **Time:** $O(r)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

Project the `day` column through MySQL's `DATE_FORMAT` function. The format token `%W` emits the full weekday name, `%M` emits the full month name, `%e` emits an unpadded day of the month, and `%Y` emits the four-digit year.

Literal punctuation and spaces in the format string produce the exact required shape. Alias the expression back to `day` so the result schema matches the contract. Because the query contains no ordering clause, it also respects the permission to return rows in any order.

Each input row is formatted independently and emitted exactly once. The database derives every textual component from the same typed date, so weekday, month, day, and year cannot become inconsistent with one another.

#### Complexity detail

The query scans and formats all $r$ rows once, giving $O(r)$ time. Apart from the required result relation and fixed-size formatting state for the current date, it requires $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Concatenate separate date functions:** `DAYNAME`, `MONTHNAME`, `DAY`, and `YEAR` can be joined manually, but the punctuation and spacing are easier to get wrong.
- **Client-side formatting:** Moving raw dates to application code violates the requirement to solve the transformation in SQL.
- **Single-digit days:** `%e` produces `9`, not `09`.
- **Case sensitivity:** Full English names must retain capitalization such as `Monday` and `August`.
- **Leap day:** The weekday and month must be derived from the actual valid date rather than hard-coded.
- **Column alias:** The formatted expression must be returned under the name `day`.
- **Row order:** No `ORDER BY` is necessary because any order is accepted.

</details>
