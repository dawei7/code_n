## Description

You receive an array `nums` whose entries are only `1`, `2`, or `3`, together with a same-length binary array `locked`. The array is considered sortable when it can be put into non-decreasing order using a restricted adjacent swap.

Indices `i` and `i + 1` may be swapped only when `nums[i] - nums[i + 1] = 1` and `locked[i] = 0`. In one operation, any index may be permanently unlocked by setting its lock value to zero. Find the minimum number of unlock operations that make sorting possible, or return `-1` when even unlocking every index cannot suffice.
