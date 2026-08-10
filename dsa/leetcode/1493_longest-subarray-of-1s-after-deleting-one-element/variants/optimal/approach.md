## General

**Reframing the mandatory deletion**

Exactly one array element must be removed. For any chosen deletion index `i`, the only all-ones subarray that can become newly connected across that gap consists of consecutive ones immediately to the left of `i` plus consecutive ones immediately to its right.

If `nums[i]` is zero, deleting it can join two neighboring runs of ones. If `nums[i]` is one, deletion shortens a run by one, which is necessary when the entire array is ones. The stored solution evaluates every possible deletion index efficiently by precomputing the two run lengths needed for each candidate.

**Meaning of the left array**

`left` has length `n + 1` and begins filled with zeros. Its meaning is:

> `left[i]` is the number of consecutive ones immediately before original index `i`.

The first loop uses `enumerate(nums, 1)`, so the first array value is paired with `i = 1`. If that value is one, `left[1] = left[0] + 1`. More generally, original value `nums[i - 1]` contributes to `left[i]`.

When the current value is one, extending the previous consecutive run is correct. When it is zero, the conditional assignment is skipped and the prefilled zero remains, correctly breaking the run. The extra slot at `left[0]` acts as a zero-length boundary before the array and removes the need for a special case at the first element.

For example, with `nums = [1, 1, 0, 1]`, `left` becomes `[0, 1, 2, 0, 1]`. At deletion index two, `left[2]` says that two consecutive ones lie immediately before the zero.

**Meaning of the right array**

`right` also has length `n + 1`. The reverse loop visits original indices from `n - 1` down to zero. Its meaning is:

> `right[i]` is the number of consecutive ones beginning at original index `i`.

If `nums[i]` is one, the run consists of that one plus the run beginning at `i + 1`, so the code assigns `right[i] = right[i + 1] + 1`. If the value is zero, the prefilled zero remains. The extra `right[n]` slot represents the empty boundary after the array.

For the same example, `right` begins with run values corresponding to two ones before the zero and one after it. The boundary entry makes `right[i + 1]` safe even when deleting the final element.

**Evaluating each deletion**

The final generator considers every original index `i` and computes

`left[i] + right[i + 1]`.

`left[i]` counts consecutive ones ending immediately before the deleted position. `right[i + 1]` counts consecutive ones starting immediately after it. Once index `i` is removed, those two regions become adjacent.

When the deleted element is zero, their sum is the length of the bridged all-ones run. When the deleted element is one, each side belongs to the original run around that one, and the sum is that run's length minus one. When there is a zero adjacent to one side, that side's precomputed value is zero, so the formula still works without branching.

Taking `max` over all deletion positions chooses the best valid result. The constraints guarantee `n \ge 1`, so the generator is nonempty and `max` is well-defined.

**Why examining only the immediate runs is sufficient**

After deleting one position, elements retain their relative order. The only formerly separated positions that become adjacent are `i - 1` and `i + 1`. Therefore, an all-ones subarray affected by the deletion can extend left only until the nearest zero and right only until the nearest zero. Those exact maximal lengths are stored in `left[i]` and `right[i + 1]`.

Any all-ones subarray elsewhere in the resulting array also corresponds to choosing a deletion outside that run. The method evaluates every deletion index, including such choices, so the maximum cannot miss it. Thus the formula covers both newly joined runs and untouched runs under the mandatory deletion.

## Complexity detail

Let $N$ be the array length. The forward loop visits each element once, the reverse loop visits each element once, and the final maximum evaluates $N$ deletion candidates. Three linear passes give $O(N)$ time.

The two arrays each contain $N+1$ integers, so the exact implementation uses $O(N)$ auxiliary space. The generator passed to `max` is lazy and does not create another $N$-element candidate list.

The manifest states $O(N)$ time and $O(1)$ space. Its time bound matches, but its space bound does not match the stored prefix-and-suffix arrays. A sliding window that permits at most one zero can achieve constant auxiliary space. This distinction matters: boundary padding makes the current code clear and safe, but it is still linear storage.

## Alternatives and edge cases

- **Sliding window with at most one zero:** Move a right pointer forward and shrink the left boundary whenever the window contains more than one zero. The best post-deletion length is window length minus one, giving $O(N)$ time and $O(1)$ space.
- **Track adjacent one-run lengths:** Maintain the current and previous runs separated by a zero. This can also use constant space, though its state transitions are easier to mishandle than the window.
- **Delete every index and rescan:** It directly follows the definition but costs $O(N^2)$ time.
- **All ones:** Every candidate deletes one of the ones, and the maximum becomes $N-1$, correctly enforcing that one deletion is mandatory.
- **Single element:** Whether that element is zero or one, deleting it leaves no nonempty all-ones subarray, so the answer is zero.
- **All zeros:** Both adjacent-run lengths are zero for every deletion, producing zero.
- **One zero between two runs:** Deleting that zero joins the complete left and right runs, and the formula adds their lengths.
- **Zero at an endpoint:** One side is the padded boundary value zero, while the other side contributes the adjacent run.
- **Deleting a one:** The two neighboring pieces of its original run add to the run length minus one.
- **Boundary padding:** Arrays of length $N+1$ make `left[0]` and `right[N]` valid sentinels and prevent out-of-range access.
