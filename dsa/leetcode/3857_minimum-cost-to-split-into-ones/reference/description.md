## Description

You are given a positive integer `n`.

In one operation, select a current integer `x` and replace it with two positive integers `a` and `b` whose sum is `x`.

That operation costs `a * b`. Further operations may split either resulting part, and the total cost is the sum of the costs of every performed split.

Return the minimum total cost needed to continue until the original value has become exactly `n` separate ones.
