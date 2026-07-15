# Day of the Year

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1154 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/day-of-the-year/) |

## Problem Description

### Goal

You are given a string `date` representing a Gregorian calendar date in `YYYY-MM-DD` format. Return that date's day number within its year, counting January 1 as day $1$ and continuing through the calendar months in order.

The string always represents a valid date from January 1, 1900 through December 31, 2019. The calculation must therefore respect the Gregorian leap-year rules: February has 29 days in a leap year and 28 otherwise. All other month lengths follow the ordinary Gregorian calendar.

### Function Contract

**Inputs**

- `date`: A valid Gregorian date string of length 10 in `YYYY-MM-DD` format. Positions `4` and `7` contain `"-"`, and every other character is a digit.

The represented date lies between January 1, 1900 and December 31, 2019, inclusive.

**Return value**

- The 1-indexed day number of `date` within its year.

### Examples

**Example 1**

- Input: `date = "2019-01-09"`
- Output: `9`

**Example 2**

- Input: `date = "2019-02-10"`
- Output: `41`

**Example 3**

- Input: `date = "2000-03-01"`
- Output: `61`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Separate the calendar fields.** Splitting `date` on `"-"` yields the numeric year, month, and day. The desired ordinal consists of the days in every complete month before the given month plus the current day number.

**Give February the correct length.** In the Gregorian calendar, a year is a leap year when it is divisible by $400$, or when it is divisible by $4$ but not by $100$. This distinction makes 2000 a leap year but 1900 a common year. Start with the twelve ordinary month lengths and set February to 29 only when that condition holds.

Summing `month_days[:month - 1]` includes exactly the completed months. Adding `day` then counts the days already reached in the current month, including the given date itself. Because the input is guaranteed valid, no normalization or date validation is needed.

#### Complexity detail

The input always contains 10 characters, and the calculation examines at most 12 month lengths. Both limits are fixed independently of any scalable input quantity, so parsing and summation take $O(1)$ time. The twelve-element month table and parsed fields also occupy $O(1)$ space.

#### Alternatives and edge cases

- **Use a date library:** A standard-library date parser can compute the ordinal, but it introduces an unnecessary dependency on library formatting and timezone-free date behavior for a small fixed calculation.
- **Use cumulative month offsets:** Precomputed offsets also give a constant-time result, provided one extra day is added after February in leap years.
- **Century years:** Divisibility by $100$ cancels the usual divisible-by-$4$ rule unless the year is also divisible by $400$.
- **January dates:** There are no preceding months, so the answer is the numeric day directly.
- **Leap day and dates after February:** February 29 is valid only in leap years, and every later date in such a year has an ordinal one greater than the corresponding common-year date.
- **Year boundaries:** January 1 returns $1$; December 31 returns $365$ in a common year and $366$ in a leap year.

</details>
