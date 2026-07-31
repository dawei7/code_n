## Description

You are given a binary string `s` and positive integers `encCost` and
`flatCost`. A character `"1"` marks a sensitive element, whereas `"0"` marks
a non-sensitive element. The entire string begins as one segment and may be
partitioned further by applying the permitted split rule to current segments.

For a segment of length `L` containing `X` sensitive elements, its unsplit cost
is `flatCost` when `X = 0`. If `X > 0`, that segment instead costs
`L * X * encCost`.

Only an even-length segment may be split, and such a split must produce its two
contiguous halves of equal length. The split segment's contribution is then
replaced by the sum of the two resulting segments' costs; either half may be
split again when its own length is even.

Return the minimum total cost among all partitions reachable through these
equal-halving decisions.
