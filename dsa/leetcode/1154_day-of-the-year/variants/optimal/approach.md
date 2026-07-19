## General
**Separate the calendar fields.** Splitting `date` on `"-"` yields the numeric year, month, and day. The desired ordinal consists of the days in every complete month before the given month plus the current day number.

**Give February the correct length.** In the Gregorian calendar, a year is a leap year when it is divisible by $400$, or when it is divisible by $4$ but not by $100$. This distinction makes 2000 a leap year but 1900 a common year. Start with the twelve ordinary month lengths and set February to 29 only when that condition holds.

Summing `month_days[:month - 1]` includes exactly the completed months. Adding `day` then counts the days already reached in the current month, including the given date itself. Because the input is guaranteed valid, no normalization or date validation is needed.

## Complexity detail
The input always contains 10 characters, and the calculation examines at most 12 month lengths. Both limits are fixed independently of any scalable input quantity, so parsing and summation take $O(1)$ time. The twelve-element month table and parsed fields also occupy $O(1)$ space.

## Alternatives and edge cases
- **Use a date library:** A standard-library date parser can compute the ordinal, but it introduces an unnecessary dependency on library formatting and timezone-free date behavior for a small fixed calculation.
- **Use cumulative month offsets:** Precomputed offsets also give a constant-time result, provided one extra day is added after February in leap years.
- **Century years:** Divisibility by $100$ cancels the usual divisible-by-$4$ rule unless the year is also divisible by $400$.
- **January dates:** There are no preceding months, so the answer is the numeric day directly.
- **Leap day and dates after February:** February 29 is valid only in leap years, and every later date in such a year has an ordinal one greater than the corresponding common-year date.
- **Year boundaries:** January 1 returns $1$; December 31 returns $365$ in a common year and $366$ in a leap year.
