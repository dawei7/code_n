## General

**Work from the direction in which useful sums become known**

An allowed operation merges a left value into its immediate right neighbor when the left value is no larger. The merged value is their sum and occupies the right side.

To decide whether an element can join a larger block to its right, it is useful to know the greatest value that right block can already become. That information is available naturally when scanning from right to left. The exact solution processes indices `n - 2` down through zero.

**Interpret the mutated entries as suffix-block values**

At index `i + 1`, after the right-to-left processing already completed there, `nums[i + 1]` represents the maximum merged value obtainable for the contiguous mergeable block beginning at `i + 1`.

The code checks:

`if nums[i] <= nums[i + 1]`.

If true, first realize the right block's merges, producing value `nums[i + 1]` immediately to the right of `nums[i]`. The operation condition is satisfied, so `nums[i]` can merge into that block. Their combined value is stored as:

`nums[i] += nums[i + 1]`.

The source stores the conceptual block sum at its leftmost original index even though actual forward operations leave the sum at the right endpoint. This is a dynamic-programming representation, not a literal simulation of array positions.

**Why making the right value as large as possible is always helpful**

All numbers are positive. Merging within the right block increases its value. A larger immediate right value:

- makes condition `nums[i] <= rightValue` easier to satisfy;
- produces a larger sum if the merge succeeds.

There is no advantage to keeping a smaller attainable right-block value. If `nums[i]` cannot be merged into the maximum possible right block, it cannot be merged by choosing fewer positive merges and making that neighbor smaller.

This monotonicity is what makes the greedy right-to-left consolidation safe.

**What happens at a failed boundary**

If `nums[i] > nums[i + 1]`, the left value cannot merge into the best consolidated block immediately to its right. The code leaves `nums[i]` unchanged.

That position becomes the start of a different candidate block. When the scan later reaches `i - 1`, it may still merge into `nums[i]` if its value is small enough. Thus a failed boundary separates rightward blocks but does not end the whole computation.

**A walkthrough**

For `nums = [2, 3, 7, 9, 3]`:

- Begin at index three: 9 is greater than 3, so no mergeable block crosses that boundary.
- At index two: 7 is no larger than 9, so store `7 + 9 = 16` at index two.
- At index one: 3 is no larger than 16, so store 19.
- At index zero: 2 is no larger than 19, so store 21.

The mutated list contains representations of overlapping suffix blocks, and its maximum is 21. A real operation sequence can realize it by merging 7 into 9, then 3 into 16, then 2 into 19, with indices shifting as deletions occur.

For `[5, 3, 3]`:

- The last pair merges because 3 <= 3, producing represented value 6 at index one.
- Then 5 <= 6, producing 11 at index zero.

The answer is 11.

**Why entries need not be deleted in the simulation**

Physically deleting elements would shift indices and add implementation complexity. The right-to-left DP needs only one number from the processed suffix: the consolidated value adjacent to the current position.

Leaving old entries in `nums` does not cause false future transitions because the scan always compares index `i` with exactly `i + 1`, where the required block representation was stored. At the end, stale interior representations cannot exceed the larger positive sum stored at the left edge of any block that absorbed them.

**Why returning `max(nums)` is necessary**

The first array element is not guaranteed to join everything. Failed boundaries can leave several separate final blocks. Each mutated entry at a block start represents a value that can be achieved as one final element.

Taking the maximum across the list selects the largest attainable block sum. Returning only `nums[0]` would be wrong when the best block starts later.

**Why the greedy recurrence is correct**

Assume `nums[i + 1]` is the largest value attainable by a mergeable block beginning there. If `nums[i] <= nums[i + 1]`, realizing that block and merging `nums[i]` produces their total, which is optimal because all terms are positive and no smaller right realization gives a larger result. If the inequality fails against this maximum, no legal realization of the immediate right block can accept `nums[i]`, so the best block beginning at `i` is just the current value until possibly combined from farther left later.

Backward induction establishes the stored block meanings. Every stored combined value corresponds to a legal operation sequence, and every possible larger block would have to cross the same immediate boundaries the recurrence tests. The maximum stored value is therefore the largest achievable final element.

## Complexity detail

The backward loop visits each of the `n - 1` adjacent boundaries once and performs constant work. The final `max(nums)` scan visits `n` values. Total time complexity is `O(n)`.

The algorithm uses only the loop index and mutates `nums` to store block sums, so auxiliary space is `O(1)`. The mutation is observable to the caller; the list no longer necessarily contains its original values after the function returns.

Python integers grow as sums grow, so a block total exceeding fixed-width integer ranges remains exact.

## Alternatives and edge cases

- **Explicitly delete and merge:** It follows the operation statement literally but can shift array contents repeatedly and degrade to quadratic time.
- **Separate DP array:** Store block sums without mutating input, using `O(n)` additional space.
- **Left-to-right greed:** A current right neighbor may later become much larger through suffix merges, information a forward pass does not yet know.
- **All boundaries merge:** The leftmost stored sum becomes the total of the entire array.
- **No boundary merges:** Every entry stays unchanged and the answer is the original maximum.
- **Equal adjacent values:** The `<=` condition allows their merge.
- **Failed boundary followed by earlier success:** A left value may merge into the block starting at the failed boundary even though that block cannot merge farther right.
- **Single-element input:** The loop is empty and `max` returns that element.
- **Positive-value guarantee:** It makes maximizing the right block always helpful. Negative values would invalidate that monotonic argument.
- **Input mutation:** Callers needing the original array must pass a copy; the exact solution intentionally reuses it as DP storage.
- **Conceptual position:** Stored sums sit at left block starts for computation, even though literal operations leave sums at right endpoints.
- **Largest block not at zero:** Final `max` considers every block start.
