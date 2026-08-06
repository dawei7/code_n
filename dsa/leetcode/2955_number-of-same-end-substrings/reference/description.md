## Description

You are given a 0-indexed lowercase English string `s` and an array `queries`.
Each query `[left, right]` selects the inclusive substring from index `left`
through index `right`.

A nonempty string is same-end when its first and last characters are equal.
This includes every single-character string, since its two ends are the same
position. For each selected range, count all contiguous substrings lying
entirely inside that range that are same-end. Return the counts in the same
order as the input queries.
