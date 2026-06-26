"""
Description
-----------
Given a frequency array freq[1..n] (how many times
            each value 1..n appears in a multiset), find the
            value of the k-th smallest element (1-indexed).
            Use an order-statistic BIT: build BIT[i] = freq[i],
            then find the smallest index idx such that
            BIT.prefix(idx) >= k, by binary lifting on the
            BIT's bit structure (descend the BIT starting from
            the highest set bit). O(log n) per query.
            Source: https://www.geeksforgeeks.org/dsa/order-statistic-tree-using-bit/

Examples
--------
Example 1:
Input:  freq = [2, 1, 3, 0, 2], n = 5, k = 4
Output: 2 (1, 1, 2, 3, ...)

Example 2:
Input:  freq = [1, 2, 3], n = 3, k = 3
Output: 2

Example 3:
Input:  freq = [0, 0, 5], n = 3, k = 1
Output: 3
"""

def solve(freq, n, k):
    # Write your code here.
    return None
