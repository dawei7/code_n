## General
**Translate matching values into target positions**

Map every distinct target value to its index. Scan `arr`, discard values absent from `target`, and replace each remaining value by its target index. A sequence chosen from `arr` matches `target` in order exactly when these mapped indices are strictly increasing.

Duplicates in `arr` may produce repeated mapped indices, but a strictly increasing subsequence can use at most one occurrence of each target value. The distinctness of `target` is what makes this one-dimensional index mapping possible.

**Keep the longest already-correct subsequence**

Compute the length $L$ of the longest strictly increasing subsequence of mapped indices. Maintain `tails[length - 1]` as the smallest possible final index of an increasing subsequence of that length. For each index, binary-search the first tail not smaller than it and replace that tail, or extend the list when no such tail exists.

The tails list does not necessarily store one actual subsequence, but its length equals the maximum feasible length: replacement preserves every attainable length while leaving the smallest ending index for future extensions.

Any solution can retain at most $L$ target values already present in correct order, so at least $n-L$ insertions are necessary. Conversely, keep an increasing subsequence of length $L$ and insert every missing target value in the appropriate gaps; this uses exactly $n-L$ operations. Therefore the minimum is `len(target) - len(tails)`.

## Complexity detail
Building the target-index map takes $O(n)$ time and space. Each of the $m$ array values performs an expected $O(1)$ lookup; each matching value performs a binary search over at most $n$ tails, for $O(m\log n)$ worst-case additional time. The map and tails use $O(n)$ space.

## Alternatives and edge cases
- **Longest common subsequence table:** general LCS gives the retained length but costs $O(nm)$ time and potentially $O(nm)$ space.
- **Quadratic LIS dynamic programming:** comparing every earlier mapped index takes $O(m^2)$ time in the all-matching case.
- **Greedily take the next target value:** committing to the earliest requested value can miss a longer subsequence that starts later in `target`.
- **Values outside `target`:** ignore them; they neither help nor prevent a subsequence.
- **Duplicate values in `arr`:** repeated mapped indices cannot both belong to a strictly increasing subsequence.
- **No matching values:** retain nothing and insert all $n$ target elements.
- **Already a subsequence:** the LIS length is $n$, so zero insertions are needed.
- **Reverse order:** when every target value appears only in reverse, at most one can be retained.
- **Single target value:** the answer is zero if it occurs in `arr`, otherwise one.
