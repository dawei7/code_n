## Description

You are given an `m x n` integer matrix `grid`. A valid selection takes
exactly one cell value from each of its `m` rows. The chosen column does not
need to be the same from one row to another.

Choices in different rows are independent, but every selected value
participates in one combined bitwise OR. Consequently, a bit is set in the
result whenever at least one chosen value contains that bit, while it remains
zero only when all chosen values omit it.

Return the smallest possible integer value of that OR over all valid selections.
