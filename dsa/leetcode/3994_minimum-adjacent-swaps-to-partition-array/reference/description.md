## Description

You are given an integer array `nums` and two integers `a` and `b` with `a < b`.

Call an array **good** when it can be divided into three contiguous parts, in this order:

1. every value in the first part is less than `a`;
2. every value in the second part belongs to the inclusive range `[a, b]`; and
3. every value in the third part is greater than `b`.

Any of these three parts may be empty.

One adjacent swap exchanges two neighboring elements of `nums`. Determine the minimum number of adjacent swaps needed to make the array good. Because this count can be large, return it modulo $10^9+7$.
