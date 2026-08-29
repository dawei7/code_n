## General

**Maintain the number of equal pairs in one window**

For each distinct value with frequency $f$ in a subarray, it contributes

$$
\binom f2
$$

equal-index pairs. The current pair total `cur` is the sum across values.

The sliding window has left endpoint `i` and expands one element at a time on the right.

**Add a new rightmost value**

Suppose incoming value `x` already appears `cnt[x]` times in the window. The new occurrence forms one pair with each existing occurrence, so it creates exactly `cnt[x]` new pairs.

The code performs:

`cur += cnt[x]`

before incrementing `cnt[x]`.

Afterward, both the frequency map and `cur` exactly describe the expanded window.

**Know how many pairs removal would destroy**

Let leftmost value `nums[i]` currently have frequency $f$. Removing that one occurrence destroys its pairs with the other $f-1$ equal occurrences.

The hypothetical pair count after removal would be

$$
\texttt{cur}-(f-1)
=
\texttt{cur}-f+1.
$$

This is the loop condition:

`cur-cnt[nums[i]]+1>=k`.

As long as the shortened window would remain good, the algorithm actually removes the leftmost occurrence:

- decrement its count to $f-1$;
- subtract that new count, which equals the destroyed $f-1$ pairs;
- advance `i`.

**Stop at the shortest good suffix ending here**

When shrinking stops and `cur>=k`, current window `[i..right]` is good, but removing its leftmost element would make it bad.

Therefore, `i` is the largest possible start index of a good subarray ending at this right endpoint. Every earlier start `0,1,...,i-1` only adds elements; adding elements can never reduce the number of equal pairs.

So all starts from zero through `i` are good, giving exactly `i+1` good subarrays ending here. The method adds that amount to `ans`.

If `cur<k`, even the full current window beginning at `i` is not good, and no later start can help. Nothing is added.

**Why shrinking before counting is useful**

One common sliding-window formulation keeps the first bad left boundary and counts remaining suffixes. This exact source instead keeps the shortest good window and counts all prefixes extending it leftward.

Both exploit monotonicity, but the variables and formula must match the chosen invariant.

**Trace repeated values**

For five ones and `k=10`, pair totals as the right endpoint grows are 0, 1, 3, 6, and 10. At the final position, removing the leftmost one would leave four ones and six pairs, so the shrink condition fails.

`i` remains zero, and `i+1=1` counts only the whole five-element subarray.

**Why pair counts are monotone under extension**

Adding an element creates a nonnegative number of pairs and never destroys existing pairs. Thus, once a start yields a good subarray for a fixed endpoint, every earlier start is also good.

Similarly, removing from the left can only decrease or preserve pairs. This monotonicity makes a two-pointer boundary possible.


Before counting at each right endpoint:

- `cnt` contains exact frequencies in `nums[i..right]`;
- `cur` is its exact equal-pair count;
- if `cur>=k`, removing `nums[i]` would drop below `k`.

The update formulas preserve exact counts, and the shrink loop establishes minimality. The `i+1` formula then counts every and only good subarray ending at that endpoint. Summing over all endpoints counts each good subarray once.

**Large result**

There can be $n(n+1)/2$ good subarrays, so the answer may exceed 32-bit range. Python integers grow automatically.

**Why the unusual while condition looks ahead**

The loop does not first remove `nums[i]` and then discover whether that was too much. It calculates the exact would-be pair count while the element is still present. Removal happens only when that value remains at least `k`.

This look-ahead preserves a good current window whenever one exists. If the shortened window would be bad, the left endpoint stays where it is and supplies the shortest good suffix. Avoiding an overshoot also avoids having to restore a removed frequency and pair count afterward.

When the current window is already bad, the hypothetical shortened count is no larger and cannot satisfy the loop condition, so shrinking stops automatically.

## Complexity detail

The right endpoint visits each of $n$ elements once. Left endpoint `i` only moves forward and advances at most $n$ times total. Expected counter operations are $O(1)$, so total expected time is $O(n)$.

The counter may store $O(n)$ distinct values, giving $O(n)$ auxiliary space. All other state is constant.

## Alternatives and edge cases

- **Enumerate subarrays:** Maintaining pair counts for every start still costs $O(n^2)$.
- **All values distinct:** `cur` remains zero, so no subarray is good for positive `k`.
- **All values equal:** A length $L$ window has $L(L-1)/2$ pairs.
- **Removal formula:** Removing frequency-$f$ value destroys exactly $f-1$ pairs.
- **Repeated frequencies:** Counter stores occurrences, not merely membership.
- **Minimal good window:** It makes `i+1` the number of valid starts.
- **`cur<k`:** No subarray ending here and starting at or after `i` qualifies.
- **Large `k`:** It may exceed every possible pair count and yield zero.
- **Boolean monotonicity:** Adding elements cannot reduce equal-pair count.
- **64-bit result:** Fixed-width implementations should use a wide accumulator.
