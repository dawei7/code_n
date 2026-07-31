## General

Adding the same integer $x$ to every element preserves the relative ordering of all values. In particular, the smallest value of `nums1` becomes the smallest value of the transformed multiset, regardless of how that multiset is rearranged to form `nums2`.

Let $a = \min(\texttt{nums1})$ and $b = \min(\texttt{nums2})$. Because every transformed value equals its original value plus $x$, the two minima satisfy $b = a + x$. Therefore, the required shift is $x = b - a$.

This identity is sufficient because the problem guarantees that a valid uniform shift exists. Finding both minima and subtracting them avoids sorting or matching individual occurrences, and duplicates do not affect the argument.

## Complexity detail

Let $n$ be the common length of the two arrays. Finding each minimum scans one length-$n$ array, so the total time is $O(n)$. The algorithm stores only the two minima and their difference, using $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Sort both arrays:** After sorting, any pair of values at the same position reveals the shift. This costs $O(n \log n)$ time and may require additional storage, although only the minima are needed.
- **Compare sums:** Since `sum(nums2) - sum(nums1) = nx`, dividing by $n$ also recovers the shift. This is linear, but the minimum identity is more direct and avoids a division; fixed-width languages must also consider sum overflow.
- **Reordered values:** Comparing `nums2[0] - nums1[0]` is invalid because the transformed elements may be permuted.
- **Duplicates:** Repeated minimum values remain repeated after the shift, so they do not create ambiguity.
- **Negative and zero shifts:** The result may be negative or zero even though every array element is nonnegative.
