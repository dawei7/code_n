## General

**Turn the absolute index constraint into a moving eligible prefix.** Any pair can be ordered so the first index `j` is no greater than the second `i`. Then

$$
\lvert i-j\rvert\ge\texttt{indexDifference}
$$

becomes `j <= i - indexDifference`. For a fixed current right endpoint `i`, the legal partners are exactly a prefix of the array.

As `i` moves right by one, this prefix gains at most one new index: `j = i - indexDifference`. The source processes that new candidate once rather than rescanning the whole prefix.

**Compress every eligible value into two extremes.** To satisfy

$$
\lvert\texttt{nums[i]}-\texttt{nums[j]}\rvert
\ge\texttt{valueDifference},
$$

an eligible value must be sufficiently below current value or sufficiently above it. Among the prefix, the minimum value maximizes the first difference, and the maximum value maximizes the second. No middle value can succeed if both extremes fail.

Variables `mi` and `mx` store indices of the smallest and largest eligible values. Storing indices is essential because the required return type is an index pair.

**Maintain the invariant before each test.** The loop starts with `i = indexDifference`. It computes newly eligible `j = i - indexDifference`, compares `nums[j]` against both stored extremes, and updates their indices.

After that update, `nums[mi]` is the minimum and `nums[mx]` is the maximum over indices `0..i-indexDifference`.

The implementation initializes both indices to zero. At the first loop iteration, zero is exactly the first eligible index, so this initialization is consistent. Later updates only improve the corresponding extreme.

**Test the two possible directions.** If current value is at least `valueDifference` above the minimum, the code returns `[mi, i]`. If the maximum is at least that far above current value, it returns `[mx, i]`.

Both candidate first indices lie in the eligible prefix, so their distance from `i` is automatically at least `indexDifference`. The arithmetic test supplies the value condition.

**Why failure of both extremes proves failure for current `i`.** Suppose some eligible `j` satisfies the absolute value condition. If `nums[j] <= nums[i]`, then `nums[mi] <= nums[j]`, so current-minus-minimum is at least current-minus-that-candidate and must also pass. If `nums[j] > nums[i]`, `nums[mx] >= nums[j]` and maximum-minus-current must pass. Therefore a valid partner cannot hide between the extrema.

The loop tries every possible right endpoint whose eligible prefix is nonempty. If it never returns, no oriented pair exists; because every unordered pair has an orientation, no valid pair exists at all.

**Special case `indexDifference=0`.** Current index becomes eligible before it is tested. When `valueDifference=0`, pair `[0,0]` is valid and returned, matching the explicit statement that indices may be equal. For a positive value threshold, self-difference zero fails, while extrema from prior indices may succeed later.

**Why this is necessary for version II.** The first version's $n\le100$ could tolerate testing every pair. Here $n$ reaches $10^5$, making quadratic enumeration unacceptable. The extrema summarize a large eligible prefix in constant state and reduce the scan to linear time.

**No sorting is allowed or needed.** Sorting values would destroy original indices and complicate the index-distance constraint. The running prefix extrema preserve positions and exploit the direction of the scan.

## Complexity detail

Every array index enters the eligible prefix once, and every right endpoint is tested once. Each iteration performs constant work, so total time is $O(n)$. Only the two extreme indices and loop scalars are stored, giving $O(1)$ auxiliary space.

The source does not mutate or copy `nums`. The manifest's $O(n)$ time and $O(1)$ space exactly match the implementation.

## Alternatives and edge cases

- **All-pairs scan:** It is $O(n^2)$ and too slow for the version-II limit.
- **Prefix min/max arrays:** They support the same queries but allocate $O(n)$ space when two running indices are enough.
- **Index threshold exceeds available span:** No loop iteration occurs and `[-1,-1]` is returned.
- **Value difference zero:** The first distance-eligible pair passes; with zero index difference, equal indices pass.
- **Duplicate values:** They can satisfy a zero threshold but not a positive one unless paired with a far-enough other extreme.
- **Extreme ties:** Keeping the earlier stored index is fine because any valid answer is accepted.
- **Both value directions:** Check current above minimum and maximum above current to implement absolute difference.
- **Large numeric range:** Only subtraction and comparison are used; Python avoids overflow.
- **Why an interior prefix value is unnecessary:** For a fixed current value, the largest absolute difference over the eligible prefix is attained at its minimum or maximum. If neither extreme reaches the threshold, no value between them can reach it either.
- **Add before checking:** At current index `i`, index `i - indexDifference` has just become legal and must participate in the comparisons immediately. Delaying the update by one iteration would incorrectly enforce a strictly greater index gap.
- **Same index when the threshold is zero:** Updating the extrema with the current position before testing intentionally permits `i == j`. The contract uses an absolute index difference of at least zero, so this is valid rather than an accidental reuse.
