## General

**Define a subproblem with two prefix lengths**

A subsequence may skip characters, but it must preserve their relative order. This makes prefixes a natural way to divide the problem. Define `f[i][j]` as the length of the longest common subsequence between:

- the first `i` characters of `text1`;
- the first `j` characters of `text2`.

The desired answer is `f[m][n]`, where `m = len(text1)` and `n = len(text2)`.

The table has `m + 1` rows and `n + 1` columns because prefix length zero is a meaningful base case. `f[0][j]` compares an empty first string with a prefix of the second, and `f[i][0]` compares a prefix of the first string with an empty second string. An empty string has no nonempty subsequence, so all of these values are zero. Initializing the entire table with zeros supplies both boundaries automatically.

**When the two newest characters match**

For state `f[i][j]`, the newest characters in the two prefixes are `text1[i - 1]` and `text2[j - 1]`. The minus one is necessary because `i` and `j` are lengths, while Python string indices are zero-based.

If those two characters are equal, they can be appended to a longest common subsequence of the shorter prefixes that exclude both newest characters. Appending the matching character preserves order because it comes after every character in both shorter prefixes. Therefore,

`f[i][j] = f[i - 1][j - 1] + 1`.

Using this match is safe rather than merely one possible guess. Adding one final character to each prefix can increase their LCS by at most one, and the matching endpoints exhibit exactly such a one-character extension of `f[i - 1][j - 1]`. An optimal common subsequence can therefore be chosen to use this shared final character without sacrificing length.

For example, when comparing prefixes `"abc"` and `"axc"`, the final characters are both `"c"`. The best common subsequence before them comes from `"ab"` and `"ax"` and has length one. Appending `"c"` gives length two.

**When the two newest characters differ**

If `text1[i - 1] != text2[j - 1]`, the two newest characters cannot be paired with each other. A common subsequence of maximum length must omit at least one of them:

- if it omits `text1[i - 1]`, its best possible length is `f[i - 1][j]`;
- if it omits `text2[j - 1]`, its best possible length is `f[i][j - 1]`.

The algorithm keeps the better option:

`f[i][j] = max(f[i - 1][j], f[i][j - 1])`.

This transition does not greedily decide which literal character is part of the final subsequence. It records only the best length available after each possible omission. Future states can build on that length, which is sufficient because the problem asks only for the length, not the subsequence itself.

**Fill states only after their dependencies**

The outer loop increases `i` from one through `m`, and the inner loop increases `j` from one through `n`. At `f[i][j]`, all referenced values are already available:

- `f[i - 1][j - 1]` and `f[i - 1][j]` are in the completed previous row;
- `f[i][j - 1]` is immediately to the left in the current row.

This dependency order is the bottom-up version of a recursive process that compares the two current characters and removes one or both. Each pair of prefix lengths is solved exactly once, avoiding the repeated subproblems of plain recursion.

**Why the dynamic program is correct**

The proof follows the combined prefix length. Base states with an empty prefix correctly have LCS length zero. Assume all smaller states are correct.

For matching final characters, appending that shared character to an optimal subsequence of the two shorter prefixes constructs a common subsequence of length `f[i - 1][j - 1] + 1`. No solution can gain more than one new matched character by adding the two endpoints, so this constructed length is optimal.

For differing final characters, no common subsequence can match those endpoints together. Every candidate must exclude at least one endpoint and therefore belongs to one of the two smaller subproblems. By the induction assumption, their best lengths are `f[i - 1][j]` and `f[i][j - 1]`. Taking the maximum considers both exhaustive possibilities and gives the optimal current length.

Thus every table cell receives the correct LCS length for its two prefixes. The bottom-right cell compares both full strings and is the requested answer.

**What the table does and does not preserve**

The table stores lengths only. It does not store parent pointers or actual subsequence strings. This avoids the cost and complexity of copying strings in every cell. If reconstruction were required, one could start at `f[m][n]` and walk toward the origin according to the transitions, but this contract needs only the integer.

Repeated characters cause no special problem. Prefix states distinguish positions even when character values repeat, and the recurrence preserves order automatically. A character position cannot be used twice because each transition moves to smaller prefix lengths before adding a match.

## Complexity detail

The two nested loops visit all `mn` pairs of nonempty prefix lengths. Each cell performs one character comparison and a constant number of table accesses, additions, or maximum operations. The exact solution therefore takes `O(mn)` time.

The exact code allocates `(m + 1)(n + 1)` integers in `f`. Its auxiliary space complexity is consequently `O(mn)`.

This is important because the local variant manifest states `O(min(m, n))` space, but that bound describes a rolling-row or rolling-column optimization that the exact `solution.py` does not implement. The current code retains the entire table, so attributing `O(min(m, n))` space to it would be inaccurate. The time bound in the manifest does match the implementation.

No recursion stack is used. The input strings themselves and the returned integer are not counted as auxiliary storage.

## Alternatives and edge cases

- **Plain recursion:** At a mismatch it explores both possible omissions and repeatedly solves the same prefix pairs, leading to exponential time in the worst case.
- **Top-down memoization:** Caching `(i, j)` states gives the same `O(mn)` time and `O(mn)` stored-state bound. It can be intuitive, but recursion depth may approach the combined string lengths.
- **Rolling two rows:** Since a cell needs only the previous row and the already computed part of the current row, the table can be reduced to `O(n)` space. Swapping the strings so the shorter one defines the row width yields `O(min(m, n))` space.
- **One rolling row:** Careful tracking of the old diagonal value can reduce the storage to one array while retaining `O(mn)` time. Update direction and the saved diagonal are easy to get wrong.
- **Reconstruct the subsequence:** Keeping the full table makes reconstruction possible through a backward walk, but the exact solution correctly stops at the length because no sequence is requested.
- **Identical strings:** Every pair of aligned characters matches, and the result is the common string length.
- **No character in common:** Every match test fails, the zero boundaries propagate through all maximum operations, and the answer is zero.
- **One-character strings:** The sole interior cell becomes one if the characters match and zero otherwise.
- **Repeated letters:** Positions remain ordered by the prefix indices. The algorithm finds the best legal pairing without reusing a position.
- **Different string lengths:** The table is rectangular and the recurrence is symmetric in meaning, so no special case is needed.
- **Subsequence versus substring:** Characters may be skipped. Requiring contiguity would be the longest-common-substring problem and would use a different mismatch transition.
- **Manifest space claim:** The advertised `O(min(m, n))` bound should not be used to describe this exact implementation unless the solution is actually rewritten to a rolling-array form. This approach intentionally documents the protected source as it exists.
