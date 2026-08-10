## General

The competitive source keeps one dynamic-programming row. It processes source characters from left to right, and `ways[j]` records how many index selections from the source prefix processed so far form the first `j` characters of `T`.

Let $N=|S|$ and $M=|T|$. The list has `M + 1` entries so it can represent target prefix lengths from zero through $M$. The returned `ways[M]` is the count for the complete target.

**The base value that starts every subsequence**

`ways[0] = 1` because every processed source prefix contains the empty target exactly once: choose no indices. All positive target-prefix counts begin at zero because no source characters have been processed yet.

The zero-prefix value stays one throughout the algorithm. Source characters can always be ignored, and there is never a second distinct way to choose no characters.

This base value allows the first matching source character to extend the empty subsequence into a one-character target prefix.

**What one matching source character contributes**

Suppose the current source character `S_char` equals `T[j]`. Any previously counted way to form target prefix length `j` can append this source position and become a way to form target prefix length `j + 1`.

The update is therefore:

`ways[j + 1] += ways[j]`.

The existing value of `ways[j + 1]` represents selections that formed that longer target prefix without using the current source position. The added `ways[j]` represents selections that do use it. The two groups are disjoint and together cover all possibilities after processing this character.

If the characters do not match, no selection ending with the current source character can form that target position. Leaving the entry unchanged corresponds to skipping the character.

**Why the target loop must run backward**

All updates for one `S_char` must read counts from before that source character was processed. A backward scan from target index `M - 1` to zero guarantees this.

When updating `ways[j + 1]`, the source reads `ways[j]`, a lower-index entry that has not yet been changed during the current backward pass. Therefore the current source position is used at most once.

A forward scan would be wrong. For `S = "a"` and `T = "aa"`, it could first change `ways[1]` from zero to one, then immediately use that new value to change `ways[2]` to one. That falsely claims a single source position supplies both target characters.

Backward iteration protects the temporal meaning of the row: values read on the right-hand side belong to the previous source prefix, while destination values accumulate the new prefix's results.

**How the source implements reverse enumeration**

`enumerate(T)` produces target index-character pairs in forward order. The source materializes those pairs with `list(...)`, wraps them in `reversed(...)`, and then loops from the final target position down to the first.

This achieves the correct dependency order. A direct `range(M - 1, -1, -1)` would avoid creating the temporary list of pairs on every source iteration, but both have the same asymptotic $O(M)$ transient space bound and $O(NM)$ time.

**Why the count represents distinct index selections**

Each source position is processed exactly once. Every update either leaves an existing selection unchanged, meaning the position is skipped, or extends a shorter selection with this exact new position.

Because source positions arrive left to right, appending the current position preserves increasing index order automatically. Two ways that differ at any chosen position remain separate counts even when repeated characters make their resulting strings identical.

This gives an exhaustive, non-overlapping partition by the last processed source position, just as a two-dimensional prefix table would.

**Tracing the three `b` choices**

For `S = "rabbbit"` and `T = "rabbit"`, early characters build one way to form `"ra"`. Each of the three source `b` characters updates the target prefixes ending in `b`.

Because the scan is backward, a particular `b` can extend `"rab"` to `"rabb"` or extend `"ra"` to `"rab"` based only on counts that existed before that same source `b`. It cannot occupy both positions in one selection.

After all three `b` characters, the count for choosing two ordered `b` positions is three. The trailing `i` and `t` extend those three ways, and `ways[len(T)]` returns three.

**Why longer and impossible targets behave naturally**

If `T` is longer than `S`, not enough source positions can ever be selected. Entries beyond the number of processed source characters remain zero, so the final result is zero without a special branch.

Character mismatches simply produce no updates. The method does not need to search for next occurrences or build actual subsequence strings.

The parameter names use uppercase `S` and `T`, but the comparison is ordinary case-sensitive Python string equality. The 32-bit result guarantee needs no special handling because Python integers do not overflow.

## Complexity detail

The outer loop runs $N$ times. The inner loop examines all $M$ target characters each time, so total time is $O(NM)$. Creating `list(enumerate(T))` also costs $O(M)$ per source character and is included in that product.

`ways` contains $M+1$ integers. During each outer iteration, the materialized enumeration contains $M$ index-character pairs. These allocations coexist only for that iteration, so peak auxiliary space is still $O(M)$, though with a larger constant than a direct backward range.

The returned integer needs $O(1)$ output space. The source header's coarse $O(n^2)$ time is consistent only when both string lengths are treated as the same scale; $O(NM)$ is the precise two-input bound.

The manifest's linear-space statement matches this selected implementation, provided its variable $m$ denotes target length. If the target is much larger than the source, an implementation could swap conceptual formulations only with care because source and target roles are not symmetric.

## Alternatives and edge cases

- **Full two-dimensional table:** Store every source-prefix and target-prefix state. It is the clearest derivation but uses $O(NM)$ space.
- **Two rolling rows:** Keeps old and new states separate, allowing a forward target scan with $O(M)$ memory and simpler dependency reasoning.
- **Direct backward indices:** Replace `reversed(list(enumerate(T)))` with a descending `range`; this avoids rebuilding a list of pairs on every source character.
- **Memoized include-or-skip recursion:** Matches the combinatorial decision directly but uses up to $O(NM)$ cached states and recursion depth $O(N)$.
- **Forward in-place scan:** Incorrect because it can reuse one source character for multiple target positions.
- **Empty target outside constraints:** `ways[0]` returns one, representing the empty selection.
- **Empty source outside constraints:** All positive target-prefix counts stay zero.
- **Target longer than source:** Returns zero naturally.
- **Repeated source characters:** Each position supplies separate choices, so their contributions must be added rather than deduplicated.
- **Repeated target characters:** Reverse order is especially critical because adjacent target positions may match the same current source character.
- **Case sensitivity:** Uppercase and lowercase English letters are different characters.
- **Exact arithmetic:** No modulo operation is allowed or needed.
- **Skipping a source character:** Represented by leaving all prior counts in `ways` unchanged.
- **Using a source character:** Extends only target prefixes whose next character matches it.
- **Count versus construction:** The algorithm stores counts, not the actual index selections, which is why memory depends on target length rather than the potentially huge number of subsequences.
