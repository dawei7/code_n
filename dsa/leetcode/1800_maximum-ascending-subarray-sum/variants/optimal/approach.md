## General

**Split the array at every failed strict increase**

A strictly increasing subarray can continue from index $i-1$ to index $i$ exactly when `nums[i] > nums[i - 1]`. If that inequality fails, no increasing subarray can contain both adjacent positions, so a new ascending run must begin at $i$.

The protected solution scans once while maintaining:

- `t`, the sum of the current maximal ascending run ending at the processed position;
- `ans`, the greatest ascending-run sum confirmed so far.

Both start at zero. On index zero, the condition `i == 0` starts the first run without trying to access an earlier element.

**Extend a run when the next value is larger**

If the current value `v` is strictly greater than `nums[i - 1]`, appending it preserves the ascending property. The solution adds it to `t` and immediately updates `ans = max(ans, t)`.

Every number is positive. Therefore, extending a valid ascending run always increases its sum. For a fixed run, its full maximal length has at least as large a sum as any shorter subarray inside it. Tracking the growing prefixes is safe, and the largest value reached by `t` for that run is its complete sum.

**Reset when equality or a decrease breaks the run**

If `v <= nums[i - 1]`, strict ascent fails. The current index cannot belong to the previous run, so `t` is replaced with `v`. This represents the new one-element ascending subarray beginning at $i$.

The exact code does not update `ans` inside this reset branch. That is safe under the positive-input guarantee. Since `v <= nums[i - 1]` and the previous run's sum includes the positive value `nums[i - 1]`, the previous run sum is at least `nums[i - 1]` and therefore at least `v`. That previous sum was already considered during its last extension. The new singleton cannot beat `ans` at the moment it is created.

If the new run later extends, the ascending branch updates `ans` with its growing sum. If it remains a singleton at the end, the inequality above proves it still cannot exceed the previous run's already-recorded sum.

This omitted reset update would require reconsideration if negative numbers were allowed. The source's positivity constraint is part of the implementation proof.

**Following the first example**

For `[10,20,30,5,10,50]`, `t` grows through 10, 30, and 60 for the first run. Value 5 is not greater than 30, so `t` resets to 5. Then 10 and 50 extend the new run, producing sums 15 and 65. The maximum becomes 65 for `[5,10,50]`.

For a fully increasing array `[10,20,30,40,50]`, the run never resets. `t` reaches 150, which is returned.

For `[12,17,15,13,10,11,12]`, breaks start new runs at 15, 13, and 10. The final run grows from 10 to 21 to 33, overtaking earlier sums and producing the correct answer.

**Why maximal runs are enough**

Every strictly increasing subarray lies entirely inside one maximal ascending run because it cannot cross a non-increasing adjacent pair. Within a maximal run, all elements are positive, so the whole run has a sum at least as large as every contained subarray.

The scan constructs each maximal run exactly once and records its full sum by the time the run ends or the array ends. Taking the largest recorded run sum therefore equals the maximum over all ascending subarrays.

**A precise loop invariant**

After processing index $i$, `t` equals the sum of the unique maximal ascending suffix ending at $i$. Whenever the current comparison succeeds, extending the prior suffix proves this. When it fails, the only ascending suffix crossing no failed comparison begins at $i$, so resetting to `v` proves it.

`ans` is at least the sum of every completed run and every extended current run. The reset singleton exception cannot exceed the completed prior run because values are positive and non-increasing at the boundary. At loop termination, the invariant guarantees that `ans` is the desired maximum.

## Complexity detail

Let $n$ be the length of `nums`. Each element is visited once, and every iteration performs constant-time comparison, addition, assignment, and maximum operations. Time complexity is $O(n)$.

Only loop variables and the two scalar sums are stored, so auxiliary space is $O(1)$. Both bounds match the Optimal manifest.

The input length is at least one, so returning the initially updated `ans` is always well defined. Python integers easily cover the maximum sum under the stated constraints.

## Alternatives and edge cases

- **Start from every index:** Extending a run separately from each start repeats work and can take $O(n^2)$ time.
- **Store all run sums:** It works but uses unnecessary $O(n)$ space; only the maximum and current sum matter.
- **Generic maximum-subarray algorithm:** Kadane's algorithm addresses arbitrary negative values but does not enforce strict ascent by itself.
- **Equality boundary:** Equal adjacent values break the run because ascending means strictly increasing, not non-decreasing.
- **Single element:** Index zero starts a run, updates `ans`, and returns that value.
- **Fully increasing array:** No reset occurs, so the answer is the total array sum.
- **Strictly decreasing array:** Every element starts a singleton; the first, largest value remains the answer.
- **New run at the end:** Its singleton cannot beat the previous run at a non-increasing positive boundary, explaining the safe missing reset update.
- **Positive values:** They make a complete ascending run better than every shorter subarray within it.
- **Potential negative-value variant:** The exact reset logic and maximal-run argument would need modification because extending could lower a sum.
- **Strict comparison:** The source uses `>` rather than `>=` to preserve the definition.
- **Contiguous requirement:** A decrease cannot be skipped; doing so would form a subsequence rather than a subarray.
- **Input preservation:** The algorithm reads `nums` without changing it.
