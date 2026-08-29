## General

**View a swap as a gain applied to one array's original sum**

Suppose the chosen interval is copied from `nums1` into `nums2`. At every index `i` in that interval, `nums2[i]` is removed from the second array's sum and `nums1[i]` is added. The net change is

`nums1[i] - nums2[i]`.

Across a contiguous interval, the total gain is the sum of this elementwise difference over that interval. Therefore the best possible final sum of `nums2` is its original sum plus the maximum subarray sum of

`nums1 - nums2`.

The opposite target direction is symmetric. To maximize the final sum of `nums1`, use the maximum subarray sum of `nums2 - nums1`.

The helper `f(nums1, nums2)` computes the first kind of gain. The outer method calls it once in each direction and chooses the larger resulting target sum.

**Build the difference array for one direction**

The list comprehension

`d = [a - b for a, b in zip(nums1, nums2)]`

creates one gain value per index. Because the arrays have equal length, `zip` pairs every position. If `d[i]` is positive, transferring the element from the first argument into the second target helps that target at this index. If it is negative, the local transfer hurts, but it may still belong to a profitable larger contiguous interval.

The swap interval must be contiguous, so individual positive differences cannot simply be collected from unrelated positions. Finding the best contiguous sum is exactly the maximum-subarray problem.

**Kadane's algorithm chooses whether to extend or restart**

The helper initializes `t` and `mx` to `d[0]`. Here `t` is the maximum sum of a nonempty subarray ending at the most recently processed position, and `mx` is the maximum sum of any nonempty subarray seen so far.

For each next difference `v`:

- if `t > 0`, extending the previous ending subarray with `v` produces a larger sum than starting at `v` alone, so the code uses `t += v`;
- otherwise, the previous prefix contributes nothing helpful or actively hurts, so the best ending subarray restarts with `t = v`.

Then `mx = max(mx, t)` preserves the best interval ending anywhere up to the current position.

Using `t > 0` rather than `t >= 0` does not change the numeric result. Extending a zero-sum prefix and restarting at `v` produce the same sum `v`; the code chooses the simpler restart path.

Because the source arrays are nonempty, `d[0]` exists. Initializing from it makes this a maximum nonempty subarray, matching the required nonempty swap interval when an operation is chosen.

**Evaluate both possible target arrays**

Let `s1` and `s2` be the original sums.

`s2 + f(nums1, nums2)` is the greatest sum the second array can obtain by receiving one contiguous segment from the first.

`s1 + f(nums2, nums1)` is the greatest sum the first array can obtain by receiving one contiguous segment from the second.

The score after a swap is the larger of the two resulting array sums. To maximize the score, it is enough to maximize either target array and then take the larger of those two best possibilities. The final `max` does exactly that.

The sum of both arrays is conserved by a swap, but maximizing one target is still the right viewpoint because the score asks only for the larger final sum.

**Why “do nothing” is not lost even though Kadane uses a nonempty interval**

The operation is optional, but the return expression does not explicitly include `s1` or `s2`. It remains correct because swapping the entire arrays is a legal interval and leaves the pair of array sums exchanged, so the score remains `max(s1, s2)`.

More algebraically, the full difference sum `sum(nums1 - nums2) = s1 - s2` is one candidate subarray for `f(nums1, nums2)`. Hence `s2 + f(nums1, nums2) >= s1`. In the reverse direction, `s1 + f(nums2, nums1) >= s2`. The maximum of the two candidates is therefore at least the original no-swap score.

So even if the best local gain in one direction is negative, the two-direction comparison still includes a result at least as good as doing nothing.

**Why the maximum-subarray reduction is exact**

Every legal swap interval changes the target sum by exactly the sum of the corresponding difference interval, so no swap can outperform the maximum subarray gain computed by Kadane.

Conversely, the interval achieving Kadane's maximum is a legal contiguous swap. Performing it realizes exactly the calculated target sum. Evaluating both target directions covers whichever of the two final arrays supplies the score. Therefore the returned maximum is achievable and no legal operation can exceed it.

## Complexity detail

Let `n` be the common array length. Each helper call builds a length-`n` difference list and scans it once. The exact scan uses `d[1:]`, which also constructs a slice containing `n - 1` values. Two helper calls plus two input sums still perform only a constant number of linear passes, so total time is `O(n)`.

The conceptual Kadane state `t` and `mx` is `O(1)`, but the exact implementation materializes `d` and the temporary slice `d[1:]`. Its peak auxiliary space is therefore `O(n)`, not the manifest's stated `O(1)`. A streaming loop over `zip(nums1, nums2)`, or an index loop without a difference list or slice, would achieve genuine constant auxiliary space.

The original arrays are only read. The difference list is separate, so this method does not mutate either input.

Input values and sums fit comfortably in Python integers. In fixed-width languages, sums can reach roughly `10^9` under the stated constraints and should still be stored in an appropriately wide type.

## Alternatives and edge cases

- **Streaming Kadane in each direction:** Compute each difference as it is scanned and keep only current and best gains. This implements the same algorithm in `O(n)` time and `O(1)` auxiliary space.
- **Prefix sums and all interval pairs:** A prefix-difference array makes any interval gain constant-time, but enumerating `O(n^2)` intervals remains too slow. Kadane finds the best interval in one pass.
- **Swap only individually profitable indices:** Chosen indices must form one contiguous subarray. Skipping a negative middle position may be illegal even when positive values appear on both sides.
- **Check only improvement to the initially larger-sum array:** The initially smaller array may receive a segment that makes it the new larger array and produces the optimal score. Both directions are required.
- **Use the same difference direction for both targets:** Gains reverse sign when the receiving array changes. `nums1 - nums2` improves `nums2`, while `nums2 - nums1` improves `nums1`.
- **Allow an empty Kadane subarray with gain zero:** This is another clean way to encode the optional operation. The exact code uses nonempty Kadane, but full-array swapping and the two directions already preserve the no-swap score.
- **All differences positive in one direction:** Kadane takes the entire interval. This swaps the complete arrays in that direction and transfers the full sum difference.
- **All differences negative in one direction:** That helper returns the least harmful single index, but the reverse helper has all positive differences and covers the useful or no-worse choice.
- **Equal arrays:** Every difference is zero, both candidates equal the common original sum, and any swap or no swap has the same score.
- **One element:** The only nonempty interval is the full array. Swapping exchanges the two values, so the maximum score remains the larger input value; the formula produces it.
- **Zero current sum in Kadane:** Restarting rather than extending changes only the represented interval boundary, not the gain value or final answer.
- **Exact-source allocation:** Both the difference comprehension and `d[1:]` consume linear temporary storage. Describing only the two scalar Kadane variables would understate the literal Python implementation.
- **Input mutation:** No sorting or assignment touches `nums1` or `nums2`; only newly created difference data is changed through scalar variables.
