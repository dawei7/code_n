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
