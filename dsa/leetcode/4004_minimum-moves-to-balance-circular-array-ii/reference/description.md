## Description

The integer array `balance` describes people arranged in a circle. Entry `balance[i]` is person `i`'s net balance, which may initially be positive, zero, or negative. Person `0` and person `n - 1` are neighbors, just as every other pair of consecutive indices is.

One move transfers exactly one unit of balance from any person to either the left neighbor or the right neighbor. The sender loses one unit and the chosen neighbor gains one unit. A unit may cross several neighbor edges through several moves, with each crossed edge counted separately.

Determine the minimum number of moves required to make every person's balance non-negative. Extra positive balance does not need to be moved or consumed. If the total balance is insufficient to eliminate all negative entries, return `-1`.
