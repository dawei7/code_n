## Description

You are given two 0-indexed binary arrays `nums1` and `nums2` of the same
length. Choose indices `i` and `j` with $i \le j$ so that the sum of
`nums1[i:j + 1]` equals the sum over the identical inclusive range in `nums2`.
Only corresponding ranges with the same endpoints may be compared.

The width of such a pair is $j - i + 1$. Return the greatest achievable width
over all qualifying index pairs. If no nonempty range has equal sums in the two
arrays, return `0`.
