## General
**Sort the comparison array.** Create a sorted copy of `arr2`. For each value `x` from `arr1`, use binary search to find the first sorted value that is not smaller than `x`.

Only the insertion position and its immediate predecessor can be closest to `x`: every value farther right is at least as large as the insertion candidate, and every value farther left is no larger than the predecessor. Check each existing neighbor. If either absolute difference is at most `d`, `x` is disqualified; otherwise count it.

This nearest-neighbor argument covers every element of `arr2`, so a counted occurrence satisfies the universal distance condition and every disqualified occurrence has a concrete comparison value within the forbidden threshold.

## Complexity detail
Sorting the $m$ comparison values takes $O(m \log m)$ time. The $n$ binary searches take $O(n \log m)$ time. The sorted copy uses $O(m)$ space.

## Alternatives and edge cases
- **Compare every pair:** Test each `arr1` occurrence against all of `arr2`. It is direct and correct but takes $O(nm)$ time.
- **Two sorted arrays:** Sort both arrays and sweep nearest neighbors with two pointers in $O(n \log n + m \log m)$ time.
- **Exact threshold:** A difference equal to `d` disqualifies the value because qualifying differences must be strictly greater.
- **Zero threshold:** Only equal values are too close when `d = 0`.
- **Repeated values:** Count occurrences from `arr1`, not distinct values.
- **Insertion at an end:** Check only the one neighbor that exists.
- **Negative integers:** Absolute difference and sorted order handle them without special cases.
