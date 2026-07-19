## General
**Express every subarray through two prefix sums**

Start with prefix sum zero before the array. If $P_i$ is the sum of the first $i$ elements, then the sum of a subarray ending before position $j$ and starting at position $i$ is $P_j-P_i$. Thus every candidate is the difference between two prefix sums.

**Use absolute value to remove chronological direction**

For any two prefix sums $a$ and $b$, the relevant magnitude is $\lvert a-b\rvert$, which is unchanged when their order is reversed. Consequently, the largest possible magnitude among all prefix pairs is simply the difference between the greatest prefix sum and the smallest prefix sum. Their positions do not need to be ordered manually: whichever occurs later determines whether the corresponding subarray sum is positive or negative.

**Track only the two extrema**

Scan the array while maintaining the current prefix sum and the smallest and largest prefix sums seen, including the initial zero. At the end, `maximum_prefix - minimum_prefix` is attainable by the subarray between those two prefix positions and dominates every other pairwise difference, so it is exactly the requested answer.

## Complexity detail
The scan performs constant work for each of the $n$ elements, taking $O(n)$ time. Only the current prefix sum and two extrema are stored, so the auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Two Kadane scans:** Track the maximum and minimum subarray sums and return the larger of their absolute values. This is also $O(n)$ time and $O(1)$ space.
- **Enumerate all subarrays:** Extending a running sum from every start index is correct but requires $O(n^2)$ time.
- **Prefix array plus pair enumeration:** Materializing all prefix sums uses $O(n)$ space and comparing every pair remains quadratic; only the extrema are needed.
- **All positive:** The full array gives the maximum positive sum.
- **All negative:** The full array gives the most negative sum, whose magnitude is returned.
- **All zero:** The answer is zero, matching the permitted empty subarray.
- **Cancellation:** A total array sum near zero does not rule out a large-magnitude interior subarray.
- **Initial prefix:** Including prefix zero is necessary for subarrays that begin at index zero.
