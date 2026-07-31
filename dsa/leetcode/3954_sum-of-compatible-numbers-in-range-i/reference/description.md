## Description

You are given two integers, `n` and `k`. Consider a positive integer `x` compatible when it meets both requirements below:

- its absolute distance from `n` is at most `k`, so `abs(n - x) <= k`;
- its bitwise AND with `n` is zero, so `(n & x) == 0`.

Return the sum of every positive compatible integer `x`.

Here, `&` is the bitwise AND operator. For any integers `i` and `j`, their absolute difference is `abs(i - j)`.
