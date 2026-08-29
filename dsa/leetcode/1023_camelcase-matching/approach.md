## General

**Translate insertion into a constrained subsequence test**

A query matches the pattern when it can be created by inserting lowercase letters into the pattern. Looking in the opposite direction, the original pattern characters must appear in the query in the same order, and every query character not used for that match must be lowercase.

The first requirement resembles an ordinary subsequence check. The second requirement is the crucial extra rule. An unmatched lowercase letter may be explained as an insertion, but an unmatched uppercase letter cannot. Therefore, the algorithm may skip lowercase query characters while searching for the next pattern character, but it must reject immediately when a different uppercase character blocks the search.

The helper `check(s, t)` treats `s` as one query and `t` as the pattern. The pointer `i` is the next unprocessed position in `s`, while `j` is the next unmatched position in `t`.

**How the inner loop searches safely**

While a pattern character remains, the code runs:

`while i < m and s[i] != t[j] and s[i].islower(): i += 1`.

This skips a query character only when all three facts hold:

- The query still has a character.
- That character does not match the required pattern character.
- The query character is lowercase.

Such a character can legally be one of the lowercase insertions, so discarding it loses no valid match.

The loop stops for one of three reasons. It may find `s[i] == t[j]`, it may reach the end of the query, or it may encounter a mismatching uppercase character. Only the first reason is successful.

The next condition, `if i == m or s[i] != t[j]: return False`, distinguishes those cases. Reaching the end means the required pattern character is absent. A mismatch while still inside the query means the current query character must be uppercase because mismatching lowercase letters would have been skipped. That uppercase letter cannot be inserted, and it does not equal the required pattern character, so no legal alignment can pass it.

When the characters match, `i, j = i + 1, j + 1` consumes both. Pattern characters cannot be reordered or reused, and this simultaneous advance preserves their required left-to-right order.

**Why greedily taking the first match is safe**

When `s[i] == t[j]`, the helper immediately pairs them instead of searching for a later copy. This earliest-match choice cannot destroy a solution. A later occurrence would leave the current matching query character unused. If the current character is uppercase, leaving it unused is illegal. If it is lowercase, matching it earlier only leaves a longer suffix in which to match the remaining pattern, never a shorter one.

Thus, among all legal alignments, using the earliest available exact match is always at least as flexible as postponing the match. No backtracking or dynamic programming is needed.

**What happens after the entire pattern matches**

The main loop ends when `j == n`. At that point every pattern character has been matched, but the query may have a suffix left.

Any remaining lowercase letters can legally have been inserted after the pattern, so the second loop skips them:

`while i < m and s[i].islower(): i += 1`.

The helper returns `i == m`. If the query is exhausted, every unmatched character was lowercase and the match is valid. If a character remains, the first remaining one is uppercase, and there is no pattern character left to match it. The query must therefore be rejected.

This final scan is essential. A plain subsequence test would incorrectly accept `"FooBarTest"` for pattern `"FB"` because it can find `F` and `B` while ignoring the extra uppercase `T`. The actual rules allow inserting `"oo"` and `"ar"`, but they do not allow inserting `T`.

**A successful trace**

Use query `"FootBall"` and pattern `"FB"`.

The pointers begin at the two `F` characters, so they match immediately. Both pointers advance. The next required pattern character is `B`. Query letters `o`, `o`, and `t` differ from `B` but are lowercase, so the inner loop skips them. It then reaches uppercase `B`, which matches and is consumed.

The pattern is finished. The remaining query suffix `"all"` is entirely lowercase, so the trailing loop consumes it and `i == m` is true. Conceptually, `"FootBall"` is obtained from `"FB"` by inserting `"oot"` between the pattern letters and `"all"` afterward.

**A failure caused by an extra uppercase character**

Use query `"FooBarTest"` with pattern `"FB"`. The helper matches `F`, skips lowercase `oo`, and matches `B`. It then skips lowercase `ar` in the trailing loop. The next character is uppercase `T`, which the loop may not skip. Since the pattern has no character left for it, `i != m` and the helper returns `False`.

