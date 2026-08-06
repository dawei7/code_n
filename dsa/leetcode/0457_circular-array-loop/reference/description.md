## Description

Consider a game played on a circular array `nums` of nonzero integers. From position `i`, the value `nums[i]` determines the mandatory move:

- A positive value moves forward by `nums[i]` positions.
- A negative value moves backward by `abs(nums[i])` positions.

Movement wraps around both ends of the array: moving forward past the last position continues at the first, and moving backward past the first continues at the last.

A cycle is a repeating sequence of positions `seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...` produced by those movement rules. It is valid only when $k > 1$ and every jump on the cycle has the same direction—either all values are positive or all are negative.

Return `true` if any valid cycle exists; otherwise, return `false`.
