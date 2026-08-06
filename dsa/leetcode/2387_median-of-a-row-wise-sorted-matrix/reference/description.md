## Description

Given an $m \times n$ integer matrix `grid`, treat all of its entries as one collection and return its median. Both dimensions are odd, so the matrix contains an odd number of values and the median is the single middle value after global ordering.

Each row is independently sorted in non-decreasing order, but values in different rows have no ordering relationship. The solution must exploit that row structure and run in strictly less than $O(mn)$ time rather than reading and sorting every entry.
