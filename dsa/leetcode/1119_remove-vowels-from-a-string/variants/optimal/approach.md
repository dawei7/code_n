## General
**Use constant-time vowel membership:** Store the five vowels in a set. For each input character, test whether it belongs to that fixed set.

**Build only the retained subsequence:** Append a character to an output buffer exactly when it is not a vowel, then join the buffer once. Because the scan proceeds left to right, appended consonants preserve their source order automatically.

Every vowel is excluded by the membership condition, so none can appear in the result. Every consonant fails that condition and is appended once, so none is lost or duplicated. These two character classes cover the lowercase alphabet, proving the returned string is exactly the requested deletion result.

## Complexity detail
The scan visits each of the $n$ characters once and membership in a fixed five-element set is expected $O(1)$, giving $O(n)$ time. The output buffer and returned string can contain $n$ consonants, so output-related storage is $O(n)$; the vowel set itself is constant size.

## Alternatives and edge cases
- **Generator expression plus `join`:** It expresses the same one-pass filter compactly and has the same bounds.
- **Five whole-string replacements:** It is still linear up to a fixed factor of five, but repeatedly allocates intermediate strings.
- **Remove one vowel occurrence at a time:** Repeated searching and copying can require $O(n^2)$ time for an all-vowel input.
- **Repeated string concatenation:** Depending on the language, immutable-string growth can copy the accumulated prefix and become quadratic; use a buffer.
- **All vowels:** No character is appended, so joining the empty buffer returns `""`.
- **No vowels:** Every character is retained in its original order.
- **Repeated vowels:** Each occurrence is tested and removed independently.
- **Letter `y`:** It is not one of the five vowels specified by this contract and must remain.
