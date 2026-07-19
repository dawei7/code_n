## General
**Build the occurrence profile**

Allocate 26 counters, one for each lowercase English letter. Scan `s` once and
increment the counter selected by each character. The fixed alphabet gives
direct access to every occurrence count without storing the characters
themselves.

**Compare only characters that appear**

Because $N \ge 1$, at least one counter is positive. Use the first positive
counter as the required frequency, then inspect all 26 counters. A zero counter
represents a character absent from `s` and is irrelevant; every positive
counter must equal the required frequency.

If the comparison succeeds, every appearing character has the same count. If
it fails, the required frequency and the unequal positive counter identify two
appearing characters with different counts. These two directions establish
that the returned Boolean exactly matches the contract.

## Complexity detail
The scan performs $N$ constant-time counter updates. Inspecting the 26 counters
adds a fixed amount of work, so the total time is $O(N)$. The counter array has
exactly 26 entries regardless of $N$, which is $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Hash-map counting:** A dictionary or `Counter` can store only characters
  that appear and makes the final comparison concise, but it uses space
  proportional to the number of distinct characters in a generalized
  alphabet.
- **Repeated full-string counting:** Calling a full-string count for each
  possible lowercase letter remains $O(N)$ under this fixed 26-letter
  alphabet, but it scans the same input repeatedly and has a larger constant
  factor.
- A one-character string is valid because its sole present character sets the
  only positive frequency.
- A string containing just one distinct character is valid regardless of how
  many times that character repeats.
- If all characters are distinct, every positive count is one, so the result
  is `true`.
- Zero counters must be ignored; absent letters do not need to match the
  positive occurrence count.
