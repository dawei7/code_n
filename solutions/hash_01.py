"""
Description
-----------
Given an array and a target, return the indices of the two
values that sum to target. The setup picks a reachable target
(sum of two random distinct positions). Single pass with a
value->index hash map; O(n).
Source: https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/

Examples
--------
Example 1:
Input:  arr = [2, 7, 11, 15], target = 9, n = 4
Output: [0, 1]

Example 2:
Input:  arr = [3, 2, 4], target = 6, n = 3
Output: [1, 2]

Example 3:
Input:  arr = [3, 3], target = 6, n = 2
Output: [0, 1]
"""

def solve(arr, target, n):
    # Write your code here.
    visited = dict()
    for i in range(n):
        second_el =  target - arr[i]
        if second_el in visited:
            return [visited[second_el], i]
        else:
            visited[arr[i]] = i

    return [-1,-1]














