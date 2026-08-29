## General

**Search over a prefix length, not arbitrary removals.** Choosing `k` means removing exactly the first `k` indices of `removable`. If `p` remains a subsequence after `k` removals, it also remains one after any smaller prefix because restoring characters cannot destroy an existing subsequence. If it fails after `k` removals, every larger prefix also fails because deleting more characters cannot create a missing subsequence. Feasibility is therefore monotone: true values of `k` form a prefix followed by false values.

**Implement one feasibility check literally.** `check(k)` creates Boolean list `rem` with one entry per position of `s`. It marks each index in `removable[:k]` as true. The removable indices are distinct, so every mark corresponds to one deleted character, although repeated marking would not otherwise hurt the Boolean representation.

The original string is not rebuilt. Instead, two pointers scan it logically. Pointer `i` visits every original position; pointer `j` is the next character of `p` that still needs a match. A character advances `j` only when its position is not removed and `s[i] == p[j]`. Regardless of a match, `i` advances. If `j` reaches `len(p)`, every pattern character has been found in order among surviving positions, which is exactly the subsequence definition.

**Why greedy subsequence matching is correct.** When looking for `p[j]`, using its earliest available matching position in `s` leaves at least as much suffix for future pattern characters as any later choice. A later match can never make an impossible suffix possible when an earlier equal character was available. Repeating this earliest-match decision succeeds if and only if some subsequence embedding exists.

**Binary-search the last feasible prefix.** Bounds start at `l = 0` and `r = len(removable)`. Zero is always feasible because the statement guarantees that `p` is initially a subsequence. The upper endpoint may or may not be feasible. Midpoint `(l + r + 1) >> 1` rounds upward. If `check(mid)` succeeds, the answer is at least `mid`, so `l = mid`. Otherwise `mid` and all larger prefixes fail, so `r = mid - 1`.

Upper rounding is essential when two values remain. With bounds three and four, it tests four; a successful result advances the lower bound to four. A lower midpoint would retest three and could loop forever after `l = mid`.

**Trace the first example.** For `s = "abcacb"` and order `[3, 1, 0]`, testing two marks original positions three and one. Scanning surviving characters matches `a` at position zero and `b` at position five, so `"ab"` survives. Testing three also removes position zero; no surviving `a` precedes a suitable `b`, so it fails. Monotonicity makes two the maximum.

**Why the final bound is exact.** Every successful midpoint discards only smaller candidates from further consideration, and every failed midpoint discards itself and larger candidates. The closed interval always contains the largest feasible `k` and shrinks on every iteration. When the bounds meet, their shared value must be that maximum.

**Input objects remain unchanged.** The check builds a fresh removal mask and only reads `s`, `p`, and `removable`. Each binary-search trial is independent, so marks from a larger previous trial cannot leak into a smaller one.

## Complexity detail

Let $n=\lvert s\rvert$ and $r=\lvert\texttt{removable}\rvert$. Binary search performs $O(\log(r+1))$ checks. One check allocates and initializes $n$ Booleans, copies a slice of up to $r$ indices, marks it, and scans at most $n$ characters. Its cost is $O(n+r)$, which is $O(n)$ here because $r<n$. Total time is $O((n+r)\log(r+1))$, matching the manifest.

The removal mask uses $O(n)$ space. The slice `removable[:k]` creates up to $O(r)$ additional references in this exact Python source, still $O(n)$ under the constraints. Pointer state is constant.

Reallocating the mask each check is simple but contributes the full linear initialization cost. An alternative removal-time array can avoid marking a prefix on every trial, though scanning `s` remains necessary.

## Alternatives and edge cases

- **Removal-time array:** Store for each index the step at which it is removed, then a check treats positions with time below `k` as absent. This avoids a fresh prefix slice and repeated marking while preserving $O(n\log r)$ time.
- **Try every `k` sequentially:** Monotonicity permits binary search; checking all prefixes can cost $O(nr)$.
- **Rebuild the surviving string:** Joining unremoved characters and then testing a subsequence works but allocates another length-$n$ string per check. Logical skipping is sufficient.
- **Maximum answer zero:** The first listed removal can destroy the only possible embedding. Initial zero remains the last feasible bound.
- **Every listed index removable:** If `p` can still be formed after all removals, the upper endpoint stays feasible and is returned.
- **Removed matching character:** The scan must test `not rem[i]` before accepting equality; marked characters do not exist logically.
- **Repeated letters:** Earliest greedy matching remains correct and avoids backtracking among equivalent occurrences.
- **Empty removable list:** Both bounds are zero, the loop does not run, and zero is returned.
- **Distinct-index guarantee:** Boolean marking naturally supports it. The guarantee also means `k` truly represents removing `k` characters rather than fewer unique positions.
