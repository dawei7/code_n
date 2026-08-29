## General

**Translate the remaining-sum condition**

Let the total array sum be $S$, and let:

$$
k=S\bmod p.
$$

If $k=0$, the total is already divisible by `p`. Removing the empty subarray is allowed, so the solution immediately returns zero.

Otherwise, suppose a subarray with sum $X$ is removed. The remaining sum is divisible by `p` exactly when:

$$
(S-X)\bmod p=0.
$$

Since $S\bmod p=k$, this is equivalent to:

$$
X\bmod p=k.
$$

The task is therefore to find the shortest proper subarray whose sum has remainder `k` modulo `p`.

**Express a subarray through prefix remainders**

Let the prefix remainder through index `i` be:

$$
P_i=(\texttt{nums}[0]+\cdots+\texttt{nums}[i])\bmod p.
$$

For a subarray from `j + 1` through `i`, its sum modulo `p` is:

$$
(P_i-P_j)\bmod p.
$$

We want that value to equal `k`. Rearranging gives:

$$
P_j\equiv P_i-k\pmod p.
$$

When the current prefix remainder is `cur`, the source computes the required earlier remainder as:

`target = (cur - k + p) % p`.

Adding `p` before taking the modulus prevents a negative intermediate representation. Python’s modulus would already produce a nonnegative result for positive `p`, but the formula is portable and explicit.

**What the dictionary stores**

`last` maps a prefix remainder to the latest index where that remainder occurred. It starts as `{0: -1}`. Index negative one represents the empty prefix before the array, whose sum is zero. This sentinel allows a removable subarray beginning at index zero: if the needed prior remainder is zero, its length is `i - (-1) = i + 1`.

During the scan, `cur` is updated with:

`cur = (cur + x) % p`.

If `target` exists in `last` at index `j`, then the subarray `j + 1` through `i` has the required remainder `k`. Its length is `i - j`, and `ans` keeps the minimum.

After checking, the assignment `last[cur] = i` records the current prefix as the most recent occurrence of its remainder.

**Why the latest occurrence is the useful one**

For a fixed ending index `i` and required earlier remainder, every matching prefix index produces a valid remainder. To minimize removed length `i - j`, we want the largest possible `j`. Therefore, overwriting an older index with the current one is not information loss; the newer occurrence is always at least as good for every future endpoint.

This latest-index rule is what lets one dictionary entry per remainder support shortest-subarray optimization.

The lookup happens before the current index is stored. Since `k != 0` after the early return, `target` cannot equal `cur` modulo `p`, so the current prefix would not falsely create a zero-length answer anyway. The check-then-store order also matches the standard invariant that `last` describes prefixes ending strictly before the current position.

**A trace of the first example**

For `nums = [3,1,4,2]` and `p = 6`, the total remainder is `k = 4`. Initially `last = {0: -1}`.

- After three, `cur = 3` and target is five. No prefix has remainder five, so remainder three is stored at index zero.
- After one, `cur = 4` and target is zero. The sentinel gives a candidate prefix removal of length two.
- After four, `cur = 2` and target is four. Remainder four was last seen at index one, so removing index two alone has length one. This is the subarray `[4]`.
- The final scan cannot improve on length one.

The returned result is one.

**Why the whole array is rejected**

`ans` begins as `len(nums)`. The sentinel can identify the entire array as a remainder-`k` subarray, since removing it always leaves sum zero. That candidate has length exactly $N$, so taking `min(ans, N)` leaves `ans` equal to $N$.

At the end, the source returns `-1` when `ans == len(nums)`. This simultaneously means no proper qualifying subarray was found and enforces the rule that the entire array may not be removed.

If a shorter valid subarray exists, `ans < N` and its length is returned.

**Why the scan is correct**

Every candidate found through `last[target]` satisfies the modular equation, so removing it leaves a sum divisible by `p`. Conversely, take any valid removable subarray ending at `i` and let `j` be the prefix index immediately before it. Its earlier remainder must equal the computed `target`. When `i` is processed, `last` contains either `j` or a later index with the same remainder. The latter yields an equally valid, shorter subarray. Thus the scan finds a candidate no longer than every valid subarray and `ans` becomes the global minimum.

The final $N$ rejection removes only the forbidden whole-array choice, establishing the returned result.

## Complexity detail

Let $N$ be the length of `nums`.

`sum(nums)` takes $O(N)$ time. The subsequent loop visits each element once and performs expected $O(1)$ dictionary operations, taking another $O(N)$. Total expected time is $O(N)$.

A prefix remainder can take only `p` possible values, and the scan creates at most one stored entry per processed prefix plus the sentinel. Therefore, the dictionary holds $O(\min(N,p))$ distinct remainder keys. Auxiliary space is $O(\min(N,p))$.

Python integers safely hold the full total used by `sum`. The running prefix is reduced modulo `p` at every step.

## Alternatives and edge cases

- **Enumerate every subarray:** Rolling sums reduce each candidate check to constant time but still produce $O(N^2)$ candidates, which is too slow at the maximum length.
- **Store every index per remainder:** This is unnecessary for the shortest answer. Only the latest prior index can minimize length for a future endpoint.
- **Store the earliest index:** That strategy is useful for longest-subarray problems, but here it produces longer removals and can miss the minimum.
- **Sliding window:** Ordinary window movement relies on monotonic sums. The target is a modular remainder, which can wrap around, so prefix remainders are the appropriate tool even though values are positive.
- **Total already divisible:** `k == 0` returns zero immediately, representing removal of the allowed empty subarray.
- **Only whole array works:** The best length stays $N$, and the final check returns `-1` because removing everything is forbidden.
- **One-element array:** If its sum is divisible, return zero; otherwise, the only nonempty candidate is the whole array, so return `-1`.
- **Subarray beginning at zero:** The sentinel remainder zero at index negative one yields the correct length `i + 1`.
- **Subarray ending at the last index:** It is considered normally during the final loop iteration; only a full-length result is rejected.
- **Repeated prefix remainder:** The dictionary overwrites the old index because the later one gives shorter future subarrays.
- **`p = 1`:** Every integer sum is divisible by one, so `k` is zero and the result is zero.
- **Large values:** Only their remainders affect the scan. Python handles the initial sum without overflow; fixed-width languages should reduce while summing or use a wide type.
- **Positive-number contract:** The prefix-modulo proof does not depend on positivity, though the input guarantees it.
- **Expected hash performance:** The linear bound assumes expected constant-time dictionary operations; the stored-key count remains bounded by $\min(N,p)$.
