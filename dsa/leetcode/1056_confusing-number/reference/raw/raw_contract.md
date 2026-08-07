## Function Contract

**Inputs**

- `n`: a non-negative integer to rotate.

The complete decimal representation is rotated by $180$ degrees. Its digit positions reverse, each digit must have a valid rotated image, and leading zeros in the rotated representation are ignored when interpreting the result as an integer.

Let $D$ be the number of decimal digits in `n`, with zero having one digit.

**Return value**

- `true` when the rotation is valid and its numeric value is different from `n`; otherwise, `false`.
