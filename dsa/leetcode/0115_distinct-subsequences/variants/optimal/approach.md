## General
**Count index selections, not merely distinct resulting text**

Let `dp[j]` be the number of increasing source-index selections within the processed source prefix that spell `t[:j]`. Different index sets count separately even when repeated source characters make their selected text look identical.

Set `dp[0] = 1`: every source prefix has exactly one way to form the empty target—select no indices. All positive target lengths initially have zero ways before any source character is processed.

**Backward updates prevent one source position from being selected twice**

For current source character `char`, if `char = t[j - 1]`, add `dp[j - 1]` to `dp[j]`. Existing `dp[j]` counts subsequences that skip this source position; the added term counts those that use it as their final selected index.

Iterate `j` from right to left. Then `dp[j - 1]` still describes the source prefix before `char`. A forward update could first use `char` to increase `dp[j - 1]` and immediately reuse the same position to increase `dp[j]`.

**Every update partitions choices by use of the current index**

After processing `s[:i]`, each `dp[j]` equals the number of increasing index selections within that prefix spelling `t[:j]`.

**Trace repeated characters as different index choices**

In `rabbbit`, each of the three source `b` positions can participate in different index choices. Backward updates accumulate those choices without merging them merely because their resulting text is the same.

**Use-or-omit partitions the source index choices**

For target prefix `t[:j]`, every subsequence choice either omits the current source position, leaving its existing count unchanged, or uses that position as the final character. The second case is possible only on a character match and extends exactly one choice forming `t[:j-1]` from earlier positions.

The cases are disjoint because they differ on whether the current index is selected, and together exhaust all index sets. Backward target updates ensure the extending count still refers to the source prefix before the current character, so no position is reused.

## Complexity detail
For source length `n`, each character examines at most `m = len(t)` target positions, giving $O(nm)$ time. The target-prefix table uses $O(m)$ space.

## Alternatives and edge cases
- **Enumerate source subsequences:** explores exponentially many index sets.
- **Two-dimensional DP:** is correct in $O(nm)$ time but uses $O(nm)$ space.
- **Update target positions forward:** reuses one source character multiple times and overcounts.
- An empty target has one subsequence in every source. A nonempty target cannot be formed from an empty source or when `len(t) > len(s)`.
- Large answers may exceed narrow integer types; use the numeric width guaranteed by the platform language contract.
