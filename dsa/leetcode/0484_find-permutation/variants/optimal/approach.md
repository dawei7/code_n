## General

If there were no `D` requirements, the lexicographically smallest permutation of `1` through `n + 1` would simply be

`[1, 2, 3, ..., n + 1]`.

An `I` already agrees with that ascending order. A maximal run of `D` characters is the only place where the order must change. The solution starts with the globally smallest ascending permutation and reverses exactly the value block covered by each decrease run.

**A pattern position connects two permutation positions.** Character `s[i]` describes the comparison between `ans[i]` and `ans[i + 1]`. Therefore, if a run of `D` starts at pattern index `i` and stops just before pattern index `j`, it contains `j - i` decrease signs but affects `j - i + 1` numbers: indices `i` through `j` of `ans`. This is why the slice is `ans[i : j + 1]`. Python excludes the right endpoint of a slice, so `j + 1` is required to include `ans[j]`.

Suppose the run is three `D`s. The corresponding ascending block might be `[4, 5, 6, 7]`. Reversing it produces `[7, 6, 5, 4]`, giving all three required strict decreases. Reversing only three values would satisfy only two comparisons and leave one `D` uncovered.

The code finds a run by setting `j = i` and advancing `j` while `j < n` and `s[j] == 'D'`. If `s[i]` itself is `I`, `j` does not move. The one-element slice `ans[i : i + 1]` reverses to itself, correctly doing no work. If one or more `D`s are found, the whole affected block is reversed at once.

**Why use exactly these values.** Consider a decrease run of length `r` beginning at output position `i`. It needs `r + 1` values in strictly descending order. To keep the full permutation lexicographically smallest, those positions should use the smallest values not already committed by earlier positions: the consecutive set

`i + 1, i + 2, ..., i + r + 1`.

Any choice that brought a larger future value into this earlier block would make the permutation larger at the first position where the choices differ. Once that smallest possible set is fixed, there is only one order satisfying all `r` decreases: descending order. Reversing the corresponding portion of the initial ascending array produces exactly that order.

**Why block boundaries still satisfy `I`.** A decrease block changes values only inside its consecutive range. Before reversal, every value in a later block is larger than every value in an earlier block because the original array is ascending and blocks use disjoint consecutive value ranges. Reversal changes their internal order but not their sets.

If an `I` separates two blocks, the last value of the left reversed block is its smallest value, while the first value of the next block is at least the smallest unused larger value. Hence the boundary comparison remains increasing. For an isolated `I` with no adjacent `D` run, the corresponding ascending values remain in their original order. Thus all `D` comparisons are created inside reversed blocks and all `I` comparisons remain valid between or outside them.

For example, take `s = "DDID"`. The initial answer is `[1, 2, 3, 4, 5]`. The first run covers pattern indices `0` and `1`, so the code reverses answer positions `0` through `2` to obtain `[3, 2, 1, 4, 5]`. The `I` at index `2` requires `1 < 4`, already true. The final `D` reverses `[4, 5]` into `[5, 4]`. The result `[3, 2, 1, 5, 4]` matches `D, D, I, D` and uses the smallest possible values at every earliest position.

**Advance without missing or repeating a run.** After processing the slice, the code sets `i = max(i + 1, j)`. When `s[i]` was `I`, `j == i`, so this becomes `i + 1` and advances past that character. When a `D` run ended at `j`, it becomes `j`. If `j < n`, `s[j]` is the first following `I` and is processed on the next iteration; if `j == n`, the loop ends. The already reversed block included answer position `j`, but pattern character `j`, when present, still describes the boundary from that position to `j + 1` and must not be skipped.

Correctness follows from combining feasibility and minimality. Every maximal `D` run is turned into the required descending block, and every `I` boundary remains increasing, so the returned array matches the pattern. Each block uses the smallest still-available consecutive values, in the only order that satisfies its decreases. Therefore no valid permutation can place a smaller number at the first position where it differs from this construction. That is precisely the definition of lexicographic minimality.

## Complexity detail

Let $n$ be the length of `s`, so the returned permutation has $n + 1$ values. Building `list(range(1, n + 2))` costs $O(n)$ time. The scan advances across each pattern character a constant number of times. Reversed answer slices for maximal `D` runs are disjoint except for harmless boundaries, so their total length is $O(n)$. Overall time is therefore $O(n)$.

The returned `ans` list uses $O(n)$ space. In this exact Python implementation, `ans[i : j + 1]` creates a temporary slice and `[::-1]` creates its reversed copy; a run can span the entire pattern, so peak temporary space is also $O(n)$. The manifest's $O(n)$ space includes the output and these possible temporaries. An explicit in-place two-pointer reversal could reduce auxiliary space to $O(1)$ while retaining the required output array.

## Alternatives and edge cases

- **Stack construction:** Push increasing values while reading `D`s and flush the stack at each `I`. Popping reverses each decrease block and also runs in $O(n)$ time, but it uses a separate stack.
- **In-place two-pointer reversal:** Swap endpoints of every affected block rather than assigning reversed slices. This preserves the same reasoning and reduces temporary auxiliary storage, at the cost of a few more implementation lines.
- **Brute-force permutations:** Enumerating all $(n+1)!$ permutations and selecting the first match is impossible for `n` up to $10^5$. The block structure determines the minimum directly.
- **All `I` characters:** Every processed slice has length one, so the answer remains `[1, 2, ..., n + 1]`, the smallest permutation overall.
- **All `D` characters:** One run reaches `j = n` and reverses the entire array, producing `[n + 1, n, ..., 1]`, the only fully decreasing permutation.
- **Run at the end:** The answer slice includes position `n` through the `j + 1` endpoint, so the final value is not omitted.
- **One `D`:** Two adjacent values are reversed. A single pattern comparison always affects two permutation positions.
- **Repeated values are impossible:** `ans` begins as the exact range `1` through `n + 1`, and reversal only changes order, so the permutation property is preserved automatically.
