## General
**Turn subarray divisibility into equal prefix remainders**

Let `prefix[i]` be the sum through index `i`. A subarray after an earlier prefix `j` has sum `prefix[i] - prefix[j]`. This difference is divisible by `k` exactly when the two prefix sums have the same remainder modulo `k`.

**Remember the earliest index for each remainder**

Initialize remainder zero at virtual index `-1`, representing the empty prefix. As the running remainder is updated, check whether it was seen at an index at least two positions earlier. If so, the elements between those prefix boundaries form a valid subarray.

**Do not replace an earlier occurrence**

Store a remainder only on its first appearance. An earlier index provides the largest possible gap for every later match; replacing it could hide a valid length-two-or-more interval. The virtual `-1` entry likewise allows a divisible prefix ending at index one or later.

**Why absence of a match proves failure**

Every contiguous subarray is the difference of two prefix sums. If a qualifying subarray existed, its boundary prefixes would have equal remainders and an index gap equal to the subarray length, so the scan would detect it at the later boundary. Exhausting the array therefore rules out all candidates.

## Complexity detail
The scan performs expected $O(1)$ hash work for each of `n` values, giving $O(n)$ time. There are at most $n + 1$ observed prefixes and at most `k` distinct remainders, so space is $O(\min(n, k))$.

## Alternatives and edge cases
- **Enumerate every subarray sum:** is correct but takes $O(n^2)$ time even with a running inner sum.
- **Prefix-sum array plus pair checks:** avoids repeated addition but still examines quadratically many boundary pairs.
- **Delayed remainder set:** can enforce the two-element minimum by adding the previous remainder after each check, with the same linear bounds.
- **Two zeros:** form a sum of zero, which is divisible by every positive `k`.
- **Match one index apart:** represents a one-element subarray and must be rejected.
- **Divisible prefix:** is detected through the virtual remainder-zero prefix.
- **Remainder collisions:** only the earliest index needs to be retained.
