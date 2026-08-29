## General

**The key's first distinct letters define a decoding dictionary**

The cipher table is determined by the order in which distinct lowercase letters first appear in `key`. The first distinct key letter maps to plain `a`, the second maps to `b`, and so on through the twenty-sixth mapping to `z`.

The solution stores these substitutions in dictionary `d`. It begins with `{" ": " "}` because spaces must survive unchanged. Preloading the space also ensures that spaces encountered while scanning `key` do not consume a position in the alphabet.

The integer `i` counts how many distinct lowercase key letters have been mapped. It starts at zero, so the first new letter maps to `ascii_lowercase[0]`, which is `a`.

**Ignore every repeated appearance after the first**

The loop visits key characters from left to right. For each character `c`, it checks `if c not in d`. If `c` is a new lowercase letter, the method assigns

`d[c] = ascii_lowercase[i]`

and increments `i`. If it is a repeated letter, its existing mapping remains unchanged and `i` does not move.

This precisely implements “use the first appearance.” Once a key character has been assigned its alphabet position, later copies cannot overwrite it.

For a partial key beginning `"happy boy"`, the first new characters are `h`, `a`, `p`, `y`, `b`, and `o`. They receive `a`, `b`, `c`, `d`, `e`, and `f`. The second `p` and the spaces are already in `d` and are skipped.

The source guarantees that every lowercase English letter appears in the key at least once. At the end of the scan, `d` therefore contains mappings for all 26 letters plus space, and `i` has advanced exactly 26 times.

**Translate the message in its original order**

The return expression

`"".join(d[c] for c in message)`

looks up each message character and yields its decoded replacement. `join` concatenates those replacements in the same order, producing the final plaintext string.

A lowercase cipher character uses the mapping established by its first key appearance. A space uses the preinstalled mapping to another space. The message constraints guarantee no other character type, so every lookup succeeds.

Repeated message letters are translated repeatedly to the same plaintext letter because the dictionary is fixed after key processing. The procedure is substitution, not stateful decoding; one message character never changes the meaning of a later one.

**Why the mapping is a complete one-to-one substitution**

Every new key letter receives the next unused plaintext alphabet character. Because the key eventually introduces 26 distinct lowercase letters and the plaintext sequence also has 26 distinct positions, no two cipher letters receive the same plaintext letter and no plaintext letter is omitted.

Suppose a cipher letter `c` first appears as the `r`-th distinct lowercase letter of `key`. When that position is scanned, exactly `r - 1` distinct letters have been mapped, so `i = r - 1` and `d[c]` becomes the `r`-th regular alphabet letter. The membership check prevents any later occurrence from changing that assignment.

Thus `d` exactly matches the substitution table specified by the key. Looking up every message character applies that table, while the explicit space mapping preserves separators. The joined string is therefore exactly the decoded message.

**The fixed alphabet makes dictionary storage constant-size**

Although the key may contain up to 2000 characters, it can add only 26 lowercase keys plus one space entry. Repetition affects scan time but not dictionary size. This is why the mapping is constant auxiliary space under the English-alphabet contract.

The exact source relies on `ascii_lowercase` being available in its Python environment, conventionally from the standard-library `string` definitions. It denotes `abcdefghijklmnopqrstuvwxyz` and supplies the plaintext ordering.

## Complexity detail

Let `k` be the key length and `m` the message length. The first loop examines each key character once, with expected constant-time dictionary membership and insertion. Decoding examines each message character once, and joining writes an output of length `m`. Total expected time is `O(k + m)`.

The dictionary contains at most 27 entries, so auxiliary mapping space is `O(1)` because the alphabet is fixed. The generator used by `join` does not build a separate list of all decoded characters.

The returned string itself has length `m` and necessarily occupies `O(m)` output space. Complexity conventions usually exclude required output storage; if it is included, total newly allocated memory is `O(m)`.

Python dictionary operations have expected constant time. With single-character keys from a tiny fixed domain, this assumption is especially benign. Neither input string is modified because Python strings are immutable.

## Alternatives and edge cases

- **A 26-entry array indexed by character code:** Record each cipher letter's plaintext character at `ord(c) - ord('a')`. This has the same asymptotic bounds but needs a separate branch for spaces and explicit index arithmetic.
- **Build an ordered distinct-key string first:** Remove spaces and duplicates, then zip with the alphabet. This can be readable but may create extra strings or sets; the one-pass dictionary builds the mapping directly.
- **Use the last appearance of each key letter:** Overwriting mappings would violate the first-appearance order and could assign several alphabet positions incorrectly.
- **Advance `i` for spaces:** Spaces are not one of the 26 substitution letters. Preloading them in `d` ensures they never consume an alphabet position.
- **Advance `i` for repeated letters:** Only newly discovered characters advance the substitution order. Repeats must be ignored.
- **Map plaintext to cipher instead of cipher to plaintext:** Decoding needs to look up each encrypted message character and retrieve its regular alphabet replacement. Reversing the dictionary would require another inversion step.
- **Key begins with spaces:** They are already mapped and skipped; the first lowercase letter still receives `a`.
- **Many repeated letters before a new one:** Repetition leaves both the existing mapping and `i` unchanged, preserving first-distinct order.
- **Message contains only spaces:** Every character maps to itself, so the returned string is identical.
- **Message repeats one cipher letter:** Each occurrence receives the same decoded character, as a substitution cipher requires.
- **All 26 letters guaranteed:** No message lowercase lookup can fail because every letter has a key mapping by the end of the first pass.
- **Missing-letter invalid input:** The contract excludes it. If a missing key letter appeared in the message, direct dictionary lookup would raise an error rather than invent a mapping.
- **Non-lowercase characters:** The source excludes them. The mapping covers only lowercase English letters and space.
- **Input preservation:** Both strings are read only, and the result is newly constructed.
- **Output length:** Substitution replaces each input character with exactly one character, so decoded length equals message length.
