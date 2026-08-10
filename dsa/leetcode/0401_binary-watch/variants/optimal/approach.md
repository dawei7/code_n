## General

**Enumerate the complete legal watch domain**

The watch does not describe an unbounded search problem. A displayed hour can only be `0` through `11`, and a displayed minute can only be `0` through `59`. There are exactly

$$
12\cdot60=720
$$

legal time values.

The exact solution checks every one of those 720 pairs. For each hour `i` and minute `j`, it counts the lit bits in their binary representations. If the combined count equals `turnedOn`, it formats and includes the time.

Because the domain size is fixed by the physical watch rather than by a growing input, exhaustive enumeration is both simple and optimal for this contract.

**Why binary one-bits correspond to lit LEDs**

The four hour LEDs represent binary place values, and the six minute LEDs do the same. A bit equal to one means its LED is on. Therefore the number of lit hour LEDs is the population count—the number of one bits—of the hour value. The minute count is calculated identically.

For example, hour `4` is binary `0100`, so one hour LED is on. Minute `51` is binary `110011`, so four minute LEDs are on. Time `4:51` uses five lit LEDs in total.

Leading zero bits do not need to be written by `bin`. Omitting them does not change the one-bit count because every omitted bit is zero.

**How the exact one-bit expression works**

The filter is

```text
(bin(i) + bin(j)).count('1') == turnedOn
```

`bin(i)` and `bin(j)` produce strings such as `"0b100"` and `"0b110011"`. Concatenating them joins the two representations. Counting character `'1'` in the combined string equals the sum of the separate one-bit counts.

The `0b` prefixes contain no digit `1`, so they do not affect the count. Mathematically,

$$
\operatorname{ones}(i)+\operatorname{ones}(j)
=
\operatorname{count}_{\texttt{'1'}}(\texttt{bin}(i)+\texttt{bin}(j)).
$$

Calling `i.bit_count() + j.bit_count()` would express the same calculation without strings, but the exact source’s expression is correct over these bounded values.

**The loops generate only valid times**

`range(12)` produces hours `0` through `11`. `range(60)` produces minutes `0` through `59`. The method never generates invalid bit patterns corresponding to hours `12` through `15` or minutes `60` through `63`, even though the physical LED groups could represent them.

This is an important advantage of enumerating values rather than blindly enumerating all ten-bit masks: validity is enforced by the loop ranges themselves.

Every legal displayed time corresponds to exactly one `(i, j)` pair, so no possible answer is missed and no answer is duplicated.

**Formatting is part of correctness**

The expression

```text
'{:d}:{:02d}'.format(i, j)
```

formats the hour as an ordinary decimal integer and the minute as exactly two decimal digits.

- `{:d}` gives `0`, `1`, ..., `11` without an hour-leading zero;
- `{:02d}` pads a one-digit minute with one leading zero while leaving two-digit minutes unchanged.

Thus hour `4`, minute `5` becomes `"4:05"`, not `"04:05"` and not `"4:5"`.

The colon is included between the two formatted fields, so every output string follows the required watch notation.

**Tracing `turnedOn = 1`**

Exactly one bit may be set. For hour zero, valid minutes with one set bit are powers of two that fit below 60: `1`, `2`, `4`, `8`, `16`, and `32`. These yield `0:01`, `0:02`, `0:04`, `0:08`, `0:16`, and `0:32`.

For minute zero, valid hours with one set bit are `1`, `2`, `4`, and `8`, yielding `1:00`, `2:00`, `4:00`, and `8:00`.

Any time with both a nonzero one-bit hour and a nonzero one-bit minute has at least two lit LEDs and is excluded. The list comprehension produces exactly the ten expected possibilities.

**Why `turnedOn = 9` has no answer**

Although the watch physically has ten LEDs, valid display ranges exclude some high-bit combinations.

Among hours `0..11`, the maximum number of one bits is three. Among minutes `0..59`, the maximum is five. Therefore a valid time can light at most eight LEDs. Requests for nine or ten lit LEDs yield an empty list naturally; no explicit early return is required.

**A correctness argument**

For every returned string, its loop values are a legal hour and minute, the filter proves their combined one-bit count equals `turnedOn`, and formatting matches the required representation. Therefore every output is valid.

Conversely, consider any valid time using exactly `turnedOn` LEDs. Its hour appears once in `range(12)` and its minute appears once in `range(60)`. At that pair, the binary one-bit count equals the number of lit LEDs, so the filter accepts it and the method includes its correctly formatted string. Therefore every valid answer is returned.

## Complexity detail

The nested loops always examine exactly 720 pairs. Binary representations contain at most four hour bits and six minute bits, so their conversion and counting take bounded constant time. Runtime is therefore $O(1)$ with respect to `turnedOn`.

The list comprehension allocates the required answer strings. Excluding output storage, only bounded temporary binary and formatted strings are used, so auxiliary space is $O(1)$. Even if output is counted, there are at most 720 legal times of bounded string length, which is still constant under this fixed-domain problem.

This package uses a bounded-domain complexity certificate because `turnedOn` has only eleven legal values and the watch has only 1024 raw LED masks. There is no meaningful asymptotic input scale beyond this fixed device.

## Alternatives and edge cases

- **Enumerate all 1024 LED masks:** Split each ten-bit mask into four hour bits and six minute bits, reject hour values at least 12 or minute values at least 60, and keep masks with the requested population count. This is also constant time but requires explicit validity checks.

- **Generate combinations of lit LEDs:** Choose exactly `turnedOn` positions among ten LEDs, convert them to hour/minute values, and reject invalid displays. It may examine fewer states for some counts but is more complicated than 720 direct checks.

- **Use `int.bit_count`:** `i.bit_count() + j.bit_count()` avoids binary strings and states the population-count operation directly. It is an equivalent implementation detail.

- **`turnedOn = 0`:** Only hour zero and minute zero have no one bits, so the result is `"0:00"`.

- **`turnedOn = 9` or `10`:** No legal time has that many lit bits, so the result is empty.

- **Invalid raw LED patterns:** The value ranges prevent hours `12..15` and minutes `60..63` from ever entering the result.

- **Minute leading zero:** The `02d` format field guarantees values below ten use two digits.

- **Hour leading zero:** The ordinary decimal field deliberately does not pad the hour.

- **Any output order:** Nested iteration orders times by hour and then minute, but the contract allows this or any other order.

- **No duplicate times:** Each legal hour-minute pair is visited once, and one pair has one unique display string.
