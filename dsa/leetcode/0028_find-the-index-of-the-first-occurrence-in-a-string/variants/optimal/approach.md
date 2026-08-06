## General
**A mismatch can reuse a border of the matched pattern prefix**

Knuth-Morris-Pratt matching stores, for every pattern prefix ending at position `i`, the length of its longest proper prefix that is also a suffix. A **proper** prefix is shorter than the whole prefix. This `lps` value identifies how many already-matched pattern characters can remain useful after a mismatch.

Build the array with `border`, the length of the proper border currently being tested. If `needle[i] == needle[border]`, extend the border and record its new length. On a mismatch with a nonzero border, replace it by `lps[border - 1]` and test the same `needle[i]` again. If the border is zero, leave the current LPS entry at zero and advance `i`.

The fallback follows borders of borders. Those are exactly the shorter prefixes that could also be suffixes; restarting at every intermediate length would repeat comparisons and lose the linear bound.

**Scan the haystack without ever rewinding it**

Maintain `matched`, the number of leading needle characters matching the current haystack suffix. On a mismatch with `matched > 0`, fall back to `lps[matched - 1]` and compare the same haystack character again. Only when `matched == 0` may the scan advance past a mismatch. On a match, increase `matched`; the `for` loop then advances `i` to the next haystack character.

When `matched` reaches the needle length at position `i`, the complete occurrence ends there, so the candidate returns `i - len(needle) + 1`.

**What remains true after every fallback**

Before each haystack comparison, `needle[:matched]` equals the length-`matched` suffix of the processed haystack prefix. If the next characters mismatch, any surviving candidate must be both a suffix of those matched text characters and a prefix of `needle`. The LPS fallback selects the longest such candidate. It therefore discards no possible occurrence while avoiding a backward move in the haystack.

**Trace overlapping partial matches**

For haystack `mississippi` and needle `issip`, the attempt beginning at index 1 matches `issi` and then mismatches. The LPS data finds the longest pattern prefix that is also a suffix of the matched portion, so scanning continues without moving the haystack index backward. The next viable alignment completes at indices `4..8`, and the algorithm returns `4`.

A pattern such as `ababaca` makes the reuse more visible: after matching `ababa`, a mismatch can retain the border `aba` rather than rechecking those three characters from the text.

**Failure links preserve every viable alignment**

On mismatch, the LPS fallback keeps the longest proper pattern prefix already known to equal the current text suffix. The just-tested longer alignment is impossible, and an alignment not corresponding to a border cannot end at the same text position, so no viable candidate is skipped.

The haystack index never moves backward; only the amount of matched pattern is shortened. When the pattern first becomes complete, all earlier text endpoints have already been processed without a complete match. Its computed start is therefore the smallest valid occurrence index.

## Complexity detail
Let `n = len(haystack)` and `m = len(needle)`. During LPS construction, `i` advances through the pattern once; `border` can increase at most $m$ times in total, and every fallback decreases it, so this phase is $O(m)$. During matching, `i` advances through the haystack once; `matched` likewise has only linearly many increases and fallback decreases, so this phase is $O(n)$. Combined time is $O(n + m)$, and the LPS array uses $O(m)$ auxiliary space.

## Alternatives and edge cases
- **Try the pattern at every start:** simple but can repeat almost the entire pattern at many positions and require $O(nm)$ time.
- **Rolling hash:** offers expected linear matching and is useful for many patterns, but requires collision handling for deterministic correctness.
- **Built-in search:** often highly optimized, but hides the algorithm and its worst-case contract.
- If $m > n$, no complete occurrence is possible and the scan naturally returns `-1`; an early return is optional.
- The stated contract makes `needle` nonempty. In APIs where an empty needle is allowed, the conventional first-occurrence result is index `0` and should be handled before building LPS.
- Overlapping occurrences are safe because LPS preserves reusable suffixes; this problem returns immediately at the first complete one.
