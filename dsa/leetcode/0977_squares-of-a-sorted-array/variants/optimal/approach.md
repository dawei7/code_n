## General
**Find the largest remaining magnitude at an endpoint:** Because `nums` is non-decreasing, the value with greatest absolute magnitude among an unprocessed interval must be at its left or right boundary. Interior values lie numerically between those endpoints and cannot have a larger magnitude than both.

**Fill the answer from right to left:** Maintain `left` and `right` at the current boundaries and an output position starting at `N - 1`. Compare `abs(nums[left])` with `abs(nums[right])`. Square the larger magnitude into the current output position, move that boundary inward, and decrement the output position. Equal magnitudes may be taken from either end because their squares are identical.

Each step places the largest square that has not yet been written. Therefore everything placed to its right is at least as large, and the remaining unwritten positions need only receive smaller or equal squares. When the pointers cross, every input occurrence has been consumed once and the output is in non-decreasing order.

## Complexity detail
The two pointers move inward a total of $N$ times, and each iteration performs constant work, so time is $O(N)$. The returned array contains $N$ squares and uses $O(N)$ space; aside from that result, the algorithm uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Square and sort:** Applying a comparison sort after squaring is concise but costs $O(N\log N)$ time and ignores the useful input ordering.
- **Insert squares into order:** Repeated insertion is correct but can take $O(N^2)$ time when the squared sequence arrives in descending order.
- **All-negative input:** The squares appear in reverse order, which the endpoint comparison handles without a special branch.
- **All-nonnegative input:** The right endpoint wins each comparison, reproducing the naturally ordered squares.
- **Equal magnitudes:** Values such as `-3` and `3` produce duplicate squares, and both occurrences must remain in the result.
