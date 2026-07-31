## General

**Turn removals into a longest-kept-set problem.** Minimizing removals is equivalent to maximizing the number of retained elements. Sort the values. If a retained set has sorted minimum at position `left` and maximum at `right`, every sorted value between them also lies within those extremes. Adding any omitted interior value cannot violate the balance condition, so some optimal retained set is a contiguous interval of the sorted array.

**Find the longest balanced interval.** Move `right` from left to right. While `ordered[right] > k * ordered[left]`, advance `left` until the current extremes are balanced. The left pointer never needs to move backward: increasing the maximum cannot make an earlier invalid minimum valid again.

After shrinking, the interval from `left` through `right` is balanced. Record its maximum length. The answer is the original length minus that longest retained interval. Every recorded window is feasible, and the monotone left pointer preserves the widest feasible window ending at each right endpoint, so the global maximum is found.

## Complexity detail

Let $n$ be the array length. Sorting costs $O(n\log n)$ time. Both sliding-window pointers advance at most $n$ times, adding $O(n)$ work. Total time is $O(n\log n)$. The sorted copy uses $O(n)$ auxiliary space.

The benchmark uses $S=n$. The accepted sort-and-window method is $O(S\log S)$, while checking every possible sorted interval is $O(S^2)$.

## Alternatives and edge cases

- **Check every retained interval:** This is correct after sorting but quadratic; the monotone window removes repeated comparisons.
- **Binary search for each minimum:** Finding the greatest allowed maximum with binary search gives $O(n\log n)$ after sorting, but two pointers make the scan linear.
- **Remove values greedily from one end:** A local choice between the current minimum and maximum can miss the longest feasible middle interval.
- **Single element:** It is balanced and requires zero removals.
- **Multiplier one:** Only equal values can coexist, so the best window is a largest duplicate group.
- **Inclusive boundary:** A maximum exactly equal to `k * minimum` remains valid.
- **Large multiplication:** Fixed-width languages should widen before computing `k * minimum`.
- **Input order:** Removals select values, not an original contiguous subarray; sorting is therefore valid.
