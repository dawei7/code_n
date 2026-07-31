## Description

You are given two integers, `l` and `r`.

Call an integer **good** when its decimal digits form a strictly monotone sequence: the digits must be either strictly increasing throughout or strictly decreasing throughout. Every one-digit positive integer is good.

An integer is **fancy** when either the integer itself is good or the sum of its decimal digits is good.

Return the number of fancy integers in the inclusive range `[l, r]`.

A digit sequence is strictly increasing when every digit after the first is strictly greater than the digit immediately before it.

A digit sequence is strictly decreasing when every digit after the first is strictly less than the digit immediately before it.
