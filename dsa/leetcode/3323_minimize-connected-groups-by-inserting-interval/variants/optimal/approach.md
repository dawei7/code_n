## General

Sort the intervals by start and merge every overlap or endpoint touch. This converts the input into disjoint connected groups `[left_i, right_i]` in increasing order, with a positive uncovered gap between consecutive groups. No inserted interval needs to distinguish between original intervals already inside the same group.

Suppose one new interval connects merged groups $i$ through $j$. It can begin at `right_i` and end at `left_j`; this is the shortest possible interval touching both extreme groups, and every intermediate group then lies between those endpoints. Therefore the block is connectable exactly when `left_j - right_i <= k`. Joining $q=j-i+1$ groups replaces them with one and reduces the original group count by $q-1$.

Use a two-pointer window over the merged groups. For each right endpoint $j$, advance the left endpoint while `left_j - right_i > k`. The surviving window is the longest connectable block ending at $j$, because later left endpoints only shorten the required span. Record the largest window size `most_joined`. If the merged input has $m$ groups, the answer is `m - most_joined + 1`.

The formula also covers the requirement to insert exactly one interval. When no gap can be bridged, `most_joined` remains one; a zero-length interval placed inside any existing group satisfies the length limit and leaves all $m$ groups unchanged.

## Complexity detail

Let $n=\lvert\texttt{intervals}\rvert$ and let $m\leq n$ be the number of merged groups. Sorting takes $O(n\log n)$ time. Merging and the sliding window each take $O(n)$ time because both pointers move only forward. The sorted intervals and merged groups require $O(n)$ auxiliary space under the package contract; the in-place native sort may reuse the input list but the merged list still uses $O(n)$ space.

## Alternatives and edge cases

- **Binary search from each group:** Searching for the furthest reachable start gives $O(n\log n)$ after merging, but the monotone two-pointer boundary makes the scan linear.
- **Test every pair of groups:** Checking all possible extreme pairs is correct but can take $O(n^2)$ time when many groups are bridgeable.
- **Skip the merge step:** Overlapping original intervals are already one group; treating them separately overcounts both the initial and joined group totals.
- **Endpoint contact:** Intervals such as `[1, 2]` and `[2, 5]` are connected and must merge because their union has no gap.
- **Exact length:** A span equal to `k` is legal; only a strictly larger span forces the left pointer forward.
- **One existing group:** Adding an interval cannot reduce the answer below one.
- **No bridgeable gap:** Insert a zero-length interval inside a group, satisfying the exactly-one requirement without creating a new group.
- **Unsorted input:** Sorting is necessary before either merging or applying the monotone window argument.
