## General

**Fix the two characters before optimizing the substring**

For an ordered pair `(major, minor)`, ignore every other character and score
each `major` as $+1$ and each `minor` as $-1$. A substring containing both
characters then has score

$$
\operatorname{count}(\texttt{major})
-
\operatorname{count}(\texttt{minor}),
$$

which is exactly its variance for this ordering. Try every ordered pair of
distinct letters present in `s`; reversing a pair is necessary because either
letter may be the more frequent one in the optimal substring.

**Kadane's reset must preserve one minor occurrence**

Scan `s` while tracking `major_count`, `minor_count`, and how many `minor`
characters remain later in the string. A candidate score is valid only after
at least one `minor` has been included. Update the answer with
`major_count - minor_count` under that condition.

When `major_count < minor_count`, the current prefix has negative score and
would normally be discarded by Kadane's algorithm. Reset both counts only if
another `minor` remains in the suffix. If none remains, retaining the current
minor is essential: resetting would make it impossible for a later
major-heavy suffix to satisfy the requirement that both characters occur.

**Why the pair scans cover the optimum**

Take an optimal substring and order its most frequent selected character as
`major` and its least frequent selected character as `minor`. The scan for
that ordered pair assigns its variance exactly as the substring's signed
score. Kadane-style removal discards only negative prefixes that cannot improve
a later score, except when their last available minor must be retained for
validity. Therefore the scan finds the best valid score for that pair.
Checking every ordered pair includes the pair from the global optimum, so the
largest recorded score is the requested answer.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$. There are at most
$26\cdot25$ ordered distinct-letter pairs, and each performs one $O(n)$ scan.
Because the alphabet size is fixed, total time is $O(n)$. The frequency table
and scan counters have fixed size, using $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate all substrings:** Updating character counts for every start and end is correct but takes $O(n^2)$ time.
- **Unconstrained Kadane scan:** Allowing a candidate before `minor` occurs incorrectly compares against an absent character.
- **Only unordered pairs:** The best excess may occur in either direction, so both orderings must be scanned.
- **One distinct character:** The answer is zero because choosing the same character yields difference zero.
- **All characters distinct:** Every present-character count is one, so the answer is zero.
- **Minor appears once at the beginning:** Do not discard that only required occurrence when no later minor exists.
- **Tied counts:** Their difference is zero, though a smaller substring may still have positive variance.
- **Ignored characters:** Characters outside the active ordered pair neither change the score nor invalidate contiguity.
