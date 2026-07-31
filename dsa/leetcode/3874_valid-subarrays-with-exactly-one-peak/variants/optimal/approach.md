## General

**Identify peaks in the original array**

Scan the interior indices and record every position whose value is strictly greater than both neighbors. These global peak positions are the only objects that matter when enforcing “exactly one”; the endpoints of a selected subarray do not change whether an index is a peak.

**Give each valid subarray to its unique peak**

Consider one recorded peak $p$. Let $q$ be the preceding peak, or $-1$ if none exists, and let $s$ be the following peak, or $n$ if none exists. To include $p$ but exclude $q$, a left endpoint must be greater than $q$. It must also remain inside the array and satisfy $p-l\le k$. The earliest legal endpoint is therefore

$$
L=\max(0,p-k,q+1).
$$

Every index from $L$ through $p$ is a valid left choice, giving $p-L+1$ possibilities.

Symmetrically, the right endpoint must be less than $s$, stay within the array, and satisfy $r-p\le k$. Its latest legal value is

$$
R=\min(n-1,p+k,s-1),
$$

which gives $R-p+1$ right choices.

The choices on the two sides are independent, so peak $p$ contributes

$$
(p-L+1)(R-p+1)
$$

valid subarrays. The neighboring-peak bounds guarantee that none of them contains another peak. Conversely, every valid subarray has one unique peak and appears in exactly that peak's product, so summing all products counts every valid interval once.

## Complexity detail

Finding peaks and summing their contributions each take $O(n)$ time. The peak-position list contains at most $n$ indices, so the auxiliary space is $O(n)$.

The benchmark defines size as $n$ and uses single-peak mountain arrays of lengths `16`, `64`, and `256`, with `k = n`. The accepted source and an independent delayed-contribution scan should retain linear scaling. A correct control that enumerates every subarray performs $O(n^2)$ work and should fail only the scaling verdict.

## Alternatives and edge cases

- **Delayed one-pass contributions:** Keep only the previous two discovered peaks and finalize a peak when the next one appears; this preserves $O(n)$ time while reducing auxiliary space to $O(1)$.
- **Enumerate all subarrays:** Maintaining a peak count while extending every left endpoint is correct, but examines $\Theta(n^2)$ intervals.
- **No peaks:** A monotone array or an array shorter than three elements contributes `0`.
- **Strict comparison:** Equal neighboring values prevent an index from being a peak; plateaus must not be counted.
- **Length-one selection:** `[nums[p]]` is valid for every global peak $p$ because both endpoint distances are zero and the interval contains that one peak.
- **Nearby peaks:** The previous and next peak positions, not merely the `k` window, limit endpoint choices so a counted subarray never contains two peaks.
- **Large `k`:** When `k` exceeds the distance to an array boundary, the boundary or neighboring peak becomes the active limit.
- **Large answer:** The number of intervals can exceed 32-bit range, so languages with fixed-width integers need a 64-bit return and accumulator.
