"""Solution for hash_01: Two Sum.

Given an array and a target, return the indices of the two
values that sum to target. The setup picks a reachable target
(sum of two random distinct positions). Single pass with a
value->index hash map; O(n).
Source: https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/

Inputs passed to solve():
    arr: list of n random integers (can include negatives).
    target: sum of two distinct positions in arr.
    n: length of arr.

Goal:
    a sorted pair of indices [i, j] with arr[i] + arr[j] == target, or [-1, -1].

Samples:
Sample 1 input:  arr = [2, 7, 11, 15], target = 9, n = 4
Sample 1 output: [0, 1]

Sample 2 input:  arr = [3, 2, 4], target = 6, n = 3
Sample 2 output: [1, 2]

Sample 3 input:  arr = [3, 3], target = 6, n = 2
Sample 3 output: [0, 1]

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














