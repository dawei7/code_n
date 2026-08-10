## General

**Search contiguous ranges with a sliding window**

A substring must occupy consecutive positions, so the solution represents one
candidate as the inclusive interval from `j` to `i`. The `for` loop advances
`i` from left to right, adding one new character at a time. The left boundary
`j` moves only when the new character makes the window invalid.

`cnt` maps each character currently present in the window to its frequency.
Keeping frequencies, rather than only a set, is necessary because removing one
copy from the left does not necessarily remove that character from the window.
A key is deleted only when its count becomes zero. Consequently,
`len(cnt)` is exactly the number of distinct characters in `s[j:i + 1]`.

The current window is allowed to contain one or two distinct characters.
Because the input is nonempty, even a single-character substring is valid, so
the result can begin at zero and be updated normally.

**Add the right endpoint, then repair validity**

For each pair `(i, c)`, the source increments `cnt[c]`. Before that addition,
the previous iteration ended with at most two keys. Therefore the new window
has at most three distinct characters; only one new type can have arrived.

While `len(cnt) > 2`, the algorithm removes `s[j]` from the left. It decrements
that character's frequency. If the result is zero, no occurrence remains in
the window, so the key is removed from the counter. Then `j` advances.

The loop may discard several characters of a repeated run before a key
vanishes. For example, if the invalid window begins with `"eee"`, removing
only its first `e` does not reduce the distinct count. Shrinking must continue
until all occurrences of one of the three types have left.

When the loop stops, the window again has at most two distinct characters.
Its inclusive length is `i - j + 1`, which is compared with `ans`.

**Why the smallest valid left boundary is best**

For a fixed right endpoint `i`, any substring beginning to the right of `j`
is shorter. The shrinking loop stops immediately when validity is restored, so
`j` is the earliest start that remains valid after adding `s[i]`.

This means `s[j:i + 1]` is the longest valid substring ending at `i`. Taking
the maximum over every right endpoint therefore considers a representative
that is at least as long as every valid substring in the string.

There is no reason to move `j` left again. Any character excluded earlier was
removed because a window ending at some earlier or current position had too
many distinct types. Future right endpoints cannot make that older, larger
window valid; they only add characters. This monotonicity is what makes the
method linear rather than restarting a scan at every index.

**Trace `"eceba"`**

At `i = 0`, the window is `"e"` and `ans` becomes one. Adding `c` produces
`"ec"`, still valid, so the answer becomes two. Adding the next `e` produces
`"ece"` with counts `e:2` and `c:1`; the answer becomes three.

Adding `b` creates three keys. Shrinking removes the leading `e`, but one `e`
remains, so the window is still invalid. Removing `c` drops its count to zero,
deletes that key, and advances `j` to two. The repaired window is `"eb"`.

Finally, adding `a` creates `"eba"` with three types. Removing the remaining
`e` restores validity, leaving `"ba"`. No later window exceeds the earlier
length three, so the result is three.

For `"ccaabbb"`, the window first contains only `c` and `a`. When `b` arrives,
both leading `c` values must leave before that key disappears. The resulting
window `"aab"` can then expand through all remaining `b` values to `"aabbb"`,
whose length is five.

**Establish the invariant and result**

After the shrinking loop of every iteration:

- the counter contains exactly the positive frequencies of the current window;
- it has at most two keys;
- `j` is the smallest start that makes the current right endpoint valid;
- `ans` is the largest valid window length seen through index `i`.

Incrementing the new character maintains accurate counts. The removal loop
restores the distinct limit without skipping the first valid start. Updating
the maximum then extends the final claim. At the last index, every possible
right endpoint has been processed, so `ans` is globally optimal.

**Exact-source import**

The selected source calls `Counter()` but does not import it. A standalone
Python module needs `from collections import Counter`; otherwise the method
raises `NameError` when called. The counting-window algorithm is sound once
the standard-library dependency is present.

## Complexity detail

Let $n$ be the string length. The right pointer visits every index once. The
left pointer also advances at most $n$ times across the complete execution;
although it appears inside a nested loop, it never resets. Counter operations
are expected $O(1)$, so total time is $O(n)$.

The counter has at most three keys transiently and at most two after repair.
Under the stated English-letter alphabet, this is constant auxiliary storage,
so space is $O(1)$. More generally, a version for at most $k$ distinct
characters would use $O(k)$ map entries.

These bounds match the manifest, subject to the missing import required for
the source to execute.

## Alternatives and edge cases

- **Last-occurrence map:** Store the rightmost index of each active character; when a third appears, remove the character with the smallest last index and jump the left boundary past it.
- **Fixed frequency array:** English letters can be counted in an array indexed by character code, avoiding hash-map overhead at the cost of tying the implementation to a known alphabet.
- **Brute-force starts:** Expanding from every position can take $O(n^2)$ time because the same characters are revisited.
- **One-character string:** The single window is valid and produces one.
- **One distinct character:** The left boundary never moves, so the entire string is returned.
- **Exactly two types:** The complete string is valid regardless of how often the characters alternate.
- **Third type after long duplicates:** Shrinking continues until an entire old character count reaches zero, not merely for one step.
- **Substring versus subsequence:** Characters cannot be skipped; the window always represents a contiguous slice.
- **English-letter guarantee:** It keeps the possible alphabet finite and validates the stated constant-space interpretation.
- **Missing `Counter` import:** Add the standard-library import in a standalone environment before relying on the selected source.