Another failure occurs with query `"FrameBuffer"` and pattern `"FoBa"`. After matching `F`, lowercase `r` can be skipped, but lowercase `a` does not equal the required `o` and can also be skipped. Eventually the scan encounters uppercase `B` while still needing lowercase `o`. Because `B` is neither skippable nor a match, failure is immediate. No later `o` could repair the illegal unmatched uppercase character.

**Why the helper is correct**

Before each attempt to match `t[j]`, all pattern characters before `j` have been matched in order, and every skipped query character before `i` is lowercase. The inner loop preserves this fact by skipping only legal insertions.

If the helper rejects inside the main loop, either the query ended before all pattern characters were found or a mismatching uppercase query character was encountered. Neither obstacle can be crossed using lowercase insertions, so no valid construction exists.

If a match is found, consuming the earliest exact character preserves the possibility of every remaining alignment. After all pattern characters are consumed, the trailing loop accepts exactly when every leftover query character is lowercase. Therefore, `check` returns true if and only if the query can be formed from the pattern by lowercase insertions.

The outer list comprehension calls this independent test for every query and preserves their input order, producing one Boolean answer per string.

## Complexity detail

For one query of length `M` and a pattern of length `P`, pointer `i` only moves forward and advances at most `M` times. Pointer `j` advances at most `P` times. Neither pointer ever retreats, so the helper takes `O(M + P)` time rather than multiplying the two lengths.

Let

$$
S = \sum_{q \in \texttt{queries}} \left(\lvert q\rvert + \lvert\texttt{pattern}\rvert\right).
$$

Across all queries, total time is `O(S)`, matching the manifest. If the repeated pattern length is treated as a small fixed constraint, this is often described simply as linear in the total query characters.

The helper stores lengths, two indices, and references to its two strings, all constant-sized. It creates no substring, stack, or matching table, so auxiliary space is `O(1)` per query. The returned Boolean list contains one item per query and requires `O(Q)` output space for `Q = len(queries)`. The manifest's `O(1)` space bound uses the usual convention of excluding required output storage.

## Alternatives and edge cases

- **Ordinary subsequence matching:** Checking only whether `pattern` is a subsequence of a query is insufficient because it would skip unmatched uppercase letters. The lowercase-only insertion restriction must be enforced.
- **Delete lowercase letters and compare uppercase skeletons:** Matching the uppercase sequences is necessary but not sufficient when the pattern itself contains lowercase letters. The exact positions and order of every pattern character still matter.
- **Regular expression construction:** One could place a lowercase-letter wildcard around pattern characters, but escaping and anchoring are easy to mishandle, and a two-pointer scan is simpler and strictly linear.
- **Dynamic programming:** A table over query and pattern positions can model skip-or-match choices, but lowercase skips and forced uppercase matches make the greedy earliest-match argument sufficient. DP adds `O(MP)` time or space without benefit.
- **Backtracking over repeated lowercase letters:** Trying every occurrence of a pattern character is unnecessary. Matching the earliest occurrence leaves the largest possible suffix and is always safe.
- **Exact equality:** If query and pattern are identical, every character matches in order, both pointers finish together, and the result is true.
- **All-lowercase additions:** Extra lowercase letters may appear before, between, or after pattern characters. Both loops allow precisely those insertions.
- **Unexpected uppercase before a needed character:** It causes immediate failure even if the needed character appears later, because that uppercase character cannot be explained as an insertion.
- **Unexpected uppercase after the pattern:** The trailing loop stops and returns false, preventing a plain-subsequence false positive.
- **Lowercase pattern characters:** They must be matched exactly and in order. Other lowercase query characters may be skipped around them.
- **Pattern containing uppercase and lowercase:** Character case is part of equality. Lowercase `f` never matches uppercase `F`, and uppercase mismatches cannot be skipped.
- **Repeated characters:** The earliest matching occurrence is consumed. This is safe because pointers only need to preserve order, and earlier consumption leaves at least as much suffix for later pattern characters.
- **One-character pattern:** The method finds that exact character, rejects any blocking uppercase before it, and then requires every remaining query character to be lowercase.
- **Nonempty contract:** Both queries and pattern contain at least one character, so the exact code does not need a special empty-pattern branch. Its trailing logic would still describe the right restriction for an empty pattern: only all-lowercase queries could match.
