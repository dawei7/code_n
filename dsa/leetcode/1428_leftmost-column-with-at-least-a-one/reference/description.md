## Description

A row-sorted binary matrix contains only `0` and `1`, and each individual row is sorted in non-decreasing order. Thus, within a row, every `0` precedes every `1`; the rows themselves do not need to be ordered relative to one another.

The matrix is hidden behind a read-only `BinaryMatrix` interface. `get(row, col)` reveals one zero-based cell, while `dimensions()` returns `[rows, cols]`. The underlying storage must not be accessed directly. A submission that makes more than 1,000 calls to `get` is judged wrong, and attempts to bypass the interface are disallowed.

Return the zero-based index of the leftmost column containing at least one `1`. Return `-1` when the matrix has no `1`. For custom tests, the complete matrix is supplied as `mat`, but the solution still receives only the interface.
