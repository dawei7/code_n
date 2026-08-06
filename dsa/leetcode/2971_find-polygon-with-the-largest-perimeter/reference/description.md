## Description

You are given an array of **positive** integers `nums` of length `n`.

A **polygon** is a closed plane figure that has at least `3` sides. The **longest side** of a polygon is **smaller** than the sum of its other sides.

Conversely, if you have `k` (`k >= 3`) **positive** real numbers `a_1`, `a_2`, `a_3`, ..., `a_k` where `a_1 <= a_2 <= a_3 <= ... <= a_k` **and** `a_1 + a_2 + a_3 + ... + a_k-1 > a_k`, then there **always** exists a polygon with `k` sides whose lengths are `a_1`, `a_2`, `a_3`, ..., `a_k`.

The **perimeter** of a polygon is the sum of lengths of its sides.

Return *the **largest** possible **perimeter** of a **polygon** whose sides can be formed from* `nums`, *or* `-1` *if it is not possible to create a polygon*.
