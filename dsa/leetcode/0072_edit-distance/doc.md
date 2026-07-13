# Edit Distance

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 72 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/edit-distance/) |

## Problem Description
### Goal
You are given a source string `word1` and a target string `word2`. One operation may insert a character, delete a character, or replace one character with another, and every operation has cost one.

Return the minimum total operations needed to transform the complete source into the complete target. Characters already aligned and equal require no operation. Either string may be empty, in which case every character of the other must be inserted or deleted.

### Function Contract
**Inputs**

- `word1`: the source string
- `word2`: the target string

**Return value**

The minimum edit count as an integer.

### Examples
**Example 1**

- Input: `word1 = "horse", word2 = "ros"`
- Output: `3`

**Example 2**

- Input: `word1 = "intention", word2 = "execution"`
- Output: `5`

**Example 3**

- Input: `word1 = "", word2 = "abc"`
- Output: `3`

### Required Complexity

- **Time:** $O(mn)$
- **Space:** $O(\min(m,n))$

<details>
<summary>Approach</summary>

#### General

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

#### Complexity detail

All `mn` prefix pairs are computed once, giving $O(mn)$ time. Two rows over the shorter string use $O(\min(m,n))$ space.

#### Alternatives and edge cases

- **Unmemoized recursion:** branches among three operations and repeats prefix states exponentially.
- **Full DP table:** has the same time complexity and is useful for reconstructing edits, but uses $O(mn)$ space.
- **Greedy character matching:** can make locally attractive alignments that require more edits globally.
- If either word is empty, the distance is the other word's length. Identical strings follow diagonal zero-cost transitions and return zero.
- Two-row compression computes the distance but not the edit script. Reconstructing the actual operations normally requires the full table or additional divide-and-conquer machinery.

</details>
