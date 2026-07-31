## General

**Only a target prefix can be supplied by the original string.** Every appended character comes after all positions of `s`. Consequently, any characters of `t` selected from `s` must precede every character supplied by the appended portion. The part already matched inside `s` must therefore be a prefix of `t`, and the appended portion must contain the remaining suffix.

**Greedily maximize that prefix.** Keep `matched` at the first unmatched index of `t` and scan `s` from left to right. When the current source character equals `t[matched]`, consume it and advance `matched`; otherwise skip it. Choosing the earliest available occurrence is always safe because it leaves every later source position available for subsequent target characters. Replacing that occurrence with a later equal one could never enable an additional match.

After the scan, `t[:matched]` is a subsequence of `s`. It is also the longest target prefix that can be matched: if some longer prefix were possible, its first `matched + 1` selected positions would give a match for the next character no later than the greedy scan, contradicting where the scan stopped. At least $m-\texttt{matched}$ characters must therefore be appended, and appending exactly `t[matched:]` achieves that bound.

## Complexity detail

Let $n = \lvert\texttt{s}\rvert$ and $m = \lvert\texttt{t}\rvert$. The scan visits each source character once and advances the target pointer at most $m$ times, for $O(n+m)$ time. The algorithm stores only one index and uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Test every target prefix:** Checking successively shorter prefixes of `t` against `s` is correct but can rescan both strings and take $O(nm)$ time.
- **Dynamic programming:** A longest-common-subsequence table can recover how much of `t` appears in order, but general LCS permits matching a non-prefix subset and uses unnecessary $O(nm)$ time and space for this one-sided contract.
- **Target already a subsequence:** The pointer reaches $m$, so the returned suffix length is zero.
- **No first-character match:** The pointer remains zero and every character of `t` must be appended.
- **Repeated letters:** Advancing on the earliest matching occurrence preserves the most room for later copies and counts each target position separately.
- **Order mismatch:** Characters present in `s` but appearing too early or too late for the current target pointer cannot contribute and are correctly skipped.
