## General

**Exactly one edit is different from at most one**

The method must reject both strings that need two or more changes and strings
that are already equal. An edit is one insertion, one deletion, or one
replacement with a different character. Performing zero edits does not satisfy
the contract.

String lengths immediately restrict the possibilities. A replacement preserves
length. An insertion or deletion changes length by exactly one. Therefore, if
the lengths differ by more than one, the answer is false without examining any
characters.

The selected solution first ensures that `s` is the longer string, or that both
have equal length. If `len(s) < len(t)`, it calls the same method with the
arguments reversed. This is safe because “one edit apart” is symmetric:
inserting into one direction is deleting in the other, and replacement works
both ways. At most one such swap occurs.

**Find the first position where the strings disagree**

After normalization, let `m = len(s)` and `n = len(t)`, with $m \ge n$ and
$m-n \le 1$. The loop enumerates every character of the shorter string `t` and
compares it with `s` at the same index.

Before the first mismatch at index `i`, the prefixes `s[:i]` and `t[:i]` are
identical. Any single permitted edit must therefore explain the mismatch and
leave everything afterward aligned. There is no benefit to editing an earlier
matching position, because that would introduce a difference rather than fix
one.

Once the first mismatch is found, the length relationship uniquely determines
which operation remains possible.

**Equal lengths require one replacement**

If $m=n$, insertion and deletion would make the final lengths unequal. The only
possible edit is replacing `s[i]` with `t[i]`. Because the characters differ,
that replacement is a real edit rather than replacing a character by itself.

After spending the one allowed edit at `i`, every later character must already
match in the same position. The source tests
`s[i + 1:] == t[i + 1:]`. If the suffixes are equal, exactly one replacement
converts the strings. If they differ anywhere, at least a second edit would be
needed.

**A one-character length gap requires one deletion**

After normalization, the only unequal-length case is $m=n+1$. The longer
string `s` must delete exactly one character.

At a first mismatch at `i`, the natural candidate is `s[i]`. After deleting
it, `s[i + 1]` must align with `t[i]`, and all remaining characters must match
under that one-position shift. The comparison
`s[i + 1:] == t[i:]` verifies the complete remainder.

Viewed in the original argument order, the same event may be an insertion into
the shorter input. Normalization lets the code reason about only deletion from
the longer representation.

**Handle the no-mismatch prefix carefully**

The loop may finish without finding any disagreement among all `n` positions.
If $m=n$, the strings are identical. They are zero edits apart, so the source
returns false.

If $m=n+1$, every character of `t` matches the prefix of `s`, and the only
unmatched character is `s[-1]`. Deleting that final character is exactly one
edit, so the result is true. The expression `m == n + 1` distinguishes these
outcomes.

This also handles empty strings. `""` versus `""` skips the loop and returns
false. `"a"` versus `""` skips the loop and returns true because deleting
`"a"` is one edit.

**Trace representative cases**

For `"ab"` and `"acb"`, normalization swaps them, so the longer string is
`"acb"`. Index zero matches. At index one, `c` differs from `b`; deleting `c`
leaves suffix `"b"`, equal to the shorter suffix beginning at one. The answer
is true.

For `"cab"` and `"cad"`, lengths match and the first mismatch is at the final
index. Both suffixes after it are empty, so one replacement suffices.

For `"ab"` and `"cd"`, equal lengths mismatch at zero, but the remaining
suffixes `"b"` and `"d"` differ. One replacement cannot repair both positions,
so the answer is false.

**Why the first mismatch test is complete**

There are only three possible length differences. A gap greater than one is
impossible. Equal lengths force a replacement at the first mismatch. A gap of
one forces deletion of the longer string's first unmatched character. After
that forced edit, exact suffix equality is both necessary and sufficient.

If no mismatch appears, the length gap alone tells whether the one edit is the
extra final character or no edit at all. These exhaustive cases prove the
returned Boolean.

## Complexity detail

Let $m$ and $n$ be the input lengths. The common-prefix scan and at most one
suffix comparison inspect $O(m+n)$ total characters, so time is $O(m+n)$.
The one recursive normalization call does not grow with input length.

However, Python slicing creates new string objects. The expressions after a
mismatch can copy linear-size suffixes, so the exact selected source uses
$O(m+n)$ auxiliary space in the worst case, not the manifest's $O(1)$.
An index-based suffix comparison would realize constant auxiliary space.

## Alternatives and edge cases

- **Two-index scan without slicing:** Advance through the common prefix, skip one position according to the length gap, and compare the remainder. It preserves $O(m+n)$ time and achieves $O(1)$ space.
- **Full edit-distance dynamic programming:** Solves a much more general problem in $O(mn)$ time and space, which is unnecessary when only distance exactly one matters.
- **Count mismatches only:** Works for equal-length replacement, but fails for insertion/deletion because later positions are shifted.
- **Equal strings:** Must return false because the requirement is exactly one edit.
- **Length difference above one:** No single allowed operation can bridge it.
- **Mismatch at index zero:** The same suffix rules work without a special case.
- **Extra character at the end:** No mismatch occurs in the shorter prefix; the length check returns true.
- **Both strings empty:** They are zero edits apart and correctly return false.
- **Argument swap:** It occurs at most once and converts insertion reasoning into deletion reasoning.
- **Python slices:** They are a material space cost even though they make the suffix condition concise.
