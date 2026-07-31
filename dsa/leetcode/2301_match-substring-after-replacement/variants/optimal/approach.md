## General

**Represent exactly the allowed one-step relation**

Insert every directed `(old, new)` mapping into a hash set. Pattern character
$a$ can match text character $b$ exactly when $a=b$ or `(a, b)` is in that
set. This test neither reverses mappings nor follows transitive chains.

**Test each contiguous alignment**

Slide a length-$P$ window across `s`. At an alignment, compare every
`sub` position with the corresponding text character using the relation above.
Abandon the alignment at its first invalid pair. If every position matches,
return `true`; if all alignments fail, return `false`.

Every possible substring position is examined. Within one position, the
per-character rule is exactly equivalent to leaving that occurrence unchanged
or applying one listed mapping once. Thus a fully accepted alignment constructs
a legal transformed `sub`, while any legal transformed occurrence would pass
all comparisons at its alignment.

## Complexity detail

Let $S$, $P$, and $R$ denote the lengths of `s`, `sub`, and `mappings`.
Building the relation set takes $O(R)$ expected time and space. There are
$S-P+1$ alignments with up to $P$ constant-time checks each, giving
$O(SP+R)$ expected time and $O(R)$ auxiliary space.

## Alternatives and edge cases

- **Scan mappings for every character pair:** This is correct but can add a factor of $R$, taking $O(SPR)$ time.
- **Generate transformed strings:** Enumerating replacement choices grows exponentially with the pattern length.
- **Reverse a mapping:** `[a, b]` permits `a` to become `b`, never the reverse unless separately listed.
- **Chain mappings:** `[a, b]` and `[b, c]` do not allow one `a` occurrence to become `c`.
- **Repeated pattern character:** The same mapping may be applied independently to several occurrences.
- **No replacement:** Equal characters always match even when no identity mapping is present.
- **Case sensitivity:** Uppercase and lowercase characters remain distinct.
- **Later alignment:** A failed prefix window does not rule out a match beginning farther right.
