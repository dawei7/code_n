## Description

You are given a positive-integer array `nums`. One operation selects any single element and changes only that element in one of the following ways:

- multiply it by an integer factor $k \ge 2$; or
- divide it by an integer factor $k$ when $2 \le k < \texttt{nums[i]}$ and `nums[i]` is divisible by $k$.

The chosen factor may differ between operations and between elements. Determine the minimum total number of operations needed to make every array element equal to the same positive integer. The final common value is not specified in advance.
