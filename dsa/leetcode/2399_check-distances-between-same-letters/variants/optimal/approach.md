## General

**Translate spacing into an index difference.** If a letter occurs first at
index $p$ and again at index $q$, the positions strictly between them number
$q-p-1$. This is the only quantity that needs comparison with the letter's
entry in `distance`.

**Store one first position per alphabet letter.** Scan `s` from left to right
and map each character to its index from 0 through 25. A fixed array initialized
to `-1` distinguishes unseen letters. On the first occurrence, record the
current string index. On the guaranteed second occurrence, compute the index
difference and immediately return `False` if it differs from the requirement.

If the scan finishes, every present letter has had its two occurrences
compared successfully, so the string is well-spaced. No check is performed for
an unseen letter, which exactly implements the rule that its `distance` entry
is ignored. Conversely, any violated present-letter requirement is detected
when that letter appears for the second time.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$. The string is scanned once and every operation
per character is constant, giving $O(n)$ time. The first-position array always
contains 26 entries because the alphabet is fixed, so auxiliary space is
$O(1)$.

## Alternatives and edge cases

- **Position lists:** Build a list of two positions for every present letter
  and validate afterward; this is also linear but stores more structure than
  necessary.
- **Repeated string search:** Calling a prefix search for each second
  occurrence is correct but can rescan earlier characters and take $O(n^2)$
  time in a scalable alphabet model.
- **Adjacent occurrences:** Their number of intervening characters is zero
  because the formula subtracts one from the index difference.
- **Absent letters:** Their `distance` entries may contain any legal value and
  must never cause failure.
- **Late mismatch:** Returning early is safe, but a valid string or a mismatch
  belonging to the final letter can require scanning all $n$ characters.
- **Exactly two occurrences:** The input guarantee means no third-occurrence
  state or occurrence-count validation is required.
