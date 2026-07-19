## General
**Derive the only possible part sum:** Let the array total be `total`. Equal parts require `total % 3 == 0`; otherwise no partition exists. When divisible, every part must sum to `target = total // 3`.

**Close each part as soon as its target is reached:** Scan left to right, accumulating `current`. Whenever `current == target`, count one completed non-empty part and reset `current` to zero. Closing at the earliest possible boundary leaves the longest suffix available for the remaining parts and cannot remove a feasible later boundary.

**Require at least three completed parts:** Return true once the full scan yields three or more target-sum groups. This wording matters when `target == 0`: extra zero-sum groups can be merged into the third part, preserving exactly three non-empty parts with equal sums.

If a valid partition exists, the first valid prefix reaches `target`, and taking its earliest occurrence cannot prevent the remainder from being split because the skipped difference has sum zero. Repeating the argument for the second part establishes that the greedy scan finds at least three groups exactly when a valid three-part partition exists.

## Complexity detail
Computing the total and scanning for target-sum groups each visit the $N$ elements once, giving $O(N)$ time. The total, target, running sum, and part counter use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Try every split pair:** Prefix sums make each part sum constant-time to query, but checking all boundary pairs still costs $O(N^2)$ time and $O(N)$ space.
- **Backtracking partitions:** Exploring boundary choices is unnecessary and may become exponential without memoization.
- **Total not divisible by three:** Return false immediately.
- **Zero target:** More than three zero-sum groups are acceptable because adjacent groups can be merged.
- **Negative values:** Running sums need not be monotone, but equality with the fixed target remains valid.
