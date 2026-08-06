## Description

Evaluate a string that represents a ternary conditional expression. The expression may contain arbitrarily nested conditionals, and every conditional uses `T` or `F` as its condition.

The expression is guaranteed to be valid. Its only characters are the digits `0` through `9`, `?`, `:`, `T`, and `F`; every numeric value is a single digit. As in the usual ternary operator, conditionals associate from right to left. For example, `F?1:T?4:5` means `F?1:(T?4:5)`.

Return the value produced by evaluating the complete expression. The result is always one character: a digit, `T`, or `F`.
