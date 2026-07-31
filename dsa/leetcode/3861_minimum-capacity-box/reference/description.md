## Description

You are given an integer array `capacity`, where `capacity[i]` is the capacity
of the box at index `i`, and an integer `itemSize` describing one item's size.
A box can store the item exactly when its capacity is at least `itemSize`.

Among all boxes that can store the item, select one whose capacity is minimum.
The objective concerns the capacity value, not merely the first box that fits.
If the same minimum eligible capacity occurs at several indices, select its
smallest index.

Return the chosen box index. If every capacity is smaller than `itemSize`, no
box is eligible and the required result is `-1`.
