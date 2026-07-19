## General
**Look toward the ocean**

For index `i`, only the tallest building among indices greater than `i` matters. If `heights[i]` exceeds that maximum, it exceeds every building to its right; otherwise at least one building blocks its view.

**Scan from right to left**

The rightmost building has no obstruction, so begin beyond it with a maximum of zero. While moving left, compare each height with the tallest height already seen. Record the index when the current height is strictly larger, then update the running maximum.

**Keep the comparison strict**

An equal-height building to the right prevents a view. Therefore an index is recorded only for `height > tallest_to_right`, not for equality. Since heights are positive, the initial zero correctly admits the last building.

**Restore increasing index order**

The reverse scan discovers visible buildings from right to left, so their indices are collected in decreasing order. Reverse the result once at the end to satisfy the required increasing order.

At each index, the running value is exactly the maximum of the suffix strictly to its right. The comparison is therefore equivalent to the definition of an ocean view, proving that every and only qualifying index is recorded.

## Complexity detail
The reverse scan visits all $n$ buildings once and the final reversal touches at most $n$ recorded indices, for $O(n)$ time. The returned list can contain all $n$ indices and requires $O(n)$ output space; excluding that output, the scan uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Monotonic stack:** Scanning left to right and removing shorter obstructed candidates also gives $O(n)$ time, but a suffix maximum is simpler when only visibility is required.
- **Suffix-maximum array:** Precomputing the maximum to the right of every index is correct and linear but allocates an unnecessary $O(n)$ auxiliary array.
- **Check every later building:** Directly validating each index takes $O(n^2)$ time in decreasing or equal-height arrays.
- **Single building:** Index zero always has an ocean view.
- **Strictly decreasing heights:** Every building is visible.
- **Strictly increasing heights:** Only the final building is visible.
- **Equal heights:** Among an equal-height suffix, only its rightmost occurrence can be visible.
- **Last building:** It always qualifies because there is no building between it and the ocean.
- **Output order:** Reverse the indices after the right-to-left scan rather than returning discovery order.
