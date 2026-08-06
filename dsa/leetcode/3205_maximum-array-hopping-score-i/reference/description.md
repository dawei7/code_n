## Description

Start at index `0` of `nums` and reach its final index through one or more forward hops. From a current index `i`, a hop may land at any index `j` with $j>i$.

Landing at `j` earns `(j - i) * nums[j]` points. The value at the starting index does not itself earn points; every hop is weighted by the value at its destination.

Choose the increasing sequence of visited indices that maximizes the total score, and return that maximum.
