## General

Convert `n`, `2 * n`, and `3 * n` to decimal text and concatenate them. A valid result must have exactly nine characters: without this length check, a longer sequence could contain all digits from `1` through `9` while also repeating one of them.

Next compare the set of characters in the sequence with the set `{"1", ..., "9"}`. Equality rules out `0` and any other character, while also requiring every nonzero digit to appear. Together with the nine-character length, set equality forces each required digit to occur exactly once. Therefore the two checks are both necessary and sufficient for the definition of fascinating.

## Complexity detail

Because $100 \le n \le 999$, the three decimal representations contain at most $3+4+4=11$ characters. Construction, set creation, and comparison therefore take $O(1)$ time and $O(1)$ auxiliary space over the complete legal input domain. This fixed workload bound is recorded in the bounded-domain certificate.

## Alternatives and edge cases

- **Sort the characters:** Comparing the sorted sequence with `"123456789"` is correct but performs more machinery than a fixed-size membership check.
- **Digit-frequency array:** Counting ten decimal digits is equally valid and makes the exact-once rule explicit, but requires a longer loop and cleanup logic.
- **Arithmetic digit extraction:** Repeated division avoids string conversion, although concatenation and length bookkeeping become less direct.
- Set equality without the nine-character check can accept a longer sequence that repeats digits.
- Any zero immediately makes the number non-fascinating because zero is absent from the required set.
- When `2 * n` or `3 * n` has four digits, the combined sequence is longer than nine characters and must fail.
