## General

**Represent alternation by the direction of the boundary comparison**

An alternating subarray switches direction at every adjacent pair. If one pair rises with `a < b`, the next must fall with `b > c`, then rise again, and so on. Equal neighbors cannot appear in an alternating subarray of length greater than one because neither strict direction holds.

When extending a run by one value, the full history is unnecessary. We need only know the direction of its most recent comparison. The source computes directional run lengths on both sides of every possible deleted index.

**Left arrays describe runs ending at an index**

`l1[i]` is the longest alternating subarray ending at `i` whose final comparison is a rise:

`nums[i - 1] < nums[i]`.

`l2[i]` is the corresponding longest run whose final comparison is a fall:

`nums[i - 1] > nums[i]`.

Every entry begins at 1. A one-element subarray has no comparison, so it can serve as the base before either a future rise or fall.

When `nums[i - 1] < nums[i]`, the new final comparison rises. To preserve alternation, the run ending at `i - 1` must previously end with a fall. Therefore:

`l1[i] = l2[i - 1] + 1`.

When `nums[i - 1] > nums[i]`, the new comparison falls and must follow a rise:

`l2[i] = l1[i - 1] + 1`.

If the two values are equal, neither state extends and both remain 1.

During this left-to-right pass, the source updates `ans` with both directional lengths. This records the best alternating subarray without any deletion. It also covers every solution that deletes an irrelevant element outside the selected subarray.

**Right arrays describe runs starting at an index**

The source then scans from right to left.

`r1[i]` is the longest alternating subarray starting at `i` whose first comparison is a rise:

`nums[i] < nums[i + 1]`.

`r2[i]` is the longest starting run whose first comparison is a fall:

`nums[i] > nums[i + 1]`.

If `nums[i + 1] > nums[i]`, the first comparison from `i` rises. The remaining run starting at `i + 1` must begin with a fall, giving:

`r1[i] = r2[i + 1] + 1`.

If `nums[i + 1] < nums[i]`, the first comparison falls and must be followed by a rise:

`r2[i] = r1[i + 1] + 1`.

Again, equality leaves both states at their one-element bases.

The numeric suffixes “1” and “2” have consistent directional meanings: state 1 represents a rise, and state 2 represents a fall. On the left it is the last comparison; on the right it is the first comparison.

**Only an interior deletion can create a new opportunity**

Removing the first or last element does not create a new adjacency inside the remaining array. Any alternating subarray after such a deletion was already an alternating subarray before deletion, so the no-deletion baseline covers it.

Removing an interior element `nums[i]` connects `nums[i - 1]` directly to `nums[i + 1]`. A post-deletion subarray can improve on the baseline only if it crosses this newly created bridge. Otherwise, it lies wholly on one side and already existed before deletion.

Therefore the source tests only `i` from 1 through `n - 2` and tries to join the best compatible left and right runs.

**Stitch across a rising bridge**

Suppose

`nums[i - 1] < nums[i + 1]`.

After deleting index `i`, the new bridge is a rise.

The comparison immediately before that bridge, when it exists, must be a fall. The longest compatible left run is therefore `l2[i - 1]`.

The comparison immediately after the bridge, when it exists, must also be a fall because directions alternate as

`fall, rise, fall`.

The longest compatible right run is `r2[i + 1]`.

The candidate length is

`l2[i - 1] + r2[i + 1]`.

There is no subtraction for overlap: the left and right runs occupy disjoint sides, and the middle element has been removed.

If either side contributes only one element, its state length is 1 and has no conflicting internal comparison. Treating that singleton as compatible with either direction is correct.

**Stitch across a falling bridge**

If

`nums[i - 1] > nums[i + 1]`,

the new bridge falls. It must have a rise immediately before and a rise immediately after:

`rise, fall, rise`.

The compatible candidate is therefore

`l1[i - 1] + r1[i + 1]`.

If the neighbors are equal, the bridge is neither a strict rise nor a strict fall. No alternating subarray can cross it, so the source adds no stitched candidate.

**Trace the useful deletion in the second example**

For `[3,2,1,2,3,2,1]`, remove index 3, whose value is 2. Its new neighbors are 1 and 3, so the bridge is a rise.

The best compatible left run ending at the left neighbor with a fall is `[2,1]`, length 2. The best compatible right run beginning at 3 with a fall is `[3,2]`, also length 2.

Joining them across the new rise gives

`[2,1,3,2]`,

whose comparisons are `fall, rise, fall`. Its length is 4.

The longer-looking portions `[3,2,1]` and `[3,2,1]` cannot both be used because each contains two consecutive falls, so they are not alternating. The directional arrays correctly stop at the incompatible repeated direction.

**Why taking these maxima covers every valid result**

A best result falls into one of two cases.

If no element is removed, or the selected subarray does not cross the removed position, it was already a contiguous alternating subarray of the original array. The left pass records its length in `ans`.

Otherwise, exactly one interior element is removed and the selected subarray crosses the resulting bridge. Its left portion must end with the opposite direction from the bridge, and its right portion must begin with that same opposite direction. The appropriate `l` and `r` states are the maximum possible portions with those requirements, so the source's stitched candidate is at least as long as that result.

Conversely, every stitched candidate is a real alternating subarray after deleting `i`: each side alternates internally, and both boundary directions alternate with the bridge. The computed maximum is therefore attainable and cannot miss a better valid selection.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. Initializing four arrays takes $O(N)$ time. The left pass, right pass, and interior-stitch pass each scan the array once and perform constant work per index. Total running time is $O(N)$.

The four directional arrays each contain $N$ integers, so auxiliary space is $O(N)$. The answer itself is one integer.

The source initializes `ans` to zero, but the constraints guarantee $N\ge2$, so the left pass executes at least once and raises it to at least 1. A length-one subarray is always available.

## Alternatives and edge cases

- **Try every deletion and rescan:** Removing each possible index and finding the longest alternating run costs $O(N^2)$ time.
- **Dynamic programming with a deletion-used flag:** Directional states can be updated in one pass with careful bridge handling, but the left/right decomposition makes the exact compatibility at each deleted index more explicit.
- **Store comparison signs first:** Convert adjacent pairs to rise, fall, or equal, then seek longest alternating sign runs and bridge two signs around a deletion. This is equivalent but requires precise conversion between sign length and element length.
- **No deletion needed:** The left pass records the complete optimum, such as the full array in the first example.
- **Delete an endpoint:** It creates no new adjacency and cannot improve beyond a subarray that already existed, so explicit endpoint stitching is unnecessary.
- **Equal neighboring values:** They reset both directional extensions to length 1 because strict comparison is required.
- **Equal values across the removed index:** Deleting the middle creates an equal bridge, which cannot be crossed by an alternating result.
- **Two-element array:** There is no interior index to test. Unequal values give answer 2; equal values give answer 1.
- **Singleton side of a bridge:** A one-element directional state is compatible with either required direction because it contains no internal comparison.
- **Selected subarray need not use the entire post-deletion array:** The directional arrays choose only the maximal compatible run on each side, and the baseline covers results confined to one side.
- **At most one removal:** The baseline represents zero removals, while every stitched candidate represents exactly one interior removal.
