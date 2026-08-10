## General

**Encode each nucleotide with three bits**

The primary competitive method avoids allocating a ten-character slice for
every position. It uses `ord(s[i]) & 7`, retaining the lowest three bits of the
character's ASCII code. For the only legal characters, the values are distinct:
`A` maps to 1, `C` to 3, `G` to 7, and `T` to 4.

Because each code fits in three bits and no two legal nucleotides share a code,
concatenating ten codes produces an exact 30-bit representation of a DNA
window. This is not a probabilistic hash for the valid alphabet: two different
length-10 strings cannot have the same 30-bit encoding.

**Roll the 10-character encoding forward**

For each input character, the expression shifts `rolling_hash` left by three
bits, making room for one new nucleotide code. The mask `0x3fffffff` keeps only
the low 30 bits because hexadecimal `0x3fffffff` is thirty 1-bits. Any code
older than the latest ten characters is discarded. Finally, bitwise OR inserts
the new three-bit code.

After at least ten characters have been processed, `rolling_hash` therefore
represents exactly the window ending at index `i`, whose start is `i - 9`.
Every update uses a constant number of integer bit operations.

**Understand the harmless prefix states**

The loop begins recording hashes immediately, even for prefixes of lengths one
through nine, although those are not valid answer windows. This looks
suspicious but is harmless for the stated alphabet. Every character code is
nonzero, so an encoding of length ten has a nonzero group in its highest three
bits and needs at least 28 significant bits. An encoding of at most nine
characters uses at most 27 bits. A short prefix therefore cannot equal any
valid ten-character encoding.

The short prefix encodings also have different effective lengths and nonzero
leading codes, so they do not repeat one another. They occupy a few unnecessary
dictionary entries but cannot trigger an answer.

**Use a three-state dictionary value**

The variable named `dict` maps each encoded window to a boolean. Its absence
means unseen. On first sight, the method stores `True`. Seeing a key whose value
is `True` proves a second occurrence, so it appends the exact substring
`s[i - 9 : i + 1]` and changes the value to `False`.

Later occurrences find the key but see `False`, so they are ignored. This
ensures one output copy per repeated DNA sequence. The name `dict` shadows
Python's built-in `dict` constructor inside the method; that is poor style but
does not break the current operations.

**Why extracting text only on repetition is useful**

The rolling integer is enough for detection, while the required result must
contain strings. The solution creates a ten-character slice only when a key is
seen for the second time. It does not slice every candidate window. For the
fixed length ten, both strategies are asymptotically linear, but this design
reduces repeated substring creation.

At index `i`, the half-open slice ending at `i + 1` starts at `i - 9`, so it
contains exactly ten characters. Prefix states never reach this branch under
valid input, avoiding negative-start slices.

**Trace repeated `A` characters**

Once the tenth `A` is processed, the hash represents `AAAAAAAAAA` and is stored
as `True`. The eleventh `A` produces the identical latest-ten-character hash.
The method appends `AAAAAAAAAA` and flips the flag to `False`. Each subsequent
`A` produces the same key, but the false flag prevents another append.

Overlapping windows are correctly treated as separate occurrences because the
rolling update advances by one character at a time.

**Why the primary method is exact**

Every appended string corresponds to a 30-bit key already seen once. Since the
three-bit mapping is injective for legal nucleotides and the key represents
exactly ten current characters, the earlier key represents the same substring.
Thus every output really repeats.

Conversely, equal length-10 substrings have identical character codes and hence
identical 30-bit keys. The first occurrence stores `True`; the second appends
the text. Therefore every repeated sequence appears, and the boolean state
prevents additional copies.

**The second method is not the selected entry point**

The class also defines `findRepeatedDnaSequences2`. LeetCode calls
`findRepeatedDnaSequences`, so this second method is an unused alternative. It
materializes every ten-character slice into list `l`, counts them with
`collections.Counter`, and returns keys whose count exceeds one. Variable `r`
is created but never used.

That alternate method is logically straightforward and also linear for fixed
window length, but it allocates all candidate slices. It does not affect the
behavior of the primary method unless called explicitly.

## Complexity detail

Let $n$ be the input length. The primary loop performs one constant-width shift,
mask, insertion, and expected dictionary lookup per character. It creates an
answer slice only once per repeated distinct sequence, and each slice has fixed
length ten. Expected time is therefore $O(n)$.

The dictionary can contain one key for each distinct window plus nine prefix
states, and the result can contain linearly many fixed-length strings. Auxiliary
space is $O(n)$. Python integers remain bounded to 30 bits after masking, so
their size does not grow with the input.

## Alternatives and edge cases

- **Two-bit encoding:** Since there are four symbols, 20 bits suffice for ten nucleotides and give a smaller exact key.
- **Counter of slices:** The secondary method is simpler but materializes every candidate substring.
- **Two hash sets:** Store seen encodings and repeated strings or encodings, avoiding a boolean state map.
- **Start after ten characters:** An explicit warm-up phase would avoid the nine harmless prefix entries and make the invariant easier to see.
- **String shorter than ten:** Only prefix keys are stored and no answer is appended; the result is empty.
- **Length exactly ten:** One valid key is seen once, so the result is empty.
- **Overlapping occurrences:** Rolling by one character detects them correctly.
- **Third and later occurrences:** The false dictionary flag prevents duplicate output.
- **Alphabet restriction:** The exactness proof depends on the four legal characters having distinct low three bits.
- **Shadowed built-in:** Rename `dict` to `state` or `seen` for clearer, safer Python style.
