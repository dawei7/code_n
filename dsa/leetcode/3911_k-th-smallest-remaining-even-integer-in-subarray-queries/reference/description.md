## Description

The integer array `nums` is strictly increasing. Each query `[l, r, k]` selects the non-empty subarray from index `l` through index `r`, inclusive.

Begin with the infinite sequence of positive even integers `2, 4, 6, 8, ...`. For the current query, remove every sequence value that occurs in the selected subarray; odd subarray values have no effect because they are not members of that sequence. Find the $k$-th smallest even integer that remains. Return the answers in query order.
