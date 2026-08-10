## General

**A monotonic subarray is an adjacent run.** Because the answer must be a subarray, its elements are contiguous. A strictly increasing run continues only while each next value is greater than the immediately previous value. A strictly decreasing run continues only while each next value is smaller. One failed adjacent comparison ends every longer run of that direction crossing the boundary.

The exact source handles the two directions in two separate passes. This differs from the local manifest's description of tracking both directions together, but it computes the same desired maximum.

**First pass: longest strictly increasing run.** The source initializes `ans = t = 1`. Every nonempty array has a one-element subarray, and a singleton is vacuously both strictly increasing and strictly decreasing.

It iterates through `enumerate(nums[1:])`. The sliced value `x` is logically `nums[i + 1]`, while `nums[i]` is its immediate predecessor in the original array.

If `nums[i] < x`, the adjacent pair is strictly increasing. The current increasing run ending at `nums[i]` can extend to `x`, so `t += 1`. The source updates `ans` with this length.

Otherwise, the current value cannot belong to an increasing subarray that crosses the pair. This includes both a decrease and an equality. The longest increasing run ending at the current value restarts as the singleton, so `t = 1`.

After this pass, `ans` is the longest strictly increasing subarray length seen anywhere.

**Second pass: longest strictly decreasing run.** The source resets `t = 1` and traverses a newly created `nums[1:]` slice again. This time it extends when `nums[i] > x`. Every other comparison resets the decreasing run to one.

`ans` is not reset. It already holds the best increasing length and is updated with every decreasing length. On completion it is the maximum over both categories, exactly what the task requests.

**Why equality resets both directions.** Strict monotonicity excludes equal adjacent values. A pair such as `3,3` is neither increasing nor decreasing, so no length-two-or-longer valid subarray can cross it. Each pass's `else` branch correctly resets to a singleton.

**A run-length invariant.** During the first pass, after processing the pair ending at original index $r$, `t` equals the length of the longest strictly increasing subarray ending at $r$. If the new pair rises, appending the value extends the previous run by one. If not, no earlier start can cross the failed boundary, so only length one remains. This proves the update by induction.

The identical argument with reversed inequality holds in the second pass for decreasing subarrays. Since every valid subarray has an ending index and a direction, taking the maximum of these ending-at-index run lengths covers all candidates.

**A trace for `[1,4,3,3,2]`.** In the increasing pass, `1 < 4` extends `t` to two and sets `ans=2`. The comparison `4 < 3` fails, then `3 < 3` fails, and `3 < 2` fails, so no longer increasing run exists.

In the decreasing pass, `1 > 4` fails. `4 > 3` extends to two. Equality between the two threes resets the run. The final `3 > 2` extends to two. The global answer stays two.

For `[3,2,1]`, the increasing pass never exceeds one. The decreasing pass extends from one to two to three, so the method returns three.

For `[3,3,3,3]`, both passes reset on every pair and `ans` remains one.

**Why two passes are sufficient.** A valid answer is either increasing or decreasing; there is no third direction and no requirement to switch direction within a subarray. A mountain such as `[1,3,2]` is not strictly monotonic as a whole, though each length-two side is a valid candidate. Evaluating the two pure-direction run types separately and taking their maximum is exhaustive.

**The indexing trick in `enumerate(nums[1:])`.** On the sliced sequence, loop index zero corresponds to original index one. Therefore, comparing `nums[i]` with current `x` compares original positions zero and one. At general loop index $i$, `x` comes from original $i+1$, so the code always checks adjacent original elements. This is correct, but a direct index loop would make the relationship more obvious and avoid slicing.

## Complexity detail

Each pass examines $n-1$ adjacent pairs and performs constant work, so total time is $O(n)$.

The local manifest claims $O(1)$ auxiliary space, but the exact Python source evaluates `nums[1:]` separately for each pass. A list slice allocates a new list of $n-1$ references. The first slice can be released before the second is created, so peak additional space is $O(n)$ rather than $O(2n)$, but it is not $O(1)$.

A direct loop over `range(1, len(nums))` or a lazy `pairwise(nums)` traversal would preserve the same logic with constant auxiliary space. The checked-in implementation's actual space bound must include its slice.

## Alternatives and edge cases

- **One combined pass:** Maintain increasing and decreasing run lengths simultaneously, resetting the opposite one after each comparison. This matches the manifest summary and uses half as many comparisons.
- **`pairwise(nums)` in two passes:** It avoids list slices, though a fresh iterator is needed for each traversal.
- **Brute force from every start:** Extend increasing and decreasing candidates until failure, taking $O(n^2)$ time.
- **Single element:** Both loops are empty and initialization correctly returns one.
- **Equal adjacent elements:** They reset both directional runs because the inequalities are strict.
- **Entire array increasing:** The first pass grows `t` to $n$; the second cannot reduce `ans`.
- **Entire array decreasing:** The second pass grows to $n$.
- **Direction change:** The old directional run ends, but a new run may start with the current element as length one and extend on later pairs.
- **Mountain or valley:** The whole shape is not valid; the method returns the longer pure-direction side.
- **Two elements:** One of less, greater, or equal applies, yielding answer two for unequal values and one for equal values.
- **Why `ans` is retained:** It combines the best increasing result with later decreasing candidates.
- **Why `t` is reset between passes:** An increasing run length has no meaning as starting state for the decreasing scan.
- **Slice indexing:** Loop `i` refers to the predecessor in the original list, while `x` is original `nums[i + 1]`.
- **Input mutation:** Slices copy references but the source never changes any element.
- **Manifest space discrepancy:** The abstract run algorithm is constant-state, but the exact list slicing makes auxiliary space linear.
