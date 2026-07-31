## Description

You are given an integer array `nums`.

A tuple `(i, j, k)` is called good when its three indices are distinct and the values at those positions are equal: `nums[i] == nums[j] == nums[k]`.

The distance of a good tuple is

$$
\lvert i-j \rvert + \lvert j-k \rvert + \lvert k-i \rvert,
$$

where each pair contributes its absolute index difference.

Return the smallest distance among all good tuples. If the array contains no good tuple, return `-1`.
