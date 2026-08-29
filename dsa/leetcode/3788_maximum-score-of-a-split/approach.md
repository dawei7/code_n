## General

**Precompute the minimum to the right of every boundary**

For split index `i`, the prefix ends at `i` while the suffix begins at `i+1`. The score needs the minimum value in that entire suffix.

The source creates `suf` so that

$$
\texttt{suf}[i]=\min(\texttt{nums}[i],\ldots,\texttt{nums}[N-1]).
$$

It initializes every position with `nums[-1]` and then fills indices from `n-2` down to zero using

`suf[i] = min(nums[i], suf[i+1])`.

The last position is correct initially because a one-element suffix has that element as its minimum. If `suf[i+1]` is the minimum from `i+1` onward, comparing it with `nums[i]` gives the minimum from `i` onward. This backward recurrence establishes the whole array.

For `[4,2,7,1]`, initialization places 1 at the last position. Moving left produces `suf[2]=min(7,1)=1`, then `suf[1]=min(2,1)=1`, and finally `suf[0]=min(4,1)=1`. This trace shows that a distant minimum propagates through every earlier suffix that contains it.

**Build each prefix sum incrementally**

The second loop scans valid split indices `0` through `n-2`. Before evaluating index `i`, it adds `nums[i]` to `pre`.

After this update,

$$
\texttt{pre}=\sum_{j=0}^{i}\texttt{nums}[j],
$$

which is exactly `prefixSum(i)`. The required suffix minimum is `suf[i+1]`, not `suf[i]`, because the split element belongs to the prefix.

The candidate is therefore

`pre - suf[i+1]`.

Each iteration updates `ans` with the larger of its current value and this candidate.

**Keep prefix and suffix roles separate**

The score subtracts one suffix value—the minimum—not the suffix sum. The precomputation stores only minima, while `pre` stores only the cumulative prefix total.

For `[10,-1,3,-4,-5]`, suffix minima are `[-5,-5,-5,-5,-5]`. At split two, `pre=12` and the suffix beginning at three has minimum -5, giving $12-(-5)=17$.

At split three, the prefix becomes eight and the suffix minimum remains -5, giving 13. The running maximum correctly retains 17.

**Initialize for negative answers**

`ans` starts at negative infinity rather than zero. Scores may all be negative because array values may be negative.

For `[-7,-5,3]`, split zero scores $-7-(-5)=-2$, while split one scores $-12-3=-15$. Initializing to zero would incorrectly return an unattainable score. Negative infinity guarantees the first valid split is recorded.

There is always at least one split because `n>=2`, so `ans` is finite before return.

**Why every candidate is exact and every split is visited**

The backward induction proves `suf[i+1]` is the exact minimum over the right side of split `i`. The forward accumulation proves `pre` is the exact sum over its left side.

The loop range `range(n-1)` includes every legal index and excludes `n-1`, whose suffix would be empty. Thus each valid split produces one accurate score and no invalid split is considered. Taking their maximum returns the required value.

At the beginning of each forward iteration, `pre` contains the sum through the preceding index. Adding `nums[i]` before evaluating the score is therefore essential: evaluating first would use a prefix ending at `i-1` and shift every split definition by one.

**The manifest describes different storage**

The manifest summary says the solution scans from right to left while maintaining suffix state and gives $O(1)$ space. The exact source allocates the length-$N$ array `suf` and then performs a separate left-to-right prefix scan.

Its time remains $O(N)$, but its actual auxiliary space is $O(N)$. No suffix sum is maintained despite the manifest wording.

## Complexity detail

Filling `suf` takes $O(N)$ time. Evaluating all $N-1$ split points also takes $O(N)$ time, so total time is $O(N)$.

The suffix-minimum array stores $N$ integers, giving $O(N)$ auxiliary space. All other state is scalar. The input array is not modified.

Prefix sums and scores can exceed 32-bit range; Python integers expand automatically.

## Alternatives and edge cases

- **Right-to-left constant-space scan:** With the total sum and a running suffix minimum, one can evaluate splits without storing every suffix minimum. That matches the manifest space claim but is not the exact source.
- **Recompute each suffix minimum:** Calling `min(nums[i+1:])` for every split can cost $O(N^2)$ and allocate repeated slices.
- **Use suffix sum instead of minimum:** The contract subtracts one minimum value, not the suffix total.
- **Use `suf[i]`:** That incorrectly allows the split element itself into the suffix minimum.
- **Initialize answer to zero:** All legal scores may be negative.
- **Two-element array:** There is one split; `pre=nums[0]` and `suf[1]=nums[1]`.
- **All positive values:** A later prefix can grow, but its shrinking suffix may also change the minimum; every split is still needed.
- **All negative values:** Subtracting a negative suffix minimum can raise the score, but the maximum may remain negative.
- **Repeated minima:** The recurrence preserves their value without needing positions.
- **Minimum at the final element:** It propagates left through every suffix containing it.
- **Large magnitudes:** Python arithmetic safely handles cumulative sums.
- **Input preservation:** Only `suf` and scalars are updated.
- **Source/manifest mismatch:** The exact file uses linear auxiliary storage.
