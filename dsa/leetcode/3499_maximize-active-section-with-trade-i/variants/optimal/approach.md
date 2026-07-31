## General

Consider three consecutive runs in the augmented string: a zero run of length $L$, a one run of length $A$, and a zero run of length $R$. The middle one run is eligible for the first conversion because zeros surround it. Turning its $A$ ones into zeros merges all three runs into one zero block of length $L + A + R$, now surrounded by ones. The second conversion turns that whole block into ones.

The middle $A$ active sections disappear and are then restored, so the trade's net gain is exactly $L + R$. Therefore, the only decision is which pair of consecutive zero runs—necessarily separated by a one run—has the largest combined length. The artificial boundary ones make a zero run at either end of `s` valid for this calculation, while an original one run touching an end cannot be the first converted block.

Scan `s` by runs. Count every encountered `'1'` to obtain the original number of active sections. Whenever a zero run ends, combine its length with the previous zero-run length, if one exists, and update the best gain. Consecutive zero runs in this sequence are always separated by at least one original one, so every evaluated pair represents one valid first conversion. If fewer than two zero runs exist, no valid trade can improve the count and the gain remains zero.

Every valid trade selects some internal one run and hence corresponds to the two zero runs immediately beside it, so its gain is among the pairs examined by the scan. Conversely, each examined pair has a separating one run and constructs the valid merge described above. Taking the largest pair therefore yields exactly the optimal trade.

## Complexity detail

Let $n = \lvert\texttt{s}\rvert$. Each character is advanced past once, including characters consumed by the inner zero-run scan, so the total time is $O(n)$. The active count, current indices, previous zero-run length, and best gain occupy $O(1)$ auxiliary space.

Every input character may change either the original active count or a candidate run length, so the worst case requires $\Omega(n)$ inspection. The scan is thus asymptotically optimal. The benchmark varies $n$ and contrasts it with a correct method that, for every active position in a long one run, repeatedly rescans that run and its adjacent zeros, producing $\Theta(n^2)$ work.

## Alternatives and edge cases

- **Run-length array:** Materializing every run makes the adjacent-zero formula direct, but it uses $O(n)$ auxiliary space in an alternating string when only the previous zero run is needed.
- **Simulate both conversions:** Rebuilding strings for every possible first block is correct but repeats linear work for many candidates and can require $O(n^2)$ time and space churn.
- **Use the longest zero run alone:** A trade activates two zero runs around the chosen one run, so the best individual zero run does not by itself determine the best trade.
- **No eligible one run:** With fewer than two zero runs, no original one run is surrounded by zeros; returning the original active count represents using no trade.
- **Zero run at an endpoint:** The added boundary one surrounds that zero run, so it may contribute to the gain.
- **One run at an endpoint:** It joins the added boundary one and is not surrounded by zeros, so it cannot be selected for the first conversion.
- **All zeros:** There is no active block to convert first, and the answer is zero.
- **All ones:** The string is already fully active, and the optional trade is skipped.
- **Tied candidates:** Any pair with the maximum sum gives the same final active count.
