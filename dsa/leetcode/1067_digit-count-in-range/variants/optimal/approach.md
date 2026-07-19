## General
**Reduce the interval to two prefixes:** Define a helper that counts occurrences of `d` from 1 through `n`. The required inclusive-range result is `count_up_to(high) - count_up_to(low - 1)`, so each bound can be processed independently.

**Analyze one decimal position:** For a position with place value $f$, split `n` into the digits above it, the current digit, and the value below it. For nonzero `d`, every complete higher-digit cycle contributes $f$ occurrences. The partial cycle contributes zero, $f$, or `lower + 1` depending on whether the current digit is below, above, or equal to `d`.

**Exclude leading zeros:** The same cycle formula would count zero in positions that a shorter number does not write. When `d == 0`, remove one full higher-digit cycle at every position. If the higher part is zero, that position has not yet appeared in any number and contributes nothing.

Each positive integer up to `n` belongs to exactly one complete or partial cycle at every written position, so the positional contributions count each occurrence once. Subtracting the two prefix totals removes precisely the values below `low`.

## Complexity detail
The place value is multiplied by ten after each iteration, so each prefix helper examines one position per decimal digit. Processing `high` and `low - 1` therefore takes $O(\log H)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Enumerate the range:** Convert every integer to a string and count characters. It is simple but takes time proportional to the range size and number of written digits.
- **Digit DP:** A tight-prefix dynamic program generalizes to richer digit constraints, but positional arithmetic is smaller and constant-space for counting one digit.
- **Digit zero:** Leading zeros are not part of ordinary decimal notation and must never be counted.
- **Single-number range:** Prefix subtraction still returns the number of occurrences within that one representation.
- **Repeated digit in one number:** Every matching decimal position contributes separately.
- **Power-of-ten boundary:** The new highest position is handled when its place value first becomes no greater than the bound.
- **Prefix below one:** `count_up_to(0)` is zero, which handles `low == 1` directly.
