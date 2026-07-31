## General

**Let the minimum force the target parity**

Let $m$ be the smallest input value. Because all values are distinct, every other input is greater than $m$. The position containing $m$ cannot subtract any other value and keep a positive result, so that position must retain $m$. Consequently, every valid `nums2` must have the same parity as $m$.

If $m$ is odd, keep each odd input unchanged. For every even value $x$, subtract $m$. Since $x>m$, the difference is positive, and even minus odd is odd. This constructs an all-odd array.

If $m$ is even and every value is even, keeping all values constructs an all-even array. The remaining case has an even minimum and at least one odd value. Consider the smallest odd value $o$. It cannot stay odd if the target is even, so it would have to subtract another odd value. No smaller odd value exists, while subtracting an even value leaves an odd result and subtracting any larger value violates the positive-difference rule. Therefore this case is impossible.

The complete characterization is thus: return `true` exactly when the global minimum is odd or no odd value exists. One pass can track both facts.

## Complexity detail

The scan takes $O(n)$ time and uses $O(1)$ auxiliary space. Every input value can independently introduce the smallest value or the first odd value, so an exact decision has an $\Omega(n)$ inspection lower bound and the scan is asymptotically optimal.

The benchmark defines size as $n$ and uses mixed-parity arrays of lengths `16`, `64`, and `256` whose odd minimum makes the answer `true`. The accepted one-pass scan and an independent minimum-plus-parity scan should retain linear growth. A correct control that searches possible subtractions for each mismatched value performs $O(n^2)$ work and should fail only the scaling verdict.

## Alternatives and edge cases

- **Sort first:** Sorting exposes the minimum and makes the construction proof easy to visualize, but raises the time bound to $O(n\log n)$ and may require extra storage.
- **Search every subtraction:** Testing candidate `j` values independently for each index is correct but can take $O(n^2)$ time.
- **Single element:** The sole value must be kept and is already a uniform-parity array.
- **Odd minimum:** Every even value can subtract that minimum to become a positive odd value.
- **All even:** Keeping all original values constructs an all-even array.
- **Even minimum with any odd value:** The smallest odd value cannot be converted to even by a legal positive subtraction, so the answer is `false`.
- **Input order:** Only values and parities matter; the minimum may appear at any index.
- **Large values:** The algorithm uses only comparisons and parity, so values near $10^9$ require no special arithmetic handling.
