## General
**Search from right to left for the `1`**

Scanning backward ensures every value already processed lies to the right of the current index. Maintain a decreasing stack of candidates for the high `3` value and a variable `middle` containing the strongest confirmed `2` value.

**Promote popped values into a confirmed middle**

When the current value is larger than the stack top, pop smaller values. Each popped value has now been seen to the right of a larger value, so it can serve as the `2` in a valid $3 > 2$ pair. Because stack values are popped in increasing order, the last popped value is the largest confirmed middle and dominates earlier candidates.

**Detect a smaller left endpoint**

Before modifying the stack, if the current value is smaller than `middle`, the indices are automatically ordered: the current value is the leftmost `1`, the value that caused `middle` to be popped is the `3`, and `middle` lies farther right as the `2`. Their strict inequalities establish a 132 pattern. If no value ever falls below a confirmed middle, no such triple exists.

**Keep only useful high candidates**

After popping, push the current value. Every value is pushed once and popped at most once; values hidden beneath a larger current value cannot offer a better unresolved high candidate than that value.

## Complexity detail
Each element enters and leaves the monotonic stack at most once, so total time is $O(n)$. The stack can contain all elements of a monotone input, requiring $O(n)$ space.

## Alternatives and edge cases
- **Prefix minimum plus ordered suffix set:** query for a suffix value strictly between the minimum and current value in $O(n \log n)$ time.
- **Prefix minimum plus a suffix scan:** is straightforward but takes $O(n^2)$ on arrays with no pattern.
- **Three nested loops:** directly checks the definition in $O(n^3)$ time.
- **Fewer than three elements:** cannot contain the required three indices.
- **Duplicate values:** inequalities are strict, so equal endpoints never form a pattern by themselves.
- **Increasing array:** contains no smaller later `2`; a decreasing array contains no middle high `3`.
- **Negative values:** initialize the confirmed middle below every finite integer rather than assuming nonnegative input.
