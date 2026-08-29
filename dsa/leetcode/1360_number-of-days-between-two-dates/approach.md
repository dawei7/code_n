## General

Directly comparing year, month, and day fields becomes awkward when the interval crosses month ends or leap years. The solution converts each calendar date to a single ordinal: the number of days from a shared reference year through that date. The desired distance is then the absolute difference of the two ordinals.

**Apply the Gregorian leap-year rule exactly**

A year is a leap year when it is divisible by four, except that century years must also be divisible by four hundred. The helper returns
`year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)`.

This handles the important cases:

- 2020 is divisible by four and not by one hundred, so it is a leap year.
- 1900 is divisible by one hundred but not four hundred, so it is not a leap year.
- 2000 is divisible by four hundred, so it is a leap year.

A leap year has 366 days; an ordinary year has 365.

**Give February its correct length**

`daysInMonth` constructs the twelve month lengths. Every fixed month uses its usual number of days. February is `28 + int(isLeapYear(year))`, so the Boolean contributes one only in a leap year.

The function receives a one-based month and indexes the list with `month - 1`. Valid-date input guarantees that the month is in the supported range.

**Convert a date to one cumulative count**

`calcDays` splits a string such as `"2020-01-15"` at hyphens and converts the three fields to integers.

It then adds three pieces:

1. For every complete year from 1971 through `year - 1`, add 365 plus its leap-day indicator.
2. For every complete month before `month` in the target year, add that month’s length.
3. Add `day` for the position inside the target month.

The resulting scale is one-based: 1971-01-01 maps to one rather than zero. That offset is harmless because both dates use the same reference and convention. Subtracting their ordinals cancels the common one.

For two consecutive dates, the later ordinal is exactly one greater. At a year boundary, all completed months of the old year and the first day of the new year still differ by one. At February 29 in a leap year, the extra day exists in the month table and is counted exactly once.

**Take an absolute difference**

The input order does not promise that `date1` is earlier. `abs(calcDays(date1) - calcDays(date2))` returns a nonnegative distance in either order.

Both ordinal calculations count exactly the complete calendar days preceding the date plus one shared offset. Their difference is therefore exactly the number of day transitions between the dates. Equal dates have equal ordinals and return zero.

No date-time library, time zone, or clock conversion is involved. These are pure Gregorian calendar dates, so daylight-saving changes and local time zones are irrelevant.

As a boundary trace, compare 2020-02-28 with 2020-03-01. Both calculations include the same complete years. The March ordinal includes January’s thirty-one days and February’s twenty-nine days, while the February ordinal includes January plus day twenty-eight. Their difference is two, accounting for February 29 and the transition to March 1. In 2019, the analogous difference is one because February has only twenty-eight days.

## Complexity detail

For a date in year $Y$, `calcDays` loops through $Y - 1971$ complete years and at most eleven months. Under the stated fixed range from 1971 through 2100, both loop bounds are capped constants, so each conversion and the whole method run in $O(1)$ time.

If the year range were allowed to grow without a fixed bound, the exact loop-based implementation would take $O(Y-1971)$ time per date. A closed formula for leap years before $Y$ could make that generalized version constant-time.

The method uses a twelve-element month list, parsed scalars, and counters. Twelve is fixed, so auxiliary space is $O(1)$. The short list is recreated for each month-length call but never grows with the date range.

## Alternatives and edge cases

- **Standard date library:** Parse both dates and subtract date objects. It is concise, but an interview may expect the calendar arithmetic to be implemented directly.
- **Closed-form ordinal:** Count ordinary days plus leap years using divisions by four, one hundred, and four hundred. This avoids the year loop and stays $O(1)$ for unbounded years.
- **Simulate day by day:** Correct but unnecessarily slow for large date ranges and much more prone to month-boundary mistakes.
- **Equal dates:** Their ordinal difference is zero.
- **Reverse input order:** The absolute value makes the result symmetric.
- **Leap day:** February 29 is counted only when the year helper returns true.
- **Century boundary:** A year such as 2100 is not a leap year because it is not divisible by four hundred.
- **January date:** The month loop is empty, and only complete years plus the day are counted.
- **December date:** All eleven earlier month lengths are included before adding the day.
- **One-based ordinal:** Mapping the reference date to one instead of zero does not affect differences.
- **Valid-date guarantee:** The code does not reject malformed strings or impossible dates; the contract guarantees correct formatting and calendar validity.
- **Reference-year inclusion:** The year loop excludes the target year and the month loop supplies only its completed months, preventing the current year’s days from being counted twice.
