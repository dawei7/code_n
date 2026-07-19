## General
**The cost is minimized at a median**

For a chosen target `t`, the move count is $\operatorname{sum}(\operatorname{abs}(x - t))$. If fewer than half the values lie at or below `t`, moving `t` one step upward reduces more distances than it increases; symmetrically, if fewer than half lie at or above it, moving downward improves the cost. A target cannot be optimal until it reaches the middle of the sorted values, so any median minimizes the total absolute deviation.

**Sort once and choose the middle value**

Sort a copy of the array and select the element at index $\lfloor n/2 \rfloor$. Sum every absolute difference from that median. For odd length it is the unique middle order statistic; for even length every integer between the two middle values has the same minimum cost, so choosing the upper median is valid.

**Pairing extremes gives the same total**

After sorting, each smallest/largest pair must move across the gap between them regardless of which median in the middle interval is chosen. Summing `largest - smallest` while moving inward is an equivalent view and explains why the particular even-length median does not matter.

## Complexity detail
Sorting dominates at $O(n \log n)$ time, followed by an $O(n)$ distance scan. A sorted copy uses $O(n)$ auxiliary space; in-place sorting reduces explicit copy space according to the language's sort implementation.

## Alternatives and edge cases
- **Quickselect the median:** gives expected $O(n)$ time and can avoid fully ordering the array, but requires careful pivot handling for robust worst-case behavior.
- **Pair sorted extremes:** computes the answer directly without explicitly naming the median and has the same sorting complexity.
- **Try every input value as target:** is correct because a median is an input value, but recomputing all distances costs $O(n^2)$.
- **Use the arithmetic mean:** minimizes squared error, not absolute movement, and can be suboptimal here.
- **One element or all equal:** needs zero moves.
- **Even length:** any target between the two central values has equal optimal cost.
- **Negative values:** sorting and absolute differences work unchanged.
- **Large total distance:** fixed-width languages may need a wider accumulator than the element type.
