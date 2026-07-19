## General
**Locate the portions that are already usable**

Scan from the left to find the longest non-decreasing prefix, ending at `prefix_end`. If it reaches the final element, no removal is needed. Separately scan from the right to find the longest non-decreasing suffix, beginning at `suffix_start`.

Keeping only the prefix removes `N - prefix_end - 1` elements, while keeping only the suffix removes `suffix_start` elements. The smaller value is an initial valid answer. Any better removal must keep some prefix and some suffix and join them without introducing a decrease.

**Find the closest compatible join**

Set `left = 0` in the sorted prefix and `right = suffix_start` in the sorted suffix. If `arr[left] <= arr[right]`, those retained boundary values can be joined, so removing the open gap between them costs `right - left - 1`. Advancing `left` may shorten that gap further.

If `arr[left] > arr[right]`, the current suffix value cannot follow this prefix value or any later, at-least-as-large prefix value. Advance `right` until a compatible suffix boundary is found. Because both retained regions are non-decreasing, neither pointer ever needs to move backward.

Every valid answer keeps a prefix ending somewhere at or before `prefix_end` and a suffix beginning somewhere at or after `suffix_start`. The two-pointer scan considers the shortest compatible gap for each reachable prefix boundary. It therefore includes an optimal join, while the initial prefix-only and suffix-only candidates cover removals that leave one side empty.

## Complexity detail
The prefix scan, suffix scan, and merge scan each move monotonically across at most $N$ elements, so the total time is $O(N)$.

Only indices and the current best length are stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Binary search each prefix value:** search the sorted suffix for the first compatible value. This is correct but takes $O(N \log N)$ time.
- **Test every removal interval:** precompute whether prefixes and suffixes are sorted, then enumerate all pairs of cut positions. This is correct but requires $O(N^2)$ time.
- **Copy and sort retained arrays:** constructing every candidate remainder and checking its order can require cubic work and substantial temporary space.
- **Already non-decreasing:** the longest prefix spans the array, so the answer is `0`.
- **Strictly decreasing:** no two adjacent retained values can remain in their original order, so exactly $N-1$ elements must be removed.
- **Equal values:** equality is compatible with non-decreasing order and must use `<=`, not `<`.
- **Remove only a prefix or suffix:** the initial candidates handle cases where no two-sided join improves the answer.
- **Single element:** the array is already non-decreasing, and removing nothing is optimal.
- **Join across a long middle drop:** only the elements strictly between the chosen compatible boundaries are removed.
