## Description

A **confusing number** changes into a different valid number when all of its decimal digits are rotated by $180$ degrees. The digits `0`, `1`, and `8` remain `0`, `1`, and `8`; `6` becomes `9`, and `9` becomes `6`. Any occurrence of `2`, `3`, `4`, `5`, or `7` makes the rotated representation invalid.

Rotating a complete number reverses the positions of its mapped digits. Leading zeros in the result are ignored: rotating `8000` produces `0008`, which denotes `8`. A number is confusing only when its rotation is valid and its resulting numeric value differs from the original.

Given `n`, count every confusing number in the inclusive range `[1, n]`.
