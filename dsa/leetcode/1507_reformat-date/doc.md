# Reformat Date

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1507 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/reformat-date/) |

## Problem Description
### Goal

You are given a valid calendar date written as `Day Month Year`. The day is an integer from 1 through 31 followed by its English ordinal suffix, such as `1st`, `2nd`, `3rd`, or `20th`. The month is one of the twelve three-letter abbreviations from `Jan` through `Dec`, and the four-digit year lies from 1900 through 2100.

Convert this date to `YYYY-MM-DD` form. The year remains first, while the month and day must each use exactly two digits, including a leading zero when necessary.

### Function Contract
**Inputs**

- `date`: A valid date string containing exactly three space-separated fields: an ordinal day, an English month abbreviation, and a four-digit year from 1900 through 2100.
- The ordinal day uses one of the suffixes `st`, `nd`, `rd`, or `th`. No validity checking or calendar correction is required.

**Return value**

Return the same date as a string in `YYYY-MM-DD` format, with two-digit month and day fields.

### Examples
**Example 1**

- Input: `date = "20th Oct 2052"`
- Output: `"2052-10-20"`

**Example 2**

- Input: `date = "6th Jun 1933"`
- Output: `"1933-06-06"`

**Example 3**

- Input: `date = "26th May 1960"`
- Output: `"1960-05-26"`
