## General

**Turn two subsequences into one constrained subsequence**

The required constructed string is a non-empty subsequence of `word1` followed by a non-empty subsequence of `word2`. Concatenate the source words:

`s = word1 + word2`.

Any allowed construction is now a subsequence of `s` that uses at least one index from each side of the boundary. Its chosen indices from `word1` automatically precede its chosen indices from `word2`.

The exact solution computes longest palindromic subsequence lengths for every interval of `s` and separately records only palindromes whose matching outer endpoints cross the word boundary.

**Define the interval DP**

`f[i][j]` is the length of a longest palindromic subsequence inside inclusive substring `s[i..j]`.

Every single character is a palindrome of length one, so `f[i][i] = 1`. Other cells begin at zero.

The outer loop moves `i` from right to left, and the inner loop moves `j` from `i + 1` to the end. This order ensures that smaller inner intervals needed by the recurrence are already known.

**When endpoint characters match**

If `s[i] == s[j]`, the source sets:

`f[i][j] = f[i + 1][j - 1] + 2`.

The equal endpoint characters can surround any longest palindromic subsequence of the interior, increasing its length by two.

For adjacent indices, `i + 1 > j - 1`. The accessed lower-triangle cell remains its initialized zero value, so two matching adjacent characters correctly produce length two.

For longest palindromic subsequence, matching endpoints can be included in an optimal solution. Any best solution that omits one endpoint fits in a smaller interval, while wrapping an optimal interior with the equal pair provides a solution at least as strong under the standard recurrence.

**When endpoint characters differ**

If `s[i] != s[j]`, a palindrome cannot use both as its two outermost selected characters. At least one endpoint must be omitted.

The best length is therefore:

`max(f[i + 1][j], f[i][j - 1])`.

These two states cover excluding the left endpoint or excluding the right endpoint. Their overlap causes no issue because only the maximum length is needed.

**Enforce use of both words through a cross-boundary pair**

Let `b = len(word1)`. Indices less than `b` belong to word one, while indices at least `b` belong to word two.

The source updates global `ans` only in the matching-endpoint branch and only when:

`i < len(word1) <= j`.

This means selected matching endpoint `i` comes from word one and endpoint `j` comes from word two. The palindrome represented by `f[i][j]` therefore uses at least one character from each word.

It is not enough for an interval merely to cross the boundary; a longest subsequence stored in a mismatch state might lie entirely on one side. Requiring the actual matched outer pair to cross gives a concrete certificate that both subsequences are non-empty.

**Why every valid answer has such a pair**

Take any palindrome formed by non-empty subsequences from both words. All selected word-one characters precede all selected word-two characters in the concatenation. The palindrome's first selected character must therefore come from word one, and its last selected character must come from word two.

First and last characters of a palindrome are equal. Hence every valid construction has a matching outer pair that crosses the boundary. When the DP processes those endpoints, it considers the best palindromic interior and updates `ans` to at least that construction's length.

This proves that restricting answer updates to cross-boundary matching pairs loses no valid optimum.

**Trace the second example**

For `word1 = "ab"` and `word2 = "ab"`, concatenated `s` is `"abab"` and the boundary is index two.

Matching `a` characters at indices zero and two cross the boundary. The interior interval can contribute a one-character palindrome `"b"`, producing length three, corresponding to `"aba"`.

The algorithm records three. No longer cross-boundary palindrome exists, so three is returned.

**Why zero represents no valid construction**

Individual characters have DP length one, and same-word palindromes may be longer, but neither satisfies the requirement that both chosen subsequences be non-empty.

`ans` starts at zero and changes only for a crossing equal pair. If no letter appears in both words in a way that can form palindrome endpoints, no qualifying update occurs and zero is returned.

**Why the final answer is correct**

The interval recurrence correctly computes longest palindromic subsequence length for every range. Every value used to update `ans` has equal selected endpoints from different words and therefore describes a valid construction.

Conversely, every valid palindrome has a matching cross-boundary outer pair, and the DP value for that pair is at least its length. Taking the maximum over all such pairs yields exactly the longest valid length.

## Complexity detail

Let $L=\lvert\texttt{word1}\rvert+\lvert\texttt{word2}\rvert$. The nested loops fill $O(L^2)$ upper-triangular interval states, with constant work per state. Time complexity is $O(L^2)$, matching the manifest.

The exact source allocates an $L \times L$ matrix of integers, so its space complexity is $O(L^2)$. This does not match the manifest's stated $O(L)$ space. A rolling or one-dimensional LPS recurrence would be needed for linear auxiliary storage, and the exact `solution.py` does not implement it.

The concatenated string and scalar state use $O(L)$ and $O(1)$ respectively, dominated by the table.

## Alternatives and edge cases

- **One-dimensional interval DP:** Carefully preserve diagonal and previous-row values to reduce storage to $O(L)$ while retaining $O(L^2)$ time.
- **Memoized recursion:** It computes the same interval states lazily but still uses $O(L^2)$ cache space in the worst case.
- **Compute independent LPS values per word:** It is insufficient because the palindrome must combine non-empty subsequences across the boundary.
- **Common-character-only shortcut:** Shared outer letters are necessary but not sufficient to determine the best interior length.
- **No character shared across words:** No cross-boundary equal pair exists, so the answer remains zero.
- **One shared character:** It can serve as both outer endpoints, yielding at least length two.
- **Odd-length palindrome:** Its center may come from either word or from the interval between cross endpoints.
- **Even-length palindrome:** The inner DP may contribute zero or another paired subsequence.
- **Adjacent matching endpoints:** The initialized lower-triangle zero makes their DP length two.
- **Non-empty subsequences:** Cross-boundary selected endpoints guarantee one chosen character from each word.
- **Long same-word palindrome:** It is not returned unless it can be wrapped or represented by a crossing pair.
- **Mismatching interval endpoints:** The recurrence drops one endpoint and keeps the better subinterval.
- **Equal endpoints:** Wrapping the best interior gives the standard optimal LPS state.
- **Return length only:** The table stores lengths and does not reconstruct the chosen subsequences.
- **Input preservation:** Concatenation creates `s`; neither original word is modified.
