"""Solution for dc_09: Median of Two Sorted Arrays.


            Given two sorted arrays `a` (length m) and `b`
            (length n), return the median of the merged
            sorted sequence. The divide-and-conquer solution
            binary-searches on the smaller array for the
            correct partition, achieving O(log(min(m, n))).
            Source: https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/
            

Inputs passed to solve():
    a: first sorted array of length m.
    b: second sorted array of length n.
    m: length of a.
    n: length of b (both arrays capped at 6 in the setup).

Goal:
    the median of the merged sequence (float if even total length).

Samples:
Sample 1 input:  a = [1, 3, 8], b = [7, 9], m = 3, n = 2
Sample 1 output: 7.0

Sample 2 input:  a = [1, 2], b = [3, 4], m = 2, n = 2
Sample 2 output: 2.5


"""

def solve(a, b, m, n):
    # Write your code here.
    return None
