## Description

A very large 0-indexed integer array `nums` has the property that every value's
occurrences are adjacent. Equivalently, each distinct value appears in one
contiguous run and can never reappear after a different value. Partition the
array into maximal blocks of equal numbers and return the number of blocks.

The source-native input is a `BigArray`, not a materialized array. Its
`size()` method returns the length and `at(index)` returns one value. The array
may contain up to $10^{15}$ elements, so the solution must locate block
boundaries with a small number of queries rather than inspect every index.
