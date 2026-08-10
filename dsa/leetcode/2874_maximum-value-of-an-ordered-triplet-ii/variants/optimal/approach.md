## General

**Why three nested choices can become three running maxima.** The requested value is

$$
(\texttt{nums[i]}-\texttt{nums[j]})\cdot\texttt{nums[k]},
\qquad i<j<k.
$$

The second version allows $10^5$ elements, so enumerating triplets or even pairs is impossible. The expression is naturally staged. First choose an earlier value for `i`, then form a difference when `j` arrives, then multiply that stored difference when a later `k` arrives.

Because every array value is positive, the best `i` for a fixed `j` is simply the largest earlier value. Likewise, the best already-formed difference for a fixed positive `nums[k]` is the largest earlier difference. No full prefix or suffix arrays are necessary; each best value can be compressed into one scalar.

The protected source uses:

- `mx` for the maximum value available at an earlier index;
- `mx_diff` for the maximum profitable ordered difference available from two earlier indices;
- `ans` for the maximum completed product.

All three begin at zero, matching the rule that a result below zero should be reported as zero.

**Statement order enforces $i<j<k$.** When current loop value is `x`, the solution first calculates `mx_diff * x`. At that instant, `mx_diff` was formed before the current iteration, so its $i$ and $j$ indices are both strictly earlier. Current index can safely be $k$.

Next it calculates `mx - x`. Current `mx` still excludes `x` because the prefix maximum update has not happened yet. Therefore this candidate uses an earlier $i$ and current index as $j$. The updated difference will be used only by future iterations, whose indices can serve as $k$.

Finally, `mx = max(mx, x)` records current value for future middle positions. This staged update is a compact substitute for explicitly storing indices.

**The formal state after a processed prefix.** After processing positions through $p$, `mx` equals the largest `nums[i]` with $i\le p$. Variable `mx_diff` equals the largest of zero and `nums[i] - nums[j]` over $i<j\le p$. Variable `ans` equals the largest of zero and every complete triplet whose final index is at most $p$.

The next iteration preserves these claims. It completes the best prior pair using current positive multiplier, creates the best pair ending at the current middle position using the best prior first value, and then extends the prefix maximum. By induction, after the last position `ans` covers every legal triplet.

**Why only the largest difference matters.** For a fixed positive multiplier $x$, if $d_1\ge d_2$, then $d_1x\ge d_2x$. Hence any smaller stored difference can never beat the largest one at any future position and may be discarded. Negative differences are also unnecessary because their product with a positive input is negative and the answer is clamped to zero.

**Trace `[1,10,3,4,19]`.** After `1` and `10`, `mx` is ten but no positive ordered difference exists yet because ten appeared too late to precede one. When `3` arrives, `mx - x = 10 - 3 = 7` becomes `mx_diff`. At `4`, answer candidate is `7 * 4 = 28`; the best difference remains seven. At `19`, the candidate becomes `7 * 19 = 133`, corresponding to indices $(1,2,4)$. The update sequence prevents `19` from becoming a first or middle value before it has been evaluated as the final value.

**Why a suffix maximum is unnecessary.** A common linear solution fixes `j`, stores the maximum on its left, and precomputes the maximum on its right. This source instead fixes each `k` as it arrives and retains the best left-side difference. That moves all needed information forward through the scan and eliminates $O(n)$ auxiliary arrays.

## Complexity detail

There is one pass over `nums`. Every element triggers three constant-time maximum or arithmetic updates, so running time is $O(n)$. The state does not grow with the array: `ans`, `mx`, and `mx_diff` are scalars, giving $O(1)$ auxiliary space.

With values up to $10^6$, a product can approach $10^{12}$ and does not fit a 32-bit signed integer. Python handles arbitrary-size integers; languages with fixed-width types should promote before subtraction and multiplication. The manifest's time and space bounds accurately reflect this exact implementation.

## Alternatives and edge cases

- **Cubic brute force:** It is conceptually direct but performs $O(n^3)$ work, which is infeasible for $10^5$ elements.
- **Quadratic pair scan:** Maintaining the best `i` while enumerating `j,k` reduces one loop but remains far too slow for this version.
- **Prefix/suffix arrays:** They provide an $O(n)$ solution by fixing `j`, but use $O(n)$ extra memory compared with the source's streaming state.
- **All increasing values:** No positive earlier-minus-later difference exists; `mx_diff` stays zero and the required result is zero.
- **Best first value appears late:** It cannot pair with an earlier middle value. The update order admits it to `mx` only for future positions.
- **Current-index reuse:** Updating `mx_diff` before `ans` would illegally allow current `x` to be both `j` and `k`.
- **Overflow:** Store the result in a 64-bit or wider integer outside Python.
- **Positive inputs:** The one-maximum-difference compression relies on future multipliers being positive; signed inputs would require tracking both extreme differences.
