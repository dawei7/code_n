## Description

You are given a 2D integer array `intervals`, where `intervals[i] = [l_i, r_i, weight_i]`. Interval `i` starts at position `l_i` and ends at `r_i`, and has a weight of `weight_i`. You can choose *up to* 4 **non-overlapping** intervals. The **score** of the chosen intervals is defined as the total sum of their weights.

Return the <span data-keyword="lexicographically-smaller-array">lexicographically smallest</span> array of at most 4 indices from `intervals` with **maximum** score, representing your choice of non-overlapping intervals.

Two intervals are said to be **non-overlapping** if they do not share any points. In particular, intervals sharing a left or right boundary are considered overlapping.
