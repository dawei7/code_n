## Description

A **confusing number** becomes a different valid number when its display is rotated by $180$ degrees. Rotating the display reverses the positional order of its digits while transforming each digit individually.

Only five digits remain valid under this rotation:

- `0`, `1`, `6`, `8`, and `9` become `0`, `1`, `9`, `8`, and `6`, respectively.
- `2`, `3`, `4`, `5`, and `7` become invalid.

Leading zeros in the rotated display do not affect its numeric value. For example, rotating `8000` produces the display `0008`, which represents the number `8`.

Given an integer `n`, determine whether every rotated digit is valid and the resulting number differs from `n`.
