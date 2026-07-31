## Description

Given an integer array `nums` and an integer `k`, choose a non-empty subsequence at indices $i_1<i_2<\dots<i_m$. Every two consecutive selected indices must be separated by at least `k`, so $i_{t+1}-i_t\ge k$.

The chosen values must alternate strictly: they may begin with either an increase or a decrease, but every later comparison must reverse the preceding direction. Thus the pattern is either `nums[i1] < nums[i2] > nums[i3] < ...` or `nums[i1] > nums[i2] < nums[i3] > ...`. Equal consecutive selected values are not allowed. A one-element subsequence is strictly alternating by definition.

Its score is the sum of all selected values. Return the greatest score among all valid subsequences.
