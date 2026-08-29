## General

**A valid answer can stay inside one string or cross the concatenation boundary.** Because either selected substring may be empty, the longest palindromic substring already present in `s` or `t` is always a candidate.

If a palindrome uses characters from both strings, its outer part taken from `s` must match the reverse of its outer part taken from `t`. Any unmatched center lies entirely on one side of the concatenation boundary and must itself be a palindrome.

The source computes exactly these two ingredients: longest palindromes beginning at each position, and matching cross-string blocks after reversing `t`.

**Precompute palindromic substrings by expanding every center.** Helper `calc(u)` creates array `g` where `g[l]` becomes the maximum length of a palindromic substring of `u` beginning at index `l`.

For each center index, it calls `expand` twice:

- `expand(u, g, i, i)` finds odd-length palindromes;
- `expand(u, g, i, i + 1)` finds even-length palindromes.

While the two boundary characters match, the substring `u[l..r]` is a palindrome. The assignment

`g[l] = max(g[l], r - l + 1)`

records its length for its starting position, then both boundaries move outward.

Every palindrome has either one character or one gap as its center, so one of these expansions discovers it. Taking a maximum leaves the longest palindrome for each start.

**Reverse `t` so mirrored outer pieces become equal substrings.** Let `v = t[::-1]`. If block $A$ appears in `s` and the same block appears in `v`, then the corresponding block in original `t` is $\operatorname{reverse}(A)$. Concatenating $A$ from `s` with that original block from `t` gives the mirrored outer structure

$$
A+\operatorname{reverse}(A).
$$

The source replaces local `t` with its reverse and computes `g2 = calc(t)` on that reversed representation. Palindromicity is preserved under reversal, so a palindrome recorded in reversed `t` corresponds to a palindrome on the original `t` side as well.

**Use longest-common-substring DP for the matched outer block.** Table entry `f[i][j]` is the length of the longest equal substring ending at `s[i-1]` and reversed-`t[j-1]`.

When characters match,

`f[i][j] = f[i - 1][j - 1] + 1`.

When they differ, the zero-initialized entry remains zero. There is no transition from left or above, so this is a common-substring table, not a common-subsequence table. Contiguity is essential because the selected pieces from both inputs must be substrings.

If `L = f[i][j]`, the matching blocks occupy `s[i-L:i]` and reversed `t[j-L:j]`. They can form an even palindrome of length $2L$.

**Attach the best possible center from either side.** The matched block in `s` ends just before index `i`. If `i < len(s)`, `g1[i]` is the longest palindrome starting immediately after it. This gives a candidate

$$
2L+\texttt{g1}[i].
$$

Its shape is $A+P+\operatorname{reverse}(A)$, where $P$ is the middle palindrome taken from the `s` substring.

Symmetrically, `g2[j]` supplies a middle palindrome on the reversed-`t` side, corresponding to a center contained in the selected original `t` substring. The code evaluates both choices. If the matching block reaches the end of one working string, the conditional contributes zero because no characters remain for a center there.

A crossing palindrome cannot need unrelated centers on both sides: after removing all mirrored cross-boundary pairs, the unmatched center is one contiguous palindrome and lies on only one side of the boundary.

**Include one-string answers.** `ans = max(*g1, *g2)` initializes the result with the longest palindrome found entirely in either input. This covers cases such as `s = "b"` and `t = "aaaa"`, where the best answer uses an empty substring from `s`.

For `s = "abcde"` and `t = "ecdba"`, reversing `t` exposes matching outer block `"ab"` with the start of `s`. A suitable one-character center `"c"` follows in `s`, producing `"abcba"` of length five.

**Why the construction is complete.** Take any optimal palindrome. If it lies in one string, `calc` includes it. Otherwise, strip matching characters from its two ends while both sides cross the concatenation boundary. The stripped `s` block equals the reverse of the stripped `t` block, so the common-substring DP discovers their full contiguous match. What remains is empty or a palindromic center wholly in one source, and the corresponding `g` array offers a center at least as long. Thus one candidate reaches the optimum. Every candidate the code builds has mirrored equal outer blocks and a palindromic center, so it is valid.

**The source is not the rolling-space implementation described by the manifest.** It allocates the entire `(m+1) * (n+1)` table. Its time agrees with the small-version manifest, but its space does not.

## Complexity detail

Let $m=\lvert s\rvert$ and $n=\lvert t\rvert$. Expanding all odd and even centers costs $O(m^2)$ for `s` and $O(n^2)$ for reversed `t` in the worst case, such as repeated equal characters.

The common-substring table performs $mn$ constant-time cell checks, costing $O(mn)$. Total time is

$$
O(m^2+n^2+mn).
$$

The full DP table uses $O(mn)$ space. Palindrome arrays and reversed `t` use $O(m+n)$. Peak auxiliary space is $O(mn+m+n)=O(mn)$, not the manifest's $O(m+n)$ rolling-space claim.

With both lengths at most thirty, this full table is small and practical.

## Alternatives and edge cases

- **Enumerate every substring pair and test concatenations:** There are far too many pairs, and repeated palindrome checks add more work.
- **Longest common subsequence:** It permits gaps, but selected pieces and mirrored outer blocks must be contiguous.
- **Rolling the common-substring DP:** Only the previous row is needed, reducing space to $O(n)$; the protected source does not apply it.
- **Use only crossing palindromes:** Either substring may be empty, so palindromes wholly inside one source must be considered.
- **Even palindrome:** The center contribution may be zero, leaving exactly two mirrored blocks.
- **Odd palindrome:** A one-character or longer odd center can come from either side.
- **No shared character:** Cross-string DP remains zero, and the best single-character palindrome gives answer one.
- **Entire input palindrome:** `calc` records it at start zero.
- **Boundary index at string end:** The conditional center term becomes zero and avoids an out-of-range lookup.
- **Reversing `t`:** This turns a needed reverse match into ordinary substring equality.
- **Duplicate candidate constructions:** Only maximum length matters, so the source does not reconstruct or deduplicate strings.
- **Manifest fidelity:** The exact file uses quadratic center expansion and a full two-dimensional table.
