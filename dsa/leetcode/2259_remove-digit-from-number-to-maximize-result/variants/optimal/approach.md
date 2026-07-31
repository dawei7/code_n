## General

**Compare deletion choices at their first difference**

Suppose the same target digit occurs at indices $i<j$. Deleting at $i$ shifts
`number[i + 1]` into position $i$, while deleting at $j$ leaves the target
digit at position $i$. These two results first differ at the earliest position
after the removed occurrence. If the character immediately after a target
digit is larger than that digit, removing this occurrence puts the larger
character earlier and is better than keeping the target there.

Scan from left to right and remove the first occurrence satisfying that ascent.
No later deletion can beat it because its result keeps the smaller target
digit at the first position where the two strings differ.

**Fall back to the final occurrence**

If no target digit is followed by a larger character, postponing the deletion
never makes the result worse. Between consecutive candidate occurrences, the
characters exposed by deleting earlier are no larger than the target that a
later deletion retains. Therefore the last occurrence is optimal. Track every
seen target as the fallback while scanning, then splice it out.

All candidates have equal length and contain no leading zero, so lexicographic
order and decimal numeric order agree. The local first-difference comparison
therefore proves that the chosen splice maximizes the requested value.

## Complexity detail

Let $n=\lvert\texttt{number}\rvert$. The scan and construction of the returned
string each take $O(n)$ time. The returned string and Python's slice
construction occupy $O(n)$ space.

## Alternatives and edge cases

- **Enumerate every deletion:** Building and comparing all candidate strings is correct but takes $O(n^2)$ time and space across the candidates.
- **Convert candidates to integers:** Numeric conversion is unnecessary and can be unavailable for very long variants of the problem.
- **Only one occurrence:** That occurrence must be removed.
- **Larger successor:** Remove the first target immediately before a larger digit.
- **Equal successor:** Equality gives no advantage; continue searching.
- **Strictly non-increasing suffix:** Remove the final target occurrence.
- **Adjacent repeated targets:** Different deletions can produce the same result.
- **Target at the end:** It becomes the fallback when no earlier ascent is better.
