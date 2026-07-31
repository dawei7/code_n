## General

The receiver is sorted ascending, so the last occurrence of `target` lies immediately before the first element that is strictly greater than `target`. Searching for that boundary handles an entire duplicate run at once.

**Half-open search interval**

Maintain `[left, right)` as the unresolved range, initially covering the complete array. At each step, inspect its middle element. If `this[middle] <= target`, the first greater value must be to the right, so set `left = middle + 1`. Otherwise, the middle position could be the desired boundary, so set `right = middle`.

The update always shrinks the interval. Values before `left` are known to be at most `target`, while positions from `right` onward are known to be greater than `target`. When `left === right`, that index is therefore the first position whose value exceeds the target, or the array length when no such value exists.

**Validate the predecessor**

The only possible last occurrence is `left - 1`. If that index is valid and stores exactly `target`, return it. Otherwise, every element before the boundary is smaller than the missing target, so return `-1`. Defining the method with a normal function binds `this` to the receiving array.

## Complexity detail

Let $n$ be the receiver length. Each comparison halves the unresolved interval, giving $O(\log n)$ time. The search stores only two boundaries, one midpoint, and one candidate index, so it uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **`lastIndexOf`:** This directly returns the required value, but it performs a linear search and does not meet the $O(\log n)$ follow-up.
- **Left-to-right scan:** Recording every matching index is correct but costs $O(n)$ time even though the input is sorted.
- **Find any match, then scan right:** Binary search locates one occurrence quickly, but a duplicate run may contain $O(n)$ values, making the final scan linear.
- **Search for the first target:** A lower-bound search identifies the beginning, not the required final occurrence.
- If the target is smaller than every element, the boundary is index $0$ and the predecessor is invalid.
- If the target is larger than every element, the boundary is $n$; the final element must still be checked for equality.
- A one-element receiver follows the same search and validation without a special case.
- Duplicate values at either array boundary must return the last matching index, not merely any match.
