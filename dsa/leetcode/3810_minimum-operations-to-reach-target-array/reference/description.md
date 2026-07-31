## Description

You are given two integer arrays, `nums` and `target`, of the same length. The current contents of `nums` must be changed into the desired array `target`.

You may perform the following operation any number of times, including zero:

1. Choose an integer `x`.
2. In the current `nums`, identify **all** maximal contiguous segments whose elements equal `x`. A segment is maximal when it cannot be extended one position to the left or right while keeping every element equal to `x`.
3. Update every identified segment simultaneously. For each of its indices `i`, assign `nums[i] = target[i]`.

Return the minimum number of operations needed to make `nums` equal to `target`.
