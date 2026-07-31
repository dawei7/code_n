## General

The forward construction must know whether spending the one allowed mismatch at a candidate index still leaves an exact completion. Build `suffix_matches[i]` by scanning `word1` backward: it records how many trailing characters of `word2` can be matched, in order, inside `word1[i:]`. One backward pointer into the end of `word2` is sufficient because only the longest matchable suffix length matters.

Then scan `word1` from left to right while targeting the next character of `word2`. If the current source character matches, select its index immediately. Replacing a later exact selection with this earlier equal character preserves every later index and the mismatch budget, so the earliest exact choice cannot destroy a valid completion.

When the characters differ and the mismatch is unused, select the current index only if `suffix_matches[index + 1]` is at least the number of target characters that would remain. That condition proves the rest can be matched exactly after spending the mismatch now. Otherwise skip the index. Each accepted position is therefore the earliest one that can belong to a valid completion, which makes the complete index list lexicographically smallest. If the scan cannot select all target positions, no valid sequence exists.

## Complexity detail

Let $n=\lvert word1\rvert$ and $m=\lvert word2\rvert$. The backward and forward scans each take $O(n)$ time, while producing the answer takes at most $O(m)$ time, for $O(n+m)$ total. The suffix-feasibility array uses $O(n)$ auxiliary space; the returned list uses $O(m)$ output space.

## Alternatives and edge cases

- **Dynamic programming over both positions:** Tracking every source-target pair requires $O(nm)$ time or space and is infeasible at length $3\cdot10^5$.
- **Always spending the mismatch early:** An early mismatch may leave a suffix that cannot match exactly; the backward feasibility count prevents that failure.
- **Delaying every mismatch:** Waiting for an exact match can produce a lexicographically larger index list even when an earlier mismatch permits completion.
- **One-character target:** Index 0 is always valid because its sole character may be changed if necessary.
- **Exact subsequence:** Exact matches use no mismatch and are selected at their earliest possible indices.
