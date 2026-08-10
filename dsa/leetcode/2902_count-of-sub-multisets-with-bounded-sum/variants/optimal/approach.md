## General

**Count multiplicities, not index subsets.** Equal values are indistinguishable in a sub-multiset. If value five occurs three times, choosing “the first five” and choosing “the second five” are the same multiset. The only meaningful choice is to use zero, one, two, or three copies.

The source begins with `Counter(nums)` so each distinct value is processed once together with its frequency.

**Dynamic-programming state.** `dp[s]` is the number of sub-multisets formed from values processed so far whose sum is exactly `s`. Only sums through `r` matter because all values are nonnegative; once a partial sum exceeds `r`, adding more elements can never bring it back.

Initially, `dp[0] = 1` for the empty multiset and every positive sum has count zero.

For a positive value `num` occurring `freq` times, the direct bounded-knapsack transition would be:

$$
\text{new}[s]
=
\sum_{t=0}^{\texttt{freq}}
\text{dp}[s-t\cdot\texttt{num}],
$$

using only nonnegative indexes. Computing this sum from scratch for every `s` would add a factor of `freq`.

**Stride prefix sums remove the frequency factor.** The source copies old `dp` into `stride` and scans upward from `num`:

`stride[i] += stride[i - num]`.

Afterward,

$$
\texttt{stride}[i]
=
\texttt{dp}[i]
+\texttt{dp}[i-\texttt{num}]
+\texttt{dp}[i-2\texttt{num}]
+\cdots.
$$

This is a prefix sum along one residue class modulo `num`. For example, indexes two, five, eight, and eleven form one stride when `num=3`.

The unlimited sum includes choices using more than `freq` copies. To retain only $t=0$ through `freq`, subtract the prefix ending one step before the allowed window:

$$
\text{new}[i]
=
\texttt{stride}[i]
-\texttt{stride}[i-(\texttt{freq}+1)\texttt{num}].
$$

When that subtraction index is negative, every available term is within the limit and `new[i] = stride[i]`. These are exactly the two branches assigning back to `dp[i]`.

**Why zero is handled separately.** Adding a zero never changes the sum. If zero occurs `z` times, a sub-multiset of any positive values can be combined with zero copies, one copy, through $z$ copies. Those are $z+1$ distinct multisets, all with the same sum.

The source removes zero from the Counter, runs DP only for positive values, and multiplies the final range count by `zeros + 1`.

**Why the transition counts each multiset once.** Values are processed by distinct key. For the current value, selecting multiplicity $t$ extends every older multiset in exactly one way. Different $t$ values produce different multiplicities of `num`, while different older DP choices differ on some previously processed value. Thus the recurrence is a bijection over sub-multisets rather than over original indices.

After all values, `sum(dp[l:r+1])` counts exact sums in the inclusive requested range. Multiplying by zero choices and reducing modulo $10^9+7$ gives the requested answer.

**A serious arithmetic detail in the protected source.** `kMod` is defined, but no DP or stride update applies it. The code computes exact Python integers throughout and reduces only the final answer. This is mathematically correct because modular reduction may be postponed over additions and subtractions.

However, counts can be enormous—up to a product of `freq+1` factors and potentially exponential in the number of distinct values. Python integers then grow to thousands of bits, making additions, copies, time, and memory much larger than the stated word-operation analysis. A robust modular solution should reduce every transition, for example with `% kMod`, while ensuring subtractions are normalized.

**Why descending assignment is safe.** `stride` was built from a copy of the old DP before assignments begin. The later loop writes `dp` from high sums down, but every formula reads only `stride`, not newly written DP values. The update order therefore cannot reuse current value more than its bounded frequency.

## Complexity detail

Let $D$ be the number of distinct positive values. Counting inputs costs $O(n)$. For each distinct value, copying and scanning arrays through `r` costs $O(r)$ arithmetic operations, giving $O(n+Dr)$ operations. `dp` and `stride` each use $O(r)$ entries, while the Counter uses $O(D)$, for $O(r+D)$ space.

Those bounds assume fixed-size modular integers. Because the exact source postpones modulo reduction, integer bit lengths can grow with the combinatorial count, so its true bit complexity and memory can substantially exceed the manifest's $O(n+Dr)$ time and $O(r)$ word-space model.

## Alternatives and edge cases

- **Reduce modulo every update:** Preserve bounded integer sizes and the intended complexity; normalize `stride[a] - stride[b]` modulo $10^9+7$.
- **Naive multiplicity loop:** It is simpler but costs $O(DrF)$ when frequencies can be large.
- **All zeros:** Positive-value DP remains `dp[0]=1`, and the answer is `zeros+1` exactly when zero lies in `[l,r]`.
- **Empty multiset:** It contributes once when `l=0`, multiplied across the possible zero multiplicities.
- **Value greater than `r`:** It cannot contribute a positive copy to an in-range sum, so DP remains unchanged for tracked sums.
- **Repeated equal values:** Counter frequency ensures multiplicity choices are counted once, not by combinations of indices.
- **Inclusive range:** Slice `dp[l:r+1]` includes both endpoints.
- **Late modulo defect:** The final value is correct in theory, but unchecked big integers can violate practical performance expectations.
