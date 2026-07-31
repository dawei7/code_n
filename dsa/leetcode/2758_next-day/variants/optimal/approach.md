## General

JavaScript's `Date` object already knows the lengths of months and the Gregorian leap-year rules. The remaining choice is which calendar fields to use. An ISO date-only string such as `"2014-06-20"` represents a UTC date, so the method advances the receiver through `getUTCDate()` and `setUTCDate(...)`. This avoids making the answer depend on the machine's local time zone.

Create a new `Date` from the receiver so the method has no reason to mutate the original object. Increase the copied object's UTC day-of-month by one. `setUTCDate` normalizes an out-of-range day automatically: the day after the last day of a month becomes day one of the next month, and the day after December 31 enters the following year. The same normalization handles February 29 precisely when the year is a leap year.

Finally, `toISOString()` expresses the normalized instant in UTC. Its first ten characters are exactly the required `YYYY-MM-DD` portion. Thus the output names the calendar day immediately after the receiver while remaining independent of local daylight-saving or time-zone settings.

## Complexity detail

Each invocation makes one fixed-size `Date` copy, performs one calendar-field update, creates one ISO representation, and extracts a fixed-width prefix. These operations do not scale with the date's numeric value, so the time complexity is $O(1)$ and the auxiliary space complexity is $O(1)$.

The certificate uses asymptotic optimality because every call must return one value, giving an $\Omega(1)$ lower bound, while the accepted implementation achieves the matching $O(1)$ upper bound. There is no meaningful legal input-size axis on which to calibrate a slower runtime class.

## Alternatives and edge cases

- **Add 86,400,000 milliseconds:** This can work for UTC-midnight inputs, but reasoning in calendar fields states the intent more directly and avoids tying the method to elapsed-time behavior around local daylight-saving transitions.
- **Use local `getDate` and `setDate`:** The result can depend on the runtime's time zone because ISO date strings are interpreted in UTC; UTC accessors preserve the source date's calendar meaning.
- **Month and year rollover:** `setUTCDate` normalizes values beyond the current month's last day, so no month-length table is needed.
- **Leap years:** Native date normalization includes February 29 in years such as 2020 and skips it in non-leap centuries such as 2100.
- **Receiver preservation:** Advancing a copy leaves the original `Date` unchanged, preventing a surprising side effect from a formatting helper.
