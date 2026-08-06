## Function Contract

**Input**

- `n`: the positive inclusive upper bound.

The complete rotation map is:

- `0` becomes `0`.
- `1` becomes `1`.
- `6` becomes `9`.
- `8` becomes `8`.
- `9` becomes `6`.

Digits `2`, `3`, `4`, `5`, and `7` have no valid rotated form. When a valid number is rotated, reverse the digit positions, apply the map, discard any leading zeros in the result, and compare the resulting integer with the original.

Let $D$ be the number of decimal digits in `n`.

**Return value**

- The number of integers in `[1, n]` whose rotated value is valid and different from the original integer.
