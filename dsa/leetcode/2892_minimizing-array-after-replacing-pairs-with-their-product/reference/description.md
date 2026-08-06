## Description

You are given an integer array `nums` and a positive integer `k`. In one operation, choose two adjacent values $x$ and $y$ whose product satisfies $xy \le k$. Remove both values and insert the single value $xy$ in their position, reducing the array length by one. The new product can participate in later operations with either adjacent neighbor.

Perform this operation any number of times, including zero times. Return the smallest array length that can be reached while respecting the product limit at every merge.
