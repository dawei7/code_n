## General
**Turn classification into two counting problems:** Every confusing number is rotatable, but a rotatable number is not confusing when its rotation equals itself. Therefore the answer is

$$
\text{rotatable values at most } n - \text{unchanged rotations at most } n.
$$

This avoids generating nearly two million rotatable candidates at the legal maximum.

**Count all rotatable values by their decimal prefix:** A positive length-$L$ value made only from `0`, `1`, `6`, `8`, and `9` has four choices for its first digit and five choices thereafter. All lengths shorter than $D$ therefore contribute $4 \cdot 5^{L-1}$ each.

For length $D$, scan the digits of `n` from left to right. At each position, count smaller permitted digits and multiply by $5$ raised to the number of remaining positions. Those choices produce complete valid numbers below the current prefix. If the corresponding digit of `n` is not permitted, no equal-prefix continuation exists and the count is finished. Otherwise continue, adding `n` itself after the final position.

**Count unchanged rotations from only the left half:** A number unchanged by rotation is determined by its left half. Its first digit has choices `1`, `6`, `8`, or `9`; an interior paired position has all five rotatable choices; and the center of an odd-length number must be `0`, `1`, or `8`. The right half is forced by reversing and mapping the chosen left-half digits.

Multiply these choice counts to include every shorter length. For length $D$, rank valid left halves against the corresponding prefix of `n` in the same way as the rotatable count. If that entire prefix is legal, mirror it through `ROTATION` and include the resulting number only when it does not exceed `n`.

Every rotatable integer belongs to exactly one length and one decimal prefix counted by the first procedure. Every unchanged rotation belongs to that set and is counted exactly once by its unique determining left half. Subtracting the second set from the first consequently leaves precisely the valid rotations whose numeric value changes.

## Complexity detail
Let $D$ be the number of decimal digits in `n`. Counting all shorter unchanged lengths uses a triangular number of position-choice operations, and ranking the current left half recomputes at most $D$ remaining-choice products. The total time is $O(D^2)$. The decimal strings and mirrored candidate use $O(D)$ auxiliary space.

## Alternatives and edge cases
- **Generate every rotatable number:** A depth-first traversal over the five valid digits is mathematically correct, but it visits about 1.95 million candidates at `n = 10^9` and exceeds cOde(n)'s execution-step guard.
- **Scan every integer:** Rotating every value from `1` through `n` takes $O(nD)$ time and spends most work rejecting invalid digits.
- **Generate unchanged rotations explicitly:** Constructing all left halves is much smaller than generating all rotatable values, but prefix counting obtains the same total using only decimal positions.
- **Leading zeros after rotation:** Numeric comparison naturally treats `0008` as `8`; leading zeros are never allowed in the original number.
- **Unchanged values:** `1`, `8`, `11`, and `69` are rotatable but must be subtracted.
- **Middle digit:** An odd-length unchanged rotation can use only `0`, `1`, or `8` at its center because `6` and `9` swap.
- **Inclusive maximum:** `1_000_000_000` is rotatable and changes to `1`, so the upper endpoint contributes when `n` reaches the legal maximum.
