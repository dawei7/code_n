## Description

Given an $m\times n$ integer matrix `grid` and a non-negative threshold $k$, count the rectangular submatrices whose largest element is at most $k$. A submatrix is determined by inclusive row bounds and inclusive column bounds and contains every cell inside that rectangle; rows or columns cannot be skipped.

Within every selected row, the values across the selected columns must be in non-increasing order from left to right. Equality is allowed, and no ordering relation is required between different rows. Return the total number of rectangles satisfying both the threshold condition and the per-row ordering condition.
