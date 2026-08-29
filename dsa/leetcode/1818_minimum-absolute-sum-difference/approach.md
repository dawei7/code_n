## General

**One replacement changes only one term**

The original total is

$$
S=\sum_{i=0}^{n-1}\lvert\texttt{nums1}[i]-\texttt{nums2}[i]\rvert.
$$

If position $i$ is replaced with some value $x$ that appears anywhere in `nums1`, every other term stays unchanged. The old contribution

$$
d_1=\lvert\texttt{nums1}[i]-\texttt{nums2}[i]\rvert
$$

becomes

$$
d_2=\lvert x-\texttt{nums2}[i]\rvert.
$$

That replacement improves the total by $d_1-d_2$. Since at most one replacement is allowed, the global optimum is the original total minus the largest improvement available at any index.

**Sort all legal replacement values**

The replacement value may be any element occurring in `nums1`, not necessarily one from a different position. The solution creates sorted copy `nums = sorted(nums1)`.

For a fixed target `b = nums2[i]`, the best replacement is the value in this sorted list closest to $b$.

**Why only two binary-search neighbors matter**

`bisect_left(nums, b)` returns the first position whose value is at least $b$.

- If that index is inside the list, `nums[i]` is the smallest legal value on or above $b$.
- If the index is positive, `nums[i - 1]` is the largest legal value below $b$.

Every value farther left is no closer than the predecessor, and every value farther right is no closer than the lower-bound value. Thus checking at most these two candidates finds the minimum possible `d2`.

If an exact value $b$ exists in `nums1`, the lower-bound candidate gives zero replacement difference.

**Track the largest saving**

For each paired original value `a` and target `b`, the solution computes current difference `d1` and best achievable difference `d2`. It updates

`mx = max(mx, d1 - d2)`.

`mx` begins at zero, representing the legal choice to make no replacement. The closest legal replacement can never be worse than the original `a` because `a` itself is present in the sorted candidate list. Therefore $d_2\leq d_1$ and improvements are nonnegative.

**Following the first example**

For `nums1 = [1,7,5]`, the sorted candidates are `[1,5,7]`. At the second pair, $a=7$ and $b=3$, so $d_1=4$.

Binary search around 3 finds neighbors 1 and 5. Either has distance two, so $d_2=2$ and the improvement is two. The original total is five, and subtracting two gives three.

Other positions offer no larger saving, so the method returns three.

**Why the baseline is reduced modulo before subtraction**

The exact code computes

`s = original_total % mod`

before finding `mx`, then returns `(s - mx + mod) % mod`.

This is algebraically valid because modular arithmetic respects subtraction:

$$
(S\bmod M-mx)\bmod M=(S-mx)\bmod M.
$$

The optimization itself still uses unmodded individual differences and improvement, so modulo does not distort which replacement is best.

Adding `mod` before the final remainder avoids a negative intermediate in languages whose remainder semantics differ. Under the stated value bounds, one addition is ample because `mx` is at most $10^5-1$, much smaller than the modulus. Python's modulo would handle negative values correctly regardless.

**Why the algorithm is correct**

For each possible replaced index, binary search finds the legal `nums1` value minimizing that index's new difference. Therefore `d1 - d2` is the maximum saving obtainable by replacing that index.

Taking the maximum across all indices considers every possible single replacement location. Subtracting that saving from the independent-term baseline yields the minimum total after at most one replacement.

## Complexity detail

Let $n$ be the array length. Sorting the replacement candidates takes $O(n\log n)$ time. Computing the baseline is $O(n)$.

For each of $n$ index pairs, binary search costs $O(\log n)$ and neighbor checks are constant. Total time is $O(n\log n)$, matching the manifest.

The sorted copy uses $O(n)$ auxiliary space. Other variables are scalar, so total auxiliary space is $O(n)$.

The original arrays are not modified.

## Alternatives and edge cases

- **Try every replacement value at every index:** It costs $O(n^2)$ and is too slow.
- **Balanced search tree:** It can provide predecessor and successor queries, but sorting once is simpler for a static candidate set.
- **Value-frequency array:** The bounded value range permits presence lookup and nearest searches, though implementation details differ.
- **Already equal arrays:** Every `d1` is zero, `mx` stays zero, and the answer is zero.
- **Exact target value exists:** Best new difference is zero.
- **Lower-bound index zero:** Only the first at-or-above candidate exists.
- **Lower-bound at list end:** Only the last below-target candidate exists.
- **Duplicate candidate values:** They do not change nearest distance; keeping duplicates is harmless.
- **Replace with the same original value:** This realizes zero improvement and supports the “at most one” rule.
- **Single-element arrays:** The only legal replacement value is the existing value, so the total cannot improve.
- **Modulo after optimization:** The best replacement is chosen from true differences, not modular residues.
- **Large original total:** Python safely sums it before taking the modulus.
- **Sorted copy:** It preserves `nums1` for current-difference calculations and caller expectations.
- **One replacement limit:** Savings from different indices cannot be combined; only the maximum is subtracted.
