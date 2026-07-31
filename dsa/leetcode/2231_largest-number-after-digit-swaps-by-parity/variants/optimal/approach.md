## General

**Identify what swaps preserve**

Swapping two same-parity digits leaves every position occupied by a digit of the same parity as before. Conversely, arbitrary swaps among all odd digits can realize any permutation of the odd digits across odd-occupied positions, and the same is true independently for even digits.

Split the decimal characters into odd and even collections and sort each collection. Scan the original representation from left to right. At an odd position, place the largest unused odd digit; at an even position, place the largest unused even digit.

**Make the earliest digit maximal**

Decimal values compare lexicographically when their lengths are equal. At each position, the algorithm chooses the greatest digit that can legally occupy that position. Any different legal result must first differ at some position where it chooses a smaller same-parity digit, so it is numerically smaller regardless of its suffix. The greedy reconstruction is therefore globally maximal.

## Complexity detail

The legal value is at most $10^9$, so its decimal representation contains at most ten digits. Sorting and scanning this fixed bounded representation take $O(1)$ time and $O(1)$ auxiliary space under the stated contract.

The bounded-domain certificate records why digit-count scaling cannot supply an honest asymptotic runtime verdict and replaces it with broad oracle comparison across the legal magnitude range.

## Alternatives and edge cases

- **Priority queues:** Separate max-heaps for odd and even digits produce the same greedy order but add machinery for at most ten digits.
- **Repeated maximum search:** Selecting the best remaining same-parity digit at every position is correct but performs avoidable repeated scans.
- **Unrestricted sorting:** Sorting all digits together can move an odd digit into an even position and violate the swap rule.
- **Repeated digits:** Equal digits are interchangeable and do not affect maximality.
- **One parity only:** All digits can be arranged in descending order.
- **Single digit:** No swap changes the value.
- **Digit zero:** Zero is even and participates only in the even collection.
