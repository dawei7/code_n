# Number of Days Between Two Dates

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1360 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/number-of-days-between-two-dates/) |

## Problem Description

### Goal

Given two valid Gregorian calendar dates, determine the absolute number of whole days separating them. Each input uses the fixed `YYYY-MM-DD` representation, with a four-digit year followed by a two-digit month and day.

The dates may arrive in either chronological order and may be identical. Calendar conversion must account for different month lengths and leap years, including the century rule that a year divisible by $100$ is not a leap year unless it is also divisible by $400$. Return the nonnegative difference.

### Function Contract

**Inputs**

- `date1` and `date2`: valid dates formatted as `YYYY-MM-DD`, within the supported Gregorian range.

**Return value**

- The absolute number of days between the two dates.

### Examples

**Example 1**

- Input: `date1 = "2019-06-29", date2 = "2019-06-30"`
- Output: `1`

**Example 2**

- Input: `date1 = "2020-01-15", date2 = "2019-12-31"`
- Output: `15`

**Example 3**

- Input: `date1 = "2020-02-28", date2 = "2020-03-01"`
- Output: `2`
- Explanation: February 29 contributes an additional day in leap year 2020.

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Map each date to one ordinal.** Parse its year, month, and day. Count all days in complete years before the given year: $365(y-1)$ ordinary days, plus one for every multiple of $4$, minus multiples of $100$, plus multiples of $400$. This inclusion-exclusion exactly implements the Gregorian leap-year rule.

Add the fixed cumulative number of days before the current month, add one more when the date is after February in a leap year, and finally add the day of the month. The resulting ordinal increases by exactly one between consecutive valid dates.

**Subtract on a shared scale.** Both dates use the same arbitrary ordinal origin, so subtracting their ordinals cancels that origin. Taking the absolute value makes the result independent of input order and yields zero for identical dates.

#### Complexity detail

Parsing fixed-width components and evaluating a fixed number of arithmetic operations takes $O(1)$ time. The month-prefix constants and scalar date fields require $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Standard date library:** Parse both dates and subtract native date objects. This is concise when the runtime's calendar semantics and accepted imports are known.
- **Advance one day at a time:** Simulate calendar transitions until the later date is reached. It is correct but takes $O(D)$ time for a $D$-day gap.
- **Leap-day boundary:** February 28 to March 1 spans two days in a leap year and one otherwise.
- **Century exception:** Year 2100 is divisible by $100$ but not $400$, so it is not a leap year.
- **Reverse order:** Apply absolute value after ordinal subtraction rather than assuming `date1` is earlier.
- **Same date:** Equal ordinals correctly produce zero.

</details>
