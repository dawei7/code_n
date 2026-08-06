## Description

Write a JavaScript generator function that accepts a nonnegative integer `n` and yields the factorial sequence through `n!`. For positive `n`, the sequence contains `1!`, `2!`, and every subsequent factorial up to `n!`, in that order. Each value is produced on the next advancement of the generator.

Factorial multiplication follows $i! = i \cdot (i - 1)!$. The special input `n = 0` must still yield one value, because $0!$ is defined as $1$; for positive inputs, do not emit a separate `0!` entry before `1!`.
