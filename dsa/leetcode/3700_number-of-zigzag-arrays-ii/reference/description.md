## Description

Given integers `n`, `l`, and `r`, count the arrays of length `n` whose values all belong to the inclusive range `[l, r]` and which satisfy both ZigZag rules:

- neighboring elements must be different; and
- no three consecutive elements may form a strictly increasing sequence or a strictly decreasing sequence.

Return the number of valid ZigZag arrays modulo $10^9+7$.

A sequence is **strictly increasing** when every element after the first is greater than the element immediately before it. It is **strictly decreasing** when every element after the first is smaller than its immediate predecessor.
