"""Solution for randomized_02: Reservoir Sampling.

Pick k items uniformly at random from a stream of unknown
length. Fill the reservoir with the first k items; for each
subsequent item i, replace a random reservoir slot with
probability k / (i + 1). O(n) time, O(k) space.
Source: https://www.geeksforgeeks.org/reservoir-sampling/

Inputs passed to solve():
    stream: list of n integers (the stream).
    k: reservoir size (>= 1).
    n: stream length.

Goal:
    a list of k items (the reservoir) sampled uniformly from the stream.

Samples:
Sample 1 input:  stream = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3, n = 10
Sample 1 output: k items, each a stream element


"""

def solve(stream, k, n):
    # Write your code here.
    return None
