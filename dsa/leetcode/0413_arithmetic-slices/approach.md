## General

**Count slices by their right endpoint**

An arithmetic slice is a contiguous subarray of length at least three whose adjacent differences are all equal. A direct approach could choose every start and end position and then inspect the whole interval, but that repeats the same difference comparisons many times. The optimal solution instead scans adjacent pairs once and asks a local question at every step:

> How many arithmetic slices become valid for the first time when the current element is used as their right endpoint?

Every slice has exactly one right endpoint, so adding these per-endpoint counts counts every valid slice exactly once.

The loop uses `pairwise(nums)`. It yields `(nums[0], nums[1])`, then `(nums[1], nums[2])`, and so on. For each pair `(a, b)`, the current adjacent difference is `b - a`. The variable `d` stores the preceding adjacent difference, while `cnt` stores the number of arithmetic slices ending at the previous element that can be extended through the current equal difference.

**Why equal consecutive differences create new slices**

Suppose the preceding difference and the current difference are equal. The last three elements then have equal adjacent differences, so they form one new length-three arithmetic slice. In addition, every arithmetic slice that ended at the previous element can be extended by the current element. Extension preserves contiguity, and the new final difference matches the common difference already used by that slice.

If `cnt` such extendable slices existed before processing the current pair, the current element creates `cnt + 1` slices:

- `cnt` longer slices obtained by extending the old ones; and
- one new three-element slice formed by the newest two equal differences.

The statement `cnt += 1` produces exactly this new count. The following `ans += cnt` adds all slices whose right endpoint is the current element to the global answer.

For `nums = [1,2,3,4]`, the pair differences are `1,1,1`. The first difference only establishes a possible common difference, so it contributes no slice. At the second equal difference, `cnt` becomes `1`, representing `[1,2,3]`. At the third equal difference, `cnt` becomes `2`, representing the newly completed `[2,3,4]` and the extension `[1,2,3,4]`. The total is `1 + 2 = 3`.

This also explains why the algorithm does not merely add one for each matching difference. A long arithmetic run contains overlapping slices of several lengths. `cnt` preserves exactly how many earlier starting positions remain valid for the current endpoint.

**Why a changed difference resets the state**

When `b - a != d`, no arithmetic slice ending before `b` can be extended through this pair: its last adjacent difference would disagree with the new one. The solution therefore stores the new difference in `d` and sets `cnt = 0`.

Zero is correct rather than one because a single adjacent pair contains only two elements. It establishes the first difference of a possible future slice but does not yet meet the minimum length of three. If the next pair has this same new difference, `cnt` will increase from zero to one, counting the first length-three slice of the new run.

Changing the difference does not erase slices already counted in `ans`. Those slices have earlier right endpoints and remain valid answers; only the extendable suffix state is reset.

**The purpose of the `3000` sentinel**

Before any pair has been processed, there is no preceding difference. The implementation initializes `d = 3000` to make the first comparison fail deliberately. The constraints give

$$
-1000 \le \texttt{nums}[i] \le 1000,
$$

so any real adjacent difference lies between $-2000$ and $2000$. Therefore `3000` cannot equal a legitimate first difference. The first pair always enters the reset branch, records its real difference, and leaves `cnt` at zero.

This avoids a separate special case for the first pair. The choice is safe only because it is outside the complete permitted difference range; an arbitrary in-range sentinel could falsely make a two-element prefix look like it had two equal differences.

**A run-length view of the same counting rule**

Suppose a maximal arithmetic run contains $L$ elements. It has $L-1$ identical adjacent differences. After the first difference establishes the run, the remaining differences make `cnt` take values

$$
1,2,\ldots,L-2.
$$

Their sum is

$$
1+2+\cdots+(L-2)=\frac{(L-1)(L-2)}{2}.
$$

That is also the number of contiguous subarrays of length at least three inside the run. The incremental update computes this triangular number while scanning, without needing to know in advance where the run ends.

**Why the answer is correct**

After each processed adjacent pair, `cnt` equals the number of arithmetic slices ending at the pair's second element that use the current difference. This is true initially because the first pair cannot form a slice and `cnt` is zero. If the next difference changes, no previous slice extends and the invariant resets to zero. If it matches, every old ending slice extends and exactly one new length-three slice appears, so incrementing `cnt` preserves the invariant.

`ans` accumulates these ending-at-current counts. Every arithmetic slice is added when its final element is processed, and no slice can be added at two different endpoints. Therefore the final `ans` is exactly the number requested.

## Complexity detail

Let $n$ be the number of elements in `nums`. `pairwise(nums)` exposes $n-1$ adjacent pairs when $n \ge 2$, and the loop performs constant work for each. The time complexity is $O(n)$.

The algorithm stores only `ans`, `cnt`, `d`, and the current pair. These do not grow with the input, so the auxiliary-space complexity is $O(1)$. The iterator returned by `pairwise` is lazy and does not create a separate list of all pairs.

The output is a single integer. Python integers grow as needed, although the stated length bound keeps the maximum number of slices well within an ordinary manageable range.

## Alternatives and edge cases

- **Enumerate every subarray and verify it:** This can take $O(n^3)$ time because there are $O(n^2)$ candidate intervals and each may require an $O(n)$ scan. It repeats comparisons that the running state preserves.
- **Fix each start and extend until a mismatch:** Reusing the established difference improves the brute force to $O(n^2)$ time, but it still revisits long arithmetic runs from many starting positions.
- **Full dynamic-programming array:** Store at every index the number of arithmetic slices ending there. This is $O(n)$ time and $O(n)$ space. Only the previous state is required, so `cnt` compresses it to constant space.
- **Count each maximal run with a formula:** Track the run length and add its triangular count when the difference changes. This also reaches $O(n)$ time and $O(1)$ space, but the incremental endpoint count avoids a final flush special case.
- **Fewer than three elements:** `pairwise` yields at most one pair, `cnt` never becomes positive, and the correct result is zero.
- **Constant-valued array:** Every difference is zero. Zero is a valid common difference, and the same recurrence counts all qualifying subarrays.
- **Negative common difference:** Subtraction and equality work identically for decreasing arrays; no assumption of increasing values is made.
- **Difference changes and later returns:** A mismatch resets `cnt`. A later occurrence of the old difference begins a new run and cannot connect across the intervening mismatch.
- **Sentinel safety:** `3000` is outside the possible $[-2000,2000]$ range. If the value constraints changed, this sentinel would need reevaluation or replacement with an explicit “no previous difference” state.
- **Contiguous requirement:** The adjacent-pair scan counts only subarrays. It never skips elements, so it does not accidentally count arithmetic subsequences.
