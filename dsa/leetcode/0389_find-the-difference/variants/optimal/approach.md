## General
**Cancel matching character occurrences**

Initialize an integer accumulator to zero. XOR it with the code point of every character in `s` and every character in `t`. XOR is associative and commutative, so the shuffled order has no effect on the final value.

**Duplicates cancel by multiplicity**

Every occurrence contributed by `s` has one corresponding occurrence in `t`. Pairing equal code points makes each pair vanish because $x \oplus x = 0$. This remains true when a character appears many times: all matched occurrences can be paired independently.

**Why only the added character remains**

After all paired occurrences cancel, the accumulator is `0 ^ extra`, which equals the extra character's code point. Converting that code point back to a character therefore returns exactly the occurrence added to `t`.

## Complexity detail
If `s` has length `n`, then `t` has length $n + 1$. Scanning both strings takes $O(n)$ time. The accumulator uses $O(1)$ space.

## Alternatives and edge cases
- **Fixed frequency array:** increment for `s` and decrement for `t`, then locate the unmatched count; it is also linear with constant lowercase-alphabet space.
- **Character-code sum difference:** is linear and concise, but XOR avoids relying on a potentially overflowing numeric sum in fixed-width languages.
- **Sort and compare:** reveals the first mismatch in $O(n \log n)$ time.
- **Match each occurrence by scanning unused positions:** is correct but can take $O(n^2)$ time.
- If `s` is empty, the only character in `t` is the answer.
- The extra character may equal characters already present in `s`.
- The extra occurrence can appear anywhere after shuffling.
- Repeated letters must cancel occurrence by occurrence.
