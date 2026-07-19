## General
**Map each date to one ordinal.** Parse its year, month, and day. Count all days in complete years before the given year: $365(y-1)$ ordinary days, plus one for every multiple of $4$, minus multiples of $100$, plus multiples of $400$. This inclusion-exclusion exactly implements the Gregorian leap-year rule.

Add the fixed cumulative number of days before the current month, add one more when the date is after February in a leap year, and finally add the day of the month. The resulting ordinal increases by exactly one between consecutive valid dates.

**Subtract on a shared scale.** Both dates use the same arbitrary ordinal origin, so subtracting their ordinals cancels that origin. Taking the absolute value makes the result independent of input order and yields zero for identical dates.

## Complexity detail
Parsing fixed-width components and evaluating a fixed number of arithmetic operations takes $O(1)$ time. The month-prefix constants and scalar date fields require $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Standard date library:** Parse both dates and subtract native date objects. This is concise when the runtime's calendar semantics and accepted imports are known.
- **Advance one day at a time:** Simulate calendar transitions until the later date is reached. It is correct but takes $O(D)$ time for a $D$-day gap.
- **Leap-day boundary:** February 28 to March 1 spans two days in a leap year and one otherwise.
- **Century exception:** Year 2100 is divisible by $100$ but not $400$, so it is not a leap year.
- **Reverse order:** Apply absolute value after ordinal subtraction rather than assuming `date1` is earlier.
- **Same date:** Equal ordinals correctly produce zero.
