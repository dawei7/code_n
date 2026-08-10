## General

**Store replacement permission in the forward direction**

Each mapping `[old,new]` permits one character of `sub` equal to `old` to become `new`. The dictionary of sets stores `new` inside `d[old]`.

Sets remove duplicate mapping pairs and provide expected constant-time membership checks. Direction is essential: permission from `o` to `0` does not imply permission from `0` to `o`.

**Test every possible alignment**

A matching result must occupy a contiguous substring of `s` with length `len(sub)`. If `S=len(s)` and `P=len(sub)`, its start can be zero through `S-P`.

`range(len(s)-len(sub)+1)` enumerates exactly these alignments, including the final one ending at the last character.

For each start `i`, the slice `s[i:i+len(sub)]` extracts the candidate text.

**Compare aligned characters**

`zip(candidate, sub)` yields `a` from `s` and `b` from `sub` at the same relative position.

That position is compatible when either `a==b`, requiring no replacement, or `a in d[b]`, meaning the original sub character `b` may be replaced directly by target character `a`.

The orientation `a in d[b]` matches old-to-new semantics. Reversing the lookup would incorrectly permit mappings backward.

**Why replacement chains are not followed**

Each sub character can be replaced at most once. If mappings contain `a\to b` and `b\to c`, an original `a` cannot become `c` through two operations.

The set stores only direct pairs and the condition performs one lookup, correctly excluding transitive chaining.

**Require every position in an alignment**

`all(...)` returns true only when every aligned pair is compatible. It short-circuits at the first mismatch, avoiding unnecessary checks within that window.

If an alignment passes, each mismatching position has its own permitted direct replacement. Replacements apply independently to character occurrences, so using the same mapping at several positions is allowed.

The method immediately returns true on the first successful alignment.

**Case and character categories remain exact**

Strings may contain uppercase letters, lowercase letters, and digits. Dictionary keys and equality are case-sensitive, so `A` and `a` remain distinct.

No normalization or numeric conversion occurs. Each character is treated as the exact symbol supplied.

**Trace the directed example**

With mapping `o\to0`, an original `o` in `sub` can match a `0` in `s`. But if `sub` contains `0` and `s` contains `o`, `o in d['0']` is false unless the reverse mapping was explicitly supplied.

This is why `"f00l"` cannot be turned into `"fool"` using only `o\to0`.

**Why the exhaustive alignment scan is correct**

Every possible substring occurrence has one enumerated start. For a fixed start, the per-position predicate is true exactly when the original character can remain or undergo one allowed replacement to equal the target text character.

If `all` succeeds, performing those replacements makes `sub` equal that substring. If a solution exists, its alignment and direct per-position operations cause the corresponding `all` to succeed. The method therefore returns true exactly when required.

## Complexity detail

Let `S=len(s)`, `P=len(sub)`, and `R` be the number of mappings. Building sets takes expected `O(R)` time and `O(R)` space.

There are `S-P+1` alignments. The exact source creates a length-`P` slice and may check `P` pairs for each, so worst-case time is `O((S-P+1)P+R)`, commonly written `O(SP+R)`.

Each slice uses `O(P)` temporary space, while the persistent mapping structure uses `O(R)`. Peak auxiliary space is `O(R+P)`.

## Alternatives and edge cases

- **Avoid window slicing:** Compare `s[i+j]` directly to reduce temporary space while keeping the same time bound.
- **Boolean character matrix:** The fixed alphanumeric alphabet permits constant-size direct lookup instead of sets.
- **Transitive closure:** It would incorrectly allow more than one replacement per character.
- **Regular expressions:** Per-character directed mappings are possible to encode but less transparent.
- **No mappings:** Only exact substring matches pass.
- **Exact character:** Equality succeeds without consulting mappings.
- **Repeated use of one mapping:** Different positions may each apply the same allowed replacement.
- **Reverse-only mapping:** It does not authorize the forward comparison.
- **Equal string lengths:** There is exactly one alignment.
- **Final alignment:** The `+1` in the range includes it.
- **Case sensitivity:** Uppercase and lowercase are distinct.
- **Early mismatch:** `all` short-circuits safely.
- **Input preservation:** No input string or mapping row is modified.
- **Bare direct replacement:** A mapping may be used even when the same old character appears several times; the “once” restriction is per character occurrence, not per mapping rule.
- **Unused mappings:** Rules unrelated to characters in `sub` simply remain in the dictionary and never affect a comparison.
- **Duplicate mapping rows:** Set insertion collapses them without changing permission.
- **Digit characters:** They are ordinary mapping keys and values, not converted to numbers.
- **Substring contiguity:** Testing fixed-length slices prevents a subsequence-style match with gaps.
- **Short-circuit success:** The first passing alignment proves existence, so later starts need not be tested.
- **Mismatching lengths:** Every candidate slice has exactly `len(sub)` characters, making `zip` cover all required positions.
- **Default dictionary access:** Looking up an unmapped old character creates an empty set in this `defaultdict`, which makes the membership test false.
