## General
**Choose the contiguous block that remains.** Any sequence of $k$ end removals leaves exactly $n-k$ consecutive cards in the middle. Conversely, every contiguous block of that length can be left by taking all cards before it from the left and all cards after it from the right. Maximizing the taken sum is therefore equivalent to minimizing the sum of the block that remains.

**Slide every possible remainder.** Compute the total card sum and the sum of the first window of length $n-k$. Slide that fixed-length window across the array by adding the entering card and subtracting the leaving card, retaining the smallest window sum. Subtract that minimum from the total.

**Why the complement is optimal.** The correspondence between end choices and remaining windows is exact, so every legal strategy is represented once by a window position. The smallest remaining sum yields the largest complementary taken sum. When $k=n$, the remaining window is empty and the answer is simply the total.

## Complexity detail
Computing the total and sliding the remaining window across $n$ cards takes $O(n)$ time. Only totals, a window sum, and indices are stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Enumerate left/right counts:** For every number taken from the left, sum the matching right suffix. Repeated slicing and summing takes $O(k^2)$ time.
- **Prefix and suffix arrays:** Precompute all end sums and combine them in $O(n)$ time, but this uses $O(n)$ extra space.
- **Take every card:** If $k=n$, no middle block remains and the total is mandatory.
- **Take one card:** Choose the larger endpoint.
- **All equal values:** Every distribution between the ends has the same score.
- **Positive values:** Minimizing the complement remains valid without special handling for sign.
- **Exact move count:** Taking fewer than `k` cards is never permitted.
