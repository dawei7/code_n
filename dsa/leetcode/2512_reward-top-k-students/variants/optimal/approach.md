## General

**Translate the scoring vocabulary into one lookup table**

Each positive word always contributes $3$, each negative word always contributes $-1$, and all other words contribute $0$. Because the two provided vocabularies are disjoint, store those fixed contributions in one hash table. Splitting a report then reduces its score calculation to summing one lookup per word. Repeated occurrences are deliberately processed separately, so a word appearing twice contributes twice.

**Turn both ranking rules into one sortable key**

The required primary order is decreasing score, whereas the tie-break order is increasing student identifier. Associate each student with the pair `(-score, identifier)`. Ordinary ascending tuple order now implements both rules: a larger score produces a smaller first component, and equal first components are resolved by the smaller identifier.

Sort all such pairs and return the identifiers from the first `k`. Every student's computed score is exact because every report word contributes its prescribed table value or zero. The tuple comparison is exactly the requested ranking relation, so the sorted prefix contains precisely the top `k` students in the required order.

## Complexity detail

Let $n = \lvert\texttt{report}\rvert$, and let $F$ be the total number of words across both feedback lists and all reports. Constructing the table and scoring every report take expected $O(F)$ time under standard hash-table behavior. Sorting the $n$ ranking pairs takes $O(n \log n)$ time, for $O(F + n \log n)$ total time.

The feedback table contains at most $F$ entries, the split report words occupy at most $O(F)$ transient space across processing, and the ranking list contains $n$ pairs. The auxiliary space bound is therefore $O(F+n)$.

## Alternatives and edge cases

- **Size-`k` heap:** Keeping only the best `k` ranking keys can reduce selection work to $O(n \log k)$ before ordering the chosen keys, which is useful when $k \ll n$, but it adds heap-direction and tie-break complexity.
- **Repeated minimum selection:** Repeatedly scanning the remaining students for the next best key is correct but costs $O(n^2)$ when all students must be returned.
- **Two feedback sets:** Separate positive and negative sets are also clear and correct; a single contribution table avoids two membership tests per report word.
- **Neutral words:** A report word absent from the table contributes zero and must not affect the score.
- **Repeated words:** Every occurrence contributes independently; report scoring is not based on a set of its words.
- **Equal scores:** Smaller identifiers rank first regardless of the students' original array order.
- **Negative totals:** Scores may be negative, but descending numeric order and the same identifier tie-break still apply.
