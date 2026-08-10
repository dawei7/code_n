## General

**What can survive end-only edits**

Characters may be removed only from the beginning or end of `initial`. After any number of removals, the part left untouched must therefore be one contiguous substring of `initial`. We cannot preserve two separated pieces because removing the middle would require an operation inside the string.

Next, characters may be added at the beginning or end to obtain `target`. The untouched piece must appear contiguously inside `target` as well: target characters before it can be added to the front, and characters after it can be added to the back.

Thus any optimal transformation preserves a common substring of the two strings. If its length is $L$, the operation count is:

- remove $m-L$ characters from `initial`;
- add $n-L$ characters to form `target`.

The total is

$$
(m-L)+(n-L)=m+n-2L.
$$

Every extra preserved character saves two operations—one removal and one addition—so minimizing operations is exactly the same as finding the longest common substring.

**Dynamic programming for the longest common substring**

Define `f[i][j]` as the length of the longest equal substring that ends specifically at `initial[i-1]` and `target[j-1]`.

The word “ends” is crucial. If those two characters match, any common substring ending one position earlier in both strings can be extended:

$$
\texttt{f[i][j]}=\texttt{f[i-1][j-1]}+1.
$$

If the characters differ, no nonempty common substring can end at both positions. The table was initialized with zeros, and the code deliberately leaves `f[i][j]` as zero in that case.

This differs from longest common subsequence. A subsequence DP might carry `max(f[i-1][j], f[i][j-1])` across a mismatch, allowing skipped middle characters. End-only editing cannot preserve such disconnected characters, so carrying values across mismatches would solve the wrong problem.

The variable `mx` records the largest ending length found anywhere in the table. The longest common substring may end at any pair of positions, so returning only `f[m][n]` would incorrectly require it to end at both complete strings' final characters.

**Example trace**

For `initial = "abcde"` and `target = "cdef"`, the diagonal matches for `"cde"` build values 1, 2, and 3. Therefore `mx = 3`. The formula gives

$$
5+4-2\cdot3=3.
$$

Those operations can be realized by removing `"ab"` from the beginning and adding `"f"` to the end.

For identical strings of length $m$, the main matching diagonal reaches $m$, and the formula becomes $m+m-2m=0$.

If the strings have no common character, `mx` remains zero. All of `initial` must be removed and all of `target` added, for $m+n$ operations.

**Why the formula is both achievable and minimal**

Take a longest common substring of length $L$. Remove the prefix and suffix surrounding its occurrence in `initial`, costing $m-L$. Then add the prefix and suffix surrounding the matching occurrence in `target`, costing $n-L$. This constructs a valid sequence with $m+n-2L$ operations.

Conversely, examine any valid operation sequence. The original characters that are never removed remain consecutive because removals happen only at the ends. Additions at the ends do not split them, so those surviving characters appear as one common substring in the final target. If $K$ original characters survive, at least $m-K$ removals and $n-K$ additions are necessary. Since $K\le L$, every sequence costs at least $m+n-2L$. The constructed sequence reaches that lower bound, proving optimality.

**Relation to the manifest**

The manifest describes rolling dynamic-programming rows, but the exact source allocates `f = [[0] * (n + 1) for _ in range(m + 1)]`. It stores every row. The recurrence is the same as a rolling-row solution, but the actual space usage is quadratic rather than linear in one string length.

## Complexity detail

Let $m=\lvert\texttt{initial}\rvert$ and $n=\lvert\texttt{target}\rvert$.

The nested loops examine every pair of characters once, performing constant work per pair. Time complexity is $O(mn)$.

The exact table has $(m+1)(n+1)$ integer cells, so auxiliary space is $O(mn)$. This contradicts the manifest's $O(n)$ claim for the present source. Only if the code retained the previous DP row and current row—or used a one-dimensional array updated in the correct direction—would its space become $O(n)$.

The strings can each have length 1000, so the table contains roughly one million Python integer references plus row-list overhead. That is materially more memory than the mathematical cell count alone might suggest.

The scalar variables `mx`, `m`, `n`, `i`, and `j` add only $O(1)$ space. The returned integer is $O(1)$ output.

Swapping strings before a rolling-row implementation could make its memory $O(\min(m,n))$, but the exact implementation does not perform that optimization.

## Alternatives and edge cases

- **Rolling-row longest-common-substring DP:** Keep only the previous and current rows because `f[i][j]` depends solely on `f[i-1][j-1]`. This preserves $O(mn)$ time and reduces space to $O(n)$ or $O(\min(m,n))$.
- **One-dimensional reverse update:** Updating columns from right to left preserves the previous diagonal value in one array. It uses less memory but is easier to implement incorrectly.
- **Longest common subsequence:** This is not valid. A subsequence may skip interior characters, but end-only operations cannot remove those interior characters while preserving both sides.
- **Suffix automaton or suffix array:** These can find a longest common substring faster for very long strings, but they are more complex and unnecessary for lengths up to 1000.
- **No common character:** `mx = 0`, so remove all $m$ initial characters and add all $n$ target characters.
- **Strings already equal:** The entire string is common, giving zero operations.
- **Common substring at different positions:** Its location does not matter; different prefixes and suffixes can be removed or added at the two ends.
- **Several longest substrings:** Only the maximum length affects the cost. Any occurrence of that length supplies an optimal transformation.
- **Repeated characters:** Ending-position states distinguish different occurrences and extend only along matching diagonals.
- **Substring versus prefix or suffix:** The preserved block may be in the middle of both strings because operations can remove or add on both ends.
- **Nonempty input contract:** Both strings have at least one character, though the DP formulation and formula would also handle an empty string.
- **Full-table initialization:** Mismatch cells stay zero because the table starts at zero; explicitly assigning zero would be equivalent but unnecessary.
