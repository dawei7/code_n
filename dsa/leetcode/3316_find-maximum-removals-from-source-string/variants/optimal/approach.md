## General

**Choose a subsequence embedding and remove every eligible unused position.** The pattern must remain a subsequence after removals. Any source position used to realize that subsequence must be kept. Any target position not used by the chosen embedding can be removed, while non-target positions may remain unused without counting as operations.

Thus the task is to choose a pattern embedding that maximizes how many `targetIndices` positions are skipped. The exact source models this directly rather than first minimizing kept target positions.

Let $S=\lvert\texttt{source}\rvert$ and $P=\lvert\texttt{pattern}\rvert$. State `f[i][j]` is the maximum number of removable target positions among the first $i$ source characters while embedding the first $j$ pattern characters. Impossible states carry negative infinity.

**Initialize only the empty embedding.** `f[0][0] = 0` because zero source characters can embed the empty pattern with zero removals. `f[0][j]` for positive $j$ remains negative infinity, correctly representing that a nonempty pattern cannot be formed from an empty source prefix.

**Option one: do not use the current source character.** At one-based DP row `i`, current character `c` is original zero-based position `i - 1`. If it is skipped as a pattern match, the embedded pattern length stays $j$.

If that position belongs to set `s`, it can be removed and earns one operation. If it is not a target position, skipping it earns zero because it cannot be removed, though it may harmlessly remain in the source. This gives

`f[i][j] = f[i - 1][j] + int((i - 1) in s)`.

Adding zero or one to negative infinity leaves the state impossible.

**Option two: keep it as the next pattern character.** If $j>0$ and `c == pattern[j - 1]`, the current source character can realize the $j$-th pattern character. The predecessor is `f[i - 1][j - 1]`. No removal reward is added, even if this index belongs to `targetIndices`, because a selected subsequence position must remain.

The source takes the maximum between skipping and matching. This explores every possible embedding boundary while retaining only the best removal count for a given prefix state.

**Why unused non-target characters cause no problem.** A subsequence does not require deleting characters between selected positions. They may remain in the source and simply not participate in the pattern. Therefore the skip transition is legal for every character; only eligible target positions contribute to the operation count.
Consider an optimal plan represented by state $(i,j)$. It either does not use source position $i-1$ in its pattern embedding, in which case it belongs to the skip transition and gains exactly the eligible-removal indicator, or it uses that position as the final character of the embedded prefix, which requires a character match and belongs to the take transition. These cases are exhaustive and disjoint.

Conversely, each finite transition constructs a legal plan from a legal smaller prefix: skipping removes the character only when allowed, and taking preserves it as an ordered match. Induction from `f[0][0]` proves every table value is exact. The problem guarantees `pattern` is a source subsequence, so `f[S][P]` is finite and is the maximum possible number of operations.

The statement's unusual stable-index rule is naturally respected. Membership uses original position `i-1` from the immutable source scan. Removing one target character never renumbers later membership decisions.

**The set ignores input sorting because membership is what matters.** `targetIndices` is sorted and distinct, but the source converts it to `set` for expected constant-time lookup. Order is not used by the recurrence.

**Actual storage is quadratic in the two lengths.** The manifest claims $O(S+P)$ space, which would be possible with two rows or one carefully updated row. The exact source allocates `(S+1)` lists, each of length `P+1`. Its auxiliary table is $O(SP)$ space. At the maximum $3000\times3000$, Python object/reference overhead is substantial. This discrepancy must be explicit.

## Complexity detail

The nested loops visit every one of the $(S+1)(P+1)$ states, performing expected constant-time set membership and a constant number of arithmetic/comparison operations. Building the target set costs $O(T)$ for $T=\lvert\texttt{targetIndices}\rvert$. Total expected time is $O(SP+T)=O(SP)$.

The full DP table uses $O(SP)$ entries. The target set uses $O(T)$ additional space. Since $T\le S$, the exact auxiliary-space bound is $O(SP+S)=O(SP)$ for nonempty pattern, not the manifest's $O(S+P)$. The result is one integer.

## Alternatives and edge cases

- **Two-row compression:** Every transition reads only row `i-1`, so retaining previous and current arrays reduces DP space to $O(P)$ without changing $O(SP)$ time.
- **One-row dynamic programming:** Update pattern positions in descending order while carefully incorporating skip rewards. It can reduce storage further but is easier to implement incorrectly.
- **Minimize kept target positions:** Compute the minimum number of eligible indices used by an embedding, then subtract from `len(targetIndices)`. This is algebraically equivalent to the source's direct maximization.
- **Greedy earliest subsequence:** It may consume removable indices unnecessarily; a later embedding can allow more operations, so DP is required.
- **Pattern equals source:** Every source position is required in the only full-length embedding, so no target position can be removed.
- **Target index not used by pattern:** The skip transition gains one, even if the character remains conceptually irrelevant after other removals.
- **Non-target index not used:** It earns zero but may stay in the source without harming subsequence validity.
- **Repeated characters:** Multiple embedding choices are exactly why states compare skip and take rather than greedily choosing the first match.
- **All target indices removable:** If the pattern can be embedded entirely in non-target positions, the answer is `len(targetIndices)`.
- **Stable original indices:** Set membership is checked against the original scan index, consistent with the contract that operations do not renumber later characters.
- **Impossible states:** Negative infinity prevents a path that has not embedded enough pattern characters from competing with a legal plan.
- **Pattern guarantee:** Because an embedding exists initially, the final state is finite even if zero removals are possible.
- **Manifest discrepancy:** The exact two-dimensional allocation is $O(SP)$ space; only a compressed variant would meet the listed linear-space claim.
