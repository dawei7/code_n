## General

**Let MySQL format each date directly.** The source column already has SQL type `DATE`, so MySQL understands its year, month, day of month, and weekday. The query applies `DATE_FORMAT` to every row rather than manually extracting numeric fields or maintaining lookup tables for month and weekday names.

The complete format string is:

`'%W, %M %e, %Y'`.

Each percent code contributes one required component, while commas and spaces in the format string are copied literally into the result.

**Full weekday name with `%W`.** `%W` produces the weekday name such as `Monday`, `Tuesday`, or `Friday`. MySQL derives this from the actual calendar date, so the query does not need a separate weekday calculation.

The capitalized full name matches the case-sensitive sample. A different code such as `%a` would produce an abbreviation and would not satisfy the requested format.

**Full month name with `%M`.** `%M` produces `January` through `December`. This differs from `%m`, which would produce a two-digit month number, and from `%b`, which would abbreviate the name. The space after the first comma comes from the literal characters in the format string.

**Unpadded day of month with `%e`.** The example expects `August 9` rather than `August 09`. MySQL’s `%e` produces the numeric day without a leading zero. Using `%d` would pad single-digit days to two positions and would fail that visible formatting requirement.

**Four-digit year with `%Y`.** `%Y` produces the complete year such as 2022. Lowercase `%y` would produce only two digits and is therefore not interchangeable.

**Literal punctuation creates the exact sentence shape.** Combining the pieces yields:

`weekday, month day, year`.

There is a comma immediately after the weekday, one space, the month, one space, the unpadded day, a second comma, one space, and the year. `DATE_FORMAT` returns this as one string.

**Preserve the requested output column name.** `AS day` aliases the formatted expression back to `day`. The result therefore has the single column name expected by the output schema rather than an engine-generated expression label.

**Trace one row.** For `2022-04-12`, MySQL determines that the weekday is Tuesday. `%M` gives April, `%e` gives 12, and `%Y` gives 2022. Literal punctuation combines them into `"Tuesday, April 12, 2022"`.

For `2021-08-09`, the important detail is that `%e` yields nine rather than `09`, producing `"Monday, August 9, 2021"`.

**Why no `ORDER BY` is needed.** The problem permits the result table in any order. The query transforms each input row independently and does not impose an arbitrary sort. SQL does not guarantee row order without `ORDER BY`, but that is fully compatible with the contract.

**One-to-one row correspondence.** `FROM Days` supplies each input date exactly once because `day` is unique. The `SELECT` contains no filter, join, grouping, or duplicate elimination. Therefore every input row produces exactly one formatted output row, and no new date can appear.
For each source `day`, the four format specifiers retrieve exactly its full weekday name, full month name, unpadded day number, and four-digit year. The literal punctuation puts them in the required order and spacing. Aliasing labels the resulting string correctly. Because the query applies this expression to every row, the complete result satisfies the requested conversion.

**Locale assumption.** MySQL’s date-name output can depend on the session locale setting. The LeetCode environment and expected examples use English names. Under a differently configured external database, `lc_time_names` would need to be English to preserve the requested text.

## Complexity detail

Let `r` be the number of rows in `Days`. The database scans each row once and performs one bounded date-formatting operation, giving `O(r)` logical time.

The query uses no growing auxiliary relation, join, grouping table, or explicit sort. Aside from the required output strings and engine scan buffers, its logical auxiliary space is `O(1)` per processed row. The full returned table naturally occupies `O(r)` output space.

## Alternatives and edge cases

- **Manual `CASE` expressions:** Weekday and month names could be mapped manually, but this is verbose and more error-prone than built-in date formatting.
- **Concatenate extracted fields:** `DAYNAME`, `MONTHNAME`, `DAY`, and `YEAR` can be combined with `CONCAT`, but `DATE_FORMAT` states the desired pattern in one place.
- **Single-digit day:** `%e` deliberately avoids a leading zero.
- **Double-digit day:** `%e` returns the ordinary two digits without changing them.
- **Leap day:** MySQL derives the correct weekday and month information from the valid `DATE` value.
- **Different years:** `%Y` always emits the full four-digit year.
- **Case sensitivity:** Full weekday and month names have the capitalization shown in the examples under the expected English locale.
- **Any-order output:** Omitting `ORDER BY` is intentional and permitted.
- **Unique source dates:** Each appears once, and the query preserves that one-to-one relationship.
- **Null dates:** The local schema does not describe nullability; if null existed, `DATE_FORMAT` would return null for that row.
- **Session locale:** An external non-English `lc_time_names` setting would change names, so English locale is an environmental dependency.
- **Alias:** `AS day` is needed to match the requested result column name.
