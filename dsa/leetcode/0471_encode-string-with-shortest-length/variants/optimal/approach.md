## General

The shortest encoding of a substring can arise in two fundamentally different ways. The entire substring may be repetitions of one smaller unit, producing `count[encoded_unit]`, or it may be best written as a concatenation of two independently encoded parts. Interval dynamic programming considers both possibilities for every substring.

Let `f[i][j]` hold one shortest representation found for the inclusive substring `s[i:j+1]`. The table stores actual encoded strings rather than only their lengths, so the final answer is directly available at `f[0][n - 1]`.

**Why the table order matters**

The outer loop moves `i` from right to left, and the inner loop moves `j` from `i` to the end. When computing `f[i][j]`:

- Every shorter interval `f[i][k]` with the same start and `k < j` was computed earlier in the current row.
- Every suffix interval `f[k + 1][j]` starts later than `i`, so it was computed during an earlier outer-loop iteration.

Therefore all subproblems needed for splits already exist. A repeated unit `f[i][i + period - 1]` is also a shorter same-start interval and is ready.

**Start with a whole-interval candidate**

Helper `g(i, j)` first considers representing the entire interval without a top-level split. Let `t = s[i:j+1]`.

If `len(t) < 5`, it returns `t` literally. The shortest possible useful repeated form has at least four syntax characters, such as `2[a]`; for strings shorter than five, encoding cannot be strictly shorter than the literal under the source rule.

For longer strings, it looks for a nontrivial period with

`k = (t + t).index(t, 1)`.

As in rotation-based periodicity testing, an occurrence of `t` inside `t + t` starting before `len(t)` means `t` repeats a smaller prefix. The earliest such start `k` is its smallest period. If `k < len(t)`, the repetition count is `len(t) // k`, and the candidate becomes

`count[f[i][i + k - 1]]` with actual bracket syntax.

Importantly, the repeated unit uses its already optimal encoding from the DP table, not necessarily its literal text. Nested encodings can therefore arise naturally.

If no proper period exists, `g` returns the literal substring.

**Try every top-level split**

For intervals longer than four, the loop considers every split point `k` from `i` through `j - 1` and forms

`f[i][k] + f[k + 1][j]`.

Both halves are already shortest encodings for their substrings. If their concatenation is strictly shorter than the current candidate, it replaces `f[i][j]`. Equal-length candidates are left unchanged, which is acceptable because the problem allows any minimum-length representation.

Splits are essential even when the whole interval is not periodic. For example, one region may be highly repetitive while a neighboring literal region is not. They should be encoded independently and concatenated.

**Why these choices cover every encoding**

Consider the top level of any valid encoding for substring `s[i:j+1]`.

- If the whole decoded interval is one repeated unit enclosed by an outer `count[...]`, `g` considers its periodic representation and recursively uses the best encoding of that unit.
- Otherwise, the encoded text has at least two top-level adjacent components. There is a boundary in the decoded string between them, and one of the DP split points considers exactly that division. Each side can use its own optimal nested encoding.
- The literal substring remains available as a fallback.

By induction on interval length, all smaller table entries are shortest. Trying the whole repetition, every possible concatenation boundary, and the literal therefore finds a minimum-length candidate for the current interval.

**Trace simple cases**

For `"aaa"`, length is below five, so the literal is kept. `3[a]` would be longer.

For `"aaaaa"`, the doubled-string search finds period one. The unit `"a"` is already stored literally, so `g` produces `"5[a]"`, which is shorter than five literal characters.

For ten `a` characters, the whole-period candidate is `"10[a]"`. Splits may discover alternatives such as `"a9[a]"`; the DP retains whichever minimum-length candidate it encounters according to strict length comparisons.

**Two exact-source caveats**

The Reference says not to use repetition syntax unless it is strictly shorter. `g` checks only `len(t) >= 5` and periodicity, not whether the resulting encoded candidate is actually shorter. For `t = "abcabc"`, it produces `"2[abc]"`, which has the same length as the literal. The overall result still has minimum length, but its representation violates that stricter wording. The document records this behavior rather than claiming the exact source enforces a check it does not contain.

The table also stores and concatenates full strings during optimization. That matters for a literal analysis of Python running time and memory, as explained below.

## Complexity detail

There are $O(n^2)$ intervals and $O(n)$ split points per interval, giving $O(n^3)$ candidate splits in the abstract interval-DP operation count. This is the manifest's time bound when candidate combination and length comparison are treated as constant-time decisions and reconstruction is deferred.

In the exact Python source, `f[i][k] + f[k + 1][j]` copies up to $O(n)$ characters for every split. Consequently, a conservative bound on actual character-copy work is $O(n^4)$. Substring creation, doubled-string periodicity searches, and formatted candidates add lower-order or implementation-dependent character work under that bound.

The table has $O(n^2)$ entries, matching the manifest's reference-count view. Because each entry retains an encoded string of length up to $O(n)$, the exact materialized character storage can reach $O(n^3)$ in a conservative worst-case accounting, plus temporary concatenations. With `n <= 150`, this representation is still practically bounded, but it is not literally $O(n^2)$ bytes.

A design storing only best lengths and reconstruction decisions would achieve the intended $O(n^2)$ table space and reconstruct one answer afterward.

## Alternatives and edge cases

- **Length-and-decision DP:** Store cost plus a split or period choice, then reconstruct once. This avoids copying full strings for every candidate and better realizes the manifest bounds.
- **Greedily encode the longest repeated region:** Local compression can prevent a better global split or nested encoding; interval DP is needed for optimality.
- **Only test whole-string repetition:** Misses inputs whose best answer concatenates several independently compressible regions.
- **KMP period detection:** A prefix function can find the smallest period in linear time per interval without doubled-string searching.
- **Length below five:** No repeated syntax can be strictly shorter, so the helper returns literal text.
- **Equal-length encoding:** The exact helper may choose it for periodic strings of length at least five, despite the Reference's strict-shortening condition.
- **Even multiple periods:** The smallest period is used for the whole-interval candidate; split DP still evaluates other top-level structures.
- **Nested repetition:** The bracket body comes from an already optimized table entry, so nested compression is supported.
- **Several optimal answers:** Strict `<` replacement keeps the first minimum-length candidate encountered, which is permitted.
- **Input preservation:** Strings are immutable and the algorithm never changes `s`.
