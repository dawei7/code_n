## General

**Translate a nonzero AND into a shared-bit condition**

A bit is 1 in the AND of several numbers only when that bit is 1 in every selected number. Therefore a subsequence has nonzero bitwise AND exactly when there exists at least one bit position that all its elements share.

Formally, for selected values $v_1,v_2,\ldots,v_q$,

$$
v_1\mathbin{\&}v_2\mathbin{\&}\cdots\mathbin{\&}v_q\ne0
$$

if and only if some bit $b$ satisfies

$$
(v_j\mathbin{\&}2^b)\ne0
\quad\text{for every }j.
$$

This equivalence is the main simplification. The algorithm does not need to track every possible cumulative AND value. It can choose a candidate surviving bit and require every subsequence element to contain that bit.

**Create one ordinary LIS problem per bit**

Fix bit position `i`. The comprehension

`[x for x in nums if x >> i & 1]`

keeps exactly the input values whose bit `i` is set. Importantly, filtering preserves their original left-to-right order.

Any subsequence selected from this filtered array is also a subsequence of `nums`. If it is strictly increasing, it meets the ordering requirement. Since every retained value contains bit `i`, that bit survives their cumulative AND, making the AND nonzero.

Thus, for a fixed bit, the best valid subsequence sharing that bit is simply the longest strictly increasing subsequence of the filtered array.

The source computes this LIS length independently for every bit that might occur and takes the maximum.

**Why maximizing over individual bits loses nothing**

Take an optimal valid subsequence from the original array. Its AND is nonzero, so at least one bit `i` remains set in that AND. Every selected value has bit `i`, which means the entire subsequence appears, in the same order, inside the filtered array for `i`. The LIS computed for that filtered array is at least as long as this optimal subsequence.

In the other direction, any increasing subsequence found in a bit-`i` filtered array is valid for the original problem because bit `i` remains set in its AND.

The best per-bit LIS can therefore be neither smaller nor larger than the true optimum; the two values are equal.

Notice that different adjacent pairs sharing different bits is not enough. One common bit must be present in every chosen value because an AND bit survives only universal membership. Trying each bit separately enforces exactly that global condition.

**Compute a strict LIS with minimum tails**

The helper `lis(arr)` uses the patience-sorting method. Its list `g` has this meaning:

> `g[length - 1]` is the smallest possible final value of a strictly increasing subsequence of that length among the processed elements.

The list `g` is itself nondecreasing. For each new value `x`, `bisect_left(g, x)` finds the first index `j` whose stored tail is greater than or equal to `x`.

If `j == len(g)`, then `x` is greater than every current tail. It can extend the longest known strictly increasing subsequence, so the source appends it.

Otherwise, the source replaces `g[j]` with `x`. This does not claim that all values in `g` form one actual subsequence. It improves the smallest possible tail for length `j + 1`. A smaller tail is never worse: it leaves at least as much room for a larger future value to extend that length.

The helper returns `len(g)`, which is the LIS length.

**Why bisect_left enforces strict increase**

For a duplicate `x` already represented in `g`, `bisect_left` returns the first position containing `x` rather than a position after it. The source replaces that tail instead of appending. Equal values therefore cannot extend a subsequence.

This is exactly what “strictly increasing” requires. Using `bisect_right` would place a duplicate after existing equal tails and would compute a longest non-decreasing subsequence instead.

For example, filtered values `[2,2,3]` produce tails `[2]` after both copies of 2, then `[2,3]`. The LIS length is 2, not 3.

**Limit the bit loop to positions that exist**

`m = max(nums).bit_length()` is one more than the highest set-bit index in the maximum input value. No value can have a set bit at position `m` or above, so filtering those positions would always produce an empty array.

The source loops over `range(m)`. The constraints cap values at $10^9$, which needs at most 30 bits, so `m <= 30`.

If every element is zero, `max(nums)` is zero and `bit_length()` returns 0. No bit loop runs, `ans` stays 0, and the result is correct: every nonempty subsequence of zeros has AND zero.

**Trace a shared-bit example**

For `nums = [2,3,6]`, the binary values are `010`, `011`, and `110`. All three contain bit 1, the value-2 bit. Filtering for that bit preserves the full array `[2,3,6]`, which is strictly increasing.

The LIS helper extends its tails three times and returns 3. Their AND is

$$
2\mathbin{\&}3\mathbin{\&}6=2,
$$

so this length is valid.

For `[5,4,7]`, different bit filters expose valid increasing pairs. Bit 0 keeps `[5,7]` and gives length 2. The full sequence is not strictly increasing because 5 is greater than 4, so no bit-specific LIS incorrectly claims length 3.

**Subsequence order is preserved automatically**

The filtered `arr` is not sorted by value. Sorting it would destroy the original index order and solve the wrong problem. The list comprehension only removes elements; it never reorders survivors. The LIS helper then chooses increasing values while respecting that preserved sequence order.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$, let $B=30$, and let $M_i$ be the number of values containing bit `i`. For each of at most $B$ bits, filtering scans all $N$ values in $O(N)$ time. The LIS helper processes $M_i$ values, and each binary search costs $O(\log M_i)$.

A precise total is

$$
O\left(NB+\sum_i M_i\log M_i\right),
$$

which is bounded by $O(NB\log N)$. Since $B$ is at most 30, this is practical for $N=10^5$.

For one bit, `arr` and `g` can each hold $O(N)$ values. They are recreated and released from one loop iteration to the next rather than retained for all bits. Exact peak auxiliary space is therefore $O(N)$, not the manifest's $O(NB)$. The manifest overstates memory by summing temporary per-bit arrays that do not coexist.

## Alternatives and edge cases

- **Track every cumulative AND in subsequence DP:** Many AND states can be considered, but combining them with strict value ordering is more complicated than the shared-bit equivalence and can create much larger state.
- **Quadratic LIS for each bit:** Dynamic programming over every earlier filtered value is correct but costs $O(BN^2)$ in the worst case.
- **Fenwick tree per bit:** Coordinate-compress values and query the best length among strictly smaller values while scanning input. This can also achieve $O(BN\log N)$ and avoids materializing filtered arrays, but patience sorting is simpler when only the length is needed.
- **Stream directly into each LIS:** Maintain 30 tail arrays and update those corresponding to set bits of each input value. This avoids rescanning and filtered arrays, though multiple tail structures can then coexist and use up to $O(NB)$ space in the worst case.
- **All zeros:** No bit position is examined and the answer is 0; a zero singleton is invalid because its AND is zero.
- **One nonzero value:** At least one bit filter contains it, yielding a valid length-one subsequence.
- **Duplicate values:** They cannot both appear in a strictly increasing subsequence. `bisect_left` replaces rather than extends on equality.
- **Bit shared by every value but values not increasing:** The bit makes those values eligible, but the LIS still enforces original-order strict increase.
- **Several surviving bits:** A valid subsequence may be counted as a candidate in more than one bit iteration. Taking a maximum does not double-count lengths or affect the result.
- **Highest possible bit:** `bit_length` includes the maximum value's highest set position, while skipping every guaranteed-empty higher position.
- **Subsequence versus subarray:** Filtering and LIS may skip arbitrary original positions; contiguity is neither required nor imposed.
