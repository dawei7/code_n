"""Solution for fenwick_07: K-th Smallest (Order-Statistic BIT).


            Given a frequency array freq[1..n] (how many times
            each value 1..n appears in a multiset), find the
            value of the k-th smallest element (1-indexed).
            Use an order-statistic BIT: build BIT[i] = freq[i],
            then find the smallest index `idx` such that
            BIT.prefix(idx) >= k, by binary lifting on the
            BIT's bit structure (descend the BIT starting from
            the highest set bit). O(log n) per query.
            Source: https://www.geeksforgeeks.org/dsa/order-statistic-tree-using-bit/
            

Inputs passed to solve():
    freq: list of n non-negative integers (frequencies of values 1..n).
    n: length of freq (small in tests, n <= 16).
    k: 1-indexed rank to find.

Goal:
    the value of the k-th smallest element (in [1, n]); -1 if k is out of range.

Samples:
Sample 1 input:  freq = [2, 1, 3, 0, 2], n = 5, k = 4
Sample 1 output: 2 (1,1,2,3,...)

Sample 2 input:  freq = [1, 2, 3], n = 3, k = 3
Sample 2 output: 2

Sample 3 input:  freq = [0, 0, 5], n = 3, k = 1
Sample 3 output: 3

"""

def solve(freq, n, k):
    # Write your code here.
    return None
