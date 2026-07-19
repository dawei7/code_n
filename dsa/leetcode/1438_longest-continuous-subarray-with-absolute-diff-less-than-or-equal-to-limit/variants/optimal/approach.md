## General
**Use a window because invalidity is monotone.** Expand a right endpoint from left to right. If the current window has `maximum - minimum > limit`, adding more elements cannot make that same left boundary valid: the maximum can only rise and the minimum can only fall. Move the left boundary forward until the window becomes valid again.

**Maintain candidate minima in increasing order.** Store indices in `min_deque` so their values increase from front to back. Before appending a new index `right`, remove back indices whose values are at least `nums[right]`. The new value is no larger and expires later, so every removed value is dominated for all future windows. The front is the current minimum.

**Maintain candidate maxima symmetrically.** Store indices in `max_deque` with decreasing values. Remove back indices whose values are at most the new value, then append `right`. The front is the current maximum.

**Expire values as the left boundary advances.** While the two front values differ by more than `limit`, increment `left`. If either deque front equals the index being removed, pop it first. Indices not at the front need no direct removal: they remain behind a more extreme live candidate and will either become a front later or be removed as dominated.

**Why the remaining window is the best one ending at right.** Shrinking stops at the smallest left boundary for which the window ending at `right` is valid. Any earlier left boundary was explicitly invalid; any later one is shorter. Thus `right - left + 1` is the longest valid window ending at this right endpoint. Taking the maximum over all endpoints yields the global answer.

**Why deque updates remain linear.** Each index is appended once to each deque and can be removed at most once from each deque, either from the back as dominated or from the front as expired. The nested loops therefore perform only $O(n)$ total deque operations rather than $O(n)$ work per endpoint.

## Complexity detail
Every array index enters and leaves each monotonic deque at most once, so the full sliding-window scan takes $O(n)$ time. In the worst case a deque can retain $O(n)$ indices, giving $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Recompute minimum and maximum for every window:** A sliding window with repeated full-window scans is correct but can take $O(n^2)$ time.
- **Balanced ordered multiset:** Insert, remove, and read both extremes in $O(\log n)$ time per element, for $O(n\log n)$ total time.
- **Two heaps with lazy deletion:** This also tracks extremes but has more bookkeeping and logarithmic operations.
- **Zero limit:** A valid window may contain only one distinct value, though repeated equal values can form a long answer.
- **Exact limit:** A maximum-minus-minimum difference equal to `limit` is valid.
- **Single element:** Its range is zero, so the answer is `1`.
- **Duplicate extremes:** Index-based deques expire the correct occurrences even when values repeat.
- **Large limit:** The entire array may remain valid, and the window never needs to shrink.
