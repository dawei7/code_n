## General
**Why positivity gives one target window per right endpoint**

Maintain a sliding window `[left, right]` and its sum. Extend `right` one position at a time. If the sum exceeds `target`, advance `left` while subtracting discarded values until the sum is at most the target.

Every value is positive, so extending the right boundary strictly increases the sum and removing the left boundary strictly decreases it. Once the sum is at most `target`, no wider window ending at `right` can equal the target, and no narrower window needs to be tested unless the current sum equals it. Thus any target-sum window ending at `right` is found in linear total pointer movement.

**Remembering the best completed left-hand partner**

Finding target windows is not enough: the algorithm must choose two that do not overlap and minimize their total lengths. Let `best_until[i]` be the shortest length of any target-sum subarray ending at or before index `i`. If none exists, store infinity.

When the current target window is `[left, right]`, every legal earlier partner must end at an index less than `left`. Therefore `best_until[left - 1]` is precisely the best possible partner for this current window. If it is finite, combine it with `right - left + 1` and minimize the answer.

After considering that pair, update the shortest target-window length seen so far and write it into `best_until[right]`. If no target window ends at `right`, carry the previous best forward.

**Why the order of updates matters**

The current window must be combined with `best_until[left - 1]` before its own length is recorded at `right`. This guarantees the earlier state contains only windows fully to the left. Reading `best_until[right]` or a global best without respecting the boundary could accidentally combine overlapping windows.

Adjacent windows are handled correctly: if the earlier window ends at `left - 1`, it is included in the prefix state and shares no index with the current window.

**Why the minimum pair is found**

Consider an optimal pair and order its subarrays by position, with the right-hand one equal to `[a,b]`. When the sliding window reaches `right = b`, positivity causes it to identify exactly that target-sum interval. The prefix value `best_until[a - 1]` is no longer than the optimal pair's left-hand interval because that interval is one of the candidates represented there.

The algorithm therefore evaluates a pair whose combined length is at most the optimum. Every evaluated pair consists of two real target-sum subarrays separated at `left`, so no evaluated value can be smaller than the true optimum. The values are equal, proving the final minimum is correct.

## Complexity detail
The right boundary visits each index once, and the left boundary only moves forward, also at most $N$ times. Each window and dynamic-programming update is constant time, giving $O(N)$ total time.

The `best_until` array stores one value per input position and uses $O(N)$ space. All other state consists of a few indices, sums, and minima.

## Alternatives and edge cases
- **Enumerate all starts and extend rightward:** Positivity lets each inner scan stop once the sum reaches or exceeds `target`, but worst-case inputs still require $O(N^2)$ time.
- **Prefix sums plus hash map:** A map from prefix sum to index finds target-sum windows in $O(N)$ expected time and also works when values are not all positive. It uses the same asymptotic space but ignores the stronger source guarantee.
- **Collect intervals then sort or search:** Recording every target window and using binary search for disjoint partners can take $O(N\log N)$ time and more bookkeeping than the one-pass prefix minimum.
- **Two directional arrays:** Compute the shortest target window ending by every prefix and starting by every suffix, then test every split. This is correct in $O(N)$ time and $O(N)$ space but requires two scans and two arrays.
- **Only one target window:** Return `-1`; a subarray cannot be paired with itself.
- **Several overlapping windows only:** Overlap disqualifies the pair even if both sums are correct.
- **Adjacent windows:** They are non-overlapping and may be optimal.
- **Singleton windows:** Any element equal to `target` forms a length-one candidate.
- **Target larger than the total sum:** No target window exists, so the result is `-1`.
- **Positive values are essential:** With zeros or negative values, shrinking on `sum > target` would no longer be sufficient and the prefix-map alternative would be required.
