## General

There are $n(n+1)/2$ nonempty subarrays, and the source limit of $n \le 1500$ permits examining each one. Fix a left endpoint and initialize `total = 0`. As the right endpoint moves one position at a time, add only the newly included value. After reaching `right`, `total` is exactly the sum of `nums[left..right]`; no earlier element needs to be added again.

The trailing decimal digit is `total % 10`. Check it first because a mismatch rejects the subarray immediately. When it equals `x`, repeatedly apply integer division by ten until the remaining value is a single digit. That remaining digit is the leading decimal digit, so the subarray is counted exactly when it also equals `x`.

The running-sum construction proves coverage and correctness together. Every pair `left <= right` is visited once, and induction over increasing `right` shows that the maintained `total` equals the corresponding subarray sum. Modulo ten extracts its last digit, while removing decimal suffix digits leaves precisely its first digit. Therefore the counter is incremented for every valid subarray and for no invalid one.

The positivity guarantee matters: every sum is positive, so there is no zero sum, minus sign, or leading-zero convention to handle.

## Complexity detail

The nested endpoint loops visit exactly $n(n+1)/2$ subarrays. A legal sum is at most $1500 \cdot 10^9 = 1.5 \cdot 10^{12}$, which has at most 13 decimal digits; leading-digit extraction therefore performs at most 12 divisions, a source-bounded constant. The running time is $O(n^2)$. The algorithm stores only the answer, running sum, indices, and one digit-extraction value, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Prefix sums:** Store cumulative totals so each `nums[l..r]` sum is a subtraction. This also takes $O(n^2)$ time but uses $O(n)$ auxiliary space instead of updating one running sum.
- **Fresh summation for every interval:** Calling `sum(nums[l:r + 1])` inside both endpoint loops is correct but revisits elements and takes $O(n^3)$ time.
- **Convert every sum to text:** Comparing the first and last characters is straightforward and remains bounded under the numeric constraints, but it allocates a new decimal string for every subarray.
- **Sliding window:** Boundary-digit validity is not monotone as a positive sum grows; an extension can change a valid sum to invalid and later back to valid, so one moving left boundary cannot count all answers.
- **Single-digit sums:** Their first and last digits are the same, so such a subarray is valid exactly when that digit equals `x`.
- **Large totals:** A legal subarray sum can reach $1.5 \cdot 10^{12}$, so fixed-width implementations need a 64-bit running sum even though the count itself is at most $n(n+1)/2$.
- **Repeated sums and overlap:** Equal sums from different index intervals are separate subarrays and must each contribute to the answer.
