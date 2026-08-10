## General

A subsequence is determined by which source indices are selected, while their original order must be preserved. Two selections can produce the same text and still count as distinct when they use different positions. That distinction is why repeated characters create multiple ways.

Brute force could choose or skip every character of `s`, producing up to $2^{|s|}$ index selections. Most of those choices lead to the same smaller questions. The selected solution records answers for all prefix pairs in a dynamic-programming table so each smaller question is solved once.

**The meaning of one table cell**

Let $N=|s|$ and $M=|t|$. Although the source names these lengths `m` and `n`, using distinct mathematical names avoids confusing a variable name with a particular string.

`f[i][j]` is the number of ways to select indices from the first `i` characters of `s` so that their characters form exactly the first `j` characters of `t`.

This definition includes both endpoints of progress:

- `i = 0` means no source characters are available;
- `j = 0` means the desired target prefix is empty;
- `f[N][M]` is the complete problem.

The table has `N + 1` rows and `M + 1` columns so these empty-prefix states are represented directly rather than handled outside the recurrence.

**Why the empty-target column is one**

For every source prefix, there is exactly one way to form the empty target: select no source indices. Therefore the source sets `f[i][0] = 1` for every row, including `f[0][0]`.

There are zero ways to form a nonempty target from an empty source. Those cells `f[0][j]` for positive `j` remain zero from table initialization.

These values are counting identities, not merely implementation conveniences. The one in the empty-target column lets a matching source character begin a length-one subsequence through the same recurrence used everywhere else.

**The exclude-or-use decision**

Consider cell `f[i][j]`, where the newly available source character is `s[i - 1]` and the target character to finish is `t[j - 1]`.

Every valid index selection falls into one of two disjoint groups.

First, selections that do not use source position `i - 1` are exactly the ways already available from the first `i - 1` source characters. Their count is `f[i - 1][j]`. The source assigns this value unconditionally because skipping is always allowed.

Second, if `s[i - 1] == t[j - 1]`, some selections can use this new source position as the final selected character. Everything before it must form the first `j - 1` target characters from the first `i - 1` source characters, giving `f[i - 1][j - 1]` additional ways.

Thus the transition is

$$
f[i][j]
=
f[i-1][j]
+
\begin{cases}
f[i-1][j-1], & \text{if } s[i-1]=t[j-1],\\
0, & \text{otherwise}.
\end{cases}
$$

The two groups cannot overlap because one excludes index `i - 1` and the other includes it. Their union covers every valid selection, so adding their counts neither misses nor double-counts a way.

**Why prefix order enforces subsequence order**

When the transition uses `s[i - 1]` for `t[j - 1]`, all earlier target characters come from the smaller source prefix ending before index `i - 1`. Therefore selected source indices remain strictly increasing.

No explicit index list is stored. The movement from smaller prefixes to larger prefixes encodes the ordering restriction. Characters may be skipped freely, but they can never be rearranged or revisited.

**How repeated letters create the answer three**

For `s = "rabbbit"` and `t = "rabbit"`, the initial `r` and `a` have essentially forced matching positions. The interesting region contains three source `b` characters but only two consecutive target `b` characters.

As each source `b` arrives, the table preserves ways that skip it and, because it matches, adds ways that use it. Selecting two positions from those three ordered `b` positions produces three distinct index choices. The final `i` and `t` extend each choice in one way, so `f[N][M]` becomes three.

The table counts index selections rather than deduplicating the produced word `"rabbit"`. All three spell the same target, but they are distinct subsequences under the problem's definition.

**Why filling from top to bottom works**

Row `i` depends only on row `i - 1`, which has already been completed by the outer `enumerate(s, 1)` loop. Within a row, column order is not essential for this full-table version because both dependencies come from the previous row.

The loops also compute states with `j > i`, where the target prefix is longer than the available source prefix. Those cells naturally remain zero: their dependencies cannot create a way from insufficient characters. An optimization could skip them, but it is not required for correctness.

**Why the final cell is sufficient**

The state definition for `f[N][M]` is precisely the number of selections from all of `s` that form all of `t`. Initialization covers the smallest prefix cases, and the transition exhaustively partitions selections at every new source position. Therefore returning that cell gives the requested count.

The contract guarantees the final answer fits a signed 32-bit integer. Python integers also grow automatically, so intermediate additions cannot overflow.

## Complexity detail

With $N=|s|$ and $M=|t|$, the nested loops evaluate all $NM$ non-base cells. Each cell uses constant-time accesses, comparison, and addition, so time is $O(NM)$.

The table contains $(N+1)(M+1)$ Python integer entries, giving $O(NM)$ auxiliary space. This is the exact complexity of the selected source.

The manifest's $O(m)$ space claim corresponds to a one-dimensional optimization that stores only one target-length row. It does not describe this full two-dimensional `f` allocation. No definition of which length is called $m$ can turn the product-sized table into linear space.

The returned count uses $O(1)$ output space. A two-row implementation would reduce auxiliary memory to $O(M)$, and an in-place one-row implementation can achieve the same bound with careful update order.

## Alternatives and edge cases

- **One-dimensional reverse update:** Store counts for target prefixes and scan target positions backward for each source character. It preserves $O(NM)$ time while reducing space to $O(M)$.
- **Two rolling rows:** Keep the previous and current table rows. It is easier to derive than an in-place row and still uses $O(M)$ space.
- **Memoized recursion:** At state `(i, j)`, skip `s[i]` and optionally use it when characters match. It has the same state count but adds recursion overhead and can hit stack limits.
- **Brute-force subsets:** Enumerating $2^N$ source selections is infeasible at length 1,000.
- **Forward one-row update:** Incorrect unless old values are preserved, because one source character can update a shorter prefix and then be reused immediately for a longer prefix.
- **Target longer than source:** The answer is zero; the table naturally leaves `f[N][M]` zero.
- **Equal strings:** There is exactly one way when every position must be selected, subject to repeated-character alternatives only if extra source positions exist.
- **Empty target outside stated constraints:** Exactly one subsequence—the empty selection—forms it.
- **Empty source outside stated constraints:** It forms only the empty target, never a nonempty one.
- **Repeated characters:** Different index choices count separately even if their resulting character sequence is identical.
- **Uppercase versus lowercase:** English-letter comparison is case-sensitive; `"A"` does not match `"a"`.
- **No modulo:** Return the exact count. The problem guarantees the final value fits 32-bit signed range.
- **Impossible prefix lengths:** States with more target characters than source characters remain zero and may be skipped as an optimization.
- **Space reporting:** Attribute $O(M)$ only to a rolling or one-dimensional implementation, not to this selected matrix source.
