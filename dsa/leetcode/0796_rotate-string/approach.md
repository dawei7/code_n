## General

**Describe a rotation as choosing a cut**

After some number of left shifts, a prefix of `s` moves to the end while the remaining suffix moves to the front.

If:

$$
s = P + Q,
$$

where `P` is the shifted prefix and `Q` is the remaining suffix, the resulting rotation is:

$$
Q + P.
$$

Trying every cut and constructing every `Q + P` would work, but it repeats much of the same string data. Concatenating `s` with itself exposes every cut result inside one doubled string.

**Why doubling contains every rotation**

Write the doubled string as:

$$
s+s=P+Q+P+Q.
$$

The length-`n` substring beginning immediately after prefix `P` is `Q + P`, exactly the rotation produced by moving `P` to the end.

As the cut moves from before index zero through before index `n - 1`, the corresponding length-`n` windows in `s + s` are all possible rotations.

For example, if `s = "abcde"`, then:

`s + s = "abcdeabcde"`.

The rotation `"cdeab"` begins at index two of the doubled string.

**Why every relevant doubled substring is a rotation**

The implication also works in reverse. Let a length-`n` match begin at index `r` within `s+s`, where `0 <= r < n`. Its characters are:

`s[r:] + s[:r]`,

which is the result of `r` left shifts.

A length-`n` pattern can also begin at index `n`, but that window is simply the second copy of `s`, identical to the zero-shift rotation. There is no other possible starting index because a length-`n` match must fit inside the length-`2n` doubled text.

Thus, among equal-length strings, substring membership in `s+s` is equivalent to being a rotation.

**Check lengths before substring membership**

A shift only rearranges characters. It never changes the number of characters, so unequal lengths must return false.

The expression begins with:

`len(s) == len(goal)`.

Python's `and` short-circuits. If lengths differ, it does not create `s+s` or run a substring search.

This check is also logically necessary for the doubled-string characterization. A shorter string might occur inside `s+s` without being a full rotation, and a longer match is impossible for unrelated reasons. Requiring equal length makes every successful occurrence represent one complete cyclic arrangement.

**Delegate the search to string membership**

When lengths match, the expression:

`goal in s + s`

asks whether `goal` occurs as a contiguous substring of the doubled string. It does not manually simulate shifts or allocate a list of rotations.

The concatenated text is temporary, and the membership operator returns one Boolean. The exact starting index is unnecessary because the task asks only whether some rotation exists.

**Trace a successful example**

For `s = "abcde"` and `goal = "cdeab"`, lengths are both five.

The doubled text is `"abcdeabcde"`. The goal appears from indices two through six. Cutting `s` after prefix `"ab"` gives suffix `"cde"` followed by that prefix, so two left shifts produce the goal.

The method returns true.

**Trace a failed arrangement**

For `goal = "abced"`, the character counts happen to match, but the cyclic order does not. No cut of `"abcde"` produces `"abced"`, and that string is not a length-five substring of `"abcdeabcde"`.

The method returns false. This shows why comparing character frequencies alone is insufficient: rotation preserves circular relative order, not just the multiset.

**Repeated characters do not break the argument**

If `s` contains repeated characters, several cuts may yield the same rotation or `goal` may occur at several doubled positions. Membership needs only one occurrence.

The cut-and-window proof depends on positions, not character uniqueness, so duplicates require no special handling.

**Zero shifts are included**

When `goal == s`, it appears at position zero of `s+s`. The problem allows “some number” of shifts, which includes zero, so returning true is correct.

Even if one interpreted the process as requiring positive shifts, shifting a length-`n` string exactly `n` times returns to the original, so the same answer would still hold for nonempty strings.

**Why the result is correct**

If the method returns true, lengths are equal and `goal` is a length-`n` substring of `s+s`. The converse-window argument identifies a cut of `s` whose suffix-plus-prefix form equals `goal`, so legal left shifts produce it.

If `goal` is a rotation, some cut writes it as `Q+P` while `s=P+Q`. The doubled string contains `P+Q+P+Q` and therefore contains `Q+P`, so membership returns true. Unequal lengths cannot be rotations. Both directions establish the equivalence.

## Complexity detail

Let $n$ be the common length after the initial check. Creating `s+s` writes $2n$ characters, taking $O(n)$ time and $O(n)$ temporary space.

The exact source delegates substring matching to Python's string-membership implementation. The manifest's $O(n)$ time bound assumes a linear-time substring search, such as a Two-Way or KMP-style runtime implementation, over a text of length `2n` and a pattern of length `n`. Under that assumption, total time is $O(n)$ and auxiliary/materialized concatenation space is $O(n)$.

The one-line source does not implement its own KMP table. If evaluated under a model where built-in membership uses naive restart-at-each-position matching, the conservative worst case would be $O(n^2)$. Thus the linear bound depends on the search guarantee supplied by the runtime, while the rotation reduction itself is linear and correct independently of that choice.

## Alternatives and edge cases

- **Explicit KMP search:** Search `goal` in `s+s` with a longest-prefix-suffix table, guaranteeing $O(n)$ time and using $O(n)$ table space without relying on library search behavior.

- **Two-Way string matching:** It can provide linear worst-case search with constant auxiliary matching state, though implementation is more involved.

- **Simulate every shift:** Construct and compare up to `n` rotations, costing $O(n^2)$ time for immutable strings.

- **Compare sorted characters:** It checks only anagrams and accepts strings whose circular order is wrong.

- **Unequal lengths:** Return false before building the doubled string.

- **Identical strings:** The zero-shift rotation appears immediately.

- **Repeated characters:** Multiple matching cuts are harmless; one is sufficient.

- **Single character:** The only equal-length rotation is the character itself.

- **Occurrence at index `n`:** It is the second copy of `s` and represents the same arrangement as zero shifts.
