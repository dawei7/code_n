## General
**Store the best chain by its final value.** Process `arr` from left to right. Let the hash entry for a value represent the greatest valid subsequence length seen so far whose last selected value equals that key. The exact indices used by the chain no longer matter once its length and final value are known.

**Extend the only possible predecessor.** For a current `value`, the preceding selected value must be exactly `value - difference`. Read that predecessor's best length from the hash map, using zero when it has not appeared, then set `dp[value] = dp.get(value - difference, 0) + 1`. This update also handles `difference = 0`: each repeated value extends the chain recorded under its own key.

**Why a single best length per value is enough.** Every chain represented in the map uses only indices earlier than the current scan position. Among chains ending at the required predecessor value, a shorter chain can never lead to a better result than the longest one because either can append the same current element. Thus discarding shorter chains loses no optimal continuation. Taking the maximum recorded length over the scan yields the global optimum.

## Complexity detail
Each of the $n$ elements performs a constant expected number of hash operations, giving $O(n)$ expected time. The map stores at most one entry per distinct array value and therefore uses $O(n)$ space in the stated bound.

## Alternatives and edge cases
- **Index-based dynamic programming:** For each index, scanning all earlier indices finds matching predecessors correctly but takes $O(n^2)$ time.
- **Sort the array first:** Sorting destroys the original relative order, which is part of the subsequence definition, and also mishandles negative `difference`.
- **Zero difference:** Repeated equal values extend one another; the answer is the maximum frequency encountered in scan order.
- **Negative difference:** The predecessor formula remains `value - difference`, so no special traversal direction is needed.
- **Duplicate non-predecessor values:** Only the best chain ending at a value is retained, since all future extensions see the same key.
- **No valid pair:** Every individual element is a length-one arithmetic subsequence.
- **Noncontiguous selection:** Irrelevant intervening values may be skipped without resetting a chain.
