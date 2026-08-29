## General

**Separate exact suffix feasibility from the one allowed mismatch.** The answer chooses `len(word2)` increasing indices from `word1`. Their characters must equal `word2` at every selected position except possibly one. Among all feasible index arrays, lexicographic order prioritizes the first selected index, then the second, and so on. This suggests scanning source indices from left to right and taking the earliest index that can still lead to a complete answer.

The difficult part is deciding whether using the one mismatch at a particular early index leaves enough exact matches for the remaining target suffix. The array `suffix_matches` answers that question.

**Meaning of `suffix_matches[index]`.** The preprocessing scans `word1` from right to left while `matched` counts how many final characters of `word2` have been greedily matched. If the current source character equals the next still-needed target character from the end, `matched` increases. Then `suffix_matches[index]` receives that count.

Consequently, `suffix_matches[index]` is the maximum length $q$ such that the last $q$ characters of `word2` can be matched exactly as a subsequence of `word1[index:]`. Greedily taking the rightmost possible match is optimal for suffix feasibility: it leaves the greatest possible prefix of the source suffix available for earlier target characters. The count never decreases as preprocessing moves left.

For a target position `target_index = j`, after selecting one source character for `word2[j]`, the remaining target is `word2[j+1:]`. That is exactly the suffix of `word2` with length `target_length - j - 1`. Therefore the condition

`suffix_matches[index + 1] >= target_length - target_index - 1`

says that every remaining target character can be matched exactly after the current source index.

**Greedily construct the smallest index array.** The forward scan considers source indices in ascending order. If `word1[index] == word2[target_index]`, the code appends the index as an exact match and advances the target. Taking the earliest exact match is always safe: it spends no mismatch and leaves at least as many later source characters as postponing that same target character.

If the characters differ, the index can be selected only by spending the one allowed change. The source requires `mismatch_available` and the suffix-feasibility condition above. If both hold, it appends this index, advances the target, and permanently sets `mismatch_available = False`. All remaining selected characters must then match exactly.

If a mismatching index cannot pass the suffix check, spending the change there could not complete the target, so the scan correctly skips it. It may later find an exact match for the current target character, or a later mismatching position whose remaining suffix is feasible.

**Why it is correct to spend the mismatch as early as safely possible.** Suppose the current index differs from the next target character but the suffix check succeeds. Selecting it creates a valid completion: change this one character and use the guaranteed exact suffix matches. Any solution that skips this source index must select a larger index for the same answer position. All earlier answer entries are already fixed, so the solution selecting the current index is lexicographically smaller regardless of its later indices. Therefore the greedy choice is forced for the lexicographically minimum answer.

If the current character is an exact match, selecting it is at least as strong: it obtains the same earliest index without consuming the mismatch. There is no benefit to skipping an exact match in hopes of changing an earlier target position later, because target positions are being filled in order and earlier ones are already fixed.

**A prefix invariant proves global lexicographic minimality.** Before considering each source index, `answer` is the lexicographically smallest feasible selected prefix for the first `target_index` target characters among all choices using the already scanned source prefix, with its recorded mismatch status. At the current index, the code selects it whenever selection is feasible and either exact or safely spends the mismatch. Any alternative that skips a feasible current selection has a larger next chosen index. When selection is not feasible, no valid completion can use it under the available mismatch state. Induction preserves the invariant until all target positions are filled.

**Why failure returns the empty array.** The scan stops early once `target_index == target_length`, because the required number of indices has been chosen. If the full source is exhausted first, every source index was either selected or proved unusable for the next target position under the remaining mismatch budget. The greedy-safe choices do not eliminate a lexicographically later feasible completion, so an unfinished target means no valid sequence exists. The conditional return therefore yields `answer` only when it has exactly the required length.

“At most one” change includes zero changes. If `word2` is already an exact subsequence, the exact-match branch can complete it without ever clearing `mismatch_available`. If a mismatch occurs at the final target position, the remaining length is zero, and the suffix condition is automatically true; the earliest available source index may safely be used.

## Complexity detail

Let $n=\lvert\texttt{word1}\rvert$ and $m=\lvert\texttt{word2}\rvert$. The reverse preprocessing scans $n$ source characters and advances `matched` at most $m$ times. The greedy construction scans at most $n$ characters and appends exactly $m$ indices on success. Total time is $O(n+m)$, conventionally simplified to $O(n)$ here because the constraints guarantee $m<n$.

`suffix_matches` has length $n+1$ and uses $O(n)$ space. The returned `answer` uses $O(m)$ result space. Excluding output, auxiliary space is $O(n)$, matching the manifest. A rightmost-position array indexed by target position, as in the editorial, can reduce preprocessing storage to $O(m)$, but the exact source stores a feasibility count for every source suffix.

## Alternatives and edge cases

- **Editorial rightmost-position array:** Store the latest feasible source index for each target suffix character, then test whether the current index lies before the next required position. It achieves $O(n+m)$ time and $O(m)$ space.
- **Dynamic programming over mismatch usage:** A table can decide feasibility for every pair of prefixes and zero/one changes, but the naive form costs $O(nm)$ and is unnecessary.
- **Try every possible changed target position:** Running a subsequence construction separately for each of $m$ mismatch locations can become $O(nm)$.
- **Always take the earliest mismatching index:** This is incorrect without the suffix check; an early change may leave too few exact characters to complete `word2`.
- **Never use a mismatch until forced:** This can miss a lexicographically smaller answer. A safely usable earlier mismatching source index beats any later exact index in the index-array ordering.
- **Exact match available:** The source takes it immediately and preserves the mismatch for later, which cannot reduce feasibility.
- **Mismatch at the final target character:** The remaining required length is zero, so any current source character can fill that position if the mismatch is still available.
- **No mismatch needed:** An exact subsequence is valid because the definition permits at most one change, not exactly one.
- **Target nearly as long as source:** The suffix test becomes especially important because selecting one unusable early index can leave insufficient positions.
- **Repeated characters:** Greedy exact matching still chooses the earliest occurrence that preserves maximum remaining source space; suffix counts do not rely on character uniqueness.
- **Unfinished target after the scan:** Returning a partial index list would violate the required size, so the source returns an empty array.
- **Lexicographic object:** The comparison is between index arrays, not the selected strings. This is why an earlier mismatching index can be preferable to a later exact-character index.
- **Source-generated comment:** The file notes that its implementation was AI-generated, but its suffix-count invariant and forward feasibility check can be verified independently as above.
- **Input mutation:** Strings are immutable, and the method only reads them. The returned indices are newly allocated and sorted automatically by the forward scan.
