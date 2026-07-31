## General

Every operation preserves the sum of `nums1`. For $k>0$, it also changes each affected position by an integer multiple of $k$. Therefore, if any difference `nums1[i] - nums2[i]` is not divisible by $k$, or if all normalized differences do not sum to zero, the target is unreachable.

For each position define its normalized surplus as

$$
d_i = \frac{\texttt{nums1[i]}-\texttt{nums2[i]}}{k}.
$$

A positive $d_i$ means that many units must leave the position; a negative value means units must enter it. Accumulate the sum of all $d_i$ as a balance and separately accumulate only their positive parts.

Each operation can remove exactly one surplus unit and satisfy exactly one deficit unit. Consequently, the total positive surplus is a lower bound on the number of operations. When the final balance is zero, total surplus equals total deficit, so pairing those units achieves that bound. The accumulated positive total is therefore the minimum answer.

When $k=0$, an operation changes nothing. The answer is zero only if the arrays already match and is otherwise `-1`.

## Complexity detail

Let $n$ be the common array length. One pass examines each aligned pair once, so the time complexity is $O(n)$. The balance and operation counters use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Explicitly pair surplus and deficit indices:** This constructs actual transfers but can take $O(n^2)$ time if each surplus scans for a remaining deficit.
- **Compare only total sums:** Equal totals are necessary but insufficient because every individual difference must also be divisible by $k$.
- **Count absolute differences:** Dividing the total absolute normalized difference by two works after feasibility is established, but summing positive units expresses the operation lower bound directly.
- **Zero step size:** No value changes when $k=0$, so unequal arrays cannot be repaired.
- **Non-divisible difference:** A single misaligned remainder makes the whole transformation impossible even when the totals match.
- **Large operation count:** Differences and the final count can exceed 32-bit range, so fixed-width languages need 64-bit arithmetic.
