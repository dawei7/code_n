## General
**Classify an optimal transformation by its final operation**

Let `dp[i][j]` be the minimum edits turning `word1[:i]` into `word2[:j]`. Transforming empty into a target prefix needs `j` insertions, while transforming a source prefix into empty needs `i` deletions.

If the final characters match, an optimal transformation can leave them untouched and inherit `dp[i - 1][j - 1]`. Otherwise its final operation is one of:

- delete `word1[i - 1]`, following `dp[i - 1][j]`;
- insert `word2[j - 1]`, following `dp[i][j - 1]`;
- replace the source final character, following `dp[i - 1][j - 1]`.

Add one to the minimum of those three exhaustive possibilities.

**Compress the table along the shorter word**

Make the shorter word the column dimension so each DP row uses $O(\min(m,n))$ entries. The previous row supplies deletion and diagonal replacement/match costs, while the current row's preceding entry supplies insertion. Initialize each new row's column zero to its source-prefix length before filling left to right.

Swapping which input is treated as rows does not change the distance because insertion in one direction corresponds to deletion in the reverse direction and replacement is symmetric.

**Row update order preserves all three predecessors**

After computing column `j` in row `i`, the current entry is the exact distance between the first `i` source characters and first `j` target characters. `current[j - 1]` already describes the current row, while `previous[j]` and `previous[j - 1]` still describe the earlier row. This is exactly the dependency pattern required by insertion, deletion, and replacement.

**Trace operations without greedily fixing an alignment**

For `horse` to `ros`, optimal prefix choices correspond to replacing `h` with `r`, deleting the extra `r`, and deleting `e`, for distance 3. The recurrence discovers this without committing greedily to character alignments.

**The final edit exhausts all optimal possibilities**

If two prefixes end in the same character, an optimal transformation may leave that character untouched and reduce to their preceding prefixes; changing it cannot improve on zero cost. If they differ, the final edit must be an insertion, deletion, or replacement, and removing that edit exposes the corresponding smaller prefix pair.

These are all allowed final operations. Adding one to their exact predecessor costs and taking the minimum therefore yields the exact distance for the current prefixes. Building from empty-prefix base cases computes the complete strings' distance without a greedy alignment commitment.

## Complexity detail
All `mn` prefix pairs are computed once, giving $O(mn)$ time. Two rows over the shorter string use $O(\min(m,n))$ space.

## Alternatives and edge cases
- **Unmemoized recursion:** branches among three operations and repeats prefix states exponentially.
- **Full DP table:** has the same time complexity and is useful for reconstructing edits, but uses $O(mn)$ space.
- **Greedy character matching:** can make locally attractive alignments that require more edits globally.
- If either word is empty, the distance is the other word's length. Identical strings follow diagonal zero-cost transitions and return zero.
- Two-row compression computes the distance but not the edit script. Reconstructing the actual operations normally requires the full table or additional divide-and-conquer machinery.
