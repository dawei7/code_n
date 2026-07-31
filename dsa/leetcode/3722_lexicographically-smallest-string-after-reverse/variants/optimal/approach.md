## General

There are exactly two operation families and $n$ choices of `k`. Enumerate every prefix reversal and every suffix reversal, constructing the resulting string and retaining the lexicographically smallest one seen.

Initialize the answer with `s`. This does not skip the required operation: reversing either end with `k = 1` is legal and produces `s` unchanged. The remaining loop can therefore begin at length two.

Every legal result belongs to one of the enumerated families for one chosen length, so the minimum considers the complete operation space. Conversely, every constructed candidate is the result of exactly one allowed operation. The smallest candidate is therefore the required string.

## Complexity detail

Let $n$ be `s.length`. There are $O(n)$ candidates, and slicing, reversing, concatenating, and comparing a candidate can each inspect $O(n)$ characters. Total time is $O(n^2)$. At any moment, candidate construction and the retained answer require $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Reverse an interior substring:** This is outside the contract; the reversed segment must be a prefix or suffix.
- **Treat the operation as optional:** Exactly one operation is required, but `k = 1` already represents the unchanged string legally.
- **Only inspect the first character:** Equal first characters may require comparing much later positions, so complete candidate comparison is necessary.
- **Single-character string:** The only legal reversal has `k = 1` and returns the input.
- **Whole-string reversal:** Choosing `k = n` is legal from either end and must be included.
- **Repeated characters:** Different choices can yield identical candidates; repeated comparison does not change correctness.
