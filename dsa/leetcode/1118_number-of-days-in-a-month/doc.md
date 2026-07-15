# Number of Days in a Month

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1118 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/number-of-days-in-a-month/) |

## Problem Description

### Goal

You are given a Gregorian calendar `year` and a numeric `month`. Return the number of days in that month. April, June, September, and November have 30 days; the other non-February months have 31.

February normally has 28 days and has 29 in a leap year. A year divisible by 400 is a leap year. Otherwise, it is a leap year exactly when it is divisible by 4 but not by 100. Apply those century exceptions rather than using divisibility by 4 alone.

### Function Contract

**Inputs**

- `year`: a Gregorian calendar year with `1583 <= year <= 2100`.
- `month`: an integer from `1` for January through `12` for December.

**Return value**

- The integer number of days in the specified month of the specified year.

### Examples

**Example 1**

- Input: `year = 1992`, `month = 7`
- Output: `31`

**Example 2**

- Input: `year = 2000`, `month = 2`
- Output: `29`

**Example 3**

- Input: `year = 1900`, `month = 2`
- Output: `28`

Although 1900 is divisible by 4, it is a century year not divisible by 400.

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Handle February with the complete Gregorian rule:** When `month == 2`, evaluate `year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)`. Return 29 when true and 28 otherwise. The order of these predicates correctly distinguishes leap centuries such as 2000 from ordinary centuries such as 1900.

**Classify the remaining months:** The four months in `{4, 6, 9, 11}` have 30 days. Every other valid non-February month has 31. Because the input month is guaranteed valid, these cases are exhaustive.

The February branch follows the calendar's necessary and sufficient leap-year condition. Outside February, year does not affect month length, and membership in the fixed 30-day set exactly separates the two remaining answers. Therefore the returned value is correct for every permitted pair.

#### Complexity detail

The algorithm performs a fixed number of comparisons, remainder operations, and membership checks, independent of the numeric input. Time is $O(1)$ and only fixed scalar or constant-table state is used, so space is $O(1)$.

#### Alternatives and edge cases

- **Twelve-entry month table:** Store ordinary month lengths and add one to February in a leap year. It has the same bounds and can make the mapping explicit.
- **Calendar-library lookup:** It can be concise but hides the required leap-year reasoning and may introduce environment-specific date ranges.
- **Divisible by four only:** This incorrectly labels 1900 as leap.
- **Exclude every century:** This incorrectly labels 2000 as non-leap because centuries divisible by 400 are leap years.
- **February in an ordinary year:** It has 28 days.
- **February in a non-century leap year:** A year such as 1992 has 29 days.
- **Thirty-day months:** April, June, September, and November are the only four.
- **Boundary years:** The same Gregorian predicates apply at 1583 and 2100; 2100 is not leap.

</details>
