## Description

An integer array `nums` was sorted in non-decreasing order and may contain duplicate values. Before reaching the function, it was rotated at an unknown pivot index `k`, where $0 \le k < \lvert\texttt{nums}\rvert$. The rotated order is `nums[k], nums[k + 1], ..., nums[n - 1], nums[0], ..., nums[k - 1]`.

For example, rotating `[0, 1, 2, 4, 4, 4, 5, 6, 6, 7]` at pivot `5` can produce `[4, 5, 6, 6, 7, 0, 1, 2, 4, 4]`.

Given the rotated array and `target`, return whether the target occurs in `nums`. Minimize the overall number of operations as much as possible.
