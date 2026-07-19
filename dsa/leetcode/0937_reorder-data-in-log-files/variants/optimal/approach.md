## General
**Split identifier from content once.** For each log, call the first-space split so the identifier and untouched remainder are available. The first character of the content determines its type because every content is guaranteed to contain either only letter words or only digit words.

**Separate the two ordering rules.** Append digit-logs directly to a dedicated list in encounter order; never sort that list. For a letter-log, store a key containing `(content, identifier)` together with the original string. Sorting these records uses the entire content first and the identifier only as the specified tie-breaker.

**Concatenate after sorting letters.** Extract the original strings from the sorted letter records and append the stable digit list. Classification is exhaustive, the tuple key exactly matches the required lexicographic rules, and preserving digit insertion order proves their relative order is unchanged.

## Complexity detail
Parsing and storing all text takes $O(S)$ time. Sorting $L$ letter keys performs $O(L\log L)$ comparisons, each potentially examining $O(C)$ characters, so total time is $O(S + LC\log L)$. Parsed keys and the result retain $O(S)$ characters.

## Alternatives and edge cases
- **Single mixed sort key:** Give letter-logs a key beginning with `0` and digit-logs a key beginning with `1` plus their original index. This is correct but unnecessarily sorts digit-logs too.
- **Insertion sort for letters:** It preserves the rules but can require $O(L^2C)$ time on reverse-ordered input.
- **Equal letter content:** Compare identifiers lexicographically; input order is not the tie-breaker.
- **Digit identifiers:** Only content determines the log type; an identifier may contain letters or digits.
- **All digit-logs:** Return the input order unchanged.
