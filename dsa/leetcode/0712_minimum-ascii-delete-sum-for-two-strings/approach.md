## General

Deleting characters preserves the relative order of everything left behind. Therefore, the two final equal strings must be a common subsequence of the originals. The goal is not merely to keep as many characters as possible: deletion costs depend on ASCII values, so the dynamic program minimizes weighted deletion cost directly.

The exact solution builds a two-dimensional table over prefixes.

**State definition**

Let `f[i][j]` be the minimum ASCII cost needed to make:

- the first `i` characters of `s1`; and
- the first `j` characters of `s2`

equal using deletions only.

Index `i` represents prefix `s1[:i]`, so its last character is `s1[i-1]` when `i > 0`. The same applies to `j`.

The requested answer for both complete strings is `f[m][n]`.

**Base row and column**

If the `s2` prefix is empty, every character in `s1[:i]` must be deleted. Thus:

$$
f[i][0]=f[i-1][0]+\operatorname{ord}(s1[i-1]).
$$

The first column is filled cumulatively.

Similarly:

$$
f[0][j]=f[0][j-1]+\operatorname{ord}(s2[j-1]).
$$

`f[0][0]` remains zero because two empty strings are already equal.

These base values also show why every character occurrence contributes separately; deleting three `e` characters costs three times `ord('e')`.

**When the last prefix characters match**

If `s1[i-1] == s2[j-1]`, both equal characters can remain as the common final suffix. No deletion cost is added:

$$
f[i][j]=f[i-1][j-1].
$$

Keeping them is always safe. Any solution that deletes one or both matching terminal characters can instead keep both after an optimal solution for the shorter prefixes; this preserves equality and cannot increase deletion cost.

**When the last characters differ**

They cannot both remain at the end of equal strings. At least one must be deleted.

Deleting `s1[i-1]` costs its ASCII value and leaves subproblem `f[i-1][j]`:

$$
\operatorname{ord}(s1[i-1])+f[i-1][j].
$$

Deleting `s2[j-1]` gives:

$$
\operatorname{ord}(s2[j-1])+f[i][j-1].
$$

The table takes the smaller of these choices.

An explicit third choice that deletes both is unnecessary. After deleting one character, the remaining subproblem is free to delete the other if that is optimal. The two branches already contain every possible deletion sequence.

**Why row-major fill order works**

Cell `f[i][j]` reads:

- `f[i-1][j-1]` from the previous row;
- `f[i-1][j]` from the previous row;
- `f[i][j-1]` from the current row's previous column.

The outer loop increases `i` and the inner loop increases `j`. All three dependencies are complete before the cell is computed.

**A trace for `"sea"` and `"eat"`**

Matching `e` and `a` can be retained as the common subsequence `"ea"`.

To reach it:

- delete `s` from the first string at cost `115`;
- delete `t` from the second at cost `116`.

Total cost is `231`.

The DP does not guess `"ea"` in advance. Its match transitions keep compatible characters, while mismatch transitions compare all necessary weighted deletions. `f[3][3]` arrives at the same minimum.

**Optimal-substructure proof**

Consider an optimal solution for prefixes `i,j`.

If their last characters match, there is an optimal solution that keeps both, reducing the problem to prefixes `i-1,j-1` with no added cost.

If they differ, at least one is deleted. If the first string's last character is deleted, everything afterward must optimally solve `i-1,j`; otherwise that portion could be replaced by a cheaper solution. The symmetric case gives `i,j-1`. Taking the minimum covers the optimal solution's first required deletion.

Together with correct empty-prefix bases, induction over increasing `i+j` proves every table entry.

**Why ASCII weighting matters**

This is not simply minimum number of deletions. Deleting one high-code character may cost more than deleting another character, so transitions add `ord(...)` rather than one.

The table automatically prefers the common subsequence whose retained ASCII total makes deletions cheapest.

## Complexity detail

Let `m = len(s1)` and `n = len(s2)`.

The table contains `(m+1)(n+1)` cells. Base initialization and each transition take constant time, so total running time is

$$
O(mn).
$$

The exact implementation allocates the full two-dimensional table:

$$
O(mn)
$$

auxiliary space.

Although the recurrence can be compressed to `O(\min(m,n))` space, that optimized bound does not describe this literal source.

## Alternatives and edge cases

- **One-row DP:** Preserve the previous diagonal in a temporary variable while overwriting one row. It keeps `O(mn)` time and reduces space to `O(\min(m,n))`.

- **Weighted common subsequence:** Maximize the ASCII sum retained in a common subsequence, then subtract twice that retained sum from the total ASCII sum of both strings. It is mathematically equivalent.

- **Top-down memoization:** Cache `(i,j)` states. It has the same asymptotic table size plus recursion overhead.

- **Identical strings:** Every paired character uses the diagonal match transition, so the answer is zero.

- **No common character:** Eventually every character from both strings is deleted, and the cost is the sum of all ASCII values.

- **Repeated characters:** Positions remain distinct; DP chooses which occurrences form the cheapest ordered common subsequence.

- **Order cannot change:** Characters may be deleted but not rearranged, which is why prefix DP is necessary.

- **Deleting both mismatched characters:** This outcome is already reachable through two consecutive one-character deletion transitions.

- **Nonempty-source constraint:** Both inputs have length at least one, though the DP base row and column correctly model empty prefixes.

- **Lowercase ASCII:** `ord` returns the required ASCII values because lowercase English letters lie in ASCII.

- **Full-table memory:** With lengths up to one thousand, the Python nested list can be significant; row compression is preferable when memory is tight.
