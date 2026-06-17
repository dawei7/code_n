"""Solution for greedy_05: Optimal Merge Pattern.

Merging two files of sizes a and b costs a + b. Total cost of
merging n files into one is the sum of pairwise merge costs.
Greedy: always merge the two smallest remaining files. Same shape
as Huffman but with a single weight per file.
Requirement: O(n log n) using a min-heap.
Source: https://www.geeksforgeeks.org/optimal-file-merge-pattern/

Inputs passed to solve():
    sizes: list of n file sizes.
    n: number of files.

Goal:
    the minimum total cost of merging all files into one.

Samples:
Sample 1 input:  sizes = [5, 2, 4, 7], n = 4
Sample 1 output: 44

Sample 2 input:  sizes = [20, 30, 10, 5, 30], n = 5
Sample 2 output: 205

Sample 3 input:  sizes = [10, 20], n = 2
Sample 3 output: 30

"""

def solve(sizes, n):
    # Write your code here.
    return None
