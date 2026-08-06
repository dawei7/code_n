## General

**Normalize insertion and deletion into one direction**

A single edit can change the length by at most one, so reject a larger length difference immediately. If `s` is
longer, swap the strings. From then on, `s` is the shorter or equal-length string, and a length-changing edit is
always handled as inserting one character into `s`.

Walk `first` through `s` and `second` through `t`. Matching characters advance both pointers. At a mismatch,
increment `edits`; a second mismatch proves that more than one edit is required. For equal lengths, the only
possible edit is replacement, so advance both pointers. When `t` is longer, skip only `t[second]`, representing the
one insertion into `s`.

If the shared scan ends with one character still remaining in `t`, count that trailing insertion. The final check
requires `edits == 1`, which deliberately rejects equal strings that need zero edits.

Before each comparison, the consumed prefixes can be made equal using exactly `edits` operations. A mismatch forces
the only alignment change permitted by the length relationship, so either that one edit restores alignment or a
later mismatch correctly rejects the pair. Reaching the end with exactly one counted mismatch or trailing character
is therefore both necessary and sufficient.

## Complexity detail

The pointers advance monotonically and inspect each string position at most once, giving $O(m + n)$ time for lengths
$m$ and $n$. The two pointers and edit counter use $O(1)$ auxiliary space; the implementation does not create suffix
slices.

## Alternatives and edge cases

- **Full edit-distance dynamic programming:** solves a more general problem in $O(mn)$ time and unnecessary extra
  space.
- **Generate every one-edit result:** creates many temporary strings and repeats work across the alphabet.
- **Compare suffix slices after the first mismatch:** is logically valid, but copying slices can use linear auxiliary
  space in Python.
- Two empty strings are zero edits apart and return `False`.
- An empty string and a one-character string are exactly one insertion apart.
- Character comparison is case-sensitive, so `"a"` and `"A"` differ by one replacement.
- A sole trailing character is counted only after all aligned prefix characters match.
