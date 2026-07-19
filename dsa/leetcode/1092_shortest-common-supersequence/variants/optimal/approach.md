## General
**Measure the maximum reusable backbone:** Build the longest-common-subsequence length table. `lcs[i][j]` records the greatest number of characters that prefixes `str1[:i]` and `str2[:j]` can share in order. Equal final characters extend the diagonal state; unequal characters take the better state after dropping one final character.

**Reconstruct the supersequence backward:** Start at `(m, n)`. When the current characters match, append that character once and move diagonally. Otherwise, move toward a neighboring state with the larger LCS length and append the character removed from the other string. Either direction is valid when the lengths tie.

**Include unmatched prefixes:** Once one index reaches zero, append the other string's remaining prefix. Reverse the collected characters because reconstruction proceeded from the end.

Every move appends the character needed to preserve whichever input index it decreases, and a diagonal move shares one matching character between both subsequences. Thus the result contains both inputs. It shares exactly an LCS of length $L$, so its length is $m+n-L$. No common supersequence can be shorter because sharing more than $L$ ordered characters would imply a longer common subsequence.

## Complexity detail
The table has $(m+1)(n+1)$ states and each takes constant time, giving $O(mn)$ time and space. Backtracking adds $O(m+n)$ time and output storage, which does not exceed the table bounds for non-empty inputs.

## Alternatives and edge cases
- **Store a complete string per DP state:** It is correct but repeatedly copies growing strings, adding a factor proportional to output length in time and space.
- **Compute an LCS string first:** Merge unmatched input segments around that LCS. It has the same asymptotic bounds but requires a second traversal through the inputs.
- **Greedy character matching:** A locally early match may reduce future overlap and does not guarantee minimum length.
- **Identical strings:** Return either input unchanged.
- **No common character:** Every shortest result has length $m+n$ and interleaves both strings.
- **One input already a subsequence:** Return the containing string.
- **Multiple optima:** Any minimum-length answer preserving both subsequences is valid.
