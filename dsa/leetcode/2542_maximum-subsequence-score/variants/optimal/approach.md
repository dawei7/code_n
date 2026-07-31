## General

The score mixes a sum to maximize with a minimum multiplier. Sort the paired values by `nums2` in descending order. While scanning, the current `nums2` value is no larger than every multiplier already seen, so it can serve as the minimum of a selection formed from the current prefix.

For a fixed current multiplier, the best sum is obtained by choosing the largest `k` `nums1` values among all eligible pairs in that prefix. Maintain those values in a min-heap together with their running sum. Push each arriving `nums1`; whenever the heap grows beyond `k`, remove its smallest value. The heap then contains exactly the largest available values of the allowed size.

Whenever the heap has `k` elements, multiply its sum by the current `nums2`. A selection's true minimum occurs at some selected pair. When the scan reaches that pair, every other selected index is already eligible, and the heap's sum is at least the sum of that selection. Thus the evaluated candidate is at least its score. Conversely, every heap candidate uses only prefix indices and includes a current-or-later threshold, so its selected minimum is at least the multiplier used; the candidate corresponds to a valid score lower bound for those indices. Taking the maximum over all thresholds yields the optimum.

## Complexity detail

Let $n$ be the array length. Sorting the pairs costs $O(n\log n)$. Each value is pushed once and at most one value is popped per iteration, adding $O(n\log k)$ time, which is contained in $O(n\log n)$. The sorted pairs and heap use $O(n)$ space in total.

## Alternatives and edge cases

- **Recompute for every multiplier:** Scanning all eligible values and selecting the largest `k` anew for each candidate minimum takes at least $O(n^2)$ time.
- **Enumerate index subsets:** Trying all $inom{n}{k}$ selections is exact but infeasible.
- **Sort by `nums1`:** Large summands alone do not control the minimum multiplier and can discard the optimal tradeoff.
- **Equal multipliers:** Their processing order does not affect correctness because all corresponding indices become eligible at the same threshold.
- **`k = 1`:** The score is simply `nums1[i] * nums2[i]`, and the heap scan considers every index.
- **`k = n`:** Every index must be selected, so the only score uses the total `nums1` sum and global minimum of `nums2`.
- **Large score:** The product can exceed 32-bit range, so fixed-width languages need 64-bit arithmetic.
