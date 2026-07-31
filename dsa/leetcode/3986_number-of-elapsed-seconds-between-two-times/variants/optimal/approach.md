## General

A clock reading has three place values. If its components are hours $h$, minutes $m$, and seconds $s$, then the number of seconds that have passed since `00:00:00` is

$$
3600h + 60m + s.
$$

Parse both input strings into those three components and evaluate this expression for each one. The source guarantees that `endTime` is not earlier than `startTime` on the same day, so subtracting the start total from the end total directly gives the requested nonnegative duration. Both totals use the same origin, which is why all time before `startTime` cancels from the difference.

## Complexity detail

Each input is exactly eight characters long and contains exactly three numeric fields. Parsing and combining those fixed-size fields therefore takes $O(1)$ time. The three parsed integers and two totals occupy $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Parse fixed slices:** Reading `time[0:2]`, `time[3:5]`, and `time[6:8]` avoids splitting the string and has the same constant bounds, but relies more directly on the fixed layout.
- **Use a date-time library:** A standard-library parser can represent the same conversion, but introduces unnecessary configuration and object creation for two guaranteed-valid time-only strings.
- **Equal times:** When both inputs are identical, their seconds-since-midnight totals are equal and the answer is `0`.
- **No overnight wrap:** `endTime` is guaranteed not to be earlier than `startTime`, so a negative difference must not be adjusted by adding one day.
- **Leading zeroes:** Components such as `"01"` and `"00"` are ordinary decimal fields; they do not change the place-value calculation.
