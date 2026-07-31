## General

**A separator count determines the word count**

Every sentence is nonempty, has no leading or trailing space, and uses exactly
one space between adjacent words. Consequently, each space marks one boundary
between two words. A sentence containing $k$ spaces therefore contains exactly
$k + 1$ words.

Scan every sentence, count its spaces, add one, and retain the largest count
seen. The separator property makes each computed count exact, and taking the
maximum across all sentences returns the requested value even when several
sentences tie.

## Complexity detail

Let $S$ be the total number of characters across all sentences. Each character
is inspected once while counting spaces, so the running time is $O(S)$. Only
the current count and maximum are retained, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Split every sentence into words:** Taking the length of each split list is
  direct and still takes $O(S)$ time, but it allocates temporary strings or a
  word list proportional to the sentence length.
- **Compare every pair of sentences:** Recounting words during pairwise
  comparisons can identify a maximum, but repeatedly scans the same text and
  takes $O(nS)$ time.
- A sentence with no spaces has one word, not zero.
- Ties require no special handling because the result is a count rather than a
  sentence index.
- The contract's single-space guarantee makes `spaces + 1` exact; inputs with
  repeated, leading, or trailing spaces would require different parsing, but
  those forms are excluded.
