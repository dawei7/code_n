## General

**Maintain the sum of values present at least once**

The window `nums[l..r]` uses each distinct value once. `cnt[x]` stores its occurrence count in the current window, while `s` stores the sum of keys whose count is positive.

When `x` enters, its count increases. Only a transition from zero to one adds `x` to `s`; duplicates do not change the distinct-value sum.

When the left value leaves, its count decreases. Only a transition to zero subtracts that value, because only then does it disappear completely from the window.

At all times, the state invariant is:

$$
\texttt{s}=\sum_{x:\texttt{cnt}[x]>0}x
$$

for exactly the occurrences between pointers `l` and `r`. The insertion and removal rules cover the only two ways membership in this set can change.

**Expand right, then shrink while valid**

All values are positive. Extending the right boundary cannot decrease the distinct sum: it either adds a new positive value or leaves the sum unchanged for a duplicate.

After inserting `nums[r]`, if `s>=k`, the current window is valid. The source records its length and repeatedly removes leftmost occurrences while validity remains.

This finds the shortest valid window ending at `r`. The first removal that makes `s<k` stops the loop; any further removal would still be invalid because removing positive distinct contributions cannot increase `s`.

**Why discarded left boundaries never need to return**

Once a valid window can drop its current left position and remain valid, keeping that position can never help produce a shorter future window. Future right extensions only add elements, so advancing `l` is safe.

If removing the last copy of a value makes the window invalid, the loop stops with `l` just after the shortest valid boundary recorded for this right endpoint. A future right extension may restore validity and shrinking resumes.

Both pointers move only forward, which is the source of linear time.

The window may become valid, shrink to invalid, and become valid again after later insertions. Keeping the counters after each shrink lets the algorithm resume from the remaining suffix rather than rebuilding state.

**Trace duplicate handling**

For `[2,2,3,1]` with `k=4`, the first 2 sets `s=2`. The second 2 changes its count but leaves `s=2`. Adding 3 makes `s=5`.

Window `[2,2,3]` is recorded with length three. Removing the first 2 leaves another copy, so `s` remains five and window `[2,3]` is recorded with length two. Removing the second 2 drops its count to zero and `s` becomes three, ending the shrink.

The algorithm correctly finds length two.

**Why the global answer is minimal**

For every right endpoint, the inner loop considers every valid left boundary encountered while shrinking and records their lengths. It stops only after the window becomes invalid.

Any valid subarray has some right endpoint `r`. When the outer scan reaches it, the maintained left pointer cannot have skipped a necessary earlier boundary: skipped boundaries were already removable from valid windows and only produced longer candidates. The shrink process reaches the shortest valid candidate for that `r`.

Taking the minimum over all recorded endpoints therefore finds the global shortest length.

Recording the candidate before removing `nums[l]` matters. The current valid window must be measured while both endpoints still belong to it; then the source tests whether an even shorter left-trimmed window remains valid.

**Represent “not found” safely**

`ans` starts at `n+1`, larger than every legal subarray length. If it remains larger than `n`, no valid window was ever observed and the source returns `-1`.

If any single value is at least `k`, inserting it makes a length-one window valid and one—the smallest possible result—is recorded.

## Complexity detail

The right pointer visits each of $N$ positions once. The left pointer also advances at most $N$ times over the entire run. Expected dictionary operations are $O(1)$, so total expected time is $O(N)$.

The frequency map may store $O(N)$ distinct keys, giving $O(N)$ auxiliary space. Keys whose count reaches zero remain in the `defaultdict`, so the map does not necessarily shrink.

## Alternatives and edge cases

- **Enumerate all subarrays:** Updating a distinct set for every start can cost $O(N^2)$.
- **Use ordinary element sum:** Duplicate values count once, so a conventional numeric sliding sum is wrong.
- **Add every entering duplicate:** This overstates the distinct sum.
- **Subtract a leaving value immediately:** It must remain in `s` while another copy is still in the window.
- **Negative values:** The monotonic shrinking proof depends on the positive-value constraint.
- **Single qualifying element:** The answer is one.
- **All values equal below `k`:** No window can improve the one-value distinct sum, so return `-1`.
- **Threshold equals current sum:** The inclusive condition enters the shrink loop.
- **No valid subarray:** Sentinel `n+1` maps to `-1`.
- **Duplicate-heavy window:** Counts preserve multiplicity while `s` preserves set semantics.
- **Input preservation:** Only pointers, counts, and sums change.
- **Candidate timing:** Measure `r-l+1` before advancing `l`.
- **Zero-count dictionary entries:** They no longer contribute to `s` even if the key remains allocated.
