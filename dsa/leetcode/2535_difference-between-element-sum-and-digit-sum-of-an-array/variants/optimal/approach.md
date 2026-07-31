## General

Compute the element sum directly. For the digit sum, repeatedly take `value % 10` to obtain the current last decimal digit, add it to the running total, and remove it with `value //= 10`.

Every positive input value eventually becomes zero, and the repeated remainders are exactly its decimal digits from right to left. Therefore the two accumulators equal the two sums defined by the problem, and their absolute difference is the required result.

## Complexity detail

Let $S$ be the total number of decimal digits across all values in `nums`. Each array element and each of its digits is processed once, so the running time is $O(S)$. The two sums and current value use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **String conversion:** Joining or converting the values makes digit extraction concise, but allocates text proportional to $S$.
- **Single-digit values:** Their element contribution equals their digit contribution, so they do not change the final difference.
- **Zero digits:** Zeroes inside values contribute nothing to the digit sum but still must be removed during extraction.
- **Positive-input guarantee:** Because every value is positive, the digit loop does not need a special case for the number zero.
