## General

**Separate reading from writing**

The input is already arranged into consecutive character groups. The solution uses:

- `i` as the first unread index of the current group;
- `j` to scan for that group's exclusive end; and
- `k` as the next output position in the same array.

At all times, `chars[0:k]` is the completed compressed prefix, while `chars[i:n]` contains groups not yet processed.

The algorithm does not need a second output array. It overwrites positions at or before the read frontier because a group's compressed representation is never longer than that group.

**Find one maximal run**

For current `i`, set `j = i + 1` and advance while `j < n` and `chars[j] == chars[i]`. When the loop stops, the group occupies indices `i` through `j-1`, and its length is `j - i`.

Stopping on the first different character makes each group maximal. The next outer iteration begins with `i = j`, so no character is skipped or included in two groups.

**Write the character and optional count**

Every group contributes its character once:

`chars[k] = chars[i]`, followed by `k += 1`.

If the group length is one, nothing else is written. This follows the required format: a singleton `a` stays `a`, not `a1`.

For length greater than one, `cnt = str(j - i)` creates the decimal count. The loop writes each digit separately. This matters for lengths at least ten: a run of 12 `b` characters contributes `'b'`, `'1'`, and `'2'`, not one multi-character array element.

Finally `i = j` advances to the next group.

**Why in-place writes cannot destroy unread input**

Before a group is processed, the write pointer satisfies `k <= i`. For a singleton, the representation length is one, equal to the group length. For a group of length $g\ge2$, the representation uses one character plus the number of decimal digits in $g$. This is never greater than $g$; for example, 2 uses `x2` of length two, and larger groups leave even more slack.

Therefore, after writing a group, the new `k` is at most `j`, the first index after the consumed group. Writes never extend into `chars[j:n]`, so no unread character is overwritten. This inductively preserves `k <= i` for the next group.

This safety property is the central reason left-to-right in-place compression works.

**Example trace**

For `['a','a','b','b','c','c','c']`, the first run has `i=0`, `j=2`, and length 2. The code writes `a2` into positions 0 and 1, leaving `k=2`. The `b` run writes `b2` at positions 2 and 3. The final `c` run writes `c3` at positions 4 and 5. The method returns `k=6`; anything at index 6 or later is irrelevant.

For twelve `b` characters after a singleton `a`, `str(12)` yields two digits and the meaningful prefix becomes `a`, `b`, `1`, `2`, of length four.

**Why returning `k` is sufficient**

The method need not shrink the Python list. The contract defines only `chars[0:k]` as meaningful after compression. `k` always points one past the last written compressed character, so it is exactly the new length.


Before each iteration, `chars[0:k]` is the correct compression of the original groups before `i`, and unread original data from `i` onward remains available. The inner scan identifies the next complete group, the writes emit exactly its specified representation, and the no-overwrite argument preserves future input. Advancing to `j` reestablishes the invariant.

When `i == n`, every original group has been encoded once. Thus the prefix and returned length are correct.

## Complexity detail

Let $n$ be the original array length. `j` moves forward over each input character exactly once across groups. The number of output writes is at most $n$. Total time is $O(n)$.

The algorithm stores a constant number of indices and current values. Under the fixed constraint $n\le2000$, the decimal count string has at most four characters, so auxiliary space is $O(1)$ as reported. In a generalized unbounded model, materializing `str(group_length)` uses $O(\log n)$ temporary characters; digits could instead be written with constant-word arithmetic assumptions.

The result reuses `chars`; no separate output array is allocated.

## Alternatives and edge cases

- **Build a separate compressed list:** It simplifies writing but violates the constant-extra-space requirement.
- **Use repeated string concatenation:** Besides not updating `chars` directly, immutable concatenation can copy growing results repeatedly.
- **Write `1` for singletons:** This violates the required format and increases the result unnecessarily.
- **Write a multi-digit count as one list item:** Each position must contain one character, so count digits must be emitted separately.
- **One input character:** The character is written to position zero and length one is returned.
- **All characters distinct:** Every group is a singleton, `k == n`, and the visible array remains unchanged.
- **One long group:** Output is the character followed by every decimal digit of `n`.
- **Group length ten or more:** `str(...)` naturally preserves digit order, such as `12` becoming `'1','2'`.
- **Symbols and digit characters:** Grouping compares character equality only; an input digit used as data is distinct from count digits by position/context, as allowed by the compression format.
- **Trailing stale cells:** They are intentionally ignored beyond returned `k` and need not be erased.
