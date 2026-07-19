## General
**Fix the final block length.** The number of ones never changes under swaps, so any completed block has exactly $k$ positions. Choosing its location is therefore equivalent to choosing a length-$k$ window.

**Count the misplaced values.** Every zero inside a chosen window must be exchanged with a one outside it. Their counts are equal, and one arbitrary-position swap fixes one pair, so the window's zero count is both necessary and sufficient. The answer is the minimum zero count over all length-$k$ windows.

**Reuse adjacent-window work.** Count zeros in the first window, then slide its boundaries one position at a time. Remove the contribution of the departing value and add the entering value. This examines every possible block, and taking the smallest maintained count proves optimality.

## Complexity detail
Counting $k$ and scanning all windows each take $O(n)$ time. The window boundaries, current zero count, and best value use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Recount every window:** Correctly finds the minimum but takes $O(nk)$ time in the worst case.
- **Simulate swaps:** Constructing each resulting array adds work without changing the zero-count criterion.
- **No ones:** The empty collection is already grouped, so return `0`.
- **One one:** A single value is already a contiguous block.
- **All ones:** The only length-$n$ window contains no zeros.
- **Arbitrary versus adjacent swaps:** Distance does not affect the cost because one swap may exchange any two positions.
