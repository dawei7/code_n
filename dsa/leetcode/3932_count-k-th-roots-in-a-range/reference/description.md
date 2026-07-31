## Description

Three integers `l`, `r`, and `k` define an inclusive range and a positive exponent. An integer `y` is a perfect $k$th power when at least one integer base `x` satisfies $y=x^k$.

Count the distinct values of `y` between `l` and `r`, including both endpoints, that have this form. The requested objects are the powered values, not the possible bases: when $k$ is even, the bases $x$ and $-x$ produce the same nonnegative value and must not be counted twice.

The range itself is nonnegative. Consequently, every relevant powered value can be represented by a nonnegative base, including $0^k=0$ when zero lies in the range.
