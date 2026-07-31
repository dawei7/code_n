## Description

You are given an integer array `nums` and an integer `k`. Begin with `val = 1`, then process the elements of `nums` from left to right.

At every index `i`, choose exactly one action:

- Multiply `val` by `nums[i]`.
- Divide `val` by `nums[i]`.
- Leave `val` unchanged.

After every array element has received one choice, compare the final rational value of `val` with `k`. Count the distinct complete sequences of choices for which the two values are exactly equal, and return that count.
