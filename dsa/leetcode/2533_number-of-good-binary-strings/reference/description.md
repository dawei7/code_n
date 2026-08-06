## Description

You are given `minLength`, `maxLength`, `oneGroup`, and `zeroGroup`. A binary string is good when its length lies in the inclusive interval `[minLength, maxLength]`, every maximal block of consecutive `1` characters has length divisible by `oneGroup`, and every maximal block of consecutive `0` characters has length divisible by `zeroGroup`.

Count all distinct good binary strings and return the count modulo $10^9+7$. A missing block has size zero, which is considered a multiple of every positive group size; consequently, an all-zero or all-one string may be valid when its one present block meets the corresponding divisibility rule.
