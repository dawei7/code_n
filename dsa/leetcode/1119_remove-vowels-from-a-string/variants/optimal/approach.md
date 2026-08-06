## General
**Use constant-time vowel membership:** Store the five vowels in a set. For each input character, test whether it belongs to that fixed set.

**Stream only the retained subsequence into `join`:** The generator yields a character exactly when it is not a vowel, and `join` assembles those yielded characters into the result. Because the generator scans left to right, the retained consonants preserve their source order automatically.

Every vowel is excluded by the membership condition, so none can appear in the result. Every consonant fails that condition and is yielded once, so none is lost or duplicated. These two character classes cover the lowercase alphabet, proving the returned string is exactly the requested deletion result.

## Complexity detail
The scan visits each of the $n$ characters once and membership in a fixed five-element set is expected $O(1)$, giving $O(n)$ time. `join` constructs a returned string that can contain $n$ consonants, so output-related storage is $O(n)$; the generator state and vowel set are constant size.

## Alternatives and edge cases
- **Explicit list buffer plus `join`:** Appending retained characters to a list makes the intermediate sequence inspectable and has the same asymptotic bounds, but stores a separate list of character references before constructing the result.
- **Five whole-string replacements:** It is still linear up to a fixed factor of five, but repeatedly allocates intermediate strings.
- **Remove one vowel occurrence at a time:** Repeated searching and copying can require $O(n^2)$ time for an all-vowel input.
- **Repeated string concatenation:** Depending on the language, immutable-string growth can copy the accumulated prefix and become quadratic; use a buffer.
- **All vowels:** No character is appended, so joining the empty buffer returns `""`.
- **No vowels:** Every character is retained in its original order.
- **Repeated vowels:** Each occurrence is tested and removed independently.
- **Letter `y`:** It is not one of the five vowels specified by this contract and must remain.
