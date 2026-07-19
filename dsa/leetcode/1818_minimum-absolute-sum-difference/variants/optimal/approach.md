## General
**Separate the original total from the best possible improvement**

First accumulate every original difference. A replacement affects only one index, so its benefit is the old difference at that index minus the smallest difference obtainable there using a value from `nums1`. The globally optimal operation is therefore the single largest nonnegative benefit among all indices. If every benefit is zero, making no replacement is optimal.

**Find the nearest permitted value efficiently**

Sort a copy of `nums1`. For a target `nums2[i]`, the replacement minimizing absolute difference is its nearest value in this ordered copy. Binary search for the insertion position; only the value at that position and its predecessor can be nearest. Compare both existing candidates with the original difference and retain the largest reduction seen.

**Why subtracting the maximum reduction is optimal**

For each index, binary search considers the closest original value on both sides of its target, so it computes the minimum attainable difference at that index. Each resulting reduction describes the best replacement whose sole changed position is that index. Because the rules permit at most one change, no valid outcome can combine reductions from different indices. Subtracting the maximum individual reduction from the unchanged total therefore gives the global minimum.

## Complexity detail
Sorting the $n$ values costs $O(n\log n)$. The second pass performs $n$ binary searches, each taking $O(\log n)$, so total time remains $O(n\log n)$. The sorted copy uses $O(n)$ space. Keep the unreduced total and best reduction until the end, then apply the modulus; reducing intermediate differences could corrupt their ordering.

## Alternatives and edge cases
- **Try every replacement at every index:** Scanning all values of `nums1` for each target is correct but takes $O(n^2)$ time.
- **Balanced ordered set:** It supports predecessor and successor queries in $O(\log n)$ without a sorted copy, but is more machinery than a one-time sort.
- **Already equal arrays:** Every original difference and every possible reduction is zero, so return zero.
- **Duplicate values:** Duplicates do not create new replacement choices; retaining them in the sorted copy is harmless.
- **One-element arrays:** The only available replacement is the existing value, so the original difference cannot improve.
- **Nearest value at an endpoint:** The insertion position may be zero or $n$; inspect only candidates whose indices exist.
- **Modulo handling:** Select the best reduction using exact totals and apply $10^9+7$ only to the final minimized sum.
